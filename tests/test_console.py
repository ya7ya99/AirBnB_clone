#!/usr/bin/python3
"""testing"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
import sys
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

""" TesttheHBNBPrompt class """


class TesttheHBNBPrompt(unittest.TestCase):
    """testing the hbnb prompt and the emptyline"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_prompt_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandEntryPoint(unittest.TestCase):
    """testing the entry point of the command interpreter containing
        EOF, quit, create, show, all, destroy, and update commands"""
    def test_EOF(self):
        use = "signal to exit the program using CTRL+D"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(use, output.getvalue().strip())

    def test_quit(self):
        use = "Quit command to exit the program"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(use, output.getvalue().strip())

    def test_create(self):
        use = (
                "create <class>\n"
                "create a new instance")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help create"))
            self.assertEqual(use, output.getvalue().strip())

    def test_show(self):
        use = (
                "show <class> <instance id>\n"
                "shows the class created")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help show"))
            self.assertEqual(use, output.getvalue().strip())

    def test_destroy(self):
        use = (
                "destroy <class> <isntance id>\n"
                "deletes an instance based on the class name and id\n"
                "(save the change into the JSON file)")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(" help destroy"))
            self.assertEqual(use, output.getvalue().strip())

    def test_all(self):
        use = (
                "all or all <class>\n"
                "all : show all instances created for all classes\n"
                "all <class> : show all instances for specific class")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(use, output.getvalue().strip())

    def test_count(self):
        use = (
                "Usage : <class name>.count().\n"
                "command to retrieve the number of instances of a class")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(use, output.getvalue().strip())

    def test_update(self):
        use = (
                "To : update <class> <id> <attribute name> <attribute value>\n"
                "Usage : <class name>.update(<id>, <attribute name>,"
                " <attribute value>)\n"
                "To : <class name>.update(<id>, <dictionary representation>)\n"
                "Updates an instance based on the class name\n"
                "and id by adding or updating attribute")
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(use, output.getvalue().strip())

    def test_quit_1(self):
        """ test_quit_1 """
        with patch('sys.stdout', new=StringIO()) as output:
            try:
                HBNBCommand().onecmd("quit")
            except SystemExit:
                pass
            self.assertEqual("", output.getvalue().strip())

    def test_emptyline(self):
        """ test_emptyline"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_create_BaseModel(self):
        """ test_create_BaseModel """
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9 a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_User(self):
        """Test creating a User instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_show_BaseModel(self):
        """ test_show_BaseModel """
        inst = BaseModel()
        pattern_start = r'\[BaseModel\] \({id}\) {{'
        pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
        pattern_end = r" 'updated_at' : '{updated_at}'}}"
        pat = pattern_start + pattern_values + pattern_end
        self.assertEqual(type(inst.id), str)
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd(f"show BaseModel {inst.id}"))
            self.assertEqual(output.getvalue().strip(), pat)

    def test_all_BaseModel(self):
        """testing the all command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[BaseModel\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_BaseModel_all(self):
        """testing the BaseModel.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[BaseModel\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_Review(self):
        """Test creating a Review instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_State(self):
        """Test creating a State instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_City(self):
        """Test creating a City instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_Amenity(self):
        """Test creating an Amenity instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_create_Place(self):
        """Test creating a Place instance"""
        pat = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Review_all(self):
        """testing the Review.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Review\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_all(self):
        """testing the User.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[User\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_all(self):
        """testing the State.all command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[State\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_all(self):
        """testing the City.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[City\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_all(self):
        """testing the Amenity.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Amenity\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_all(self):
        """testing the Place.all() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Place\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Review_show(self):
        """testing the Review.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Review\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Review.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_show(self):
        """testing the User.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[User\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("User.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_show(self):
        """testing the State.show command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[State\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("State.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_show(self):
        """testing the City.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[City\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("City.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_show(self):
        """testing the Amenity.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Amenity\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Amenity.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_show(self):
        """testing the Place.show() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pattern_start = r'\[Place\] \({id}\) {{'
            pattern_values = r"'id': '{id}', 'created_at': '{created_at}',"
            pattern_end = r" 'updated_at' : '{updated_at}'}}"
            pat = pattern_start + pattern_values + pattern_end
            self.assertFalse(HBNBCommand().onecmd("Place.show()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Review_count(self):
        """testing the Review.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_User_count(self):
        """testing the User.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_State_count(self):
        """testing the State.count command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_City_count(self):
        """testing the City.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Amenity_count(self):
        """testing the Amenity.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_Place_count(self):
        """testing the Place.count() command """
        with patch('sys.stdout', new=StringIO()) as output:
            pat = r"\d+"
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertRegex(output.getvalue().strip(), pat)

    def test_update_BaseModel(self):
        """testing the Place.count() command """
        bm_obj = BaseModel()
        id = bm_obj.id
        command = f'BaseModel.update("{id}", "age", "20")'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(bm_obj.age, "20")

    def test_User_update(self):
        """Testing update method for User"""
        user_obj = User()
        id = user_obj.id
        user_obj.update("name", "John")
        self.assertEqual(user_obj.name, "John")

    def test_State_update(self):
        """Testing update method for State"""
        state_obj = State()
        id = state_obj.id
        state_obj.update("state_name", "California")
        self.assertEqual(state_obj.state_name, "California")

    def test_City_update(self):
        """Testing update method for City"""
        city_obj = City()
        id = city_obj.id
        city_obj.update("city_name", "San Francisco")
        self.assertEqual(city_obj.city_name, "San Francisco")

    def test_Place_update(self):
        """Testing update method for Place"""
        place_obj = Place()
        id = place_obj.id
        place_obj.update("address", "123 Main St")
        self.assertEqual(place_obj.address, "123 Main St")

    def test_Amenity_update(self):
        """Testing update method for Amenity"""
        amenity_obj = Amenity()
        id = amenity_obj.id
        amenity_obj.update("type", "WiFi")
        self.assertEqual(amenity_obj.type, "WiFi")

    def test_Review_update(self):
        """Testing update method for Review"""
        review_obj = Review()
        id = review_obj.id
        review_obj.update("rating", "5")
        self.assertEqual(review_obj.rating, "5")

    def test_create_missingclass(self):
        valid = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqaul(valid, output.getvalue().strip())

    def test_show_missingclass(self):
        valid = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(valid, output.getvalue().strip())

    def test_destroy_missingclass(self):
        valid = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(valid, output.getvalue().strip())

    def test_update_missingclass(self):
        valid = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(valid, output.getvalue().strip())

    def test_update_BaseModel(self):
        """Testing the update BaseModel command"""
        bm_obj = BaseModel()
        id = bm_obj.id
        command = f'update BaseModel {id} age "20"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(bm_obj.age, "20")

    def test_update_User(self):
        user_obj = User()
        id = user_obj.id
        command = f'update User {id} name "John"'
        user_obj.update("name", "John")
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(user_obj.name, "John")

    def test_update_State(self):
        state_obj = State()
        id = state_obj.id
        command = f'update State {id} state_name "California"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(state_obj.state_name, "California")

    def test_update_City(self):
        city_obj = City()
        id = city_obj.id
        command = f'update City {id} city_name "San Francisco"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(city_obj.city_name, "San Francisco")

    def test_update_Amenity(self):
        amenity_obj = Amenity()
        id = amenity_obj.id
        command = f'update Amenity {id} type "WiFi"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(amenity_obj.type, "WiFi")

    def test_update_Place(self):
        place_obj = Place()
        id = place_obj.id
        command = f'update Place {id} address "123 Main St"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(place_obj.address, "123 Main St")

    def test_update_Review(self):
        review_obj = Review()
        id = review_obj.id
        command = f'update Review {id} rating "5"'
        self.assertFalse(HBNBCommand().onecmd(command))
        self.assertEqual(review_obj.rating, "5")

    def test_destroy_BaseModel(self):
        """testing the destroy command"""
        inst1 = BaseModel()
        command = f"BaseModel.destroy {inst1.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_User(self):
        """testing the destroy command"""
        inst_u = User()
        command = f"User.destroy {inst_u.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_City(self):
        """testing the destroy command"""
        inst_c = City()
        command = f"City.destroy {inst_c.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_Place(self):
        """testing the destroy command"""
        inst_p = Place()
        command = f"Place.destroy {inst_p.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_State(self):
        """testing the destroy command"""
        inst_s = State()
        command = f"State.destroy {inst_s.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_Review(self):
        """testing the destroy command"""
        inst_r = Review()
        command = f"Review.destroy {inst_r.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)

    def test_destroy_Amenity(self):
        """testing the destroy command"""
        inst_a = Amenity()
        command = f"Amenity.destroy {inst_a.id}"
        given = ""
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(output.getvalue().strip(), given)


if __name__ == "__main__":
    unittest.main()
