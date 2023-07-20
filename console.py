#!/usr/bin/python3

"""
the command interpreter that is the entry point
"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """
    content search for other functions
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    implementation of the quit, EOF and help commands
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_nothing(self, arg):
        """
        a class method to implement nothing
        """
        pass

    def do_all(self, arg):
        """
        Implementation of the quit method
        """
        return True

    def do_EOF(self, arg):
        """
        method to signal the close of the program
        """
        print("")
        return True

    def do_create(self, arg):
        """
        method to create a new class instance
        prints the id
        """
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg1 = parse(arg)
        obj_dict = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg1[0], arg[1])])

    def do_destroy(self, arg):
        """
        this method deletes an instance based
        on the class name and id
        """

        arg1 = parse(arg)
        obj_dict = storage.all()
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg1[0], arg1[1])]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg1 = parse(arg)
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(arg1) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_count(self, arg):
        """
        Retrieves the number of instances of specific classes
        """
        arg1 = parse(arg)
        count = 0
        for o in storage.all().values():
            if arg1[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        arg1 = parse(arg)
        obj_dict = storage.all()

        if len(arg1) == 0:
            print("** class name missing **")
            return False

        if arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        if len(arg1) == 1:
            print("** instance id missing **")
            return False

        if "{}.{}".format(arg1[0], arg1[1]) not in obj_dict.keys():
            print(" **no instance found ")
            return False

        if len(arg1) == 2:
            print("** attribute name missing **")
            return False

        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg1) == 4:
            obj = obj_dict["{}.{}".format(arg[0], arg1[1])]
            if arg1[2] in obj.__class__.__dict__.keys():
                valueType = type(obj.__class__.__dict__[arg1[2]])
                obj.__dict__[arg1[2]] = valueType(arg1[3])
            else:
                obj.__dict__[arg1[2]] = arg1[3]
        elif type(eval(arg1[2])) == dict:
            obj = obj_dict["{}.{}".format(arg1[0], arg1[1])]
            for key, value in eval(arg[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valueType(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
