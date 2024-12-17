import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.db.operations import create_object, delete_object, get_all_objects, find_by_id
from lib.utils.helpers import validate_input
from lib.utils.display import display_table

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nTaskHub - Main Menu")
        print("1. Create a Task")
        print("2. Delete a Task")
        print("3. View All Tasks")
        print("4. Find a Task by ID")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            create_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            find_task()
        elif choice == "5":
            print("Exiting TaskHub. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def create_task():
    """Create a new task and optionally assign it to a user."""
    name = input("Enter task name: ").strip()
    description = input("Enter task description: ").strip()

    assign_choice = input("Assign this task to a user? (y/n): ").strip().lower()
    user_id = None

    if assign_choice == "y":
        user = assign_task_to_user()
        if user:
            user_id = user.id

    create_object("Task", {"name": name, "description": description, "user_id": user_id})
    print("\nTask created successfully.")

def assign_task_to_user():
    """
    Assign a task to an existing user or create a new one.
    Returns:
        User object of the assigned user or None.
    """
    print("\nTask Assignment:")
    print("1. Assign to an existing user")
    print("2. Create a new user")
    choice = input("Select an option: ").strip()

    if choice == "1":
        users = get_all_objects("User")
        if not users:
            print("No users available. Please create a new user.")
            return create_new_user()

        # Construct user_list as a list of dictionaries
        user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

        # Debug print to ensure user_list structure is valid
        print("\nDEBUG: user_list content:", user_list)

        # Verify user_list is a valid list of dictionaries
        if not all(isinstance(item, dict) for item in user_list):
            print("Error: user_list is not a valid list of dictionaries.")
            return None

        # Display the table using tabulate
        try:
            display_table(user_list, ["id", "name", "email"])
        except Exception as e:
            print(f"Error while displaying the table: {e}")
            return None

        # Prompt for user ID selection
        while True:
            try:
                user_id = validate_input(input("Enter user ID to assign: "), int)
                user = find_by_id("User", user_id)
                if user:
                    return user
                print("Invalid user ID. Please try again.")
            except ValueError:
                print("Please enter a valid number for the user ID.")

    elif choice == "2":
        return create_new_user()

    else:
        print("Invalid choice. Please try again.")
        return assign_task_to_user()



def create_new_user():
    """Create a new user and return the created user object."""
    user_name = input("Enter new user's name: ").strip()
    user_email = input("Enter new user's email: ").strip()
    user = create_object("User", {"name": user_name, "email": user_email})
    print("\nNew user created successfully.")
    return user

def delete_task():
    """Delete a task based on its ID."""
    task_id = validate_input(input("Enter task ID to delete: "), int)
    if delete_object("Task", task_id):
        print("Task deleted successfully.")
    else:
        print("Task not found or could not be deleted.")

def view_tasks():
    tasks = get_all_objects("Task")
    if not tasks:
        print("No tasks found.")
        return

    # Prepare the task list for display
    task_list = []
    for task in tasks:
        try:
            # Create a dictionary for each task
            task_entry = {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "user": task.user.name if task.user and task.user.name else "Unassigned",
            }
            task_list.append(task_entry)
        except AttributeError as e:
            # Handle cases where a task object is missing attributes
            print(f"Error processing task {task}: {e}")
            continue

    # Debugging: Print the structure of task_list
    print("DEBUG: Task list:", task_list)

    # Display the table
    try:
        display_table(task_list, ["id", "name", "description", "user"])
    except ValueError as e:
        print(f"Error displaying table: {e}")

def find_task():
    """Find a specific task by its ID."""
    task_id = validate_input(input("Enter task ID to find: "), int)
    task = find_by_id("Task", task_id)
    if task:
        print("\nTask Details:")
        print(f"ID: {task.id}")
        print(f"Name: {task.name}")
        print(f"Description: {task.description}")
        user_name = task.user.name if task.user else "Unassigned"
        print(f"Assigned User: {user_name}")
    else:
        print("Task not found.")

if __name__ == "__main__":
    main_menu()
