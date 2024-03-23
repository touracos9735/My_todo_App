FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(new_file_arg,filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(new_file_arg)

if __name__=="__main__":
    print("hello from functions")