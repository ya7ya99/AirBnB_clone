# AirBnB Clone Project

## Project Description

Welcome to the AirBnB clone project! This project focuses on building a Python-based command-line interpreter for managing AirBnB objects. The overarching goal is to lay the foundation for a full web application by implementing key concepts such as serialization, deserialization, and file storage.

## Command Interpreter Overview

The command interpreter, named `console.py`, allows users to interact with AirBnB objects through various commands. These commands enable the creation, retrieval, modification, and deletion of objects. The interpreter serves as a crucial component for the development of subsequent project phases, including HTML/CSS templating, database storage, API integration, and front-end implementation.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the project repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd AirBnB_clone`
3. Run the console: `./console.py`

### How to Use the Command Interpreter

Once the console is running, you can use the following commands:

- `help`: Display a list of documented commands.
- `EOF`: End the console session.
- `quit`: Quit the console.

You can perform various operations on AirBnB objects, including creating new objects, retrieving objects, updating attributes, and deleting objects.

## Examples

**Interactive Mode:**

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
Non-Interactive Mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
These examples showcase the basic usage of the command interpreter in both interactive and non-interactive modes. Explore the available commands and enjoy building your AirBnB clone!

Contributors
Oumaima Sellouane
Yahya Khaldy
License
This project is licensed under the MIT License.
