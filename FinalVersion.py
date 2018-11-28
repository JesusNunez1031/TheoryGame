# import the modules
import tkinter
import Program_Updated

score = 0
userAnswers = set()

# the game time left, initially 30 seconds.
timeleft = 30
rules_input = Program_Updated.rules_input


# function that will start the game.
def startGame(event):
    #global rules_input
    if timeleft == 30:
        # start the countdown timer.
        countdown()
    PDA()


def showRules():
    rulesText = "Rules:\n"
    for rules in rules_input:
        rulesText += rules + "\n"
    ruleLabel.config(text=rulesText)
    ruleLabel.configure(fg="white")

def showAnswers():
    answerText = "These are your correct answers:\n "
    for answer in userAnswers:
        answerText += answer + "\n"
    answersLabel.config(text=answerText)
    answersLabel.configure(fg="green")


def PDA():
    # use the globally declared 'score'
    # and 'play' variables above.
    global score
    global timeleft


    # if a game is currently in play
    if timeleft > 0:
        showRules()

        # make the text entry box active.
        e.focus_set()

        # Get the entered submission from the user
        rawExpression = e.get()
        expression = list(rawExpression)

        # Need to run function from Program_Updated on expression and if it works score + 1 otherwise nothing

        # Defined a new function in Program_Updated(Imported Above for this to work) to take only one expression
        if Program_Updated.run_one_input(expression, rules_input) and (rawExpression not in userAnswers):
            score += 1
            userAnswers.add(rawExpression)

        # clear the text entry box.
        e.delete(0, tkinter.END)

        # update the score.
        scoreLabel.config(text="Score: " + str(score))


#Countdown timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.configure(fg="#D50000")

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
    else:
        showAnswers()

    # Driver Code


# create a GUI window
root = tkinter.Tk()

# set the title
root.title("Theory of Computation Game: PDA GAME")
root.configure(background="#311b92")

# set the size
root.geometry("1000x800")

# add an instructions label
instructions = tkinter.Label(root, text=(
    "\n\nEnter regular expressions that are accepted by the following rules to earn points: "),
                             font=('Arial', 25))
instructions.configure(background="#311b92")
instructions.configure(fg="white")
instructions.pack()

# add a score label
scoreLabel = tkinter.Label(root, text="\nPress enter to start", font=('Arial', 16))
scoreLabel.configure(background="#311b92")
scoreLabel.configure(fg="white")
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Arial', 16))
timeLabel.configure(background="#311b92")
timeLabel.configure(fg="white")

timeLabel.pack()

# label to display users answers at the end
answersLabel = tkinter.Label(root, font=('Arial', 16))
answersLabel.configure(background="#311b92")
answersLabel.pack()

# label to display Rules
ruleLabel = tkinter.Label(root, font=('Arial', 16))
ruleLabel.configure(background="#311b92")
ruleLabel.pack()

# add a text entry box for
# typing in answers
e = tkinter.Entry(root)
e.configure(background="#4CAF50")

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
