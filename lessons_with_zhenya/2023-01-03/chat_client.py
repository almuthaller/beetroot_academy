import asyncio


async def chat_client():
    # Creating connection to server with given address and port
    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    # Two asynchronous functions user_input() and read() so that waiting for user input and
    # waiting for other client's messages can happen at the same time
    async def user_input():
        while True:
            # Asyncio method to call input() asynchronously
            # https://stackoverflow.com/a/65439376
            loop = asyncio.get_event_loop()
            message = await loop.run_in_executor(None, input)

            # Sending message to server
            writer.write(message.encode())
            await writer.drain()

            # "quit" promt allows client to close their end of the connection
            if message == "quit":
                nonlocal read_task
                # Telling the read task to break out of its while loop which causes the await in read() to throw an exception
                read_task.cancel()
                # Terminating function so the gather method will be finished
                break

    async def read():
        # Loop to always be ready for incoming messages
        while True:
            try:
                # Waiting for the server to send something
                data = await reader.read(140)
                print(f"Received: {data.decode()}")
            # This exception is raised when read_task is cancelled; to make sure the program keeps running we handle it and terminate the read function
            except asyncio.exceptions.CancelledError:
                break

    # Creating two tasks so they can be gathered and run simultaneously
    write_task = asyncio.create_task(user_input())
    read_task = asyncio.create_task(read())

    # Waiting until both tasks are finished
    await asyncio.gather(write_task, read_task)

    print("Closing client end of connection")
    writer.close()


asyncio.run(chat_client())
