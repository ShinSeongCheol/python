def max(data):
    result = data[0]
    for x in range(1,len(data)):
        if result < data[x]:
            result = data[x]

    return result

print(max([5,3,9,8,7,34,1266,1321]))

    
