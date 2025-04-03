"""Given:D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
Create below:
 union of keys, #value does not matter
D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
 intersection of keys, #value does not matter
D_INTERSECTION = {'ok': 1}
D1- D2 = {'nok': 2 }
values are added for same keys
D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }"""

D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }


#D_UNION={}
#for key,value in D1.items():
 #   D_UNION[key]=value
#for key,value in D2.items():
 #   D_UNION[key]=value
#print(D_UNION)

#D_INTERSECTION={}
#for key,value in D1.items():
#   if key in D2:
#       D_INTERSECTION[key]=value
#print(D_INTERSECTION)


#D1_D2={}
#for key,value in D1.items():
 #   if key not in D2:
 #       D1_D2[key]=value
#print(D1_D2)

#D_MERGE={}
#for key1,value in D1.items():
 #   for key2,value2 in D2.items():
  #      if key1==key2:
   #         D_MERGE[key1]=value+value2
  #          
  #      else:
   #         D_MERGE[key1]=value
    #        D_MERGE[key2]=value2
       
#print(D_MERGE)
        
        
    

