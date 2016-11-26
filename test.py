class Fib(object):

    List = [0]
    last = 1

    def __init__(self):
        pass

#    def __str__(self):
#        return str(Fib.List)

#    def __len__(self):
#       return self.num

    def __call__(self, num):
        for i in range(1, num):
            Fib.List.append(Fib.last)
            Fib.last += Fib.List[-2]
        return str(Fib.List)

f = Fib()
print f(10)
