import uuid


def create_id():
    return str(uuid.uuid4())


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False
