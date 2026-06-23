# 0x0F. Python - Object-relational mapping... (API project)

## Description
This project explores accessing a REST API to gather employee TODO
list data and exporting it into different data formats (plain text
summary, CSV, JSON). The data source is the public REST API at
`https://jsonplaceholder.typicode.com`.

## Requirements
- Python 3.4.3 on Ubuntu 14.04 LTS
- PEP 8 style
- All files start with `#!/usr/bin/python3`
- All files end with a new line
- All files are executable
- Code is not executed on import (`if __name__ == "__main__":`)

## Files

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Takes an employee ID and prints their TODO list progress |
| `1-export_to_CSV.py` | Exports a given employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports a given employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports **all** employees' tasks to `todo_all_employees.json` |

## Usage

```
./0-gather_data_from_an_API.py <employee_id>
./1-export_to_CSV.py <employee_id>
./2-export_to_JSON.py <employee_id>
./3-dictionary_of_list_of_dictionaries.py
```

## Author
Kevin Ishimwe
