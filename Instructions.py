str1 = "turn off 660,55 through 986,197"
str2 = "turn on 660,55 through 986,197"
str3 = "switch 660,55 through 986,197"
str4 = "witch 660,55 through 986,197"
str5 = "switch 660,55 thrugh 986,"
strList = [str1, str2, str3, str4, str5]

#ensure Instruction is valid
for s in strList:
    s = s.replace("turn", "")
    s = s.replace("through", "")
    s = s.replace(",", " ")
    s = s.split()
    print(s)
    sOutput = True
    if len(s) != 5: #all valid Instructions are of length 5
        sOutput = False
    if not( s[0] in ["off", "on", "switch"]): #all valid Instructions begin with one of these
        sOutput = False
    for i in range(1, 5, 1): #all valid Instructions have 4 integer entries
        try:
            if not isinstance(int(s[i]), int):
                sOutput = False
        except ValueError:
            sOutput = False
    print(sOutput)

