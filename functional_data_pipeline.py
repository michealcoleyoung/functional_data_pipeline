import json


def filter_by_age(data):
    # returns only users that are 25 and older
    filtered_users = []
    for user in data:
        age = user["age"]
        if age >= 25:
            filtered_users.append(user)
    return filtered_users


def transform_names(data):
    # returns all names in uppercase
    transformed_users = []

    for user in data:
        new_user = dict(user)
        uppercase_name = user["name"].upper()
        new_user["name"] = uppercase_name
        transformed_users.append(new_user)
    return transformed_users


def extract_emails(data):
    # returns all email addresses
    email_address = []
    for user in data:
        email = user["email"]
        email_address.append(email)
    return email_address


def compose_functions(*functions):
    def composed_function(data):
        for user in reversed(functions):
            data = user(data)
        return data
    return composed_function


with open('data/users.json') as f:
    users = json.load(f)


print(f"Filter By Age: {filter_by_age(users)}")
print(f"Transform Names: {transform_names(users)}")
print(f"Extract Emails: {extract_emails(users)}")





