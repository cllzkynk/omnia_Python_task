# tee ratkaisu tänne

 


 

def nelio(sana,num):
   sana_box=sana*(int((num*num)/len(sana))+1)
   index=0
   while index+num<=len(sana_box):
    print(sana_box[index:index+num])
    index=index+num

if __name__ == "__main__":
    nelio("ab",3)
    nelio("aybabtu",5)