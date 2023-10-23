from dataclasses import dataclass

@dataclass
class artesano:
    name :str
    mail :str
    region :str
    comuna :str
    artesanias :list[str]