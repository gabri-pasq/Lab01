import random




class Domanda:
    def __init__(self, livello, quesito , risposte,corretta ):
        self.livello=livello
        self.quesito=quesito
        self.risposte=risposte
        self.corretta=corretta

    def __str__(self):
        r=""
        for indice,risposta in enumerate(self.risposte):
            if risposta == self.corretta:
                self.numeroCorretto=indice+1
            r+= "\n"+str(indice+1)+". " + risposta
        return f"Domanda: {self.quesito} {r}"

class Game:
    def __init__(self,domande):
        self.domande=domande
    def livMax(self):
        liv=0
        for d in self.domande:
            if d.livello > liv:
                liv = d.livello
        return liv

    def round(self):
        punteggio=0
        over=False
        while over == False:
            ok=False
            while ok == False:
                n = random.randint(0,len( self.domande)-1)
                if self.domande[n].livello == punteggio:
                    print(self.domande[n])
                    ris=input("Risposta: ")
                    if ris==str(self.domande[n].numeroCorretto):
                        self.domande.pop(n)
                        punteggio+=1
                        print("\nCORRETTA")
                        print("SCORE:", punteggio)
                        print()
                    else:
                        print("Risposta Corretta:",self.domande[n].corretta)
                        print()
                        over=True
                    ok=True
                if punteggio == self.livMax() or over==True:
                    over = True
                    print("PARTITA FINITA")
                    print("SCORE:", punteggio)
                    return punteggio
    def registraScore (self,punteggio):
        lista_giocatori=[]
        giocatore=Player(input("NICKNAME: "), punteggio)
        lista_giocatori.append(giocatore)
        file1 = open("punti.txt","r",encoding="utf-8")
        fine1=False
        while fine1 == False:
            riga1 = file1.readline()
            if riga1 == "":
                fine1 = True
            else:
                campi=riga1.strip("\n").split(" ")
                g=Player(campi[0],int(campi[1]))
                lista_giocatori.append(g)
        file1.close()

        lista_giocatori_ordinata= sorted(lista_giocatori,key=lambda x: x.punti,reverse=True)
        file2=open("punti.txt","w",encoding="utf-8")
        numero=0
        for gi in lista_giocatori_ordinata:
            if numero==0:
                file2.write(gi.__str__())
                numero+=1
            else:
                file2.write("\n"+gi.__str__())
        file2.close()

class Player:
    def __init__(self,nick,punti):
        self.nick=nick
        self.punti=punti
    def __str__(self):
        return f"{self.nick} {self.punti}"

def costruzione():
    lista_domande=[]
    file= open("domande.txt","r", encoding="utf-8")
    fine=False
    i=0
    risposte=set()
    while fine == False :
        riga=file.readline()
        if riga == "" :
            fine=True
        else:
            riga=riga.strip("\n")
            if i == 7:
                domanda = Domanda(livello, quesito, risposte, corretta)
                lista_domande.append(domanda)
                i = 0
                risposte=set()
            if i==0 :
                quesito = riga
            elif i == 1 :
                livello= int(riga)
            elif i==2 :
                corretta=riga
                risposte.add(riga)
            elif i==3 or i==4 or i==5 :
                risposte.add(riga)
            i+=1
    file.close()
    return lista_domande
def main():
    costruito= costruzione()
    gioco=Game(costruito)
    p=gioco.round()
    gioco.registraScore(p)

main()
