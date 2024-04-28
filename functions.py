FILEPATH = "/users/shara/Python/pythonProject/todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return list of to-do items"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a text file with modified to-do's list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
