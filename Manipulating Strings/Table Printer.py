import math


def printTable(table):
    arr = []
    for j in range(len(table)):
        mx=0
        for i in range(len(table[0])):
            mx=max(mx,len(table[j][i]))
        arr.append(mx)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(arr[j]), end=" ")
        print()

    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
