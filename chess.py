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

#Creating pieces with description of the team and type

bp = Piece('b','p') #black pawn
wp = Piece('w','p') #white pawn

bk = Piece('b','k') #black king
wk = Piece('w','k') #white king

br = Piece('b','r') #black rook
wr = Piece('w','r') #white rook

bbi = Piece('b','bi') #black bishop
wbi = Piece('w','bi') #white bishop

bq = Piece('b','q') #black queen
wq = Piece('w','q') #white queen

bkn = Piece('b','kn') #black knight
wkn = Piece('w','kn') #white knight