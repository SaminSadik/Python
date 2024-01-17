class Star_Cinema:
    __hall_list = []

    def __entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, halls):
        self.__seats = {}
        self.__show_list = ()
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = halls
        super().__entry_hall(self)

    def entry_show(self, id, movie, time):
        #? check id
        self.__show_list.append((id, movie, time))

    def book_seats(self, id, *args):
        #? check if seat is invalid or booked
        pass

    def view_show_list(self):
        print('List of Ongoing Shows:')
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, id):
        #? check id
        print('List of Available Seats:')
        for seat in self.__seats:
            print(seat)


print('-------------------------------')
print('Welcome to Star Cinema Terminal')

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

    if op == '5':
        print('Thank you for visiting Star Cinema. Come again!')
        break

    customer = Hall(5,5,'A1')

    if op == '4':
        id = input('Enter show ID: ')
        movie = input('Enter show Name: ')
        time = input('Enter show Time: ')
        customer.entry_show(id, movie, time)
        print(f'You made a new entry. [Movie: {movie} (ID {id}) @ {time}]')

    if op == '3':
        pass

    if op == '2':
        id = input('Please enter the show ID: ')
        customer.view_available_seats(id)

    if op == '1':
        customer.view_show_list()
