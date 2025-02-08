var_array = [i for i in range(101)]

result = 0
for i in range(len(var_array)):
    result+=var_array[i]
    if i == len(var_array)-1:
        result = result / len(var_array)
        
print(result)
