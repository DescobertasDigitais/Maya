#!/usr/bin/python3

import requests
import argparse, os
from colorama import Fore, Style

os.system("clear")

banner = (Style.BRIGHT + """
  __  __                   
 |  \/  | __ _ _   _  __ _ 
 | |\/| |/ _` | | | |/ _` |
 | |  | | (_| | |_| | (_| |
 |_|  |_|\__,_|\__, |\__,_|
               |___/   
                    v12.5\n""")

parser = argparse.ArgumentParser(
    usage="python3 %(prog)s --sexo M --idade 20",
    description="Gere dados de pessoas aleátorios para sua sock puppet."
)
parser.add_argument("--sexo", help="Especificar o gênero para ser gerado", choices=["M","H"], default="I")
parser.add_argument("--idade", help="Especificar a idade", type=int, default=0, required=False)

args = parser.parse_args()

def gerar_pessoa(sexo, idade):
    url = "https://www.4devs.com.br/ferramentas_online.php"
    data = {"acao":"gerar_pessoa","txt_qtde":"1","idade":idade,"sexo":sexo}

    print(banner)
    response = requests.post(url, data=data)
    dados = response.json()
    print("[-] NOME:", dados[0]["nome"])
    print("[-] IDADE:", dados[0]["idade"])
    print("[-] CPF:", dados[0]["cpf"])
    print("[-] REGISTRO GERAL:", dados[0]["rg"])
    print("[-] DATA DE NASCIMENTO:", dados[0]["data_nasc"])
    print("[-] SEXO:", dados[0]["sexo"])
    print("[-] SIGNO:", dados[0]["signo"])
    print("[-] NOME DA MÃE:", dados[0]["mae"])
    print("[-] NOME DO PAI:", dados[0]["pai"])
    print("[-] E-MAIL GERADO:", dados[0]["email"])
    print("[-] SENHA GERADA:", dados[0]["senha"])
    print("[-] CEP:", dados[0]["cep"])
    print("[-] ENDEREÇO:", dados[0]["endereco"])
    print("[-] NÚMERO DA CASA:", dados[0]["numero"])
    print("[-] NOME DO BAIRRO:", dados[0]["bairro"])
    print("[-] NOME DA CIDADE:", dados[0]["cidade"])
    print("[-] ESTADO:", dados[0]["estado"])
    print("[-] TELEFONE FIXO:", dados[0]["telefone_fixo"])
    print("[-] CELULAR:", dados[0]["celular"])
    print("[-] ALTURA E PESO:", dados[0]["altura"] + "h", "-", str(dados[0]["peso"]) + "kg")
    print("[-] TIPO SANGUINEO:", dados[0]["tipo_sanguineo"])
    print("[-] COR FAVORITA:", dados[0]["cor"])

if __name__ == "__main__":
    gerar_pessoa(args.sexo, args.idade)