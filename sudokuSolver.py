from time import sleep
import ast

def findTriple(row,col,l):
    nums = [1,2,3,4,5,6,7,8,9]

    olanlar = []
    indisler = []

    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3)   for j in range(3)   if 0 <= row <= 2 and 0 <= col <= 2]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3)   for j in range(3,6) if 0 <= row <= 2 and 3 <= col <= 5]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3)   for j in range(6,9) if 0 <= row <= 2 and 6 <= col <= 8]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3,6) for j in range(3)   if 3 <= row <= 5 and 0 <= col <= 2]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3,6) for j in range(3,6) if 3 <= row <= 5 and 3 <= col <= 5]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(3,6) for j in range(6,9) if 3 <= row <= 5 and 6 <= col <= 8]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(6,9) for j in range(6,9) if 6 <= row <= 8 and 6 <= col <= 8]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(6,9) for j in range(3)   if 6 <= row <= 8 and 0 <= col <= 2]
    t = [olanlar.append(l[i][j]) if l[i][j] != 0 else indisler.append([i, j]) for i in range(6,9) for j in range(3,6) if 6 <= row <= 8 and 3 <= col <= 5]

    kalanlar = [x for x in nums if x not in olanlar]
    return kalanlar,indisler

def findRowCol(x,l):
    rowNot = []
    colNot = []

    t = [rowNot.append(l[x[0]][i]) for i in range(9) if l[x[0]][i] != 0]
    k = [colNot.append(l[j][x[1]]) for j in range(9) if l[j][x[1]] != 0]

    return rowNot,colNot

