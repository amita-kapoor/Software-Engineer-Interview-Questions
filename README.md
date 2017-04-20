# Software-Engineer-Interview-Questions
Conatins multi solutions for different SE interview questions

## Anagram:
A common problem to access knowledge about arrays/strings and their working is Anagram check. The Problem statement is simple, given two strings determine it they are anagram or not.


__anagram.py__ contains three different implementations of the problem. In terms of time complexity all three are O(n), but because of computations involved in between they take slightly different times.

anagram1 and anagram2 functions both use 'dict' of python to solve the problem, they only differ in the way they handle 'keyerror' for accessing dictionary key without being initialized. Function anagram1 performs if check before accessing key value, and anagram2 uses 'get' method to get key values if they are assigned and returns zero if they are not assigned.
Function anagram3 uses a different approach, it adds the sum of unicode/char value of all the characters in the strings, and to ensure it works uses non-linear square sum as well.

## Sorting:
Another common problem is sorting, sorting means given an array of n numbers we arrange the array in increasing or decreasing order. There exist various algorithms for sorting, each varying in time complexity. The file __sorting.py__ contains five different sorting algorithms. Each one is run on a randomly generated array, the program gives the the time taken by each as we increase the number of elements of the array.
### Bubble Sort
It is the simplest sort with O(n^2) time complexity.
In it the largest number is brought to the end by doing element wise comparision and swap.
The process is then repeated for array from range 0 to n-1 (nth is largest already)
Continue till we reach the array with only one element.

### Insertion Sort
This also has the time complexity of O(n^2)
This is more like how we arange playing cards in sequence while playing. We take a card compare it with all the elements on its left, one by one. If we find an element which is smaller  than this, then we insert the card to the right of this small card.
We repeat the process for all the elements.

### Selection Sort
Another O(n^2) sorting algorithm. 
In this we scan the array for the smallest element, once found we swap it with first element of the array.
Next we scan the array from (1-n) for next smallest element, after scanning whole array we swap the smallest element with first position.
We continue in this manner till we reach the last position of array.

### Quick Sort
While the worst case performance of quick sort is O(n^2) it gives __nlogn__ average time complexity.
In this we choose a pivot point, and divide array in two, one containing elements greater than pivot and another containing elements less than pivot. We put the pivot in middle of these two sub-parts.
Now recursively we perform the same operation on each sub part.

### Merge sort
This sort follows divide and conquer approach. the time complexity of Merge Sort is O(nlogn).
Here the array is divided into two sub parts (like quick sort) but exactly from the middle.
The process is repeated till on;y one element is left in the sub parts. the sub parts are then merged together in keeping into account that as sub arrays merge they keep the order.

The best way to understand sorting is to be able to visualize it, in my search I found this to be a good site demonstrating nice visualizations for each sorting algo. : https://visualgo.net/en/sorting

## Graphs
One of the most common data structure that is asked in interviews. It is otherwise as well very useful in analyzing networks, data organization and as my M.Sc thesis ( https://www.researchgate.net/publication/281294552_Interpretive_structural_modeling_based_knowledge_representation) tries to prove acn be also used for Knowledge Representation.

The code __graphs_as_dictionary.py__ gives a dictionary reprsentation of graphs. it can useful for graphs without weighted edges. the implementation given is for undirected graph, but can be modified to directed graphs as well.

The python file named __graphs_traversals.py__ again implements the graphs but this time as class object. The class contains method for adding an edge in the graph. And to perform topological sorting of the graph. Topological sorting arranges the nodes of the graph in a linear order it can be very useful for scheduling type problems, or to deal with dependencies (packages or classes :) ). The code implements the two common topological sorting algorithms: The DFS based topological sort and Kahn's Algorithm. If ||V|| is the number of vertices and ||E|| the number of edges, then both algorithm take O(||V||+||E||) worst case time.






