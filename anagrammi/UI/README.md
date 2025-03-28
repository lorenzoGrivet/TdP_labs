# Esercizio Anagrammi

In questo esercizio si vuole implementare un algoritmo ricorsivo per 
trovare tutti gli anagrammi di una parola fornita dall'utente tramite 
interfaccia grafica (già fornita nel codice).
Per esempio, la parola _eat_ ha sei permutazioni compresa la parola stessa:
- eat
- eta
- aet
- ate
- tea
- tae

L'algoritmo ricorsivo deve quindi essere collegato con l'interfaccia grafica,
usando il pattern MVC. Inoltre, viene fornito un database __mark.sql__ che contiene
un vocabolario di parole inglesi valide. Questo database va sfruttato per verificare
quali anagrammi trovati sono parole esistenti, e quali siano parole inventate,
stampandole nei corrispondenti campi della GUI.



## Ragionare sulla ricorsione
Bisogna pensare a come strutturare l'algoritmo ricorsivo. Può aiutare porsi delle domande:
-Cosa rappresenta il "livello" nel mio algoritmo ricorsivo?
- Com'è fatta una soluzione parziale?
- Come faccio a riconoscere se una soluzione parziale è anche completa?
- Data una soluzione parziale, come faccio a sapere se è valida o se non è valida?
(nb. magari non posso)
- Data una soluzione completa, come faccio a sapere se è valida o se non è valida?
- Qual è la regola per generare tutte le soluzioni del livello+1 a partire da una soluzione parziale del
livello corrente?
- Qual è la struttura dati per memorizzare una soluzione (parziale o completa)?
- Qual è la struttura dati per memorizzare lo stato della ricerca (della ricorsione)?

Avendo ragionato sul problema, bisogna pensare a:
- condizione di terminazione della ricorsione
- come generare una soluzione
- servono filtri sulla chiamata ricorsiva?
- serve fare backtracking?
- ci sono delle sitruzioni da eseguire sempre?

 
