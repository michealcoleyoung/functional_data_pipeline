users = [
    {"id": 1, "name": "Alice", "age": 28, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 22, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
    {"id": 4, "name": "David", "age": 23, "email": "david@example.com"},
]

def filter_by_age(user):
    # returns only users that are 25 and older
    filtered_users = []
    for info in user:
        age = info["age"]
        if age >= 25:
            filtered_users.append(info)
    return filtered_users


def transform_names(user):
    # returns all names in uppercase
    uppercase_names = []
    for info in user:
        name = info["name"].upper()
        uppercase_names.append(name)
    return uppercase_names


def extract_emails(user):
    # returns all email addresses
    email_address = []
    for info in user:
        email = info["email"]
        email_address.append(email)
    return email_address


print(filter_by_age(users))
print(transform_names(users))
print(extract_emails(users))