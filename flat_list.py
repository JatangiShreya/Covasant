lst =[1,2,3, [1,2,3,[3,[4,5,6],2]]]
res_lst=[]
def flat_lst(lst):
    for item in lst:
        if type(item)==list:
            flat_lst(item)
        else:
            res_lst.append(item)
    return res_lst

print(flat_lst(lst))         
            
