import sys
import os

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lib.db.connection import session, engine
from lib.db.models import Base, User, Task


# Drop and recreate tables
print("Recreating the database tables...")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed data
print("Seeding data...")

# Create sample users
user1 = User(name="John Doe", email="john@example.com")
user2 = User(name="Jane Smith", email="jane@example.com")

# Create tasks
task1 = Task(name="Finish project", description="Complete the TaskHub project", user=user1)
task2 = Task(name="Buy groceries", description="Milk, Eggs, Bread", user=user2)

# Add and commit data to the database
session.add_all([user1, user2, task1, task2])
session.commit()

print("Database seeded successfully!")
