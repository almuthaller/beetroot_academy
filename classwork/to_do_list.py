"""
Small todo list

User inputs a list of todo's items like this “make an appointment, ask my friend how is his health, go on walk”. 
After it - program must wait for a next input from user. Like “go on walk - done”. 
Once it'll be inputed - program must print what's left to do for today. 
Once items will be finished - it must finish execution and print “good job!”
"""

to_do_list = input("To do list: ").split(",")
to_do_list = list(set(item.strip() for item in to_do_list))

user_input = input("Check an item from your list: ")

while True:
    done_in_input = user_input.endswith("- done")
    add_in_input = user_input.endswith("- add")

    if done_in_input:
        clear_user_input = user_input.replace(" - done", "")
        to_do_list.remove(clear_user_input)

    elif add_in_input:
        clear_user_input = user_input.replace(" - add", "")
        to_do_list.append(clear_user_input)
        to_do_list = list(set(to_do_list))

    else:
        print("Sorry, I don't know what to do with this input")

    if len(to_do_list) < 1:
        break

    print_thingy = "\n".join(to_do_list)
    print(f"Left for today: {print_thingy}")

    user_input = input("Check an item from your list: ")


print("Good job!")
