str1 = "turn off 660,55 through 986,197"
str2 = "turn on 660,55 through 986,197"
str3 = "switch 660,55 through 986,197"
str4 = "switch 660,55 through 986,197"
str5 = "switch 660,55 through 986,-1000"
strList = [str1, str2, str3, str4, str5]

#puts the Instruction into the desired format
def instructionFormat(str):
    #replace
    strReplaceList = [("turn", ""), ("through", ""), (",", " ")] #replace useless strings
    for s in strReplaceList:
        str = str.replace(s[0], s[1])
    str = str.split() #turn it from string to list
    return str

#determines if the Instruction is valid
def instructionValid(theList):
    if len(theList) != 5: #all valid Instructions are of length 5
        return False
    if theList[0] not in ["off", "on", "switch"]: #all valid instructions begin with one of these Commands
        return False
    for i in range(1, 5, 1): # all valid instructions have four integer inputs
        try:
            if not isinstance(int(theList[i]), int):
                return False
        except ValueError:
            return False
    return True

for s in strList:
    print(s)
    s = instructionFormat(s)
    print(s)
    print(instructionValid(s))