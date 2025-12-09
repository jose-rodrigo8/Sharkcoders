from time import sleep 


def Contagem(contador):
    print(contador)
    sleep(1)

def ContadorFoguete():
    contador = int(input("Qual o numero inicial da contagem decrescente? "))

    # while True:
    #     if contador == 0:
    #         print("E morreu")
    #         break
    #     else:
    #         Contagem(contador)
    #         contador -= 1

    for i in range(contador):
         Contagem(contador)
         if contador == 0:
            print("E morreu")
            break
        

ContadorFoguete()
   



            