def solver(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                saveRow = i
                saveCol = j

                kalanlar, indisler = findTriple(saveRow, saveCol, sudoku)

                for xx in kalanlar:
                    counter = 0
                    for x in indisler:
                        rowNot, colNot = findRowCol(x, sudoku)

                        if (xx not in rowNot) and (xx not in colNot):
                            counter += 1
                            sakla = x

                    if counter == 1:
                        sudoku[sakla[0]][sakla[1]] = xx
                        changed = True

                        print("CHANGED !!!!!!!!!!!!!!!!!!")
                        print("###################################################")
                        for xy in sudoku:
                            print(xy)
                        print("###################################################")
    return sudoku

def chaosSolver(matrix):
    nums = [1,2,3,4,5,6,7,8,9]
    iSayac = 0
    okayBro = []
    leftOvers = {}
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                kalanlar, indisler = findTriple(i, j, matrix)
                rowNot, colNot = findRowCol([i,j],matrix)

                for x in kalanlar:
                    if x not in rowNot and x not in colNot:
                        okayBro.append(x)
                leftOvers[str([i,j])] = okayBro
                okayBro = []

    for key,val in leftOvers.items():
        # print("{} ---> {}".format(key,val))
        keyy = ast.literal_eval(key)
        if len(val) == 1:
            matrix[keyy[0]][keyy[1]] = val[0]

    return matrix, leftOvers

def twoSolver(leftOvers,matrix):
    for index1,(key1, val1) in enumerate(leftOvers.items()):
        for index2, (key2, val2) in enumerate(leftOvers.items()):
            if val1 == val2 and len(val1) == 2 and index1 != index2:
                keyy1 = ast.literal_eval(key1)
                keyy2 = ast.literal_eval(key2)
                print("{}-{} --> {} ###twoSolver".format(keyy1,keyy2,val1))

                matrix[keyy1[0]][keyy1[1]] = val1[0]
                matrix[keyy2[0]][keyy2[1]] = val1[1]
                return matrix
    return matrix

def twoSolverLast(leftOvers,matrix):
    for index1,(key1, val1) in enumerate(leftOvers.items()):
        for index2, (key2, val2) in enumerate(leftOvers.items()):
            if val1 == val2 and len(val1) == 2 and index1 != index2:
                keyy1 = ast.literal_eval(key1)
                keyy2 = ast.literal_eval(key2)
                print("{}-{} --> {} ###twoSolverLast".format(keyy1,keyy2,val1))

                matrix[keyy1[0]][keyy1[1]] = val1[1]
                matrix[keyy2[0]][keyy2[1]] = val1[0]
                return matrix
    return matrix




# l = [[8, 0, 0, 5, 0, 3, 0, 0, 9],
#      [0, 0, 0, 6, 0, 9, 7, 0, 0],
#      [0, 0, 4, 0, 7, 0, 0, 0, 5],
#      [4, 8, 0, 0, 0, 0, 0, 0, 6],
#      [0, 0, 2, 0, 0, 0, 4, 0, 0],
#      [9, 0, 0, 0, 0, 0, 0, 3, 8],
#      [6, 0, 0, 0, 8, 0, 1, 0, 0],
#      [0, 0, 1, 3, 0, 6, 0, 0, 0],
#      [7, 0, 0, 1, 0, 5, 0, 0, 2]]

# l = [[0,8,2,0,0,0,7,0,0],
#      [0,9,0,2,0,6,0,4,0],
#      [3,0,0,0,8,0,0,0,5],
#      [0,0,3,0,0,0,0,0,6],
#      [0,5,8,0,0,1,2,3,0],
#      [7,0,0,0,0,3,8,0,0],
#      [6,0,0,0,4,0,0,0,2],
#      [0,2,0,9,0,7,0,5,0],
#      [0,0,5,0,0,0,4,7,0]]

# l = [[0,0,0,0,4,0,0,0,0],
#      [0,5,8,0,1,0,0,7,6],
#      [0,7,9,0,6,0,0,2,1],
#      [0,0,4,0,0,3,2,0,8],
#      [0,0,0,4,0,2,0,0,0],
#      [3,0,7,6,0,0,9,0,0],
#      [5,4,0,0,2,0,7,9,0],
#      [7,6,0,0,3,0,8,4,0],
#      [0,0,0,0,5,0,0,0,0]]

l = [[0,0,0,2,6,0,7,0,1],
     [6,8,0,0,7,0,0,9,0],
     [1,9,0,0,0,4,5,0,0],
     [8,2,0,1,0,0,0,4,0],
     [0,0,4,6,0,2,9,0,0],
     [0,5,0,0,0,3,0,2,8],
     [0,0,9,3,0,0,0,7,4],
     [0,4,0,0,5,0,0,3,6],
     [7,0,3,0,1,8,0,0,0]]

# l = [[0,2,0,6,0,8,0,0,0],
#      [5,8,0,0,0,9,7,0,0],
#      [0,0,0,0,4,0,0,0,0],
#      [3,7,0,0,0,0,5,0,0],
#      [6,0,0,0,0,0,0,0,4],
#      [0,0,8,0,0,0,0,1,3],
#      [0,0,0,0,2,0,0,0,0],
#      [0,0,9,8,0,0,0,3,6],
#      [0,0,0,3,0,6,0,9,0]]

# l = [[0,0,5,0,0,7,0,0,0],
#      [0,0,0,0,0,0,0,0,9],
#      [8,9,0,5,0,0,4,0,0],
#      [0,3,0,8,0,0,0,4,0],
#      [0,0,0,0,0,3,2,0,7],
#      [4,7,0,0,0,0,5,0,0],
#      [0,0,0,0,0,0,7,8,0],
#      [6,0,0,0,0,0,0,0,0],
#      [0,0,0,4,0,6,1,0,0]]

#https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html
#ZOR
# l = [[0,0,0,6,0,0,4,0,0],
#      [7,0,0,0,0,3,6,0,0],
#      [0,0,0,0,9,1,0,8,0],
#      [0,0,0,0,0,0,0,0,0],
#      [0,5,0,1,8,0,0,0,3],
#      [0,0,0,3,0,6,0,4,5],
#      [0,4,0,2,0,0,0,6,0],
#      [9,0,3,0,0,0,0,0,0],
#      [0,2,0,0,0,0,1,0,0]]

#COK ZOR

# l = [[0,2,0,0,0,0,0,0,0],
#      [0,0,0,6,0,0,0,0,3],
#      [0,7,4,0,8,0,0,0,0],
#      [0,0,0,0,0,3,0,0,2],
#      [0,8,0,0,4,0,0,1,0],
#      [6,0,0,5,0,0,0,0,0],
#      [0,0,0,0,1,0,7,8,0],
#      [5,0,0,0,0,9,0,0,0],
#      [0,0,0,0,0,0,0,4,0]]
chaos = 0
twoSolverA = 0
twoSolverB = 0

sres = []
sLeftOvers = []
res = solver(l)
while True:

    res = solver(res)
    kontrol = [res[i][j] for i in range(9) for j in range(9)]

    if all(kontrol):
        print("###################################################")
        for xy in res:
            print(xy)
        print("###################################################")
        break

    chaos += 1
    twoSolverA += 1
    twoSolverB += 1
    if chaos > 800:
        res,leftOvers = chaosSolver(res)


    if twoSolverA > 1300:
        if twoSolverA == 1301:
            sLeftOvers = leftOvers
            sres = res
        res = twoSolver(leftOvers,res)

    if twoSolverB > 1800:
        res = twoSolverLast(sLeftOvers,sres)
        chaos = 0
        twoSolverA = 0
        twoSolverB = 0





