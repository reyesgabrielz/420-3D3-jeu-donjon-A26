from models.comportement import Comportement

class ComportementFurtif(Comportement):
    def __init__(self):
        self.tour_furtif = 0

    def agir(self):
        self.tour_furtif += 1
        if self.tour_furtif % 2 == 0:
            return "defend"
        else:
            return "attaque"