#make a decorator that adds 1 to the return value of another function that multiplies two numbers

def decorator(func):
  def inner(*args, **kwargs):    
    product = func(*args, **kwargs)
    return product + 1
  return inner

@decorator
def multiply(num1, num2):
  return num1*num2

print(multiply(2,2))
#5