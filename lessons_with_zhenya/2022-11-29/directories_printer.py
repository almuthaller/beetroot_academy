# Printing all the directories and files in a mother folder using recursion.

import os


def directories_printer(root, indentation=""):
    for element in os.listdir(root):
        print(indentation + element)
        if os.path.isdir(os.path.join(root, element)):
            directories_printer(os.path.join(root, element), indentation + "\t")


mother_folder = r"/Users/Almut1/dev/pythonBeetroot/homework"
directories_printer(mother_folder)
