from random import randint 
import os 

def Limpar():
    os.system("cls")

def Cabeçalho(texto):
    Limpar()
    tamanho = len(texto) + 6 
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)
    print()

def SubCabeçalhos(texto):
    print()
    print(f"### {texto} ###")
    print()

def MenuDoPC():
    Cabeçalho("Escolhe o jogo")
    SubCabeçalhos("Menu")
    escolha = int(input(" 1 - Pênaltis \n 2 - Livres  \n 0 - Sair\n"))

    return escolha

def QualJogo():
    Cabeçalhos("Telemóvel")
    input("\n Enter para iniciar")
    while True:
        Cabeçalhos("Escolhe o jogo ")
        escolha = MenuDoPC()
        Limpar()
        if escolha == 0:
            SubCabeçalhos("Sayonara".upper())
            break
        elif escolha == 1:
            JogoPênaltis()
        elif escolha == 2:
            JogoLivres()
        else:
            SubCabeçalhos("Escolha nao valida!")

def Limpar():
    os.system("cls")

def Cabeçalhos(texto):
    Limpar()
    tamanho = len(texto) + 6 
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)
    print()

def Subcabeçalho(texto):
    print()
    print(f"### {texto} ###")
    print()

def MenuDoLivre():
    Cabeçalhos("Pênaltis")
    Subcabeçalho("Menu")
    escolha = int(input(" 1 - Jogar contra PC \n 2 - Jogar contra jogador \n 0 - Sair\n"))

    return escolha

def Jogar():
    print("Onde queres chutar no pênalti")
    print("\n 1 - Meio \n 2 - Canto inferior direito \n 3- Canto superior direito \n 4- Canto inferior esquerdo \n 5- Canto superior esquerdo \n 0 - Sair\n")

def Defender():
    print("Onde queres defender no pênalti")
    print("\n1 - Meio \n2 - Canto inferior direito \n3- Canto superior direito \n4- Canto inferior esquerdo \n5- Canto superior esquerdo \n0 - Sair\n")
    
def JogoPC():
    Limpar()
    Subcabeçalho("Vez do Jogador 1")
    Jogar()
    jagadaUm = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jagadaUm == 0:
        return
    Limpar()
    Subcabeçalho("Vez do Jogador 2")
    print("O Computador escolheu onde defender")
    jagadaDois = randint(1,5)
    input("\n Enter para Continuar")
    LogicaJogo(jagadaUm , jagadaDois)

def JogoPlayer():
    Limpar()
    Subcabeçalho("Vez do Jogador 1")
    Jogar()
    jagadaUm = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jagadaUm == 0:
        return
    Limpar()
    Subcabeçalho("Vez do Jogador 2")
    Defender()
    jagadaDois = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jagadaDois == 0:
        return
    LogicaJogo(jagadaUm , jagadaDois)

