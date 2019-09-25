# convert roman to arabic numbers (1,2,3)
#V = 5
#III = 3
#IX = 9
#post to github and create folder for all limit to 20

def value(rom):
    if (rom == 'I'):
        return 1
    if (rom == 'V'):
        return 5
    if (rom == 'X'):
        return 10
    else:
        print("Enter value below 20")
    return -1

def romantonumber(str):
    result = 0
    i = 0
    while (i < len(str)):
        numone = value(str[i])
        if (i+1 < len(str)):
            numtwo = value(str[i+1])
            if (numone >= numtwo):
                result = result + numone
                i = i + 1
            else:
                result = result + numtwo - numone
                i = i + 2
        else:
            result = result + numone
            i = i + 2
    return result

print(romantonumber(""))

