# nested loops = The inner loop will finish all of it's iterations before one iteration of the outer loop is completed

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #prints number of symbols based on input, does not go to new line because of end=""
    print(symbol) #prints number of symbols based on input, breaks line because of no modifier


