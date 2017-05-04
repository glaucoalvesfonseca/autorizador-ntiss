from selenium import webdriver
import win32con, win32api
import time

def autentica_usuario():
    """
    Função que coleta credenciais do usuário que será usado como teste.
    """
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite a senha: ')
    return usuario, senha

def solicita_servico():
    while True:
        #Solicita ao usuário um tipo de serviço
        try:            
            mensagem = '\nQue tipo de serviço quer solicitar? (Digite o número)\n 1 - Consulta;\n 2 - Exame;\n 3 - Internação\n\n Opção: '
            tipo_de_servico = int(input(mensagem))
            
            #Verifica se o status é uma opção válida
            if tipo_de_servico > 3 or tipo_de_servico < 1:
                print('Opção inválida. Tente de novo.\n')
                time.sleep(3)
            else:
                break
        #Em caso de erro, informa ao usuário e tenta de novo
        except ValueError as erro:
            print('Opção inválida. Tente de novo.\n')
            time.sleep(3)

    if tipo_de_servico == 1:
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoConsulta/solicitacaoConsulta.jsf'
        servico = 'Consulta'
    elif tipo_de_servico == 2:
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoSadt/solicitacaoSadtFat.jsf'
        servico = 'SADT'
    elif tipo_de_servico == 3:
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoInternacao/solicitacaoInternacao.jsf'
        servico = 'Internacao'
    return url, servico

def status_servico():
    while True:
        #Solicita ao usuário um status de serviço
        try:            
            mensagem = '\nQue status quer que retorne? (Digite o número)\n 1 - Autorizado;\n 2 - Pendente;\n 3 - Negado\n\n Opção: '
            status = int(input(mensagem))           

            #Verifica se o status é uma opção válida
            if status > 3 or status < 1:
                print('Opção inválida. Tente de novo.\n')
                time.sleep(3)
            else:
                break
        #Em caso de erro, informa ao usuário e tenta de novo
        except ValueError as erro:
            print('Opção inválida. Tente de novo.\n')
            time.sleep(3)
        
    if status == 1:
        return 'Autorizado'
    elif status == 2:
        return 'Pendente'
    elif status == 3:
        return 'Negado'

credenciais = autentica_usuario()
url_servico = solicita_servico()
status_do_servico = status_servico()

#Iniciando browser e abrindo página do ntiss
driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
driver.maximize_window()
driver.get('http://ntiss.neki-it.com.br/ntiss/login.jsf')

#Autenticando
driver.find_element_by_id('login').send_keys(credenciais[0])
driver.find_element_by_id('senha').send_keys(credenciais[1])
driver.find_element_by_id('botaoEntrar').click()

#Acessando página da solicitação de acordo com função solicita_servico
driver.get(url_servico[0])