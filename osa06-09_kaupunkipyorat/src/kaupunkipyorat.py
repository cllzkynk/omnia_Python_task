import math

def hae_asematiedot(asema_tiedosto: str) -> dict:
    asemat = {}
    with open(asema_tiedosto) as tiedosto:
        next(tiedosto)  
        for rivi in tiedosto:
            osat = rivi.strip().split(';')
            if len(osat) >= 4:
                try:
                    lon = float(osat[0])
                    lat = float(osat[1])
                    nimi = osat[3]
                    asemat[nimi] = (lon, lat)
                except ValueError:
                    continue
    return asemat

def etaisyys(asemat: dict, asema1: str, asema2: str) -> float:
    if asema1 not in asemat or asema2 not in asemat:
        raise ValueError("Asemaa ei löydy sanakirjasta")
    
    lon1, lat1 = asemat[asema1]
    lon2, lat2 = asemat[asema2]
    
    x_km = (lon1 - lon2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    
    return math.sqrt(x_km**2 + y_km**2)

def suurin_etaisyys(asemat: dict) -> tuple:
    max_etaisyys = 0.0
    asema1 = ""
    asema2 = ""
    asema_nimet = list(asemat.keys())
    
    for i in range(len(asema_nimet)):
        for j in range(i+1, len(asema_nimet)):
            nykyinen_etaisyys = etaisyys(asemat, asema_nimet[i], asema_nimet[j])
            if nykyinen_etaisyys > max_etaisyys:
                max_etaisyys = nykyinen_etaisyys
                asema1 = asema_nimet[i]
                asema2 = asema_nimet[j]
    
    return (asema1, asema2, max_etaisyys)