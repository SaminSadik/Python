 #! Demo Functions
def Pout(para): print(para)
def take_list(*args): print(args)

def generate_matrix(rows, cols):
    matrix = []
    for row in range(ord('A'), ord('A') + rows):
        row_values = []
        for col in range(0, cols):
            cell_value = f' {chr(row)}{col} '
            row_values.append(cell_value)
        matrix.append(row_values)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        matrix_line = ''
        for cell in row:
            matrix_line += cell + ' '
        print(matrix_line)

matrix = generate_matrix(5, 6)
print('Marked[] seats are not available:')
print_matrix(matrix)
#print(matrix)

while(True):
    cell = input('Enter an available seat to book: ')
    row = ord(cell[0]) - ord('A')
    col = ord(cell[1]) - ord('0')
    if (len(cell)>2 or row<0 or row>4 or col<0 or col>5):
        print('Invalid Entry! Try Again')
        continue
    matrix[row][col] = f'[{cell}]'
    break

print("\nModified Matrix:")
print_matrix(matrix)