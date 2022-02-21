def seperator(src):
    inp=[]
    terminal=['+','*','=']
    for pos,val in enumerate(src):
        for pos1,val1 in enumerate(val):
            if identifier(val1) and not keyword(val1) and val1 != 'main':
                inp.append(val1)
            elif val1 in terminal:
                inp.append(val1)            
    return inp  



inp=seperator(src)
print(inp)

table=[x.split() for x in open('grammar1_table','r').readlines()]
gra=[x.split() for x in open('grammer1.txt','r').readlines()]

grammer=[]
for pos, val in enumerate(gra):
    for pos1,val1 in enumerate(val):
        grammer.append(val1)


inp_val=[]
inp_buffer=[]
for val in inp:
    if identifier(val):
        inp_buffer.append('id')
        inp_val.append(val)
    else:
        inp_buffer.append(val)
inp_buffer+='$'
print("Buffer input = ",inp_buffer)



inp=inp_buffer
stack=['0']
pointer=0
val_pointer=0
temp=0
temp_dict={}    
while True:
    print(stack)
    for pos, val in enumerate(table):
        if table[pos][0]==stack[-1]:
            row=pos

            
    for pos in range(len(table[0])):
        if table[0][pos] == inp[pointer]:
            col=pos

    if table[row][col][0]=='s':
        if inp[pointer] == 'id':
            stack.append(inp_val[val_pointer])
            val_pointer+=1
            pointer+=1
        else:
            stack.append(inp[pointer])
            pointer+=1
        stack.append(table[row][col][1])
    elif table[row][col][0]=='r':
        production=grammer[(int(table[row][col][1]))]

        if (production == 'F->i'):
            F_place=inp_val[val_pointer-1]
        elif (production == 'T->F'):
            T_place = F_place
        elif (production == 'T->T*F'):
            t='t'+str(temp)
            T_place = T_place + " * " + F_place
            temp_dict.update({t:T_place})
            T_place=t
            temp+=1
        elif (production == 'E->T'):
            E_place = T_place
            
        elif (production == 'E->E+T'):
            t='t'+str(temp)
            E_place =E_place + " + "+ T_place
            temp_dict.update({t:E_place})
            E_place=t
            temp+=1
       
        pop=len(production[3:])*2
        for i in range(0,pop):
                stack.pop()
        stack.append(production[0])
            
        for j,i in enumerate(table):
            if i[0]==stack[-2][0]:
                row=int(j)
        col=int([j for j,i in enumerate(table[0]) if i==production[0]][0])
        stack.append(table[row][col])
    elif table[row][col]=='accept':
        temp_dict.update({inp_val[0] :t}) 
        print('Accepted')
        break
    elif table[row][col]=='-':
        print ("not Accepted")
        break

print(".....................Symentic Rules........................")
for i in temp_dict:
    print(i,"=",temp_dict.get(i))
