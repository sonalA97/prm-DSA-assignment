#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem Statement - 1 (Data Structure)
# You are given a graph and a number x as input. Your task is to print the DFS traversal nodes of the 
# input graph starting from node x. Complete the following function in order to give the required output.
# Input Format:
# The first line of input contains a list containing sets representing a graph. The second line of input contains the number x. 
# Output Format:
# Complete the function in order to return the required output.
# Sample Input 0:
# [[1,0],[2,0],[3,0],[3,2]]
# 3
# Sample Output 0:
# 3 0 2 

from collections import defaultdict
class function:
    def __init__(self):
        self.given_graph = defaultdict(list)
    def setAdded(self, a, b):
        self.given_graph[a].append(b)
    def dbs(self, b, data):
        datas.add(n)
        print(b, end=' ')
        for i in self.given_graph[b]:
            if i not in datas:
                self.dfsReg(i, data)
    def dbs_transversal(self, n):
        data = set()
        return self.dbs(n, data)
        
        
obj = function()
obj.setAdded(1,0)
obj.setAdded(2,0)
obj.setAdded(3,0)
obj.setAdded(3,2)
print("Output is: ")
obj.dfs_transversal(3)


# In[ ]:


# Problem Statement - 2 ( Algorithms )
# Given a string str, your task is to write a program which takes a string str as its only input and 
# returns an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which 
# could be formed from the string str.
# Input Format:
# The first and only line of input contains string str.
# Output Format:
# The output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.
# Sample Input :
# abcdef
# Sample Output :
# 6
# Explanation:
# For string 'abcdef' palindromic subsequence are : "a" ,"b", "c" ,"d","e","f"

def palindromic_seq(x):
    length = len(x)
    l1 = [[0 for i in range(length + 2)]for j in range(length + 2)]
    for i in range(length):
        l1[i][i] = 1
    for k in range(2, length + 1):
        for i in range(length):
            m = k + i - 1
            if (m < length):
                if (str[i] == str[m]):
                    l1[i][m] = (l1[i][m - 1] +
                                 l1[i + 1][m] + 1)
                else:
                    l1[i][m] = (l1[i][m - 1] +
                                 l1[i + 1][m] -
                                 l1[i + 1][m - 1])
    return l1[0][length - 1]

given_str = "abcd"
print("Total Possible P_subsequence are : ", palindromic_seq(given_str))

