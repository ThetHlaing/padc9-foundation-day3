def decorator_with_args(function):
    def wrapper(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function(*args)
    return wrapper

@decorator_with_args
def function_with_noarguments():
    print("function_with_noarguments")

function_with_noarguments()


@decorator_with_args
def function_with_arguments(a, b, c,**kwargs):
    print(a, b, c,kwargs)
    print('function_with_arguments')

function_with_arguments(1,2,3,test='1')

@decorator_with_args
def function_with_keyword_arguments():
    print("function_with_keyword_arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")