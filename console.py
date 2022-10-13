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
        if not tok[0]:
            print("** class name missing **")
        try:
            nins = eval(tok[0])()
            nins.save()
            print(nins.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Show string representation of object"""
        tok = args.split()
        if not tok[0]:
            print("** class name missing **")
        if not tok[1]:
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
        if isinstance(args[0], BaseModel) and args[1] == args[0].id:
            pass
        elif args[0] == '':
            "** class name missing **"
        elif args[1] == '':
            "** instance id missing **"
        elif isinstance(args[0], BaseModel) is False:
            "** class doesn't exist **"
        else:
            "** no instance found **"

    def do_all(self, args):
        """Prints string representation of class"""
        if isinstance(args[0], BaseModel):
            print('\n'.join(BaseModel.instances))
        else:
            "** class doesn't exist **"

    def do_update(self, args):
        """Updates instance attribute"""
        if args[0] == '':
            "** class name missing **"
        elif isinstance(args[0], BaseModel) is False:
            "** class doesn't exist **"
        elif args[1] == '':
            "** instance id missing **"
        elif isinstance(args[0], BaseModel) and args[1] != args[0].id:
            "** no instance found **"
        elif args[2] == '':
            "** attribute name missing **"
        elif args[3] == '':
            "** value missing **"
        else:
            args[0].args[2] = args[3]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
