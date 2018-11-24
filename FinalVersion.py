import copy
import time

from termcolor import colored


class Rule:
    def __init__(self, variable, productions):
        self.variable = variable
        self.productions = [productions]


def read_rules():  # Read rules from 'rules.cfg' into a list called rules_input
    rules_file = open("rules.cfg", "rt")
    data = rules_file.read()
    lines = data.split("\n")
    for line in lines:
        rules_input.append(line)
        print(line)


def read_exp():  # Expression is read from 'expression.cfg' into list exp in reverse order, removing whitespace.
    i = 0
    global exp
    exp_file = open("expression.cfg", "rt")
    data = exp_file.read()
    chars = data.split(" ")
    for char in chars[::-1]:
        i = i + 1
        exp.append(char)
    return i


def divide_rules():  # split productions into the rules class by variable
    results = []
    for rule in rules_input:
        found = False
        var = rule.split(" -> ")
        for result in results:
            if result.variable == var[0]:
                result.productions.append(var[1])
                found = True
        if not found:
            results.append(Rule(var[0], var[1]))
    return results


def print_reject():  # Prints Reject and exits program.
    print("")
    print(colored("************************************", "red"))
    print(colored("*             REJECT               *", "red"))
    print(colored("************************************", "red"))
    return


def print_accept():
    print("")
    print(colored("************************************", "green"))
    print(colored("*             ACCEPT               *", "green"))
    print(colored("************************************", "green"))
    return


def get_rule(symbol):
    global rules
    for rule in rules:
        if rule.variable == symbol:
            return rule
    return False


def operation(stack, exp):  # Performs the operations of a PDA.  Recursive.
    if len(stack) > len(exp) or (len(stack) == 0 and len(exp) > 0):
        return
    current_symbol = stack.pop()
    if current_symbol == exp[-1]:
        exp.pop()
        if test(stack, exp):
            global accepted
            accepted = True
            return
        operation(copy.deepcopy(stack), copy.deepcopy(exp))
    rule = get_rule(current_symbol)
    if rule == False:
        return
    for production in rule.productions:
        new_stack = copy.deepcopy(stack)
        for s in production.split(" ")[::-1]:
            new_stack.append(s)
        operation(new_stack, copy.deepcopy(exp))


def test(stack, exp):
    if len(stack) == 0 and len(exp) == 0:
        return True
    else:
        return False


def main():
    # Accepted is a variable used to determine whether to print accept or reject based on what test returns
    global accepted
    accepted = False
    global length
    global rules
    global var_test
    print("Rules:")
    # read_rules()
    for line in rules_input:
        print(line)
    global exp
    print("Expression:")
    # read_exp()
    print(exp)
    rules = divide_rules()
    for rule in rules:
        var_test.append(rule.variable)
    print("variables =", var_test)
    stack = []
    stack.append(rules[0].variable)

    # TODO IMPLEMENT ACCEPTING INPUTS
    #count = 0
    start = time.time()
    # Time is in seconds
    PERIOD_OF_TIME = 10
    print("\nEnter as many regular expressions as you can before the time ends: ")
    while True:
        #count += 1
        expression = input(colored("\n\nEnter the expression:\n", "blue"))
        expression = list(expression)
        print(expression)
        userInput = ''.join(expression)

        rules = divide_rules()
        for rule in rules:
            var_test.append(rule.variable)
        print("variables =", var_test)
        stack = []
        stack.append(rules[0].variable)

        var_test = []
        var = []
        final = []

        accepted = False  # Set accepted as false at every iteration before calling operation

        operation(stack, expression)
        # print(accepted) Debugging print statement
        if accepted:
            Set.add(userInput)
            print_accept()
        else:
            print_reject()
        if time.time() > start + PERIOD_OF_TIME: break

    print(colored("Your time is up! This is the set of correct regular expressions you entered: ", "blue"))
    print(Set)


exp = ['a']
# exp = ['b','*','a','+','a']
var_test = []
rules_input = ["E -> E + T", "E -> T", "T -> T * F", "T -> F", "F -> (E)", "F -> a", "F -> b"]
stack = []
var = []
final = []
Set = set()
main()
