import time

def timetest(input_func):

    def timed(*args, **kwargs):

        start_time = time.time()
        result = input_func(*args, **kwargs)
        print args
        print kwargs
        end_time = time.time()
        print "Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        )
        print result
    return timed


@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print "inside foobar"
    print args, kwargs





def add(*args):
    a = 0
    if len(args)>0:
        for i in args:
            a+=i
    return a

# print add(1,2,4,5)
# foobar(["hello, world"], foo=2, bar=5)


def square(func):
    def inner_func(*args,**kwargs):
        print "inside decorator"
        result = func(*args,**kwargs)
        return result
    return inner_func()

@square
def numbers_sum(*args,**kwargs):
    a = args
    b = kwargs
    print a
    print b
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        return "Fucking Hell"


numbers_sum(1,2)