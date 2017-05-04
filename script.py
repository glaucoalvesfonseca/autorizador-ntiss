from selenium import webdriver
import win32con, win32api
import time

def autentica_usuario():
    """
    Função que coleta credenciais do usuário que será usado como teste.
    """
    try:
        usuario = input('Digite o nome de usuario: ')
        senha = input('Digite o nome de usuario: ')
        print(usuario, senha)
    except ValueError as erro:
        print('Credenciais inválidas, tente de novo.\n')
        print('Erro: ', erro)
    return usuario, senha

credenciais = autentica_usuario()

'''        
driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
driver.maximize_window()
driver.get('http://ntiss.neki-it.com.br/ntiss/login.jsf')
'''

