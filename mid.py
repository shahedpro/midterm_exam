#---------------1------------------
class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

#---------------1------------------

#---------------2------------------
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []  
        self.rows = rows  
        self.cols = cols 
        self.hall_no = hall_no  
        Star_Cinema.entry_hall(self)

#---------------2------------------

#---------------3------------------
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {} 
        self.show_list = []  
        self.rows = rows  
        self.cols = cols  
        self.hall_no = hall_no  
        Star_Cinema.entry_hall(self)
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        seat_allocation = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation

#---------------3------------------

#---------------4------------------
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}  
        self.show_list = []
        self.rows = rows  
        self.cols = cols 
        self.hall_no = hall_no 
        Star_Cinema.entry_hall(self)
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        seat_allocation = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Error: Show with ID {} does not exist.".format(show_id))
            return
        for row, col in seat_list:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if self.seats[show_id][row - 1][col - 1] == 'Free':
                    self.seats[show_id][row - 1][col - 1] = 'Booked'
                    print("Seat ({}, {}) for Show ID {} booked successfully.".format(row, col, show_id))
                else:
                    print("Error: Seat ({}, {}) for Show ID {} is already booked.".format(row, col, show_id))
            else:
                print("Error: Invalid seat ({}, {}) for Show ID {}.".format(row, col, show_id))

#---------------4------------------

#---------------5------------------

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}  
        self.show_list = []  
        self.rows = rows
        self.cols = cols  
        self.hall_no = hall_no
        Star_Cinema.entry_hall(self)
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        seat_allocation = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Error: Show with ID {} does not exist.".format(show_id))
            return
        for row, col in seat_list:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if self.seats[show_id][row - 1][col - 1] == 'Free':
                    self.seats[show_id][row - 1][col - 1] = 'Booked'
                    print("Seat ({}, {}) for Show ID {} booked successfully.".format(row, col, show_id))
                else:
                    print("Error: Seat ({}, {}) for Show ID {} is already booked.".format(row, col, show_id))
            else:
                print("Error: Invalid seat ({}, {}) for Show ID {}.".format(row, col, show_id))

    def view_show_list(self):
        print("Shows Running:")
        for show_info in self.show_list:
            print("ID: {}, Movie: {}, Time: {}".format(show_info[0], show_info[1], show_info[2]))

#---------------5------------------

#---------------6------------------

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {} 
        self.show_list = [] 
        self.rows = rows 
        self.cols = cols  
        self.hall_no = hall_no  
        Star_Cinema.entry_hall(self)
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        seat_allocation = [['Free' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation
    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print("Error: Show with ID {} does not exist.".format(show_id))
            return
        for row, col in seat_list:
            if 1 <= row <= self.rows and 1 <= col <= self.cols:
                if self.seats[show_id][row - 1][col - 1] == 'Free':
                    self.seats[show_id][row - 1][col - 1] = 'Booked'
                    print("Seat ({}, {}) for Show ID {} booked successfully.".format(row, col, show_id))
                else:
                    print("Error: Seat ({}, {}) for Show ID {} is already booked.".format(row, col, show_id))
            else:
                print("Error: Invalid seat ({}, {}) for Show ID {}.".format(row, col, show_id))
    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("Error: Show with ID {} does not exist.".format(show_id))
            return
        print("Available seats for Show ID {}:".format(show_id))
        for i in range(self.rows):
            for j in range(self.cols):
                if self.seats[show_id][i][j] == 'Free':
                    print("Row {}, Col {}".format(i + 1, j + 1))

#---------------6------------------

#---------------7------------------

class Counter:
    def __init__(self, cinema):
        self.cinema = cinema
    def view_all_shows(self):
        print("All Shows Running:")
        for hall in self.cinema.hall_list:
            hall.view_show_list()
    def view_available_seats(self, show_id):
        for hall in self.cinema.hall_list:
            hall.view_available_seats(show_id)
    def book_tickets(self, show_id, seat_list):
        for hall in self.cinema.hall_list:
            hall.book_seats(show_id, seat_list)
cinema = Star_Cinema()
hall1 = Hall(rows=5, cols=8, hall_no=1)
hall1.entry_show(id='show1', movie_name='Movie A', time='18:00')
cinema.entry_hall(hall1)
counter = Counter(cinema)
counter.view_all_shows()
counter.view_available_seats('show1')
counter.book_tickets('show1', [(1, 2), (3, 4), (5, 6)])

#---------------7------------------

#---------------8------------------

