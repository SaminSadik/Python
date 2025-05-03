# Superclass with one initially-empty list & one object-pushing method:
class Star_Cinema:
    _hall_list = []

    def _entry_hall(self, hall):
        self._hall_list.append(hall)

# Subclass with private instance variables, & methods to access as needed:
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall
        self._booked = {} # for keeping track of the booked seats
        super()._entry_hall(self) # sending instance to superclass

# Enters a show in __show_list, validity of id is checked before calling:
    def entry_show(self, id, movie_name, time):     
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = self.generate_seats(self.__rows, self.__cols)
        # creats an 2d matrix as seats, corresponding to the id

# Modifies __seats, validity of id & seat_list is ensured before calling:
    def book_seats(self, id, seat_list):
        n = len(seat_list)
        for i in range(n):
            row = seat_list[i][0]
            col = seat_list[i][1]
            # converting seat no. to my string format:
            seat_list[i] = f'{chr(row+ord("A"))}{str(col)}'
            # updating seat to indicate it's booked:
            self.__seats[id][row][col] = f'[{seat_list[i]}]'
            # tracking which seats are booked for a show(id):
            if(id not in self._booked): self._booked[id] = []
            self._booked[id].append(seat_list[i])

        # parts of the invoice (confirmation of booking):
        print(f'Hall Number    : {self.__hall_no}')
        # ensuring finer detail(s):
        if(n>1): print('Booked Seat    :', end=" ")
        else: print('Booked Seats   :', end=" ")
        # ensuring last seat does't end with comma:
        for i in range(n-1):
            print(seat_list[i], end=', ')
        print(seat_list[n-1])
        # accessing the list of tuples for invoice:
        for show in self.__show_list:
            if show[0]==id:
                print(f'Show Name      : {show[1]}')
                print(f'Show ID        : {show[0]}')
                print(f'Show Time      : {show[2]}')

# Displays __show_list in a specific format:
    def view_show_list(self):
        print('List of Ongoing Shows:')
        counter = 1 # for numbering each available show
        for show in self.__show_list:
            print(f"{counter}. [ID {show[0]}] {show[1]} @ {show[2]}")
            counter += 1

# Displays __seats for an id (validity checked before calling):
    def view_available_seats(self, id):
        print('   List of Available Seats :   ')
        for row in self.__seats[id]:
            matrix_line = ''
            for cell in row:
                matrix_line += cell + ' '
            print(matrix_line)
        print('\nN.B. []marked seats are booked.')

# Checking if __seats of an [id] exists:
    def check_id(self, id) -> bool:
        if id in self.__seats: return True
        return False

# Generating a 2D matrix as seats for entry_show() method:    
    def generate_seats(self, rows, cols):
        matrix = []
        for row in range(ord('A'), ord('A') + rows):
            row_values = []
            for col in range(0, cols):
                cell_value = f' {chr(row)}{col} '
                row_values.append(cell_value)
            matrix.append(row_values)
        return matrix

# Calculating available no. of seats for a show(id):
    def rem_seats(self, id) -> int:
        max_seats = self.__rows * self.__cols
        if id in self._booked:
            return max_seats-len(self._booked[id])
        else: return max_seats


# creating the object with fixed rows, cols & hall_no for simplicity:
customer = Hall(5,6,'STAR1')
# entering some pre-existing shows before any input:
customer.entry_show('S1', 'Silent Voice', '09:30 AM')
customer.entry_show('S2', 'Avengers Endgame', '10:00 PM')
customer.entry_show('S3', 'Kung Fu Panda 3', '11:45 AM')

