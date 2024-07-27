import time
import pyautogui

def newAtack(duration,
            buttonAtackPosition,
            selectTroop, 
            troopPosition,
            giveUpButton, 
            giveUpConfirmButton, 
            goBackButton,
            loadingDelay):
        
    # Clica em atacar
    pyautogui.moveTo(10, 10, duration=0.5)
    pyautogui.moveTo(buttonAtackPosition['x'], buttonAtackPosition['y'], duration=duration)
    pyautogui.click(duration=duration)

    # clica em inicar ataque
    pyautogui.moveTo(1500, 650, duration=duration)
    pyautogui.click(duration=duration)

    time.sleep(loadingDelay)   # tela de loading

    # Clica na tropa
    pyautogui.moveTo(selectTroop['x'], selectTroop['y'], duration=duration)
    pyautogui.click(duration=duration)

    # Posiciona tropa
    pyautogui.moveTo(troopPosition['x'], troopPosition['y'], duration=duration)
    pyautogui.click(duration=duration)

    # Clica em desistir 
    pyautogui.moveTo(giveUpButton['x'], giveUpButton['y'], duration=duration)
    pyautogui.click(duration=duration)

    # Confirma desistencia
    pyautogui.moveTo(giveUpConfirmButton['x'], giveUpConfirmButton['y'], duration=duration)
    pyautogui.click(duration=duration)

    # Clica em voltar 
    pyautogui.moveTo(goBackButton['x'], goBackButton['y'], duration=duration)
    pyautogui.click(duration=duration)
    
    return


def collectElixir(duration, elixirPot, collectButton, closeButton):
    pyautogui.moveTo(elixirPot['x'], elixirPot['y'], duration=duration)
    pyautogui.click()

    pyautogui.moveTo(collectButton['x'], collectButton['y'], duration=duration)
    pyautogui.click()

    pyautogui.moveTo(closeButton['x'], closeButton['y'], duration=duration)
    pyautogui.click()

    return
