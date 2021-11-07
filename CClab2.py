f = open ("source.txt","rt")
lines= f.readlines()
#print(lines)


#removing tabs and \n
temp2_list=[]
temp_list=[]
main_list=[]
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
    main_list.append(res)       


print(main_list)

















