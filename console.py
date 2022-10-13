#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Take empty line""" 
        pass

    def do_quit(self, args):
        """Exit program"""
        return True

    def do_EOF(self, args):
        """End of file"""
        return True

    def do_create(self, args):
        """Create instance of BaseModel"""
        tok = args.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                nins = eval(tok[0])()
                nins.save()
                print(nins.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Show string representation of object"""
        tok = args.split()
        if len(tok) == 0:
            print("** class name missing **")
        else:
            if len(tok) == 1:
                print("** instance id missing **")
            try:
                eval(tok[0])
            except:
                print("** class doesn't exist **")

            ky = f"{tok[0]}.{tok[1]}"
            try:
                print(storage.all()[ky])
            except:
                print("** no instance found **")


    def do_destroy(self, args):
        """Destroy object"""
        tok = args.split()
        if len(tok) == 0:
            print("** class name missing **")
        if len(tok) == 1:
            print("** instance id missing **")
        try:
            eval(tok[0])
        except:
            print("** class doesn't exist **")

        ky = f"{tok[0]}.{tok[1]}"
        try:
            del storage.all()[ky]
        except:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        """Prints string representation of class"""
        tok = args.split()
        if len(tok) == 0:
            print("** class name missing **")
        try:
            eval(tok[0])
        except:
            print("** class doesn't exist **")

        el = []
        for key, value in storage.all().items():
            if tok[0] == value.__class__.__name__:
                el += list(value.__str__())
        print(el)

    def do_update(self, args):
        """Updates instance attribute"""
        tok = args.split()
        if len(tok) == 0:
            print("** class name missing **")
        if len(tok) == 1:
            print("** instance id missing **")
        if len(tok) == 2:
            print("** attribute name missing **")
        if len(tok) == 3:
            print("** value missing **")
        try:
            eval(tok[0])
        except:
            print("** class doesn't exist **")

        ky = f"{tok[0]}.{tok[1]}"
        if ky not in storage.all():
            print("** no instance found **")

        for key, value in storage.all().items():
            if tok[0] == value.__class__.__name__ and tok[1].strip('"') == value.id:
                setattr(value, tok[2], tok[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
