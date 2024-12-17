from lib.db.operations import get_all_objects

def debug_tasks():
    tasks = get_all_objects("Task")
    for task in tasks:
        print(task)

if __name__ == "__main__":
    debug_tasks()