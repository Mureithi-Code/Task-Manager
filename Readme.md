# TaskHub

**TaskHub** is a robust task management application designed to help you efficiently manage tasks and assign them to multiple users. It leverages SQLAlchemy for database interactions and supports a many-to-many relationship between tasks and users.

---

## Features

- **Task Management**: Create, view, update, and delete tasks.
- **User Management**: Add users and assign tasks to one or more users.
- **Relational Database**: Tracks relationships between tasks and users using a many-to-many schema.
- **Command-Line Interface (CLI)**: Simple and interactive CLI for managing tasks and users.

---

## Installation

### Prerequisites

- Python 3.10+
- A virtual environment tool (e.g., `venv` or `virtualenv`)
- SQLite (default) or another supported database

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd taskhub
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   Set up the database schema using Alembic:
   ```bash
   alembic upgrade head
   ```

---

## Usage

Run the application using the CLI:
```bash
python lib/cli.py
```

### Main Menu Options

1. **Create a Task**
   - Add a new task with a name, description, and optional user assignments.

2. **Delete a Task**
   - Remove a task by its ID.

3. **View All Tasks**
   - List all tasks with their associated users.

4. **Find a Task by ID**
   - Retrieve and display details of a specific task.

5. **Exit**
   - Quit the application.

---

## Database Schema

### Tables

1. **`users`**
   - Stores user information (ID, name, email).

2. **`tasks`**
   - Stores task information (ID, name, description).

3. **`task_users`**
   - Junction table to establish a many-to-many relationship between tasks and users.

---

## Development

### Updating the Database Schema

1. Modify `models.py` to reflect schema changes.
2. Generate a new migration:
   ```bash
   alembic revision --autogenerate -m "Describe changes"
   ```
3. Apply the migration:
   ```bash
   alembic upgrade head
   ```

---

## Troubleshooting

- **Database Errors**: Ensure the database is initialized and migrations are applied.
- **Dependency Issues**: Run `pip install -r requirements.txt` to install missing packages.
- **Environment Issues**: Ensure the virtual environment is activated before running commands.

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to report bugs or suggest new features.

---

## Acknowledgments

- **SQLAlchemy**: For robust ORM functionality.
- **Alembic**: For database migrations.
- **Click**: For CLI utilities (if used in the future).

---

## Contact

For questions or support, please reach out at [darkknight505c@gmail.com].

