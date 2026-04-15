from time import perf_counter


def dec(func):
    def wrapper():
        start = perf_counter()
        func()
        end = perf_counter()
        print(end-start)
    return wrapper


@dec
def time():
    for i in range(50000):
        s = 5


time()


dict={}


def cache (func):
   def wrapper(*args,**kwargs):
       if dict.get(func):
          dict.update({func:func()})

    return wrapper()

