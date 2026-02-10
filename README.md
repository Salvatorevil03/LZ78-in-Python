# Python LZ78: Compression & Analysis

Questo repository contiene un'implementazione didattica in **Python** dell'algoritmo di compressione lossless **LZ78**. Il progetto non si limita alla codifica e decodifica, ma include strumenti per la generazione di dati sintetici e l'analisi statistica delle performance in termini di entropia e tasso di compressione.

## 🚀 Funzionalità

* **Codifica LZ78**: Implementazione dinamica del dizionario con gestione incrementale dei bit per l'indirizzamento dei prefissi.
* **Decodifica LZ78**: Ricostruzione del messaggio originale a partire dal flusso di bit.
* **Generatore IID**: Generatore di simboli basato su una distribuzione di probabilità definita (Indipendenti e Identicamente Distribuiti).
* **Analisi Statistica**: Calcolo dell'entropia teorica, empirica e del tasso di codifica finale.

---

## 🛠️ Come Funziona

L'algoritmo LZ78 costruisce un dizionario di "frasi" durante la scansione dell'input. Ogni nuova frase è composta da un **prefisso** (già esistente nel dizionario) e un **nuovo simbolo**.

### Logica di Codifica
1. Legge i simboli in sequenza finché non trova una sottostringa non presente nel dizionario.
2. Memorizza la nuova frase assegnandole un indice univoco.
3. Emette in output una coppia: `(indice_prefisso, simbolo_nuovo)`.
4. Il numero di bit usati per l'indice cresce logaritmicamente con il numero di frasi memorizzate per ottimizzare lo spazio.
