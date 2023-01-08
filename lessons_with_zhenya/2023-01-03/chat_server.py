"""
You need to create a simple server that allows clients to connect to it. 
When connected, client may send a message to the server. 
After receiving a message from any of clients server resends it to all connected clients.
"""

import asyncio


class ChatServer:
    def __init__(self):
        # Empty container to save all open connections so we can distribute messages to all of them
        self.writers = set()

    # Function to operate on ONE connection, gets called by start_server when a new client connects to server
    async def handle_connection(self, reader, writer):
        # Adding this connection to our container
        self.writers.add(writer)

        # Method to receive a tuple of IP address and connection port
        addr = writer.get_extra_info("peername")
        print(f"New connection from {addr}")

        # Loop to allow sending more than one message
        while True:
            # Waiting until this user sends a message
            data = await reader.read(140)
            message = data.decode()

            print(f"Received {message} from {addr}")
            # Allowing user input "quit" to close their connection to server
            if message == "quit":
                break

            print(f"Send: {message}")

            # Asynchronous function so that it can be started at the same time for all active clients
            async def write(w):
                w.write(data)
                await w.drain()

            # List comprehension to call write function for all active clients except the sender; will be stopped and returned by await
            # "Futures" are the return values of async function calls
            write_futures = [write(w) for w in self.writers if w is not writer]
            # Waiting for all function calls to finish
            asyncio.gather(*write_futures)

        # We get here once the connection was closed by a client typing "quit"
        # Client gets removed from container so they won't receive messages any longer
        self.writers.remove(writer)

        print("Close the connection")
        # Closing connection from the server end, too
        writer.close()

    # Function to run the entire server
    async def run(self):
        server = await asyncio.start_server(self.handle_connection, "127.0.0.1", 8888)

        addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
        print(f"Serving on {addrs}")

        async with server:
            await server.serve_forever()


server = ChatServer()
asyncio.run(server.run())
