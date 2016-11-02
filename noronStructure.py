import  numpy as np
import math

class nouralNetwork(object):
    def __init__(self,inputset,outpuset,katmanSayisi,araKatman,inputsayisi,outputsayisi,*arg):

        self.katmanSayisi=katmanSayisi
        self.araKatman=araKatman
        self.arg=arg
        self.outputsayisi=outputsayisi
        self.i=0
        self.agirlikArray =[]
        self.inputsayisi=inputsayisi
        self.inpuset=inputset
        self.outpuset=outpuset


    def nonlinFonk(self, x, deriv=False):
        if (deriv == True):
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))

    def tanhFonk(self, x, deriv=False):
        if (deriv == True):
            return 1 - (math.tanh(x) * math.tanh(x))
        return math.tanh(x)

    def noronYapisi(self):
        if int(self.araKatman) > (int(self.katmanSayisi) - 2):
            return "\n*** HATA!  Arakatman sayısı Katman sayısından büyük olamaz"

        if len(self.arg) > int(self.araKatman):
            return "Ara katman sayısını aştınız. Lütfen ara katman sayısı kadar istediğiniz noron sayısını giriniz."
        if len(self.arg) < int(self.araKatman):
            return "Ara katman sayısından az sayıda noron değeri girdiniz. Lütfen ara katman sayısı kadar istediğiniz noron sayısını giriniz."



        return "Sectiğiniz kriterler: Katman Sayısı:" ,self.katmanSayisi ,"Ara katman Sayisi:",self.araKatman , " katman nöron sayıları " ,self.arg

    def agirlikBelirle(self):
        deger=len(self.arg)
        self.i=0;
        self.agirlikArray.append(2 * np.random.random((self.inputsayisi, self.arg[self.i])) - 1)
        self.i=self.i+1
        while self.i < (deger):
            self.agirlikArray.append(2 * np.random.random((self.arg[(self.i-1)],self.arg[self.i] )) - 1)
            self.i=(self.i+1)
        return self.agirlikArray

    def islemekoy(self):
        self.i=0
        deger = len(self.arg)
        self.islenmisagirlik = self.nonlinFonk(np.dot(self.inpuset, self.agirlikArray[self.i]))
        self.i = 1
        while self.i < (deger):
            self.islenmisagirlik = self.nonlinFonk(np.dot(self.islenmisagirlik, self.agirlikArray[self.i]))
            self.i = (self.i + 1)

        l1_error = ( self.outpuset - self.islenmisagirlik);
        l1_delta=l1_error*self.nonlinFonk(self.islenmisagirlik,True)
        self.agirlikArray[0]+= np.dot((self.inpuset).T, l1_delta)
        return self.agirlikArray[0]














