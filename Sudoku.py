# Sudocu solver as an excercise in Python
# have fun!

# Constants
scBoxX=3      #Max 6, but not recomendet
scBoxY=3     #Max 6, but not recomendet
scValues=['&', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A',
'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Variable=True
Constant=False
Empty=0

scFile=open("Sudoku.txt")
spam=scFile.readline()   # first line contain basic infor
print(spam)

spam=scFile.readline()
scBoxX=int(spam[0])      # secont line contain BoxSize in X direction

spam=scFile.readline()
scBoxY=int(spam[0])      # third line contain BoxSize in Y direction

spam=scFile.readline()   # skip the forth line


# now we take the sudoku from the Sudoku.txt
#
size=scBoxX*scBoxY
spam=[]
for n in range(size):
    spam.append(scFile.readline())

# now we initialise an empty Sudoku with planty of '0'
# and mark them as Variables ('True')
#
sudoku=[]
for n in range(size):
    sudoku.append([])
    for m in range(size):
        sudoku[n].append([Empty,Variable])

# and finaly we read carefuly the input and transform
# it into our sudoku matrix.
#
for y in range(len(spam)):              # for every line
    if len(spam[y])>size:
        lineX=size
    else:
        lineX=len(spam[y])
    for x in range(lineX):               # for every column
        if scValues.count(spam[y][x].upper())==1:
            sudoku[y][x]=[scValues.index(spam[y][x].upper()), Constant]
            if sudoku[y][x][0]>(scBoxX*scBoxY):
                sudoku[y][x]=[Empty, Variable]

# at this moment our basic sudoku is done.
# all numbers are at the correct place and
# all constants are marked as 'False'.
# we could begin with the search for the correct numbers but let's check
# if the constant numbers make sens
#
i=0
for j in range((scBoxX*scBoxY)**2):
    y=j//(scBoxX*scBoxY)
    x=j%(scBoxX*scBoxY)
    if sudoku[y][x][0]!=0:
        row=[egg[0] for egg in sudoku[y]]
        col=[egg[x][0] for egg in sudoku]
        box=[]
        for n in range(scBoxY):
            for m in range(scBoxX):
                box.append(sudoku[(y/scBoxY)*scBoxY+n][(x/scBoxX)*scBoxX+m][0])
        if row.count(sudoku[y][x][0])>1 or col.count(sudoku[y][x][0])>1 or box.count(sudoku[y][x][0])>1:
            i=-1
            print(j)
# in case the preset sudoku has a bug the counter 'i=-1'and
# the solving loop dont get started. this is the same value
# as in case solver cannot find a solution: a short-cut.
# now the solving loop start.
#
print(sudoku)
loopcounter=0
checker=0
direction=True
while i<((scBoxX*scBoxY)**2) and i>=0:
    if direction==True:                            # if forward

        y=i//(scBoxX*scBoxY)                       # calculate y
        x=i%(scBoxX*scBoxY)                        # and x

        if sudoku[y][x][1]:                        # if field is Variable
            if sudoku[y][x][0]==(scBoxX*scBoxY):   # if field is MAX
                sudoku[y][x][0]=0                  # set field to =0
                direction=False                    # and set direction to backward
            else:                                  # field is not '9'!
                loopcounter+=1
                sudoku[y][x][0]=sudoku[y][x][0]+1  # count up
                row=[egg[0] for egg in sudoku[y]]  # determin the numbers in the row
                col=[egg[x][0] for egg in sudoku]  # and collums
                box=[]
                for n in range(scBoxY):            # and the box
                    for m in range(scBoxX):
                        box.append(sudoku[(y/scBoxY)*scBoxY+n][(x/scBoxX)*scBoxX+m][0])

                # in case the number is unique we can jump the the next field
                if row.count(sudoku[y][x][0])==1 and col.count(sudoku[y][x][0])==1 and box.count(sudoku[y][x][0])==1:
                    i=i+1
   
        else: # in case field is 'constant' simply jump to the next one
            i=i+1
        if (x==0 and y>1) :                                   # !!            
            if checker<loopcounter//(500*(scBoxX*scBoxY)**2): # !!
                print(loopcounter)                            # !!
                checker=loopcounter//(500*(scBoxX*scBoxY)**2) # !!
                for scot in range(scBoxX*scBoxY):             # !!
                    row=[egg[0] for egg in sudoku[scot]]      # !!
                    print('{0}->{1}'.format(scot+1, row))     # !! this is only to let you see how the numbers were found
##            else:
##                row=[egg[0] for egg in sudoku[y-1]]  # !!
##                print('{0}->{1}'.format(y, row)) # !! this is only to let you see how the numbers were found               
##
##                row=[egg[0] for egg in sudoku[y]]  # !!
##                print('{0}->{1}'.format(y+1, row)) # !! this is only to let you see how the numbers were found               
    if direction==False:               # if we go backwards
        i=i-1                          # logicaly we go one field back
        y=i//(scBoxX*scBoxY)
        x=i%(scBoxX*scBoxY)
        direction = sudoku[y][x][1]    # and set the direction forward if field is Variable.
# done sudoku is solved. now we need to print it nice out.
if i<1:
    print(' ')
    print('there is no solution to your Sudoku')
else:
    print(sudoku)
    print(' ')
    for n in range(scBoxX*scBoxY):
        if n%scBoxY==0:
            print('*****'+'*'*(scBoxX*scBoxY)+'*'*(scBoxY))
        spam=''
        row=[egg[0] for egg in sudoku[n]]
        for m in range(len(row)):
            spam=spam+scValues[row[m]]
        knight='    '+'{0}> '.format(n+1)
        knight=knight[-5:]
        for ni in range(scBoxY):
            knight=knight+spam[(ni*scBoxX):((ni+1)*scBoxX)]+"*"
        print(knight)
    print('*****'+'*'*(scBoxX*scBoxY)+'*'*(scBoxY))
    print(' ')
    print(loopcounter)

