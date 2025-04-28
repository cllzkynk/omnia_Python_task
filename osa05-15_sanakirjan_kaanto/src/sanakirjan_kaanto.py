# tee ratkaisu tänne

def kaanna(s):
    uus_dict={}
    for key , value in s.items():
        uus_dict[value]=key
    s.clear()
    s.update(uus_dict)



if __name__ == "__main__":

 s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
 kaanna(s)
 print(s)