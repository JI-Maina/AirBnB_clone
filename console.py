#!/usr/bin/python3
"""Defines entry point of the command interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
