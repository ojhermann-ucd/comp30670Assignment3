str1 = "turn off 660,55 through 986,197"
str2 = "turn on 660,55 through 986,197"
str3 = "switch 660,55 through 986,197"
str4 = "witch 660,55 through 986,197"
str5 = "switch 660,55 through 986,197 789"
strList = [str1, str2, str3, str4, str5]

#turn possible inputs into testable format
for s in strList:
    s = s.replace("turn", "")
    s = s.replace("through", "")
    s = s.replace(",", " ")
    s = s.split()
    print(s)
    sOutput = True
    if len(s) != 5:
        sOutput = False
    if not( s[0] == "off" or s[0] == "on" or s[0] == "switch"): #all valid Instructions begin with one of these
        sOutput = False
    print(sOutput)