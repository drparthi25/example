mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict.iterkeys()):
    print "%s: %s" % (key, mydict[key])
for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
