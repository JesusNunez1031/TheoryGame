# import the modules
import tkinter
import random
import Program_Updated
# list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
userAnswers = set()

possibleRules = [["E -> E + T","E -> T","T -> T * F","T -> F","T -> F","F -> (E)","F -> a","F -> b"]]
# list of rules

# the game time left, initially 30 seconds.
timeleft = 10
rules_input = []

# function that will start the game.
def startGame(event):
    global rules_input
    if timeleft == 10:
        # start the countdown timer.
        countdown()


    # run the function to
    # choose the next colour.
    rules_input = possibleRules[random.randint(0, len(possibleRules)-1)]
    PDA()

def showAnswers():
    answerText = "These are your correct answers:\n "
    for answer in userAnswers:
        answerText += answer+"\n"
    answersLabel.config(text=answerText)


# Function to choose and
# display the next colour.
def PDA():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # Get the entered submission from the user
        rawExpression = e.get()
        expression = list(rawExpression)

        # Need to run function from Program_Updated on expression and if it works score + 1 otherwise nothing

        # Defined a new function in Program_Updated(Imported Above for this to work) to take only one expression

        if Program_Updated.run_one_input(expression) and (rawExpression not in userAnswers):
            score += 1
            userAnswers.add(rawExpression)

        # clear the text entry box.
        e.delete(0, tkinter.END)

        #random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value

        label.config(text="\n{}\n".format(rules_input), font=('Helvetica', 15))

        #label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))




    # Countdown timer function


def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: \n"+ str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        showAnswers()

    # Driver Code



# create a GUI window
root = tkinter.Tk()

# set the title
root.title("PDA GAME")

# set the size
root.geometry("640x480")

# add an instructions label
instructions = tkinter.Label(root, text="\n\n\nEnter answers possible from the PDA rules!",
                             font=('Helvetica', 16))
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text="\nPress enter to start",font=('Helvetica', 16))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " +str(timeleft), font=('Helvetica', 16))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Helvetica', 36))
label.pack()


#label to display users answers at the end
answersLabel = tkinter.Label(root, font=('Helvetica', 16))
answersLabel.pack()

# add a text entry box for
# typing in answers
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
