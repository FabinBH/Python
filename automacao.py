import pyautogui
import time
import pygetwindow as gw

def f_mandarMensagem(mensagem, contato, janela):

    #Muda para a janela especificada
    gw.getWindowsWithTitle(janela)[0].activate()
    time.sleep(1)

    #Pesquisa o contato
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)
    pyautogui.write(contato)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    #Envia a mensagem
    pyautogui.write(mensagem)
    pyautogui.press("enter")
#------------------------------------------------
def main():
    msg = input("Digite a mensagem: ")
    cntt = input("Nome do contato: ")
    wndw = input("Nome da janela: ")
    f_mandarMensagem(msg, cntt, wndw)


if  __name__=="__main__":
    main()