from models.comportement import Comportement

class Ennemi:
    def __init__(self, nom, hp, attaque, Comportement):
        self.nom = nom
        self.hp = hp
        self.hp_max = hp
        self.attaque = attaque
        self._comportement = Comportement

    def agir(self) -> str:
        return self._comportement.agir(self)

    def set_comportement(self, comportement: Comportement) -> None:
        self._comportement = comportement

    def recevoir_degats(self, degats):
        self.hp = max(0, self.hp - degats)

    def est_vivant(self):
        return self.hp > 0