from .handy_things import UsefulClass
from . import more_handy_things

class DoATask:
    def __init__(self):
        print("initialising task")
        self.useful = UsefulClass()

    def do_task(self):
        print("doing a task")
        self.useful.help_with_task()
        more_handy_things.do_useful_thing()
