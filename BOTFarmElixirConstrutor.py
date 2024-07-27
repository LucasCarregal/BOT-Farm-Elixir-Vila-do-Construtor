import time
import botFunction

## DEFINICOES 
collectionsQuantity = int(input('Numero de coletas de elixir: '))
attacksAmountBeforeCollect = int(input('Quantidade de ataques antes de coletar o elixir: '))
durantion = 0.3
loadingDelay = 3

## CONFIG ATACK - configurado para tela cheia
buttonAtackPosition = {'x': 200, 'y': 950}
selectTroop = {'x': 400, 'y': 950}
troopPosition = {'x': 200, 'y': 500}
giveUpButton = {'x': 200, 'y': 760}
giveUpConfirmButton = {'x': 1200, 'y': 650}
goBackButton = {'x': 1000, 'y': 870}

## CONFIG COLLECT ELIXIR - configurado para tela cheia
elixirPot = {'x': 1300, 'y': 50} # ajustar de acordo com layout da vila
collectButton = {'x': 1300, 'y': 850}
closeButton = {'x': 1550, 'y': 150}


for j in range(collectionsQuantity):
    for i in range(attacksAmountBeforeCollect):
        botFunction.newAtack(durantion, buttonAtackPosition, selectTroop, troopPosition, giveUpButton, giveUpConfirmButton, goBackButton, loadingDelay)

    time.sleep(2)
    botFunction.collectElixir(durantion, elixirPot, collectButton, closeButton)

