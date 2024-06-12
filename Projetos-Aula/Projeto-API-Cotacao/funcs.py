import customtkinter as ctk
import requests
import datetime
from main import *

def pegarCotacao(moeda1, moeda2):
    pagina = f'https://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2}'
    resposta = requests.get(pagina)

    moedas_concatenado = f'{moeda1}{moeda2}'
    dados = resposta.json()
    arrumando_datetime = datetime.datetime.now()
    data_atual = {
        'ano' : arrumando_datetime.year,
        'mes' : arrumando_datetime.month,
        'dia' : arrumando_datetime.day,
        'hora' : arrumando_datetime.hour,
        'minutos' : arrumando_datetime.minute
                }
    dados_moedas = {
        'nome_conv' : dados[moedas_concatenado]['name'],
        'alta_conv' : dados[moedas_concatenado]['high'],
        'baixa_conv' : dados[moedas_concatenado]['low'],
        'valor_conv' : dados[moedas_concatenado]['bid'],
        'data_conv' : data_atual
        }
    return dados_moedas

def mostrarConversao():
    global entrada_moeda1, entrada_moeda2, nome_conv, valor_total_conv, valor_unitario_conv, alta_conv, baixa_conv,dia_conv,mes_conv,ano_conv
    saida_moeda1 = entrada_moeda1.get().upper()
    saida_moeda2 = entrada_moeda2.get().upper()
    saida_API = pegarCotacao(saida_moeda1, saida_moeda2)
    if saida_API:
        nome_conv.configure(text=f'Conversão: {saida_API['nome_conv']}')
        valor_unitario_conv.configure(text=f'Valor Unitário: {saida_API['valor_conv']}')
        valor_total_conv.configure(text=f'Valor da Conversão: {float(entrada_valor_moeda.get()) * float(saida_API["valor_conv"])}')
        alta_conv.configure(text=f'Valor da Alta: {saida_API['alta_conv']}')
        baixa_conv.configure(text=f'Valor da Baixa: {saida_API['baixa_conv']}')
        dia_conv.configure(text=f'Dia da Conversão: {saida_API['data_conv']['dia']}')
        mes_conv.configure(text=f'Mês da Conversão: {saida_API['data_conv']['mes']}')
        ano_conv.configure(text=f'Ano da Conversão: {saida_API['data_conv']['ano']}')