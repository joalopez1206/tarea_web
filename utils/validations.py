from utils.artesano import Artesano
from database.regiones import REGIONES
ARTESANIAS = ["mármol", "madera", "cerámica", "mimbre", "metal", "cuero", "telas", "joyas", "otro"]
import re

def validate_comuna(s: str):
    if s:
        return True
    return False

def validate_artesanias(s :list[str]):
    if s:
        test1 = 1<=len(s)<=3
        test2 = any([artes in ARTESANIAS for artes in s])
        return test1 and test2
    return False

def validate_name(s: str):
    if s:
        return 1<=len(s)<=80
    return False

def validate_region(s :str):
    if s:
        return s in REGIONES
    return False

def validate_email(s :str):
    if s:
        rexpr = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
        return False if re.match(rexpr, s) is None else True  
    return False

def validate_phone(s :str):
    if s:
        rexpr = r"^[0-9]+$"
        test = False if re.match(rexpr, s) is None else True
        return len(s) >= 9 and test

def validate_entry_artesano(val: Artesano):
    is_val = True
    is_val = is_val and validate_artesanias(val.artesanias)
    is_val = is_val and validate_email(val.mail)
    is_val = is_val and validate_name(val.name)
    is_val = is_val and validate_region(val.region)
    is_val = is_val and validate_comuna(val.comuna)
    if (val.numero != ""):
        is_val = is_val and validate_phone(val.numero)
    return is_val