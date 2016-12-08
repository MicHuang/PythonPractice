import threading


class Teacher():
    def teacher_class(self):
        print('I am teaching science.')


class Stripper():
    def dance(self):
        print('I am dancing.')


class GoodTeacher(Teacher, Stripper):
    pass


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


'''
send = Messenger(name='Sender start')
receive = Messenger(name='receiver start')
send.start()
receive.start()
'''
