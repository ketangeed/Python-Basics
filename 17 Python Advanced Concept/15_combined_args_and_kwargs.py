# first args then kwargs that is the condition..

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(1, 3, 4, 6, ketan=899, shubham=67)