import time


inputList = ["010","000"]


def takesInput():

    start = time.time()
    PERIOD_OF_TIME = 5
    while True:
        userInput = input("Input as many strings as you want: ")
        inputList.append(userInput)
        if time.time() > start + PERIOD_OF_TIME: break

    print(inputList)

    # continue computations


if __name__ == '__main__':


    takesInput()


    dfa1 = {0: {'0': 0, '1': 1},
           1: {'0': 2, '1': 0},
           2: {'0': 1, '1': 2}}

    dfa2 = {0: {'0':0, '1':1},
            1: {'0':1, '1':1}}


    def accepts(transitions, initial, accepting, s):
        state = initial
        for c in s:
            state = transitions[state][c]
        return state in accepting



    print("This tests if dfa accepts '1011101', the answer is: ")
    print(accepts(dfa1,0,{0},"1011101"))

    stringInput = input("Please type the string to check: ")

    print("This tests if dfa accepts "+stringInput+", the answer is: ")
    print(accepts(dfa2, 0,{1},stringInput))


