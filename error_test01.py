import os

try:

    f = open("1.txt")
    line = f.read(2)
    num = int(line)
    f.seek(-5, os.SEEK_SET)

    print "Read num: %s" % num

except IOError, e:
    print "Catch IOError:", e

except ValueError, e:
    print "Catch ValueError:", e

else:
    print "No Error"

finally:
    try:
        f.close()
        print "File close"
    except NameError, e:
        print "Cathch Error:", e

print "try-finally:", f.closed

print

try:
    with open("1.txt") as f1:
        for line in f1.read():
            num = int(line)
            f.seek(-5, os.SEEK_SET)
            print "Read num: %s" % num
except ValueError, e:
    print "Catch Error:", e
    print "with-as:", f1.closed
