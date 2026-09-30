from models.comportement import Comportement

class ComportementDefensif(Comportement):
    def agir(self):
            if self.hp < self.hp_max * 0.5:
                return "defend"
            else:
                return "attaque"