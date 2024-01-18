class Fogadasi_fordulo:
    def __init__(self, sor: str) -> None:
        adatok = sor.split(';')
        self.ÉV = int(adatok[0]) 
        self.Hét = int(adatok[1])
        self.Forduló = int(adatok[2])
        self.Ny13p1 = int(adatok[3])
        self.T13p1 = int(adatok[4])
        self.Eredmények = adatok[5]
    
    def volt_döntetlen() -> bool:
        #for e in self.Eredmények:
            #if e == 'X':
                #return True
        #return False
    
        if 'X' in self.Eredmények:
            return True
        return False