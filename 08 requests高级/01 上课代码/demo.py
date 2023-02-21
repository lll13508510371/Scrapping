def getresult(num):
    print(num)

    return num + getresult(num - 1)


getresult(6)