def LogicaJogo(jagadaUm , jagadaDois):
    jogadas = ["Meio" , "Canto inferior direito" , "Canto superior direito" , "Canto inferior esquerdo" , "Canto superior esquerdo"]
    
    if jagadaUm == 1:
        if jagadaDois == 1:
            Limpar()
            Subcabeçalho("DEFENDEU!")
        if jagadaDois == 2:
            Limpar
            Subcabeçalho("GOOOOOOLO COM CONFIANÇA!")
        if jagadaDois == 3:
            Limpar() 
            Subcabeçalho("GOOOOOOLO MAS QUE GOLAÇO!")
        if jagadaDois == 4:
            Limpar()
            Subcabeçalho("GOOOOOOLO!")
        if jagadaDois == 5:
            Limpar()
            Subcabeçalho("GOOOOOOOLO MAS QUE GOLAÇO SIUUUUUUU!")       
    if jagadaUm == 2:
        if jagadaDois == 2:
            Limpar()
            Subcabeçalho("DEFENDEEEEU!")
        if jagadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jagadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jagadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM QUE GOL")
        if jagadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
    if jagadaUm == 3:
        if jagadaDois == 2:
            Limpar()
            Subcabeçalho("GOOOOOLO!")
        if jagadaDois == 3:
            Limpar()
            Subcabeçalho("DEFENNDEU!")
        if jagadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jagadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM QUE GOL")
        if jagadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
    if jagadaUm == 4:
        if jagadaDois == 2:
            Limpar()
            Subcabeçalho("MAS QUE GANDA GOOOOLO!")
        if jagadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jagadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jagadaDois == 4:
            Limpar()
            Subcabeçalho("TAFAREEEEEEEEELLL")
        if jagadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
    if jagadaUm == 5:
        if jagadaDois == 2:
            Limpar()
            Subcabeçalho("MAS QUE EESTOOURO CHUPA BOI!")
        if jagadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jagadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jagadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM QUE GOL")
        if jagadaDois == 5:
            Limpar()
            Subcabeçalho("PICKFOOOOOOOOOOOOOOOOOOOOOOOOORD MAS QUE DEFESA")
    print(f"\n O jogador 1 jogou {jogadas[jagadaUm - 1]} e o jogador 2 jogou {jogadas[jagadaDois - 1]}")
    input("\n Enter para Continuar")

def JogoPênaltis():
    Cabeçalhos("Pênaltis")
    input("\n Enter para iniciar")
    while True:
        Cabeçalhos("Pênaltis")
        escolha = MenuDoLivre()
        Limpar()
        if escolha == 0:
            Subcabeçalho("Sayonara".upper())
            break
        elif escolha == 1:
            JogoPC()
        elif escolha == 2:
            JogoPlayer()
        else:
            Subcabeçalho("Escolha nao valida!")

def Limpar():
    os.system("cls")

def Cabeçalhoses(texto):
    Limpar()
    tamanho = len(texto) + 6 
    print()
    print("="*tamanho)
    print(f"|| {texto} ||")
    print("="*tamanho)
    print()

def Subcabeçalhos(texto):
    print()
    print(f"### {texto} ###")
    print()

def Menu():
    Cabeçalhoses("Livres")
    SubCabeçalhos("Menu")
    escolha = int(input(" 1 - Jogar contra PC \n 2 - Jogar contra jogador \n 0 - Sair\n"))

    return escolha

def Distância():
    print("A que distância queres chutar")
    print("\n 1 - 10 metros \n 2 - 15 metros \n 3 - 20 metros \n 4 - 25 metros \n 5 - 30 metros \n 6 - 40 metros \n 7 - 50 metros \n 8 - 100 metros ")
 
def JogarLivre():
    print("Onde queres chutar no Livre")
    print("\n 1 - Meio \n 2 - Canto inferior direito \n 3- Canto superior direito \n 4- Canto inferior esquerdo \n 5- Canto superior esquerdo \n 0 - Sair\n")

def DefenderLivre():
    print("Onde queres defender no Livre")
    print("\n1 - Meio \n2 - Canto inferior direito \n3- Canto superior direito \n4- Canto inferior esquerdo \n5- Canto superior esquerdo \n0 - Sair\n")
    
def DistânciaLivre():
    Limpar()
    Subcabeçalho("Distância")
    Jogar()
    jogadaUm = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jogadaUm == 0:
        return   

def JogoPC_Livre():
    Limpar()
    Subcabeçalho("Vez do Jogador 1")
    Jogar()
    jogadaUm = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jogadaUm == 0:
        return
    Limpar()
    Subcabeçalho("Vez do Jogador 2")
    print("O Computador escolheu onde defender")
    jogadaDois = randint(1,5)
    input("\n Enter para Continuar")
    LogicaJogoLivre(jogadaUm , jogadaDois)

def JogoPlayerLivre():
    Limpar()
    Subcabeçalho("Vez do Jogador 1")
    Jogar()
    jogadaUm = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jogadaUm == 0:
        return
    Limpar()
    Subcabeçalho("Vez do Jogador 2")
    Defender()
    jogadaDois = int(input("Escolha: "))
    input("\nEnter para continuar")
    if jogadaDois == 0:
        return
    LogicaJogoLivre(jogadaUm , jogadaDois)

