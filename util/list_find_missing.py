xpected = [1,"F", 5, 6, "DFG", 7, 3, 9, 34, 3]
actual = ["F", 2, 3, "ASFFSA", 5, 2, 3]
i = 0
j = 0
missing = []
extra = []
try:
    while True:
        found = False
        try:
            while expected[i] != actual[j]:
                i+=1
            else:
                found = True
        except:
            if not found:
                extra.append(actual[j])
        finally:
            i = 0
            j+=1
         
except:
    print extra 
