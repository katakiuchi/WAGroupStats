def main():

    file = open('chat.txt', 'r', encoding="utf-8").read()
    #Lista di tutti i partecipanti alla chat, si potrebbe creare dinamicamente ma ho il culo pesante
    membri=["Magneto:", "Professor X:", "Stacy X:", "Wolverine:", "Ciclope:"]
    for persona in membri:
        print(persona+" "+str(file.count(persona)))



main()