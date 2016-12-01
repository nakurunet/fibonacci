def fibonaci (f):
    if isinstance(f,float):
        print "The number must be a whole number"
    if isinstance(f, str):
        print "Cannot allow letters"
    if isinstance(f, list):
        print "The input must not be a list"
    if isinstance(f,tuple):
        print "The input must not be a tuple"
    if (f>1000):
        print "large numbers not allowed!!!"
    if isinstance(f,bool):
        print "The number must not be a boolean"
    x = int(f)# input the amount of fibonaci numbers
    def fib():
        x = 0
        b = 1
        while 1:
            yield x
            x, b = b, x + b
    b = fib()
    b.next()

    for i in range(x):
        print b.next(),

 # to Hard code output, uncomment the next line       
 #fibonaci(5)
