# naming the strings--------------------------------------
alphaS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
alphaC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
          'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
num= [str(i) for i in range(0, 10)]


#reading the file-----------------------------------------
print("Read file-------------------------------------------\n\n")
f = open("fsa.txt","rt")
lines= f.readlines()
#print(lines)

#removing tabs and \n
temp4_list=[]
temp3_list=[]
Mul_info=[]
for x in lines:
    z = x
    z = z.replace("\n", "")
    temp3_list.append(z)
    
    for i in temp3_list:
        y = i.split("\t")
        for i in temp3_list:
            i = i.replace("\t", "")
    temp4_list.append(y)    
for a in temp4_list:
    res = [int(ele) if ele.isdigit() else ele for ele in a]
    Mul_info.append(res)

print("Multiple List is:")
print(Mul_info)

#replace a-z,A-Z,0-9 Strings---------------------

print("\n\nEnd List-------------------------------------------\n\n")
list1=[]
for i in Mul_info:
    mod=[]
    for j in i:
        if(j=="a-z"):
            mod.append(alphaS)
        elif(j=="0-9"):
            mod.append(num)
        elif(j=="A-Z"):
            mod.append(alphaC)
        elif(',' in j):
            mod.append(alphaS+alphaC+num)
        else:
            mod.append(j)
    list1.append(mod)
print(list1)



#now coding the NFA Sequence------------------------------------
# we will start from GOTO tomorrow/
inp =input("Enter language: ")
if(len(inp)==0):
        print("string not accepted")
        print(i)
state=0        
for i in inp:
    x = list1[state]
    flag = False
    for j in range(len(x)):
        if i in x[j]:
            flag = True
            state = j
            break
    if flag:
        print("Processed String", i)
        print("State ", state)
    else:
        print("String not Accepted")
if(state == 4):
    print ("String Accepted")
else:
    print ("String not Accepted")
        
        

  



