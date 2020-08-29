import time

class Counter:
    def __init__(self, function):
        self.runs = 100
        self.func = function

    def __call__(self, *args, **kwargs):
        avg = 0
        for x in range(self.runs):
            start = time.time()
            self.func(*args, **kwargs)
            finish = time.time()
            avg = (finish - start) / self.runs
        f = self.func.__name__
        print(
            "Среднее время выполнения %s запусков: %.5f секунд" % (f, self.runs, avg)
            )
        return self.func(*args, **kwargs)