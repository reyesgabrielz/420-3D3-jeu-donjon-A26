from random import random
from models.comportement import Comportement

class ComportementAleatoire(Comportement):
    def agir(self):
            return random.choice(["attaque", "defend"])