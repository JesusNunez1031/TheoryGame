# RUEL

# This machine will accept a string and check if there is a consective
def machine_accepts_characters_with_consecutive(string):
    if (type(string) != str):
        raise TypeError("Value is not a string")
    states = [0 for i in range(5)] # Size of array represents the number of states, right now we will make my_array[4] the accept state
    states[0] = 1
    count = 0
    for i in range(len(string)):
      if count == 4:
        # Count won't increment because the string has fit the criteria
        count = 4
      elif ( ord(string[i]) < ord("d") and ord(string[i]) > ord("a") - 1):
        count += 1
        # Now we will show animation of states[count] lighting up or something
        states[count-1] = 0
        states[count] = 1

      else:
        # String doesn't fit criteria yet so we set count back to 0
          states[count] = 0
          count = 0
          states[count] = 1
      print(states)
    return count == 4



print(machine_accepts_characters_with_consecutive('abcdaabsbabasbasba'))