def form_array (array, condition = 3):
    resultArray = []

    for array in array:
        if len(array) <= condition:
            resultArray.append(array)

    return resultArray


array = ['1234', '1567', '-2', 'computer science', ';']
result = form_array(array)

print(result)
