
```markdown
# The AirBnB Clone Project

![AirBnB Logo](path/to/your/image.png) <!-- Replace with the actual path to your AirBnB logo image -->

## Project Description

This is the first part of the AirBnB clone project where we worked on the backend of the project while interfacing it with a console application with the help of the `cmd` module in Python.

...

## How to start it

These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

### Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```bash
git clone https://github.com/jzamora5/AirBnB_clone.git
```

After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

- **console.py**: The main executable of the project, the command interpreter.
- **models/engine/file_storage.py**: Class that serializes instances to a JSON file and deserializes JSON file to instances.
- **models/__init__.py**: A unique FileStorage instance for the application.
- **models/base_model.py**: Class that defines all common attributes/methods for other classes.
- **models/user.py**: User class that inherits from BaseModel.
- **models/state.py**: State class that inherits from BaseModel.
- **models/city.py**: City class that inherits from BaseModel.
- **models/amenity.py**: Amenity class that inherits from BaseModel.
- **models/place.py**: Place class that inherits from BaseModel.
- **models/review.py**: Review class that inherits from BaseModel.

...

## How to use it

It can work in two different modes:

- Interactive and Non-interactive.

In Interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again and wait for a new command...

...

## Available commands and what they do

The recognizable commands by the interpreter are the following:

| Command | Description |
| ------- | ----------- |
| `quit` or `EOF` | Exits the program. |
| `help` | Provides a text describing how to use a command. |
| `create` | Creates a new instance of a valid Class, saves it (to the JSON file), and prints the id. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| `show` | Prints the string representation of an instance based on the class name and id. |
| `destroy` | Deletes an instance based on the class name and id (saves the change into a JSON file). |
| `all` | Prints all string representation of all instances based or not on the class name. |
| `update` | Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file). |
| `count` | Retrieve the number of instances of a class. |


Contributors
Oumaima Sellouane
Yahya Khaldy
## License

This project is licensed under the [MIT License](LICENSE).
