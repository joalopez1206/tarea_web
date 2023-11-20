from dataclasses import dataclass

@dataclass
class Hincha:
    name :str
    mail :str
    numero :str
    region :str
    comuna :str
    deportes :list[str]
    comentario : str
    modo_transporte :str