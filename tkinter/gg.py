from datetime import datetime,date,timedelta
class article:
    def _init_(self,ns,prix,qunt,qunm):
        self._ns=ns
        self._prix=prix
        self._qunt=qunt
        self._qunm=qunm
    def _str_(self) -> str:
        return f"{self._ns}\t{self._prix}\t{self._qunm}\t{self._qunt}"
    def  approvisionner(self,qte): 
        self._qunt = self._qunt + qte        
    def achat(self,qte): 
        if self._qunt-qte>=self._qunm:
            self._qunt -=qte
        else:
            print("impossibe d'effectuer l'achat")
    def _str_(self) :
        return f"{self._ns}\t{self._prix}\t{self._qunt}\t{self._qunm}"
class electromenager(article):
    def _init_(self, ns, prix, qunt, qunm,p,d):
        super()._init_(ns, prix, qunt, qunm)
        self.poids=p
        self.duree=d
    def datefingardantie(self):
        d=datetime.today()
        d=d.date()
        return d+timedelta(days=self.duree*30)
    def _str_(self) -> str:
        return super()._str_()+f"{self.poids}\t{self.duree}"