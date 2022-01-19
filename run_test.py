import unittest
from tests.pub_test import TestPub
# when python3 run_tests.py / name will = main / this checks if this is the file we are running.
# __name__ is a variable set by python / moste of the time it will be the name of the file/module, 
# but if we execute this through the terminal, python is going to change that name into the string
# this then bocomes the entry point of our applycation.
# __name__= classes.filename if another file passes from the entry point 
# if the file is this file then __name__=__main__ because this is the mail file.
if __name__ == "__main__":
        unittest.main()