def Chances():
    chance = randint(0,20)
    if chance <= 10:
        LogicaJogoLivre()
    elif chance > 10:
        print("Errou")
    else:
        print("escolha não válida")

def LogicaJogoLivre(jogadaUm , jogadaDois):
    jagadas = ["Meio" , "Canto inferior direito" , "Canto superior direito" , "Canto inferior esquerdo" , "Canto superior esquerdo"]
    distância = ["10 metros" , "15 metros" , "20 metros" , "25 metros" , "30 metros" , "40 metros" , "50 metros" , "100 metros"]
    if jogadaUm == 1:
        if jogadaDois == 1:
            Limpar()
            Subcabeçalho("DEFENDEU!")
        if jogadaDois == 2:
            Limpar
            Subcabeçalho("GOOOOOOLO COM CONFIANÇA!")
        if jogadaDois == 3:
            Limpar() 
            Subcabeçalho("GOOOOOOLO MAS QUE GOLAÇO!")
        if jogadaDois == 4:
            Limpar()
            Subcabeçalho("GOOOOOOLO!")
        if jogadaDois == 5:
            Limpar()
            Subcabeçalho("GOOOOOOOLO MAS QUE GOLAÇO SIUUUUUUU!")       
    if jogadaUm == 2:
        if jogadaDois == 2:
            Limpar()
            Subcabeçalho("DEFENDEEEEU!")
        if jogadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jogadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jogadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM QUE GOL")
        if jogadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
    if jogadaUm == 3:
        if jogadaDois == 2:
            Limpar()
            Subcabeçalho("GOOOOOLO!")
        if jogadaDois == 3:
            Limpar()
            Subcabeçalho("DEFENNDEU!")
        if jogadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jogadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM QUE GOL")
    if jogadaUm == 4:
        if jogadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
        if jogadaDois == 2:
            Limpar()
            Subcabeçalho("MAS QUE GANDA GOOOOLO!")
        if jogadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jogadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jogadaDois == 4:
            Limpar()
            Subcabeçalho("TAFAREEEEEEEEELLL")
        if jogadaDois == 5:
            Limpar()
            Subcabeçalho("GOLAAAAAAAAAAAAAAAAAAÇO")
    if jogadaUm == 5:
        if jogadaDois == 2:
            Limpar()
            Subcabeçalho("MAS QUE EESTOOURO CHUPA BOI!")
        if jogadaDois == 3:
            Limpar()
            Subcabeçalho("GOOOOOOOOLO MAS GOOOOOLO!")
        if jogadaDois == 1:
            Limpar() 
            Subcabeçalho("E O JOGADO COM A CONFIANÇA BATEU NO CANTO QUE GOLO!")
        if jogadaDois == 4:
            Limpar()
            Subcabeçalho("E O JOGADO É BOM , QUE GOL")
        if jogadaDois == 5:
            Limpar()
            Subcabeçalho("PICKFOOOOOOOOOOOOOOOOOOOOOOOOORD MAS QUE DEFESA")
    print(f"\n O jogador 1 chutou de {distância[randint(0,7)]} e fez {jagadas[jogadaUm - 1]} e o jogador 2 jogou {jagadas[jogadaDois - 1]}")
    input("\n Enter para Continuar")

def JogoLivres():
    Cabeçalhoses("Livres")
    input("\n Enter para iniciar")
    while True:
        Cabeçalhoses("Livres")
        escolha = Menu()
        Limpar()
        if escolha == 0:
            Subcabeçalhos("Sayonara".upper())
            break
        elif escolha == 1:
            JogoPC_Livre()
        elif escolha == 2:
            JogoPlayerLivre()
        else:
            Subcabeçalhos("Escolha nao valida!") 
        
QualJogo()