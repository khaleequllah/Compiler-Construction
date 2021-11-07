# naming the strings--------------------------------------

alphaS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z']
alphaC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
          'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
num= [str(i) for i in range(0, 10)]
ab= ['a','b']


#reading the file-----------------------------------------

print("-----------------------------Read file-------------------------------------------\n\n")
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

#replace a,b,a-z,A-Z,0-9 Strings---------------------

print("\n\n-----------------------------End List-------------------------------------------\n\n")
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
            mul=[]
            mul_set = j.split(",")
            for xy in mul_set:
                if (xy=='a-z'):
                    mul.append(alphaS)
                elif(xy=='A-Z'):
                    mul.append(alphaC)
                elif(xy=='0-9'):
                    mul.append(num)
                else:
                    mul.append(xy)
            mod.append(mul)
        else:
            mod.append(j)
    list1.append(mod)
print(list1)

#now coding the NFA Sequence------------------------------------

f = open("input.txt","rt")
lines= f.read()
list_L = lines.split()
print("\n\n------------------------Lexemes-----------------------------\n\n")
print (list_L)

for inp in list_L:
    sets=[0]
    print( "\n\n------------------------ lexeme ", inp,"-----------------------------\n")
    state=0
    for i in inp:
        tempstate=[]
        flag = False
        for state in sets:
            x = list1[state]
            for j in range(len(x)):
                if i in x[j]:
                    flag=True
                    tempstate.append(j)
                else:
                    for jj in range(len(x[j])):
                        if(i in x[j][jj]):
                            flag=True
                            tempstate.append(j)
            if flag:
                print("Processed String", i)
                print("State ", state)
            else:
                print("String not Accepted ",i)
        sets=tempstate
        print ("\nSet",sets)
    if((len(list1[0])-1) in sets):
        print ("!--------------------String Accepted------------------------!")
    else:
        print ("String not Accepted")
