def samat(merkkijono , a,b):
    if len(merkkijono)>a and len(merkkijono)>b and  merkkijono[a]==merkkijono[b]:
        return True
    else : return False
 
 
 
 
 
if __name__ == "__main__":
    print(samat("koodari", 0, 5)) 
 
 
 
 
    """
    def samat(mjono, a, b):
    if a >= len(mjono) or b >= len(mjono):
        return False
    return mjono[a] == mjono[b]
    """