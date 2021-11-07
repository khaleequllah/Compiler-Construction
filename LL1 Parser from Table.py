#print("Read file -------------------------------------------\n\n")
f = open("grammer.txt","rt")
lines= f.readlines()
#print(lines)

#removing tabs and \n
temp4_list=[]
temp3_list=[]
parseTable=[]
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
    parseTable.append(res)

#print("List is:")
#print(parseTable)

print("Printing Table -------------------------------------------\n")

for i in parseTable:
    for j in i:
        print(j,'\t',end='')
    print()

print("\nTerminal Set -------------------------------------------\n")

T_set=[]
for i in range(len(parseTable)):
    for j in parseTable[i]:
        if(i==0):
            T_set.append(j)
T_set.pop(0)        
for i in T_set:
    print(i,'\t',end='')

print("\n\nInput String -------------------------------------------\n")

stack=[]
stack.append('$')
#print(stack)
inputs=[]
print("-> Enter character then press Enter for another.")
print("-> Choose Set from the Terminal Set shown.\n")
while(True):
    st = input("Enter the string (Enter $ to end string): ")
    if(st in T_set):
        inputs.append(st)
    else:
       print("\n-> Wrong Input! \n-> Choose from Terminal Set") 
    if(st == "$"):
        break

print("\nInput Set")    
for i in inputs:
    print(i,' ',end='')

#Replace id with i for easy parsing
for n, i in enumerate(inputs):
    if i == 'id':
        inputs[n] = 'i'        


#print(T_set)

#Add keys and values in dictionary
        
parsingTable ={
    
}

for n,i in enumerate(parseTable):
    for m,j in enumerate(i):
        if(n>0):
            if(m>0):
                if(j!=''):
                    #print(j, 'i: ', n,'j: ', m )
                    #print('j: ',j, parseTable[n][0], parseTable[0][m] )
                    temp=[]
                    if(parseTable[0][m]=='id'):
                        if(j=='id'):
                            x='i'
                            parsingTable[parseTable[n][0],y]=x
                        else:
                            y='i'
                            parsingTable[parseTable[n][0],y]=j
                    else:
                        if(j=='id'):
                            x='i'
                            parsingTable[parseTable[n][0],y]=x
                        else:
                            parsingTable[parseTable[n][0],parseTable[0][m]]=j


#print("\n\nOur-------------------------------------------\n")
#print("Our Dictionary")
#print(parsingTable)

print("\n\npushing and poping stack-------------------------------------------\n")

start_symbol=parseTable[1][0]
flag = 0
user_input = inputs
stack = []
stack.append("$")
stack.append(start_symbol)
input_len = len(user_input)
index = 0
#print(user_input)
while len(stack) > 0:
    top = stack[len(stack) - 1]
    print("Top =>", top)
    current_input = user_input[index]
    if(current_input == 'i'):
        print("Current_Input => id")
    else:
        print("Current_Input => ", current_input)
    
    if top == current_input:
        stack.pop()
        index = index + 1
    else:
        key = top, current_input
        print(key)
        if key not in parsingTable:
            flag = 1
            break
        value = parsingTable[key]
        if value != '@':
            #print("val",value)
            value = value[::-1]
            #print("val",value)
            value = list(value)
            #print("val",value)
            #print(stack)
            stack.pop()
            #print(stack)
            for element in value:
                stack.append(element)
                #print(stack)
        else:
            stack.pop()
            
if flag == 0:
    print("String accepted!")
else:
    print("String not accepted!")














