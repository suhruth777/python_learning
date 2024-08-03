# Create a program to book movie tickets. The program should:

# 	1.	Display a list of available movies.
# 	2.	Ask the user to choose a movie.
# 	3.	Ask the user how many tickets they want to book.
# 	4.	Store the booking information (movie and number of tickets) in a dictionary.
# 	5.	Calculate the total cost based on a fixed ticket price.
# 	6.	Print a summary of the booking, including the total cost.


movies = ['Deadpool', 'Inception', 'Interstellar', 'Toy Story', 'Jujutsu Kaisen 0']
ticket_price = 7.50
booking_info = {}

print("Currently playing movies:")
print('-----------------------------')
for movie in movies:
    print(movie)
print('-----------------------------')

while True:
    pick_movie = input('What movie do you want to see?: ')
    ticket_amt = input('How many tickets do you want to buy?: ')
    booking_info.update({pick_movie:ticket_amt})
    break

print(booking_info)


