# python-password-encryption
Questo progetto implementa un sistema di gestione sicura delle password in Python che utilizza la crittografia per garantire la sicurezza delle informazioni. Il programma genera una chiave di crittografia, con la quale inizializza un cifrario. Le password inserite vengono criptate e successivamente decriptate utilizzando il cifrario.

## Funzionalità

- Generazione della chiave di crittografia.
- Inizializzazione del cifrario con la chiave generata.
- Crittografia delle password.
- Decriptazione delle password.

## Utilizzo

1. Assicurati di avere Python installato sul tuo sistema.
2. Installa la libreria `cryptography`:
   ```bash
   pip install cryptography
3. Esegui il file gestore_password.py per utilizzare il programma di gestione delle password.

## Struttura del progetto

`index.py`: Contiene il codice per generare la chiave, inizializzare il cifrario e gestire la crittografia e la decriptazione delle password


## Esempio di utilizzo

# Genera una chiave
chiave = genera_chiave()
cifrario = inizializza_cifrario(chiave)

# Password dell'utente
password_utente = input("Inserisci la password")

# Cripta la password
password_cifrata = cripta_password(cifrario, password_utente)

print("Password originale:", password_utente)
print("Password criptata:", password_cifrata)

# Decripta la password
password_decriptata = decripta_password(cifrario, password_cifrata)
print("Password decriptata:", password_decriptata)
