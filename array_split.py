arr = [11,12,13,14,15]
n = len(arr)
n- = 1
pos = int(input("Choose position from 0 to %d   " % n))
try:
    arr1 = arr[0:pos]
    arr2 = arr[pos:n]
    for i in arr1:
        arr2.append(i)
    print(arr2)
except:
    print("not valid")
