class State:
  def __init__(self, name):
    self.name = name #the name of this State.
    self.isfinal = False #Is this an "accept" State?

    self.arrows = {} #character: [state names]
    # the keys in the 'arrows' dictionary will be the characters for the state
    # transitions. For an empty (epsilon) transition, the empty string ('') will
    # be used. All values will be a list of state names (even if there is only
    # one destination state for a character)

  def __str__(self):
    arrows = '\n'.join(["{ch}->({states})".format(ch=ch, states=','.join(states))
                        for ch, states in self.arrows.items()])
    return "State {name}{final}. Transitions: \n{arrows}".format(
      name=self.name, final=(" (Final)" if self.isfinal else ""),
      arrows=arrows)

class Machine:
  def __init__(self, start, alphabet, states):
    self.start = start #a list of the name of the start state
    self.alphabet = alphabet #this is a list of valid input characters
    self.states = states #a dictionary of name: State

  def __str__(self):
    return ("A machine over {{{alphabet}}} containing states {{{states}}}, " +
            "starting in {{{start}}}").format(
      alphabet=','.join(self.alphabet), states=','.join(self.states.keys()),
      start=','.join(self.start))


# Homework 1: implement these functions
def is_dfa(m):
  """
  Given a Machine, return True if that machine is a DFA and False if it is
  not a valid DFA. Bonus points for also printing out all the reasons the
  machine is not a DFA when it is not.
  """

  #Implement function where I just need to check that
  # 1. There is only one start state
  # 2. Every state has a transition for the number of alphabet
  #    2 alphabet, each state has two transitions
  # 3. Each transition value has one option

  #Checking if there are multiple start states / no start states

  isdfa = True

  if (len(m.start) == 0):
    print('This machine has no start states')
    isdfa = False

  elif (len(m.start) > 1):
    print('This machine has multiple start states')
    isdfa = False

  # Checking if each transition value has only one option for each state
  for i in m.states:
    for j in m.states[i].arrows:
      if j not in m.alphabet:
        if j == '':
          print("Epsilon is not in the alphabet")
          isdfa = False
        else:
          print(str(j) + " is not in the alphabet") # Checks if current transition value is in alphabet
          isdfa = False
      # Checks if one transition value only has one transition option for any state
      elif len(m.states[i].arrows[j]) == 0:
        print("This state " + i + " using value " + str(j) + " does not have a transition => " + str(m.states[i].arrows[j]))
        isdfa = False
      elif len(m.states[i].arrows[j]) > 1:
        print("This state " + i + " using value " + str(j) + " transitions to more than one state => " + str(m.states[i].arrows[j]))
        isdfa = False
  return isdfa

# Array for final states
last_states = []

def execute_input(m, input_):
  # Just define a function where state transitions end up in some state at the end

  states = m.start
  print("start: {}".format(states))

    #if i == (len(input_) - 1):
      #Put the state in the array last_states as this is where we would end up last

  '''
  for i in range(len(input_)):
    print(input_[i])
    new_states = []
  '''
  for _ in range(len(input_)):
    new_states = []
    for i in states:
      for j in m.states[i].arrows:
        if j == input_[_] or j == "":
          for k in m.states[i].arrows[j]:
            if (j != ""):
              print("{input_char}: {state1}, {state2}".format(input_char=j, state1=i, state2=k))
            else:
              print("{input_char}: {state1}, {state2}".format(input_char="epsilon", state1=i, state2=k))
              epsilon_set = set()
              epsilon_set.add(k)
              used_input_set = set()
              while True: #For the epsiloned states, put the values of what the state would be after the current letter transition
                set_optimal = False
                for x in epsilon_set:
                  for val in m.states[x].arrows:
                    if val == _:
                      for st in m.states[x].arrows[val]:
                        if st not in used_input_set or st not in epsilon_set:
                          used_input_set.add(st)
                          set_optimal = True
                    elif val == "":
                      for st in m.states[x].arrows[val]:
                        if st not in epsilon_set:
                          epsilon_set.add(st)
                          set_optimal = True
                if not set_optimal:
                    break
              for state in used_input_set:
                new_states.append(state)
            new_states.append(k)
    states = new_states
  print(states)
  accepted = False
  for i in states:
    if m.states[i].isfinal == True:
      accepted = True
  return accepted

"""
  Given a Machine and an input string, return whether the machine accepts
  or rejects the input string. For each input character, also print the state(s)
  the machine is in. Use the format:

  <input character>: <name1>, <name2>

  and print "start" for the starting state.
  So for example, you might print:
  start: q0
  0: q1, q2
  1: q2, q4
  0: q1
  0: q3

  for some machine and the input 0100
  """

import re

# parsing logic
FORMAT = "Q:\s(?P<states>.*)\nE:\s(?P<alphabet>.*)\ns:\s(?P<start>.*)\nF:\s(?P<accept>.*)\nd:\s\n(?P<arrows>.*)"

def splitstrip(st, ch=','):
  return [it.strip() for it in st.split(ch)]

def process_file(fn):
  with open(fn) as f:
    groups = re.match(FORMAT, f.read(), flags=re.DOTALL).groupdict()

  for key in ('states', 'alphabet', 'start', 'accept'):
    groups[key] = splitstrip(groups[key])

  states = {}
  for state in groups['states']:
    states[state] = State(state)
  for state in groups['accept']:
    states[state].isfinal = True
  for src, ch, dst in [splitstrip(line) for line in groups['arrows'].splitlines()]:
    states[src].arrows.setdefault(ch, [])
    states[src].arrows[ch].append(dst)
  return Machine(groups['start'], groups['alphabet'], states)


# this uploads & processes a DFA file
uploaded = open('input_file.txt')
for fn in uploaded.keys():
  m = process_file(fn)
  input_ = '00001110'
  #print("is dfa? {result}".format(result=is_dfa(m)))
  print("accepts input {input_}? {result}".format(input_=input_,
    result=execute_input(m, input_)))
