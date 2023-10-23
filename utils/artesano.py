from dataclasses import dataclass

@dataclass
class Artesano:
    name :str
    mail :str
    numero :str
    region :str
    comuna :str
    artesanias :list[str]
    comentario : str