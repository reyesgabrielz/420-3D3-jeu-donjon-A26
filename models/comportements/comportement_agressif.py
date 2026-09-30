from models.comportement import Comportement

class ComportementAgressif(Comportement):
    def agir(self):
            return "attaque"