"""
"""
#descrever os passos manuais e tranformar em código
#ler planilha e guardar sobre o nome e nuémero  data de vencimento e guardar informação
#criiar links personalizados no whatsapp e enviar menssagem 
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
webbrowser.open('https://web.whatsapp.com/')
sleep(30)

workbook = openpyxl.load_workbook("teste.xlsx")
pagina_clientes=workbook["Planilha1"]

for linha in pagina_clientes.iter_rows(min_row=2):

    #nome, telefone e vencimento

        nome = linha[0].value
        telefone = linha[1].value
        vencimento = linha[2].value
        mensagem= f'Olá {nome} seu boleto vence no dia {vencimento}. Por favor pagar no pix 19 98151-0386 ps não é golpe'
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        try:
            seta = pyautogui.locateCenterOnScreen('enviar.png')
            sleep(5)
            pyautogui.click(seta[0],seta[1])
            sleep(5)
            pyautogui.hotkey('crtl','w')
            sleep(5)
        except:
              print(f'Não foi possivel enviar mensagem para {nome}')
              with open('erros.csv', 'a', newline= '',encoding='utf-8') as arquivo:
                    arquivo.write(f'{telefone}, {nome}')