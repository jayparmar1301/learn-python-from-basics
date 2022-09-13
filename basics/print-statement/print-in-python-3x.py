"""""""""""""""""""""""""""""""""""""""""
# python 3.x
# in python 3, print is in-build function
"""""""""""""""""""""""""""""""""""""""""
print("hello")
#output: hello

print("Hello", "world")
#output will: Hello world

name = "Jay parmar"
country = "India"
print("My name is ", name, ', I am from', country)
print("My name is {}, I am from {}".format(name, country))
print("I love {1}, I am {0}".format(name, country))
print("My name is %s, I am from %s".format(name, country))
print("My name is {name}, I am from {country}".format(name=name, country=country))
#only supported after python3.6
print(f'My name is {name}, I am from {country}')

#output: My name is Jay parmar, I am from India
#output: My name is Jay parmar, I am from India
#output: I love India, I am Jay parmar
#output: My name is Jay parmar, I am from India
#output: My name is Jay parmar, I am from India
#output: My name is Jay parmar, I am from India


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
reference documents:
https://peps.python.org/pep-3105/
https://mail.python.org/pipermail/python-dev/2005-September/056154.html
https://www.delftstack.com/howto/python/how-to-print-multiple-arguments-in-python/
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""