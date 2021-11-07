#SourceCodeinList------------------------------------------
f = open("State_info.txt","rt")
lines= f.readlines()
#print(lines)


#removing tabs and \n
temp2_list=[]
temp_list=[]
State_info=[]
for x in lines:
    z = x
    z = z.replace("\n", "")
    temp_list.append(z)
    
    for i in temp_list:
        y = i.split("\t")
        for i in temp_list:
            i = i.replace("\t", "")
    temp2_list.append(y)
    
for a in temp2_list:
    res = [int(ele) if ele.isdigit() else ele for ele in a]
    State_info.append(res)
print("State Info List is:")
print(State_info)

#SymbolinfoinList------------------------------------------
f = open("Symbol_info.txt","rt")
lines= f.readlines()
#print(lines)


#removing tabs and \n
temp4_list=[]
temp3_list=[]
Symbol_info=[]
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
    Symbol_info.append(res)

print("Symbol Info List is:")
print(Symbol_info)

#Finding Possible Entries ------------------------------------------

inm =input("Enter language: ")
list2=[]
l3=[]
f = open("Symbol_info.txt", "r")
x=f.readlines()
for line in x:
  list2.append(line.rstrip())
  rez = []
for x in list2:
  rez.append(x.replace("\t", ""))
state=0
for x in range(0,len(rez)):
  l3.append(list(rez[x]))

print('symbol',l3)

for i in inm:
  if (i in l3[state]):
    preState=state
    ind=l3[state].index(i)
    state=ind
  else:
    state= False
    break

if(state==False):
  print(inm," is not accepted")  
if (state==4):
  print(inm, " accepted")




