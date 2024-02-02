"""
Preciso automatizar minhas mensanges p/ meus clientes gostaria de saber valores, e gostaria que entrassem em contato comigo p/ explicar
melhor, quero poder mandar mensanges de cobrança em determinado dia com clientes com vencimento diferente 

Como automatizar este processo?
Descrever os passos manuais e dps transformar isso em código

- Onde está sendo feito? (versão web)
- quais tec preciso pra resolver esta demanda?

    - Teclado                       (Pyautogui)
    - Acesso ao site                (webbrownser)
    - Automatizar digitação         (link whatsapp)
    - Automatizar leitura de dados  (openpyxl) (pillow)
"""

import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(6)

# Ler planilha e guardar informações sobre nome, telefone e data de vencimento
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Planilha1']

for linha in pagina_clientes.iter_rows(min_row=2):
    # nome, telefone, vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Olá {nome} sua fatura vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://acesse.dev/vqWf9'

# Criar links personalizados do whatsapp e enviar mensagens para cada cliente
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
    
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome}{telefone}')