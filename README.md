# Cloud-Counselage-L3-Python-Assignment

# PROBLEM STATEMENT

## CODING QUESTIONS:1
Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.
Input Format

The first line contains the first integer, a. The second line contains the second integer, b.
Constraints

```
1<_a<_1010
1<_b<_1010

Output Format
Print the three lines as explained above.
Sample Input
3 2
Sample Output
5 1 6
```

## CODING QUESTIONS:2

We add a Leap Day on February 29, almost every four years. The leap day is an extra,
or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap
years:
● The year can be evenly divided by 4, is a leap year, unless:
● The year can be evenly divided by 100, it is NOT a leap year, unless:
● The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Task
You are given the year, and you have to write a function to check if the year is a leap or
not.
```
Input Format
Read y, the year that needs to be checked.
Constraints
1900<_y<_10
Output Format
The output is taken care of by the template. Your function must return a boolean value
(True/False)
Sample Input
1990
Sample Output
False
```

## CODING QUESTIONS:3

You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.

Constraints
1<_n<_105
The sum of the lengths of all the words do not exceed 106
All the words are composed of lowercase English letters only.
```
Input Format
The first line contains the integer,n.
The next n lines each contain a word.
Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according
to their appearance in the input.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
```

## CODING QUESTIONS:4

Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
```
Input Format :
There are two integers, a and b as input to the program.
Output Format:
 Print the number of common factors of a and b. Both the input value should be in a
range of 1 to 10^12.
Input:
10
15
Output:
2
```

## CODING QUESTIONS:5

You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.

```
Input string:
ababacd
Output string:
Abcd
```

## CODING QUESTIONS:6

Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the
column starting with index 0.
The matrix will hold distinct integers as elements.
We need to find a distinct number of positional elements which are either the minimum
or maximum in their corresponding row or column.
Please return -1 if any row or any column has multiple minimum or maximum
elements.
```
For example, given a matrix of size 3*3, the elements are stored as follows.
1 3 4
5 2 9
8 7 6

The expected output is 7.

In the above example, we identified the output as 7 based on below.
1 - minimum in row and column
4 - Maximum in row
2 - Minimum in column and row
9 - Maximum in row and column
8 - Maximum in row and column
7 - Maximum in column
6 - Minimum in row

Input:
m - integer - number of rows
n - integer - number of columns
m * n matrix

Output:
r - integer - result

Constraints:
0<m,n<100

Elements in the matrix are positive integers.
```

## CODING QUESTIONS:7

Write a Python program to find the first appearance of the substring 'not' and 'poor' from
a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with
'good'. Return the resulting string.
```
Sample String :
'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result :
'The lyrics is good!'
'The lyrics is poor!'
```


## CODING QUESTIONS:8

Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
```
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
```

## CODING QUESTIONS:9

Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0).
```
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
```


## CODING QUESTIONS:10

Write a Python program to check whether a given a binary tree is a valid binary search
tree (BST) or not.
Let a binary search tree (BST) is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
```
Example 1:
 2
 / \
 1 3
Binary tree [2,1,3], return true.

Example 2:
 1
 / \
 2 3

Binary tree [1,2,3], return false.
```

## CODING QUESTIONS:11

Write a Python program to sort a list of elements using the selection sort algorithm.
Note: The selection sort improves on the bubble sort by making only one exchange for
every pass through the list.
```
Sample Data:
 [14,46,43,27,57,41,45,21,70]
Expected Result:
 [14, 21, 27, 41, 43, 45, 46, 57, 70]
```


## CODING QUESTIONS:12

Write a Python program to get a week number.
```
Sample Date :
 2015, 6, 16
Expected Output :
25
```

## CODING QUESTIONS:13

Write a Python program to count the number of students of the individual class.
```
Sample data:
classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)

Expected Output:
Counter({'VI': 3, 'Example 1:V': 2, 'VII': 1})
```
