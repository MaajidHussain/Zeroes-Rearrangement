def Chocolate_Factory(Array):
    NewArray=[]
    Zero_Count=0
    
    for i in range(len(Array)):
        if Array[i] !=0:
            NewArray.append(Array[i])
        else:
            Zero_Count+=1
    NewArray.extend([0]*Zero_Count)
    return NewArray
Array=[4,5,0,1,9,0,5,0]
Array1=[6,0,1,8,0,2]
Array2=[-1,2,0,-3,0,4]
print(Chocolate_Factory(Array))
print(Chocolate_Factory(Array1))
print(Chocolate_Factory(Array2))