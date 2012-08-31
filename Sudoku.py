# Sudocu solver as an excercise in Python
# have fun!

# Constants
scBoxX=5      #Max 6, but not recomendet
scBoxY=5     #Max 6, but not recomendet
scValues=['&', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A',
'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Variable=True
Constant=False
Empty=0

print("""
please input your Sudoku you wish to solve in the folowing form (for a 3x3):

***6*5*89
*7**9*4*6
4**72**5*
**6***14*
94**1**72
*12***6**
*9**72**8
3*8*6**1*
12*8*3***

of course you can use anything instead of '*' to mark empty boxes, even a space ' '.
I used '*' only to make it more visible.
""")

# first we take the input of the Sudoku from the command line
#
size=scBoxX*scBoxY
spam=[]
for n in range(size):
    spam.append(raw_input('{0} >'.format(n+1)))

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
# in case the preset sudoku has a bug the counter 'i=-1'and
# the solving loop dont get started. this is the same value
# as in case solver cannot find a solution: a short-cut.
# now the solving loop start.
#
loopcounter=0
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
    if direction==False:               # if we go backwards
        i=i-1                          # logicaly we go one field back
        y=i//(scBoxX*scBoxY)
        x=i%(scBoxX*scBoxY)
        direction = sudoku[y][x][1]    # and set the direction forward if field is Variable.
    row=[egg[0] for egg in sudoku[y]]  # !!
    print('{0}->{1}'.format(y+1, row)) # !! this is only to let you see how the numbers were found
# done sudoku is solved. now we need to print it nice out.
if i<1:
    print(' ')
    print('there is no solution to your Sudoku')
else:
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

