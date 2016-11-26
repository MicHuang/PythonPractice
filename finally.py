try:
    f = open("1.txt")
    print int(f.read(2))
finally:
    print "File close"
    f.close()
