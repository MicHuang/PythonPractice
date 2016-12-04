def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def ask_ok(promp, retries=4, reminder="Plz try again!"):
    while True:
        ok = input(promp)
        if ok in ("y", "ye", "yes"):
            return True
        if ok in ("n", "no", "nope"):
            return False
        retries -= 1
        if retries < 0:
            print(reminder)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot('a million', 'bereft of life', 'jump')
