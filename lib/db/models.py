from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

# Base declarative class
Base = declarative_base()

# Junction table for many-to-many relationship between Task and User
task_users = Table(
    "task_users",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    # Relationship to tasks through the junction table
    tasks = relationship("Task", secondary=task_users, back_populates="users")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Relationship to users through the junction table
    users = relationship("User", secondary=task_users, back_populates="tasks")

    def __repr__(self):
        users_repr = ", ".join([user.name for user in self.users]) if self.users else "Unassigned"
        return f"Task(id={self.id}, name='{self.name}', description='{self.description}', users=[{users_repr}])"
