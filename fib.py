# I don't know who came up with this, but it wasn't me
# it calculates the Fibonacci sequence the number of 
# times you enter

howMany = input("How many Fibonaccis?: ")

def isfloat(string):
	try:
		int(string)
		return True
	except ValueError:
		print("Exiting")
		exit()

while isfloat(howMany):
    howMany = int(howMany)
    fibonacci = (lambda n, first=0, second=1:
        [] if n == 0 else
        [first] + fibonacci(n - 1, second, first + second))
    print(fibonacci(howMany))
    howMany = input("How many Fibonaccis?: ")
