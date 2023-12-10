#!/usr/bin/python3
""" import required modules """

import cmd
import os
import re
import sys
import ast
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from uuid import uuid4

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ Input Ctrl+D to exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to terminate the program """
        return True

    def emptyline(self):
        """ Empty line event handler """
        pass

    def do_create(self, line):
        """ Create a new instance of the specified class """
        if not line.split():
            print("** Missing model class name **")
            return
        model_name = line.split()[0]
        try:
            Class = globals().get(model_name)
            if issubclass(Class, BaseModel):
                my_model = Class()
                my_model.save()
                print(f"Model created with ID: {my_model.id}")
        except KeyError:
            print(f"** Class '{model_name}' doesn't exist. **")

    def do_show(self, line):
        """ Show details of a specific instance """
        if not line:
            print("**  **")
            return
        class_name, instance_id = line.split()
        model_class = globals().get(class_name)
        if not model_class or not issubclass(model_class, BaseModel):
            print(f"** Class '{class_name}' doesn't exist or isn't a model.**")
            return
        storage_path = FileStorage._FileStorage__file_path
        if not os.path.exists(storage_path) or not os.path.isfile(storage_path):
            print(f"** No object data found. **")
            return
        with open(storage_path, "r") as file:
            data = json.load(file)
        object_data = data.get(f"{class_name}.{instance_id}", None)
        if not object_data:
            print(f"** No instance found for class '{class_name}' with ID '{instance_id}'. **")
            return
        object_data.pop("__class__", None)
        print(f"[{class_name}] ({instance_id}): {object_data}")

    def do_destroy(self, line):
        """ Destroy an instance based on the class name and id """
        arguments = line.split()

        if not arguments:
            print("** Missing class name **")
            return
        class_name = arguments[0]
        obj_id = arguments[1] if len(arguments) > 1 else None

        Class = globals().get(class_name)
        if not Class or not issubclass(Class, BaseModel):
            print(f"** Class '{class_name}' doesn't exist or isn't a model. **")
            return

        if not obj_id:
            print("** Missing instance ID. **")
            return
        all_obj = {}
        search_id = f"{class_name}.{obj_id}"
        storage_path = FileStorage._FileStorage__file_path

        if os.path.exists(storage_path) and os.path.isfile(storage_path):
            with open(storage_path, "r") as file:
                all_obj = json.load(file)
            if search_id not in all_obj:
                print("** no instance found **")
                return
            del all_obj[search_id]
            objects = FileStorage._FileStorage__objects
            del objects[search_id]
            with open(storage_path, "w") as file:
                json.dump(all_obj, file)
                return
        print("** no instance found **")

    def do_all(self, line):
        """ Show all instances or instances for a specific class """
        filter_class = line.split()[0] if line else None
        if filter_class:
            Class = globals().get(filter_class)
            if not Class or not issubclass(Class, BaseModel):
                print(f"** Class '{filter_class}' doesn't exist or isn't a model. **")
                return
        all_obj = {}
        storage_path = FileStorage._FileStorage__file_path

        try:
            with open(storage_path, 'r') as file:
                all_obj = json.load(file)
        except FileNotFoundError:
            print("** No storage file found. **")
            return
        objects = self._filter_objects(all_obj, filter_class)
        if objects:
            print("[", end='')
            is_first = True
            for key, obj_dict in objects.items():
                class_name, obj_id = key.split(".")
                obj_dict.pop('__class__', None)
                if not is_first:
                    print(",", end="")
                print(f"[{class_name}] ({obj_id}) {obj_dict}", end="")
                is_first = False
            print("]")
        else:
            print("** No objects found. **")
        if filter_class:
            return {
                key: value
                for key, value in all_obj.items()
                if key.startswith(f"{filter_class}.")
            }
        return all_obj

    def do_update(self, line):
        """ Update an instance based on the class name and id """
        if not line:
            print("** Please provide a class name. **")
            return
        target_class = line.split()[0]
        model_class = globals().get(target_class)
        if not model_class or not issubclass(model_class, BaseModel):
            print(f"** Class '{target_class}' doesn't exist or isn't a model. **")
            return
        if len(line.split()) < 2:
            print("** Please provide an instance ID. **")
            return
        obj_id = line.split()[1]
        if len(line.split()) < 3:
            print("** Please provide the attribute name. **")
            return
        if len(line.split()) < 4:
            print("** Please provide the new value. **")
            return
        all_obj = {}
        search_id = f"{line.split()[0]}.{line.split()[1]}"
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        if not re.match(pat, search_id.split(".")[1]):
            print("** no instance found **")
            return
        attrib_name = line.split()[2]
        att_value = line.split()[3].strip('"')
        fileName = FileStorage._FileStorage__file_path
        if os.path.exists(fileName) and os.path.isfile(fileName):
            with open(fileName, 'r') as file:
                all_obj = json.load(file)
                if search_id not in all_obj:
                    print("** no instance found **")
                    return
        value = all_obj[search_id]
        if attrib_name in value:
            try:
                a_type = type(attrib_name).__name__
                att_value = ast.literal_eval(a_type + "('" + att_value + "')")
            except (ValueError, SyntaxError):
                pass
            value[attrib_name] = att_value
        else:
            value[attrib_name] = att_value
        with open(fileName, "w") as file:
            json.dump(all_obj, file)

    def do_count(self, line):
        """ Retrieve the number of instances of a class """
        if line:
            ClassName = line.split()[0]
            model_class = globals().get(ClassName)
            if not model_class or not issubclass(model_class, BaseModel):
                print(f"** Class '{ClassName}' doesn't exist or isn't a model. **")
                return
        objects = FileStorage._FileStorage__objects
        c = 0
        for key, value in objects.items():
            Class_Name = key.split(".")[0]
            if key.startswith(f"{Class_Name}."):
                c += 1
        print(c)
        
    def default(self, line):
        """ Method invoked for unrecognized command prefixes """
        if not line:
            return

        try:
            # Separate class name and command
            class_name, command = line.split(".", 1)

            # Handle commands with arguments
            if "(" in command and ")" in command:
                cmd_name, args = command.split("(", 1)
                args = args.strip(")").split(", ")

                # Extract object ID and attribute information for specific commands
                if cmd_name in ["show", "destroy"]:
                    obj_id = args[0].strip('"')
                    method_name = f"do_{cmd_name}"
                    if hasattr(self, method_name) and callable(getattr(self, method_name)):
                        getattr(self, method_name)(f"{class_name} {obj_id}")

                elif cmd_name == "update":
                    if args[0].startswith("{") and args[0].endswith("}"):
                        obj_id = args[1].strip('"')
                        attribute_dict = ast.literal_eval(args[0])
                        method_name = f"do_update"
                        if hasattr(self, method_name) and callable(getattr(self, method_name)):
                            for key, value in attribute_dict.items():
                                getattr(self, method_name)(f"{class_name} {obj_id} {key} {value}")
                    else:
                        # Handle update commands with individual arguments
                        obj_id = args[0].strip('"')
                        field = args[1].strip('"') if len(args) >= 2 else None
                        value = args[2].strip('"') if len(args) == 3 else None
                        method_name = f"do_update"
                        if hasattr(self, method_name) and callable(getattr(self, method_name)):
                            getattr(self, method_name)(f"{class_name} {obj_id} {field} {value}")

            # Handle simple commands without arguments
            else:
                method_name = f"do_{command}"
                if hasattr(self, method_name) and callable(getattr(self, method_name)):
                    getattr(self, method_name)(class_name)
        except ValueError:
            print(f"** Invalid command '{line}'. **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

