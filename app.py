import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.6
pyautogui.press('win')
pyautogui.write('opera gx')
pyautogui.press('enter')
time.sleep(4)

pyautogui.write('https://aula01.simplificapython.com.br/index.html')
pyautogui.press('enter')
time.sleep(4)

pyautogui.click(x=856, y=642)
pyautogui.write('admin')
pyautogui.press('tab')
pyautogui.write('simplificapython')
pyautogui.press('enter')
pyautogui.click(x=239, y=128)
time.sleep(4)

tabela = pandas.read_csv('alunos.csv')

for linha in tabela.index:
    pyautogui.click(x=871, y=368)
    nome = tabela.loc[linha, 'Nome']
    pyautogui.write(nome)
    pyautogui.press('tab')
    email = tabela.loc[linha, 'Email']
    pyautogui.write(email)
    pyautogui.press('tab')
    endereco = tabela.loc[linha, 'Endereco']
    pyautogui.write(endereco)
    pyautogui.press('tab')
    telefone = tabela.loc[linha, 'Telefone']
    pyautogui.write(telefone)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.scroll(5000)