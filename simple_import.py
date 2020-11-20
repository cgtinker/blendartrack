import os

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

filename = path + "/EventListner.py"
exec(compile(open(filename) .read(), filename, 'exec'))