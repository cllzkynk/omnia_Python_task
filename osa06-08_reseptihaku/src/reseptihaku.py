def hae_nimi(tiedosto: str, sana: str) -> list:
    reseptit = []
    with open(tiedosto, 'r', encoding='utf-8') as file:
        content = file.read().split('\n\n')  # Ttarifleri boş satırlara göre ayır
    
    for recipe in content:
        if recipe.strip():  # boş olmayan tarifler için
            lines = recipe.split('\n')
            name = lines[0].strip()
            if sana.lower() in name.lower():
                reseptit.append(name)
    return reseptit

def hae_aika(tiedosto: str, aika: int) -> list:
    reseptit = []
    with open(tiedosto, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    i = 0
    while i < len(lines):
        if lines[i]:  # nimi
            nimi = lines[i]
            i += 1
            if i < len(lines) and lines[i].isdigit() and int(lines[i]) <= aika:
                valmistusaika = lines[i]
                reseptit.append(f"{nimi}, valmistusaika {valmistusaika} min")
            # seureva recipe
            while i < len(lines) and lines[i]:
                i += 1
        i += 1
    return reseptit

def hae_raakaaine(tiedosto: str, aine: str) -> list:
    reseptit = []
    with open(tiedosto, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    i = 0
    while i < len(lines):
        if lines[i]:  # Rnimi
            nimi = lines[i]
            i += 1
            if i < len(lines) and lines[i].isdigit():  # aika 
                valmistusaika = lines[i]
                i += 1
                aineet = []
                while i < len(lines) and lines[i]:  # ingredients
                    aineet.append(lines[i].lower())
                    i += 1
                
                if aine.lower() in aineet:
                    reseptit.append(f"{nimi}, valmistusaika {valmistusaika} min")
            else:  # no aika
                while i < len(lines) and lines[i]:
                    i += 1
        i += 1
    return reseptit