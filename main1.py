# dictionary- program to remove duplicte data
dictator={'id1':{'name':['lucas'],'class':['8'],'subject':['english,math,science']},
          
'id2':{'name':['lucy'],'class':['11'],'subject':['english,math,science']},

'id3':{'name':['lucas'],'class':['8'],'subject':['english,math,science']},
'id4':{'name':['jonny'],'class':['8'],'subject':['english,math,science']},}

dict={}
for key, value in dictator.items():
    if value not in dict.values():
        dict[key]=value
print(dict)