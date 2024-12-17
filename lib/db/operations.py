from lib.db.connection import session
from lib.db.models import User, Task

# Explicit mapping of model names to SQLAlchemy classes
MODEL_MAPPING = {
    "User": User,
    "Task": Task,
}

def create_object(model_name, attributes):
    """
    Create a new object in the database.
    :param model_name: String name of the model class (e.g., 'User', 'Task')
    :param attributes: Dictionary of attribute names and values
    :return: The created object
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    obj = model(**attributes)
    session.add(obj)
    session.commit()
    print(f"{model_name} created successfully.")
    return obj

def delete_object(model_name, object_id):
    """
    Delete an object from the database by its ID.
    :param model_name: String name of the model class (e.g., 'User', 'Task')
    :param object_id: ID of the object to delete
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    obj = session.query(model).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        print(f"{model_name} with ID {object_id} deleted successfully.")
    else:
        print(f"{model_name} with ID {object_id} not found.")

def get_all_objects(model_name):
    """
    Retrieve all objects of a model type from the database.
    :param model_name: String name of the model class (e.g., 'User', 'Task')
    :return: List of objects
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    return session.query(model).all()

def find_by_id(model_name, object_id):
    """
    Find a specific object in the database by its ID.
    :param model_name: String name of the model class (e.g., 'User', 'Task')
    :param object_id: ID of the object to find
    :return: Object if found, None otherwise
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    obj = session.query(model).get(object_id)
    if obj:
        return obj
    else:
        print(f"{model_name} with ID {object_id} not found.")
        return None

def find_all_by_attribute(model_name, attribute_name, value):
    """
    Find all objects that match a specific attribute value.
    :param model_name: String name of the model class
    :param attribute_name: Name of the attribute to filter on
    :param value: Value to filter by
    :return: List of objects
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    filter_attr = getattr(model, attribute_name, None)
    if not filter_attr:
        raise AttributeError(f"Attribute '{attribute_name}' does not exist on '{model_name}'.")
    return session.query(model).filter(filter_attr == value).all()

def update_object(model_name, object_id, updates):
    """
    Update specific attributes of an object in the database.
    :param model_name: String name of the model class
    :param object_id: ID of the object to update
    :param updates: Dictionary of attribute names and new values
    """
    model = MODEL_MAPPING.get(model_name)
    if not model:
        raise KeyError(f"Model '{model_name}' does not exist.")
    obj = session.query(model).get(object_id)
    if obj:
        for key, value in updates.items():
            setattr(obj, key, value)
        session.commit()
        print(f"{model_name} with ID {object_id} updated successfully.")
    else:
        print(f"{model_name} with ID {object_id} not found.")
