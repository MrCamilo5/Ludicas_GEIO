class LudicaMamuts:
    from random import randint
    #No optimizado
    def __init__(self, ini):
        self.ini=int(ini)
        self.mamuts=[1 for i in range(ini)]
        self.pob=[ini]
        self.era=1
        self.lim=self.era
        self.d=self.dado()
        self.teorias={'Primera_teoria': self.primerateoria(),
                    'Segunda_teoria':self.segundateoria(),
                    'Tercera_teoria':self.tercerateoria(),
                    'Cuarta_teoria':self.cuartateoria()}
        pass
    def dado(self):
        return self.randint(1,6)
    def primerateoria(self):
        while self.era <=8 and len(self.mamuts)>0:
            for j in range(len(self.mamuts)):
                self.d=self.dado()
                if self.d==1:
                    self.mamuts.append(1)
                elif self.d==2 or self.d==3 or self.d==4:
                    self.mamuts.pop()
                else:
                    pass
            self.pob.append(len(self.mamuts))
            self.era+=1
        return self.pob
    def segundateoria(self):
        while len(self.mamuts)<= 4*self.ini and len(self.mamuts)>0:
            for j in range(len(self.mamuts)):
                self.d=self.dado()
                if self.d==1 and self.d==2 and self.d==3:
                    self.mamuts.append(1)
                elif self.d==4 and self.d==5:
                    self.mamuts.pop()
                else:
                    pass
            self.pob.append(len(self.mamuts))
            self.era+=1
            self.lim = self.era
        return self.pob
    def tercerateoria(self):
        while self.era <= self.lim +8 and len(self.mamuts)>0:
            for j in range(len(self.mamuts)):
                self.d=self.dado()
                if self.d==1:
                    self.mamuts.append(1)
                elif self.d==2 or self.d==3:
                    self.mamuts.pop()
                else:
                    pass
            self.pob.append(len(self.mamuts))
            self.era+=1
        return self.pob
    def cuartateoria(self):
        while len(self.mamuts)>0:
            for j in range(len(self.mamuts)):
                self.d=self.dado()
                if self.d==1:
                    self.mamuts.append(1)
                elif  self.d==2 or self.d==3 or self.d==4:
                    self.mamuts.pop()
                else:
                    pass
            self.pob.append(len(self.mamuts))
            self.era+=1
        return self.pob
    pass


corrida=LudicaMamuts(50)

print(corrida.era, corrida.teorias['Primera_teoria'],corrida.teorias['Segunda_teoria'])

import matplotlib.pyplot as plt

plt.plot(corrida.pob)
plt.show()
