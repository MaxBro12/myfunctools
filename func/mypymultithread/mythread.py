from threading import Thread


class MyThread(Thread):
    def __init__(self, func, args: tuple | None = None):
        Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        try:
            if self.args is None:
                self.func
            else:
                self.func(self.args)
        except TypeError:
            pass
