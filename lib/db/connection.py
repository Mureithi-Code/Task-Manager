from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL (SQLite in this case)
DATABASE_URL = "sqlite:///taskhub.db"

# Create the engine to interact with the database
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured session class
Session = sessionmaker(bind=engine)

# Instantiate the session
session = Session()
