from kivy.app import App
from kivy.lang import Builder
import requests

interface = Builder.load_file('tela.kv')

class MeuApp(App):
    def build(self):
        return interface
    def on_start(self):
        self.root.ids['moeda1'].text = f'Dólar: R${round(float(self.pegar_cotacao("USD")), 2)}'
        self.root.ids['moeda2'].text = f'Euro: R${round(float(self.pegar_cotacao("EUR")), 2)}'
        self.root.ids['moeda3'].text = f'Ethereum: R${round(float(self.pegar_cotacao("ETH")), 2)}'
        self.root.ids['moeda4'].text = f'Bitcoin: R${round(float(self.pegar_cotacao("BTC")), 2)}'
    def pegar_cotacao(self, moeda):
        site = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
        requisicao = requests.get(site)
        dict_requisicao = requisicao.json()
        cotacao = dict_requisicao[f'{moeda}BRL']['bid']
        return cotacao
MeuApp().run()
