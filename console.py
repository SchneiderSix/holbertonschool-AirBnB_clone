#!/usr/bin/python3
"""
Module Console
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
