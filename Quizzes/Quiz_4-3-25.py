total = 0

def sum_region(grid, row):
   global total

   print(grid[row])
   for j in grid[row]:
      print(j)
      total += j
      
      if (row < 2):
         sum_region(grid, row + 1)




grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

        
sum_region(grid, 0)

print(total)