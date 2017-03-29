def anagram(S1,S2):
    """ Checks if the two strings are anagram or not"""
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()

    if len(S1) != len(S2): return False   # Edge case check

    count = {}
    for x in S1:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    for x in S2:
        if x in count:
            count[x] -= 1
        else:
            count[x] = 1

    for i in count:
        if count[i] !=0:
            return False

    return True

def anagram2(S1,S2):
    """ Checks if the two strings are anagram or not"""
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()

    if len(S1) != len(S2): return False   # Edge case check

    count = {}
    for (x, y) in zip(S1,S2):
        count[x] = count.get(x,0)+1
        count[y] = count.get(y,0)-1


    for i in count:
        if count[i] !=0:
            return False

    return True


def anagram3(S1,S2):
    """ Checks if the two strings are anagram or not"""
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()

    if len(S1) != len(S2): return False   # Edge case check

    sum1=0
    sum10 = 0
    sum2=0
    sum20 = 0

    for (x, y) in zip(S1,S2):
        sum1 = sum1 + ord(x)
        sum2 = sum2 + ord(y)
        sum10 = sum10 + ord(x)*ord(x)/2
        sum20 = sum20 +ord(y)*ord(y)/2
    if sum1 == sum2 and sum10 == sum20:
            return True

    return False

import time

str1 = ['atima', 'dog','Tom Marvolo Riddle', 'Fir Cones','Tom Marvolo Riddle dog Fir Cones']
str2 = ['aogta', 'god', 'I am Lord Voldemort','Conifers', 'I am Lord Voldemort God Conifers']

for i in range(len(str1)):
    
    start = time.time()
    bool1 = anagram(str1[i], str2[i])
    t1 = time.time() - start

    start = time.time()
    bool2 = anagram2(str1[i], str2[i])
    t2 = time.time() - start

    start = time.time()
    bool3 = anagram3(str1[i], str2[i])
    t3 = time.time() - start

    print("Result", bool1, bool2, bool3, "Time", t1, t2, t3)
