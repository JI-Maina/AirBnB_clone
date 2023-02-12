#!/usr/bin/python3
"""Defines entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of command interpreter."""

    prompt = '(hbnb) '
    class_names = ['BaseModel', 'User']

    def do_create(self, line):
        """Creates new instance of BaseModel, saves it (to file) & prints id."""

        if line == '':
            print("** class name missing **")
        elif line not in self.class_names:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints str representation of an instance based on cls name & id."""

        if line == '':
            print("** class name missing **")
        else:
            line = line.split()
            if len(line) != 2:
                print("** instance id missing **")
            elif line[0] not in self.class_names:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if line[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on cls name & id (and saves change)."""
        
        if not line:
            print("** class name missing **")
        else:
            line = line.split()
            if len(line) != 2:
                print("** instance id missing **")
            elif line[0] not in self.class_names:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if line[1] == value.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, line):
        """Prints all str rep of all instances based or not on cls name."""

        lis = []
        if not line:
            for value in storage.all().values():
                lis.append(str(value))
            print(lis)
        elif line not in self.class_names:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                lis.append(str(value))
            print(lis)

    def do_update(self, line):
        """Updates an instance based on cls name & id by adding or updating."""
        
        if not line:
            print("** class name missing **")
            return False
        line = line.split()
        if line[0] in self.class_names:
            if len(line) > 1:
                key = line[0] + '.' + line[1]
                if key in storage.all():
                    if len(line) > 2:
                        if len(line) > 3:
                            setattr(storage.all()[key], line[2], line[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
