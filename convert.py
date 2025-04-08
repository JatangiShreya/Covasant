input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(input[-1][0])
final_res=[]
res_lst=[]
for item in input[-1]:
    sub_lst=[]
    for inner_item in item:
        ind=inner_item
        inner_item=inner_item.strip('( )').split(',')
        con_lst=[]
        for ele in inner_item:
            con_lst.append(int(ele))
        sub_lst.append(list(con_lst))
    res_lst.append(sub_lst)
final_res.append(res_lst)    
print(final_res)
        
  
