from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import win32con, win32api
import time
import random

def autentica_usuario():
    """
    Função que coleta credenciais do usuário que será usado como teste.
    """
    credenciais = dict()
    with open('credenciais.conf') as arquivo:
        for linha in arquivo:            
            (key, value) = linha.replace('\n','').split(':')
            credenciais[key] = value
    return credenciais
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

def tipo_servico():
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
    return tipo_de_servico

def solicita_servico():    
    #Realizando solicitação de consulta
    if tipo_de_servico == 1:
        #URL na página da Neki
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoConsulta/solicitacaoConsulta.jsf'        
        driver.get(url)

        #Cada campo da guia de solicitação será armazenada em um dicionário
        dados_da_guia = dict()
        #Informando dados do serviço de acordo com o arquivo
        with open('dados_Consulta_{}.conf'.format(status_do_servico)) as arquivo:
            for linha in arquivo:
                (key, value) = linha.replace('\n','').split(':')
                dados_da_guia[key] = value

        #Número de guia aleatório
        driver.find_element_by_id('solicitacaoConsultaForm:numeroGuiaOperadora').send_keys(random.randint(0, 1000))
        #Adicionando campos
        for campo in dados_da_guia:
            if campo == 'carteira':
                driver.find_element_by_id('solicitacaoConsultaForm:carteira').send_keys(dados_da_guia['carteira'])
                driver.find_element_by_id('solicitacaoConsultaForm:carteira').send_keys(Keys.TAB)
                time.sleep(2)
            else:
                driver.find_element_by_id('solicitacaoConsultaForm:{}'.format(campo)).send_keys(dados_da_guia[campo])
        #Selecionando opção Não Acidentes em Indica Acidente (menu Dropdown)
        driver.find_element_by_id('solicitacaoConsultaForm:indicacaoAcidente_label').click()
        driver.find_element_by_xpath('//*[@id="solicitacaoConsultaForm:indicacaoAcidente_1"]').click()
        #Selecionando Tipo de Consulta
        driver.find_element_by_id('solicitacaoConsultaForm:tipoConsulta_label').click()
        driver.find_element_by_xpath('//*[@id="solicitacaoConsultaForm:tipoConsulta_1"]').click()
        #Inserindo valor do serviço
        driver.find_element_by_id('solicitacaoConsultaForm:valorProcedimento_input').clear()
        driver.find_element_by_id('solicitacaoConsultaForm:valorProcedimento_input').send_keys(1000)
        #Enviando pedido
        driver.find_element_by_xpath('//*[@id="solicitacaoConsultaForm:j_idt212"]/span').click()

    elif tipo_de_servico == 2:
        #URL na página da Neki
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoSadt/solicitacaoSadtFat.jsf'
        driver.get(url)

        #Cada campo da guia de solicitação será armazenada em um dicionário
        dados_da_guia = dict()
        #Informando dados do serviço de acordo com o arquivo
        with open('dados_SADT_{}.conf'.format(status_do_servico)) as arquivo:
            for linha in arquivo:
                (key, value) = linha.replace('\n','').split(':')
                dados_da_guia[key] = value
        
        #Número de guia aleatório
        driver.find_element_by_id('solicitacaoSadtForm:j_idt122').send_keys(random.randint(0, 1000))
        time.sleep(2)
        #Adicionando campos
        for campo in dados_da_guia:
            if campo == 'carteira':
                driver.find_element_by_id('solicitacaoSadtForm:carteira').send_keys(dados_da_guia['carteira'])
                driver.find_element_by_id('solicitacaoSadtForm:carteira').send_keys(Keys.TAB)
                time.sleep(5)
            else:
                driver.find_element_by_id('solicitacaoSadtForm:{}'.format(campo)).send_keys(dados_da_guia[campo])

    elif tipo_de_servico == 3:
        #URL na página da Neki
        url = 'http://ntiss.neki-it.com.br/ntiss//tiss/solicitacaoprocedimento/solicitacaoInternacao/solicitacaoInternacao.jsf'
        servico = 'Internacao'

credenciais = autentica_usuario()
#Status que quer retornar
status_do_servico = status_servico()
#Tipo de serviço que quer solicitar
tipo_de_servico = tipo_servico()

#Iniciando browser e abrindo página do ntiss
driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
driver.maximize_window()
driver.get('http://ntiss.neki-it.com.br/ntiss/login.jsf')

#Autenticando
driver.find_element_by_id('login').send_keys(credenciais['usuario'])
driver.find_element_by_id('senha').send_keys(credenciais['senha'])
driver.find_element_by_id('botaoEntrar').click()

#Realiza o pedido
solicita_servico()
