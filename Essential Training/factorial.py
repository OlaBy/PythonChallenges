#factorial function that returns the factorial of a non-negative integer
#parameter: a non-negative integer
def factorial(num):
    if type(num) != int:
      return None
    if num <  0:
      return None

    result=1
    i=1
    while i <= num:
      result=result*i
      i=i+1
    return result