# Output Format Starts:
print('-------------------------------')
print('Welcome to Star Cinema Terminal')
# Repeating menu based on Entry(op):
while(True):
    print('-------------------------------')
    print('  What would you like to do ?  ')
    print('  [1] Check available shows')
    print('  [2] Check available seats')
    print('  [3] Book seats')
    print('  [4] Enter show')
    print('  [5] Exit Theatre')
    print('-------------------------------')
    op = input("ENTRY:  ")

    if op == '1':
        print('-------------------------------')
        customer.view_show_list()

    elif op == '2':   
        while(True):
            id = input('Please enter the show ID: ')
            # Making sure id is valid:
            if(customer.check_id(id) is False):
                print(f'Invalid ID. Try again')
                print('-------------------------------')
                customer.view_show_list() # for ease of choice
                print('-------------------------------')
                continue
            print('-------------------------------')
            customer.view_available_seats(id)
            break

    elif op == '3':
        id = input('Enter ID of your chosen show: ')
        # Making sure id is valid:
        while(customer.check_id(id) is False):
            print(f"ID {id} does't match any available show!")
            print('-------------------------------')
            customer.view_show_list() # for ease of choice
            print('-------------------------------')
            id = input("Enter a valid ID: ")

        # taking a list of seats:
        n = ''
        while(True):
            n = input('How many seats would you like to book: ')
            # Ensuring a valid list size:
            if n.isnumeric():
                # Ensuring over-booking does't occur:
                if(int(n)>customer.rem_seats(id)):
                    print("Sorry! only", customer.rem_seats(id), end="")
                    print(" seats are currently available for this show")
                else: break
            else: print('Invalid Entry! Try again')
        if n=='0': # booking 0 seats means not booking afterall
            print('Booking has been Cancelled')
            continue

        n = int(n)
        # Ensuring finer detail(s):
        if n>1: print('Enter available seats to book (separated by space):', end=' ')
        else: print('Enter an available seat to book:', end=' ')
        seat_list = input().split() # string gets split into a list
        # Handling error when extra splits were given in the list:
        if(len(seat_list)>n):
            print("[Notice: your extra inputs (later) are ignored]")
            seat_list = seat_list[:n]
        # Traversing the list through index, as size is known:
        for i in range(n):
            while(True):
                cell = seat_list[i]
                # converting string cell to numeric (row,col)
                row = ord(cell[0]) - ord('A')
                col = ord(cell[1]) - ord('0')
                # checking invalidities:
                if(len(cell)>2 or row<0 or row>4 or col<0 or col>5):
                    print(f"Seat '{cell}' is invalid")
                elif((id in customer._booked) and (cell in customer._booked[id])):
                    print(f"Seat '{cell}' is already booked!")
                elif((seat_list.count(cell)>1) or (seat_list.count((row, col))>0)):
                    print("You can't book the same seat multiple times!")
                else:
                    seat_list[i] = (row, col)
                    break # loop only breaks if (row,col) is valid
                print('-------------------------------')
                customer.view_available_seats(id) # for invalid input only
                print('-------------------------------')
                seat_list[i] = input(f"Enter a valid Seat instead of '{cell}' : ")

        # Generating top half of the Invoice (confirmation of booking):        
        print("Please provide necessary info for the invoice:")
        nam = input("Name - ")
        num = input("Contact Number - ")
        print('-------------------------------')
        print('      Booking Successful!')
        print(f'Customer Name  : {nam}')
        print(f'Contact Number : {num}')

        # Remaining invoice generated inside book_seats() method
        customer.book_seats(id, seat_list)

    elif op == '4':
        id = input('Enter unique ID of the show: ')
        # Making sure id is valid:
        while(customer.check_id(id) is True):
            print(f'Sorry! A show with ID "{id}" already exits!')
            id = input('Please try a different ID: ')
        movie = input('Enter Name of the show: ')
        time = input('Enter Time of the show: ')
        # for simplicity time is not checked & can overlap
        customer.entry_show(id, movie, time)
        print(f'You made a new entry. [Show: {movie} (ID {id}) @ {time}]')
        # confirmation of a successful entry is displayed

    # condition of program termination:
    elif op == '5':
        print('Thank you for visiting Star Cinema. Come again!\n')
        break
    
    # in case anything other than 1-5 was entered for op:
    else: print('Invalid Entry! Try 1-5')