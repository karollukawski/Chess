#Creating the chessboard

rows = 8
cols = 8
  
arr = [[0]*cols]*rows
 
# arr[0][0] = 1
  
for row in arr:
    print(row)

#Creating pieces class, which check team, type and viability of each piece

class Piece:
    def __init__(self, team, type, viability = True):
        self.team = team
        self.type = type
        self.viability = viability