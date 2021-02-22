arr = ([1,3,0,8,2,4,7,6,5])

def displayArr(arr):
    temp = ""
    i = 0
    for elem in arr:
        if i % 3 == 0:
            temp += "\n"

        if elem == 0:
            temp += " "

        else:
            temp += str(elem)

        i += 1

    print(temp)


displayArr(arr)
