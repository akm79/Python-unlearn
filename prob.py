"""def firstSecond(givenList):
    givenList.sort()
    givenList.reverse()
    for i in range(1,len(givenList)):
        if givenList[0] != givenList[i]:
            return givenList[0],givenList[i]
            break;

a=[37,23,56,89,76,54,86,89,76,86,89]
print(firstSecond(a))"""

"""def removeDuplicates(myList):
    a=[]
    for i in myList:
        if i in a:
            continue
        else:
            a.append(i)
    return a

c=[1,3,4,5,3,4,1,6,7,3]
print(removeDuplicates(c))"""

def pairSum(myList, sum):
    a=[]
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j]==sum:
                a.append(str(str(myList[i])+"+"+str(myList[j])))
    return a


a=[2,5,4,6,7,1,8]
print(pairSum(a,9))