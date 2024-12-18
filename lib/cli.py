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
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    assign_to_user = input("Assign this task to a user? (y/n): ").strip().lower()

    user_id = None  # Default to unassigned
    if assign_to_user == "y":
        print("\nTask Assignment:")
        print("1. Assign to an existing user")
        print("2. Create a new user")
        option = input("Select an option: ").strip()

        if option == "1":
            user = assign_task_to_user()
            if user:
                user_id = user.id  # Assign the user ID
        elif option == "2":
            user = create_new_user()
            if user:
                user_id = user.id

    # Create the task in the database
    create_object("Task", {"name": task_name, "description": task_description, "user_id": user_id})
    print("\nTask created successfully.")

def assign_task_to_user():
    # Fetch all users from the database
    users = get_all_objects("User")
    if not users:
        print("No users found.")
        return None  # No users to assign to

    # Prepare user list for display
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    
    # Debugging: Print user list
    print("DEBUG: user_list content:", user_list)

    # Display user list
    try:
        display_table(user_list, headers="keys")
    except Exception as e:
        print("Error while displaying the table:", str(e))
        return None

    # Prompt the user to select an ID
    while True:
        try:
            selected_id = int(input("Enter the ID of the user to assign the task: "))
            selected_user = next((user for user in users if user.id == selected_id), None)
            if not selected_user:
                print("Invalid ID. Please try again.")
                continue
            return selected_user  # Return the selected user
        except ValueError:
            print("Please enter a valid numeric ID.")

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
        display_table(task_list, headers="keys")
    except ValueError as e:
        print(f"Error displaying table: {e}")

def find_task():
    """Find a specific task by its ID and display the details in a table."""
    task_id = validate_input(input("Enter task ID to find: "), int)
    task = find_by_id("Task", task_id)
    if task:
        # Prepare the task details for display
        task_details = [{
            "ID": task.id,
            "Name": task.name,
            "Description": task.description,
            "Assigned User": task.user.name if task.user else "Unassigned",
        }]
        
        # Display the task details in a table
        try:
            display_table(task_details, headers="keys")
        except ValueError as e:
            print(f"Error displaying table: {e}")
    else:
        print("Task not found.")


if __name__ == "__main__":
    main_menu()
