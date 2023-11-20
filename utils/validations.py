from utils.artesano import Artesano
from utils.hincha import Hincha
from database.regiones import REGIONES
from database.db import check_deportes
import filetype
ARTESANIAS = ["mármol", "madera", "cerámica", "mimbre", "metal", "cuero", "telas", "joyas", "otro"]
TRANSPORTES = ["particular","locomoción pública"]
import re

def validate_deportes(ls: list[str]):
    is_val = (1 <= len(ls) <= 3)
    for deporte in ls:
        is_val = is_val and check_deportes(deporte)
    return is_val

def validate_transporte(ls: str):
    return ls in TRANSPORTES

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


def validate_files_artesano(conf_img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    is_val = True

    is_val = is_val and (1<=len(conf_img)<=3)

    for img in conf_img:
        if img is None:
            return False

        # check if the browser submitted an empty file
        if img.filename == "":
            return False
    
    # check file extension
        ftype_guess = filetype.guess(img)
        if ftype_guess == None  or ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
    # check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
    return is_val

def validate_entry_hincha(val: Hincha):
    is_val = True
    is_val = is_val and validate_email(val.mail)
    is_val = is_val and validate_name(val.name)
    is_val = is_val and validate_region(val.region)
    is_val = is_val and validate_comuna(val.comuna)
    is_val = is_val and validate_deportes(val.deportes)
    is_val = is_val and validate_transporte(val.modo_transporte)
    if (val.numero != ""):
        is_val = is_val and validate_phone(val.numero)
    return is_val