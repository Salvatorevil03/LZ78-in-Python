import math
import random

# converte un valore "n" in base 2, su N bit
def conversioneBinaria(n,N):
    # bin(4) => 0b100 
    return bin(n)[2:].zfill(N)

X = [0, 1, 2 , 3] # alfabeto sorgente
codeBook = {"0":"00", "1":"01", "2":"10", "3":"11"} # codifica sorgente per simbolo
codeBook_inverso = {"00":"0", "01":"1", "10":"2", "11":"3"} # decodifica sorgente per simbolo

# leggo frase nuova -> salvo nel dict -> creo coppia add prefix + simbolo nuovo
# e poi codifco coppia, concateno e aggiungo a codifica
# e poi vado a leggere una nuova frase
def codifica(emissione):
    dizionario = {0:""}
    coppie = []
    frase = ""
    numFrasi = 0
    numBit = 1
    codifica = ""
    for e in emissione:
        frase = frase + e
        if frase not in dizionario.values(): # trovata frase nuova
            # aggiungo frase nuova al dizionario
            # la quale avrà un suo indice
            indice = max(dizionario.keys())+1
            dizionario[indice] = frase

            # prendo la coppia (indice, frase)
            # e la converto in (add prefisso, simbolo nuovo)
            valorePrefisso = frase[0:len(frase)-1]
            indicePrefisso = next(k for k, v in dizionario.items() if v == valorePrefisso)
            coppia = (indicePrefisso,frase[len(frase)-1])
            coppie.append(coppia)

            # ora codifcio singolarmente add prefisso e simbolo nuovo
            # della coppia appena generata
            stringa = conversioneBinaria(coppia[0],numBit)+codeBook[coppia[1]]
            codifica = codifica + stringa
            numFrasi = numFrasi + 1
            """
            ogni volta che il log del num di frasi è un num intero
            vuol dire che devo aumentare in numero di bit per l'add prefisso
            """
            if math.log2(numFrasi).is_integer() and math.log2(numFrasi)!=0:
                numBit = numBit +1
            
            # finito tutto resetto "frase", per iniziare la ricerca di un'altra
            frase = ""
    if frase != "":
        # caso in cui l'ultima frase è solo add prefisso senza nuovo simbolo
        # vuol dire che non sono mai entrato nell'if per resettare frase
        # devo comunque codificare l'add prefisso
        indicePrefisso = next(k for k, v in dizionario.items() if v == frase)
        stringa = conversioneBinaria(indicePrefisso,numBit)
        codifica = codifica + stringa


    return dizionario, coppie, codifica

# leggo indirizzo su tot bit, leggo simbolo
# ho la coppia (add prefisso, simbolo nuovo)
# ottengo (indice, frase)
# la coppia la aggiungo al dizionario
# la frase la concateno all'emissione
def decodifica(emissione_codificata):
    numFrasi = 0
    numBitAdd = 1
    add = "" # indirizzo del prefisso
    count = 0 # di bit letti di address
    flag_add = True
    coppie = []
    parola_codice = ""
    dizionario = {0:""}
    decodifica = ""
    for emissione in emissione_codificata:
        if flag_add == True: # vuol dire che devo leggere indirizzo
            count = count +1
            add = add + emissione
            if count == numBitAdd: # letto il giusto numero di bit, resetto il count e inizio la ricerca di una parola codice
                count = 0
                flag_add = False
        else:
            parola_codice = parola_codice + emissione
            if parola_codice in codeBook_inverso: # riconosciuta parola codice
                # trovata la parola codice, decodifico sia l'add del prefisso che la parola codice
                # e creo la coppia decodificata (add prefisso, simbolo nuovo)
                coppia = (int(add,2),codeBook_inverso[parola_codice])
                coppie.append(coppia)

                # concateno valore del prefisso (trovato grazie al suo address nel dict che sto costruendo) con il valore del simbolo nuovo
                indice = max(dizionario.keys())+1
                dizionario[indice] = dizionario[coppia[0]]+coppia[1]

                # aggiorno la decodifica, con il nuovo blocco di emissioni
                decodifica = decodifica + dizionario[indice]

                # reset di tutto e preparazione alla ricerca di una nuova coppia
                add = ""
                parola_codice = ""
                numFrasi = numFrasi + 1
                if math.log2(numFrasi).is_integer() and math.log2(numFrasi)!=0:
                    numBitAdd = numBitAdd +1
                flag_add = True # indico che devo tornare a cercare un address
    if add != "":
        # caso di add_prefisso da solo, vedo il valore del dict al suo indice e lo aggiungo alla decodifica
        decodifica_add = int(add,2)
        decodifica = decodifica + dizionario[decodifica_add]
    return dizionario, coppie, decodifica

# genera simboli iid 0 -> 0.15 1 -> 0.30 2 -> 0.20 3 -> 0.35
def generatore_iid():
    for i in range(1,100000):
        r = random.random()  # uniforme in [0,1)
        if r < 0.15:
            yield 0
        elif r < 0.15 + 0.30:
            yield 1
        elif r < 0.15 + 0.30 + 0.20:
            yield 2
        else:
            yield 3

# entropia teorica
def entropia(pdf):
    H = 0
    for p in pdf:
        H = H - p*math.log2(p)
    return H

def entropia_empirica(emissione):
    H = 0
    n = len(emissione)
    if n == 0:
        return 0
    frequenze = {}
    for simbolo in emissione:
        if simbolo in frequenze:
            frequenze[simbolo] += 1
        else:
            frequenze[simbolo] = 1
    for count in frequenze.values():
        p = count / n
        H = H - p * math.log2(p)
    return H

def tasso_di_codifica(emissione,codifica):
    num_bit = len(codifica)
    num_emissioni = len(emissione)
    return num_bit/num_emissioni

if __name__ == "__main__":
    emissione = "2311013130323311233011021113323033212101301010310122"
    emissione = ""
    for e in generatore_iid():
        emissione = emissione+str(e)

    print("EMISSIONE:\n"+emissione+"\n")

    dizionario, coppie, emissione_codificata = codifica(emissione)

    print("DIZIONARIO:")
    print(dizionario)
    print("\n")

    print("COPPIE:")
    print(coppie)
    print("\n")

    print("CODIFICA:\n"+emissione_codificata)
    print("\n")

    dizionario, coppie, emissione = decodifica(emissione_codificata)

    print("DIZIONARIO:")
    print(dizionario)
    print("\n")

    print("COPPIE:")
    print(coppie)
    print("\n")

    print("DECODIFICA:\n"+emissione+"\n")

    print("ENTROPIA TEORICA:\n"+str(entropia([0.15, 0.3, 0.2, 0.35])))
    print("\n")

    print("ENTROPIA EMPIRICA:\n"+str(entropia_empirica(emissione)))
    print("\n")

    print("TASSO DI CODIFICA:\n"+str(tasso_di_codifica(emissione,emissione_codificata)))
    # miglior risultato 2.047370016