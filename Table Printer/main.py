tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    '''prints columns of tableData with dynamic justifying
    '''
    index = 0
    colWidths = [0] * len(tableData)
    for list in tableData:
        for item in list:
            current_length = len(item)
            if current_length > colWidths[index]: colWidths[index] = current_length
        index += 1

    for i in range(len(tableData[0])):
        line = ""
        for j in range(len(tableData)):
            line += tableData[j][i].rjust(colWidths[j]+1)
        print(line)

printTable()

# better, optimized version
def printTable2():
    colWidths = [max(len(item) for item in column) for column in tableData]

    for i in range(len(tableData[0])):
        line = "".join(tableData[j][i].rjust(colWidths[j] + 1) for j in range(len(tableData)))
        print(line)
        
printTable2()