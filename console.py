#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.base_model import BaseModel


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
        if args == "BaseModel":
            pass
        elif args == '':
            "** class name missing **"
        else:
            "** class doesn't exist **"

    def do_show(self, args):
        """Show string representation of object"""
        if isinstance(args[0], BaseModel) and args[1] == args[0].id:
            f"{args[0].__str__()}"
        elif args[0] == '':
            "** class name missing **"
        elif args[1] == '':
            "** instance id missing **"
        elif isinstance(args[0], BaseModel) is False:
            "** class doesn't exist **"
        else:
            "** no instance found **"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
