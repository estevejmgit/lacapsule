"""Prints args"""
def welcome(name, age):
    print(name, age) 
# welcome('jm',48)

"""Prints all the arguments"""
def display_elems(*args):
    for arg in args:
        print(arg)
# display_elems("okidoko",123,'33', '#-è', [1,2,3])

"""Return both addition - subtraction"""
def calculation(a, b):
    return a + b, a - b
# print(calculation(2,3))O
"""Obtain return in separate var"""
# var1, var2 = calculation(30,20)
# print(var1, var2)

"""Set default value arg"""
def show_employee(name,salary=9000):
    print("Name: %s salary: %.2f" % (name, salary))
# show_employee("Moi", 20000)

"""Closure functions"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
# closure = outer_function(10)
# result = closure(5)
# print(type(closure))  # Output: <class 'function'>
# print(result)  # Output: 15

"""Recursive call"""
def add_from_0_to_n(n):
    if n:
        return n + add_from_0_to_n(n - 1)
    else:
        return 0
# print(add_from_0_to_n(10))

"""Alias name for functions"""
def display_student(name, age):
    print(name, age)
# assign new name
showStudent = display_student
# # call using new name
# showStudent("Emma", 26)

"""Use of lambda function"""
def myfunc(n):
  return lambda a : a * n
# print(type(myfunc))
mytripler = myfunc(3)
# print(mytripler(11))