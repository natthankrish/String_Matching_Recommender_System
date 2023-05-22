class Product:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.match = 0
    
    def getName(self):
        return self.name

    def getCategory(self):
        return self.category

    def getMatch(self):
        return self.match
    
    def info(self):
        print(self.name, self.category, self.match)

    def updateMatch(self, newmatch):
        self.match = newmatch