#!/usr/bin/python3
"""
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        "EOF"
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        "Create a new class ex: create class_name"
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            cls_new = BaseModel()
            storage.save()
            print(cls_new.id)

    def do_show(self, arg):
        list_arg = HBNBCommand.check_arg(arg)
        if list_arg:
            cls_dict = storage.all()
            cls_id = list_arg[0] + "." + list_arg[1]
            if cls_id in cls_dict.keys():
                print(cls_dict[cls_id])
            else:
                print("** no instance found **")

    @staticmethod
    def check_arg(arg):
        arg = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            return arg
        return []



if __name__ == '__main__':
    HBNBCommand().cmdloop()
