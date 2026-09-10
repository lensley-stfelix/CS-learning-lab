#intro example to nested loops

multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,6):
    multiples[outer-1].append( outer * inner)
print(multiples)

#another example of nested loops, where we ahave a variable called matrix,
#the outer loop has 3 rows to iterate through,
#the inner loops says "hey, inside each row, look at the element and print it"
# the last line says, once you are done printing all the element
#in the row, your job now is to print the finished row. 
#that completes the first cycle of the outer loop, lets do it again 2x

matrix = [
    [3, 5, 7],
    [2, 4, 6],
    [8, 9, 1]
]

for row in matrix:            # Outer loop
    for value in row:         # Inner loop
        print("Value:", value)
    print("Finished row:", row)
    
#we did not create an initial variable like a list or matrix
# we are using the the for/in, with interger. 
# for interger in the range of 1 through 4, is the outer loop
#the inner loop says for "J" in the range of 1 -4 print
# "I" times "J" is = , i * j 
#we are essentiallly multiple each element in the range of 1-4, 
#but i do not know what "J" is and what we are mult it to? 
# maybe is it's for each iter, pcik an I value, mult by j value and print finish row 
#therefore 1x1 ...finished row for 1 (iter 3x)
    
for i in range(1, 4):          # Outer loop
    for j in range(1, 4):      # Inner loop
        print(i, "x", j, "=", i * j)
    print("Finished row for:", i)

#lets break down the answer 
# for i in range(1, 4):
#this means i=1 , i = 2, i=3
# for j in range(1, 4):
#this means j=1, j=2, j=3
#So for i = 1, the inner loop runs 3 times:
#therefore j = 1 --> 1 x 1 =1,  j = 2--> 1x 2 =2, j= 3 --> 1 x 3 =3


multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,6):
    print("Outer: ",outer, ", Inner: ", inner, "Outer x inner: ",inner * outer)
    multiples[outer-1].append( outer * inner)
print(multiples)

#another loop example 

for row in range(1, 4):        # Outer loop
    for col in range(1, 6):    # Inner loop
        print("*", end=" ")
    print()

multiples = []
for outer in range(1,5):
  multiples.append([])
  for inner in range(1,6):
    multiples[outer-1].append( outer * inner)
print(multiples)
for outerList in multiples:
  for innerValue in outerList:
    print (innerValue," ",end ='')
  print()
  
#practice building a 3x3 grid using nested loop 
grid = []
for row in range(3): #outer loop, has 3 rows inside the grid
    grid.append([]) #we are adding an empty row to each iter in the grid
    for col in range(3):    # inside our row, we add an element 1-3 
        grid[row].append(0) # our grid now has iter, and append element 
    print(grid)  #the final outpout at end of iter 

#The output is an infinite loop
#n = 10
#while True:
#    print(n, end=' ')
#    n = n - 1
#print('Done!')

while True:
    line = input('Enter input (# tag will not print). Type done when finished > ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')







