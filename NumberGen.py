from tkinter import *
import random

root = Tk()
root.geometry('450x450')
root.title('Random Number Generator')
# ---------------------------------------------------------------

# For padding things on the screen
MOVE = 30

# Title
title = Label(root, text = 'Random Number Generator', font = ('Comicsans', 20), padx = MOVE, pady = MOVE).grid(row = 0, column = 1, columnspan = 4)

# Type of number
chooseType = StringVar()
chooseType.set('Integer')
Radiobutton(root, text = 'Integer', font = 'Comicsans', variable = chooseType, value = 'Integer', padx = MOVE).grid(row = 1, column = 1, columnspan = 2)
Radiobutton(root, text = 'Floating point', font = 'Comicsans', variable = chooseType, value = 'Floating point', padx = MOVE).grid(row = 2, column = 1, columnspan = 2)

# Values
startTitle = Label(root, text = 'From:', font = 'Comicsans' ).grid(row = 3, column = 1, padx = MOVE, pady = (MOVE, 0))
endTitle = Label(root, text = 'To:', font = 'Comicsans' ).grid(row = 3, column = 2, padx = MOVE, pady = (MOVE, 0))

startValue = Entry(root, width = 20)
endValue = Entry(root, width = 20)

startValue.grid(row = 4, column = 1, padx = MOVE, pady = (0, MOVE) )
endValue.grid(row = 4, column = 2, padx = MOVE, pady = (0, MOVE) )

# Generate random number
showRandomNumber = Label(root)  # For destroying the last generate number in the background

def randomNumber():

    # Destroy last number in the background
    global showRandomNumber
    showRandomNumber.destroy()

    # Show random number to the screen
    if chooseType.get() == 'Integer':
        
        try:                
            number = random.randint( int( startValue.get() ), int( endValue.get() ) )
            showRandomNumber = Label(root, text = number, font = 'Comicsans', padx = MOVE, pady = MOVE)        
            showRandomNumber.grid(row = 6, column = 1, columnspan = 2)
        except:
            showRandomNumber = Label(root, text = 'WRONG INPUT', font = 'Comicsans', fg = 'red', padx = MOVE, pady = MOVE)        
            showRandomNumber.grid(row = 6, column = 1, columnspan = 2)
    
    elif chooseType.get() == 'Floating point':
        
        try:
            start = float( startValue.get() )
            end = float( endValue.get() )

            if (start <= end):
                number = random.uniform( start, end )
                showRandomNumber = Label(root, text = number, font = 'Comicsans', padx = MOVE, pady = MOVE)        
                showRandomNumber.grid(row = 6, column = 1, columnspan = 2)
            else:
                print(5/0)
        except:
            showRandomNumber = Label(root, text = 'WRONG INPUT', font = 'Comicsans', fg = 'red', padx = MOVE, pady = MOVE)        
            showRandomNumber.grid(row = 6, column = 1, columnspan = 2)

        

# Generate button
generate = Button(root, text = 'Generate', font = 'Comicsans', command = randomNumber, fg = 'white', bg = 'green').grid(row = 5, column = 1, columnspan = 2, padx = MOVE, pady = (0, MOVE) )

# ---------------------------------------------------------------
root.mainloop()
