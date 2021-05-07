layer = input("Enter the no. layers: ") #Layers of the grid

#Error Handling for layer Input
while True:
    try:
        layer = input("Enter a number: ")
        layer = int(layer)
        break
    except ValueError:
        print("Invalid Input!")

maze = [] #The final grid with all layers

#Taking input as per number of layers
for i in range(layer):
    lay = list(map(int,input(f"Enter layer {i+1}:").split()))
    maze.append(lay)

#Getting source and target
source = list(map(int,input("Enter Source Co-Ordinates:").split()))
target = list(map(int,input("Enter Target Co-Ordinates:").split()))

#Generating an empty grid of similar size of maze
empty = []
for i in range(len(maze)):
    empty.append([])
    
    for j in range(len(maze[i])):
        empty[-1].append(0)

#setting source on empty grid
i,j = source
empty[i][j] = 1

#For making a single step
def make_step(k):
  for i in range(len(empty)):
    
    for j in range(len(empty[i])):
      
      if empty[i][j] == k:
        
        if i>0 and empty[i-1][j] == 0 and maze[i-1][j] == 0:
          empty[i-1][j] = k + 1
        
        if j>0 and empty[i][j-1] == 0 and maze[i][j-1] == 0:
          empty[i][j-1] = k + 1
        
        if i<len(empty)-1 and empty[i+1][j] == 0 and maze[i+1][j] == 0:
          empty[i+1][j] = k + 1
        
        if j<len(empty[i])-1 and empty[i][j+1] == 0 and maze[i][j+1] == 0:
           empty[i][j+1] = k + 1

#Making the steps until the each empty block is reached
k = 0
while empty[target[0]][target[1]] == 0:
    k += 1
    make_step(k)


i, j = target
k = empty[i][j]
revpath = [(i,j)] #Target to Source Path (Back tracked)

while k > 1:
  
  if i > 0 and empty[i - 1][j] == k-1:
    i, j = i-1, j
    revpath.append((i, j))
    k-=1
  
  elif j > 0 and empty[i][j - 1] == k-1:
    i, j = i, j-1
    revpath.append((i, j))
    k-=1
  
  elif i < len(empty) - 1 and empty[i + 1][j] == k-1:
    i, j = i+1, j
    revpath.append((i, j))
    k-=1
  
  elif j < len(empty[i]) - 1 and empty[i][j + 1] == k-1:
    i, j = i, j+1
    revpath.append((i, j))
    k -= 1

path = revpath[::-1] #Source to Target path 
print(path)