class CompteBancaire:
    def __init__(self, nom = "", solde = 0):
        self.nom = nom
        self.solde = solde
    
    def depot(self, somme):
        self.solde += somme
    
    def retrait(self, somme):
        self -= somme
    
    def __repr__(self):
        return "Compte bancaire de {} : {} euros".format(self.nom, self.solde)
    
print(CompteBancaire("Vanessa", 2000))