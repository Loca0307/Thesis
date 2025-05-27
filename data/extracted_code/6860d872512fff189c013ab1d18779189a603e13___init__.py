def countingSort(packageList):
    count = [0] * (max(packageList) + 1)
 
    for i in packageList:
        count[i] += 1
 
    i = 0
    for j in range(len(count)):
        for k in range(count[j]):
            packageList[i] = j
            i += 1
 
    return packageList

def radixSort(packageList):
    bucket = [[] for i in range(10)]
    maxLength = 0
    for i in packageList:
        if len(str(i["Cost"])) > maxLength:
            maxLength = len(str(i["Cost"]))
    for i in range(maxLength):
        for j in packageList:
            bucket[int(j["Cost"]/(10**i)) % 10].append(j)
        packageList = []
        for z in bucket:
            packageList.extend(z)
    return packageList

def shellSort(packageList):
    n = len(packageList)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = packageList[i]
            j = i
            while j >= gap and packageList[j-gap]["Customer Name"] > temp["Customer Name"]:
                packageList[j] = packageList[j-gap]
                j -= gap
            packageList[j] = temp
        gap //= 2
