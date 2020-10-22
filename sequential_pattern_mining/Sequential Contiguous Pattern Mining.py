#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import fileinput
import itertools
import re
from itertools import product
min_sup=2
db=[]
for line in fileinput.input():
    line=line.strip('\n')
    #line=line.split()
    #print(type(line))
    db.append(line)
#print("db: ",db)
for i in range(len(db)):
    db[i]=db[i].split()

        
def count_(string, sub):
    count=0
    for i in range(len(string)-len(sub)+1):
        if string[i:i+len(sub)]==sub:
            count+=1
    return count

out={}
for line in db:
    
    track_dict={}
    temp_st=""

    st=[]
    for item in line:
        st.append(item)

    for i in range(len(st)-1):
        test=[]
        test.append(st[i])
        test.append(st[i+1])
        #print("test:",test)
        if tuple((test)) not in track_dict.keys():
            #print("yes")
            track_dict[tuple((test))]=1
        else:
            track_dict[tuple((test))]+=1
 
        track=2#number of ele
        while track+i<len(st):
            #track+=1
            if track<5:
                test.append(st[track+i])
                track+=1
                if tuple((test)) not in track_dict.keys():
                    track_dict[tuple((test))]=1
                else:
                    track_dict[tuple((test))]+=1

            else:
                break
    #end iterating the one line. update final dictionary.
    #print("track: ",track_dict)
    for k,v in track_dict.items():
        if k in out.keys():
            out[k]+=v
        else:
            out.update({k:v})
        
        

    

out={k:v for k, v in out.items() if v>=min_sup}
#print(len(out.keys()))

out_final=[]

out=sorted(out.items(),key=lambda x:(-x[1],x[0]))
if len(out)>20:
    out=out[:20]
#print(len(out))
for o in out:
    out_final.append(o)
for i in range(len(out_final)):
     print("["+str(out_final[i][1])+", "+"'"+' '.join(out_final[i][0])+"'"+"]")
#print("out_final2: ",out)  
    
#print(len(out.keys()))
    
# a="AB"
# b="ABABABA"
#print(count_(b,a))
    
    
    
    
        

