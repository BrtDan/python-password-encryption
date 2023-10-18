from cryptography.fernet import Fernet

def genera_chiave():
    return Fernet.generate_key()

def inizializza_cifrario(chiave):
    return Fernet(chiave)

def cripta_password(cifrario, password):
    return cifrario.encrypt(password.encode())

def decripta_password(cifrario, password_cifrata):
    return cifrario.decrypt(password_cifrata).decode()

def main():
    chiave = genera_chiave()
    cifrario = inizializza_cifrario(chiave)

    password_utente = input("Inserisci la password\n")

    password_cifrata = cripta_password(cifrario, password_utente)

    print("Password originale:", password_utente)
    print("Password criptata:", password_cifrata)

    password_decriptata = decripta_password(cifrario, password_cifrata)
    print("Password decriptata:", password_decriptata)

if __name__ == "__main__":
    main()
