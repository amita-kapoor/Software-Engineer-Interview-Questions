# Software-Engineer-Interview-Questions
Conatins multi solutions for different SE interview questions

## Anagram:
A common problem to access knowledge about arrays/strings and their working is Anagram check. The Problem statement is simple, given two strings determine it they are anagram or not.


__anagram.py__ contains three different implementations of the problem. In terms of time complexity all three are O(n), but because of computations involved in between they take slightly different times.

anagram1 and anagram2 functions both use 'dict' of python to solve the problem, they only differ in the way they handle 'keyerror' for accessing dictionary key without being initialized. Function anagram1 performs if check before accessing key value, and anagram2 uses 'get' method to get key values if they are assigned and returns zero if they are not assigned.
Function anagram3 uses a different approach, it adds the sum of unicode/char value of all the characters in the strings, and to ensure it works uses non-linear square sum as well.
