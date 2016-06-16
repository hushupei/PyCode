import pdb
def foo():
    sum = 0
    for i in range(10000):
        sum += i
    sumA = bar()
    sumB = bar()
    return sum
     
def bar():
    sum = 0
    for i in range(100000):
        sum += i
    return sum
  
if __name__ == "__main__":
    import cProfile
    cProfile.run("foo()")