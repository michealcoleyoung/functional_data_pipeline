# Functional Data Pipeline

This project demonstrates a functional data pipeline in Python, which processes user data to filter users by age, transform their names to uppercase, and extract their email addresses.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Features

- **Filter by Age**: Returns users who are 25 years old or older.
- **Transform Names**: Converts all user names to uppercase.
- **Extract Emails**: Extracts email addresses from the user data.
- **Composable Functions**: Chain multiple functions to create a custom data pipeline.

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/functional_data_pipeline.git
cd functional_data_pipeline
```



2. Ensure Python is installed:
   This project requires Python 3.6 or higher. You can check your Python version with:
```
python --version
```
## Example

Given the following input data in data/users.json:
```python
[
  {"id": 1, "name": "Alice", "age": 28, "email": "alice@example.com"},
  {"id": 2, "name": "Bob", "age": 22, "email": "bob@example.com"},
  {"id": 3, "name": "Charlie", "age": 35, "email": "charlie@example.com"},
  {"id": 4, "name": "David", "age": 23, "email": "david@example.com"}
]
```
The output will be:
```python
['alice@example.com', 'charlie@example.com']
```
## Dependencies
Python 3.6 or higher
