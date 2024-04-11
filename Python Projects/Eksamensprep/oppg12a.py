class Person():
    def __init__(self, navn, ektefelle="singel"):
        self.navn = navn 
        self.ektefelle = ektefelle

    def visStatus(self):
        if(self.ektefelle=="singel"):
            print("Jeg er singel")
        else:
            print("Jeg er gift med", self.ektefelle)
            
    def gifteMeg(self, nyttEktefelle):
        if(self.ektefelle!="singel"):
            print(f"Beklager {nyttEktefelle.navn}. Jeg er allerede gift med {self.ektefelle}")
        else: 
            self.ektefelle = nyttEktefelle.navn


brad = Person("Brad Pitt")
brad.visStatus()

angie = Person("Angelina Jolie")
brad.gifteMeg(angie)
brad.visStatus()

jo = Person("Jo By")
brad.gifteMeg(jo)