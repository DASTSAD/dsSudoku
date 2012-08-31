# Sudocu solver as an excercise in Python
# have fun!

print("""
please input your Sudoku you wish to solve in the folowing form:

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
spam=[]
for y in range(9):
    spam.append(raw_input('{0} >'.format(y+1)))

# now we initialise an empty Sudoku with planty of '0'
# and mark them as Variables ('True')
#
sudoku=[]
for y in range(9):
    sudoku.append([])
    for x in range(9):
        sudoku[y].append([0,True])

# anf finaly we read carefuly the input and transform
# it into our sudoku matrix.
#
for y in range(len(spam)):              # for every line
    for x in range(len(spam[y])):       # for every column
        if spam[y][x].isdigit():        # check if the character is a number
            if int(spam[y][x])>0:       # and bigger then '0'
                sudoku[y][x]=[int(spam[y][x]),False]



# at this moment our basic sudoku is done.
# all numbers are at the correct place and
# all constants are marked as 'False'.
# we could begin with the search for the correct numbers but let's check
# if the constant numbers make sens
#
i=0
for j in range(81):
    y=j//9
    x=j%9
    if sudoku[y][x][0]!=0:
        row=[egg[0] for egg in sudoku[y]]
        col=[egg[x][0] for egg in sudoku]
        box=[]
        for n in range(3):
            for m in range(3):
                box.append(sudoku[y/3*3+n][x/3*3+m][0])
        if row.count(sudoku[y][x][0])>1 or col.count(sudoku[y][x][0])>1 or box.count(sudoku[y][x][0])>1:
            i=-1
# in case the preset sudoku has a bug the counter 'i=-1'and
# the solving loop dont get started. this is the same value
# as in case solver cannot find a solution: a short-cut.
# now the solving loop start.
#
direction=True
while i<81 and i>=0:
    if direction==True:                    # if forward
        y=i//9                             # calculate y
        x=i%9                              # and x
        if sudoku[y][x][1]:                # if field is variable
            if sudoku[y][x][0]==9:         # and field is =9
                sudoku[y][x][0]=0          # set field to =0
                direction=False            # and set direction to backward
            else:                          # field is not '9'!
                sudoku[y][x][0]=sudoku[y][x][0]+1 # count up
                row=[egg[0] for egg in sudoku[y]] # determin the numbers in the row
                col=[egg[x][0] for egg in sudoku] # and collums
                box=[]
                for n in range(3):                # and the box
                    for m in range(3):
                        box.append(sudoku[y//3*3+n][x//3*3+m][0])

                # in case the number is unique we can jump the the next field
                if row.count(sudoku[y][x][0])==1 and col.count(sudoku[y][x][0])==1 and box.count(sudoku[y][x][0])==1:
                    i=i+1
        else: # in case field is 'constant' simply jump to the next one
            i=i+1
    if direction==False:               # if we go backwards
        i=i-1                          # logicaly we go one field back
        y=i//9
        x=i%9
        direction = sudoku[y][x][1]    # and set the direction forward if field is Variable.
    row=[egg[0] for egg in sudoku[y]]  # !!
    print('{0}->{1}'.format(y+1, row)) # !! this is only to let you see how the numbers were found
# done sudoku is solved. now we need to print it nice out.
if i<1:
    print('there is no solution to your Sudoku')
else:
    print(' ')
    for n in range(9):
        if (n%3)==0:
            print('*****************')
        row=[egg[0] for egg in sudoku[n]]
        spam=''
        for m in range(len(row)):
            spam=spam+str(row[m])
        print('{0}>'.format(n+1)+spam[0:3]+'*'+spam[3:6]+'*'+spam[6:])
    print('*****************')


