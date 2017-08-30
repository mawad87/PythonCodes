from sys import argv

script, filename = argv

print "We're going to read %r." % filename

txt = open(filename, 'r')

print txt.read()

txt.close()