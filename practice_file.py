import random
import urllib.request


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


def get_gander(sex='unknown'):
    if sex in ('m', 'male', 'boy', 'man'):
        sex = 'male'
    elif sex in ('f', 'female', 'gile', 'woman'):
        sex = 'female'
    else:
        print("invalid gander")
        return 0
    print(sex)


def dumb_sentence(name='Mich', action='ate', item='tuna'):
    print(name, action, item, '!')


def add_numbers(*tomato):
    total = 0
    for n in tomato:
        total += n
    print(total)


def health_calculator(age, apple_ate, cigs_smoke):
    remain = (80 - age) + apple_ate * 2 - cigs_smoke * 3.5
    print(remain)


goog_csv = "http://chart.finance.yahoo.com/table.csv?s=GOOG&a=10&b=6&c=2016&d=11&e=6&f=2016&g=d&ignore=.csv"


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


def download_csv_file(url):
    response = urllib.request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    dest_url = r'goog.csv'
    f = open(dest_url, 'w')
    f.write(csv_str)
    f.close()


'''
fw = open('sample.txt', 'w')
fw.write('Write something in my txt file.\n')
fw.write('End of the story.\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()
'''


def exception_handler():
    while True:
        try:
            number = int(input('What is your fav number?\n'))
            print('Good, I like', number, 'as well!')
            break
        except Exception as e:
            print(str(e))
            print('Dude, a number please....')
