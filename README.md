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

### Analisi Matematica
Il progetto calcola l'efficienza del processo confrontando il tasso di codifica con l'**Entropia di Shannon** $H(X)$, definita come:

$$H(X) = -\sum_{i=1}^{n} p(x_i) \log_2 p(x_i)$$

---

## 📋 Struttura del Codice

| Funzione | Descrizione |
| :--- | :--- |
| `codifica()` | Riceve una stringa di simboli e restituisce il dizionario, le coppie e la stringa binaria compressa. |
| `decodifica()` | Riceve la stringa binaria e ricostruisce il messaggio originale. |
| `generatore_iid()` | Genera una sequenza di test basata su probabilità prefissate per i simboli {0, 1, 2, 3}. |
| `entropia_empirica()` | Calcola l'entropia basata sulla frequenza reale dei simboli nell'emissione. |
| `tasso_di_codifica()` | Calcola il rapporto $\frac{\text{bit totali}}{\text{numero emissioni}}$. |

---

## 💻 Utilizzo

Per eseguire il progetto e vedere l'analisi sui dati generati:

1. Assicurati di avere Python 3.x installato.
2. Clona il repository o copia il file `.py`.
3. Esegui lo script:

```bash
python lz78_analyzer.py
```

### Esempio di Output
Lo script genererà una sequenza di 100.000 simboli e mostrerà a terminale:
* Il dizionario costruito (prime/ultime voci).
* Il confronto tra **Entropia Teorica** (basata sulle probabilità fornite) ed **Empirica**.
* Il **Tasso di Codifica** finale (che dovrebbe tendere all'entropia per sequenze molto lunghe).

---

## 📊 Parametri di Default
Il generatore utilizza la seguente distribuzione per l'alfabeto $X = \{0, 1, 2, 3\}$:
* **0**: 15%
* **1**: 30%
* **2**: 20%
* **3**: 35%

---

> **Nota:** Questo codice è progettato per scopi educativi nell'ambito della Teoria dell'Informazione e della Compressione Dati.
