import requests

with open("wordlist.txt", "r") as arquivo:
    subdominios = arquivo.read().splitlines()

alvo = "https://company.cyberpol.site"  

for subdominio in subdominios:
    url = alvo + "/" + subdominio
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            result = f"{url} -> Existe"
            print(result)
            with open('results.txt', 'a') as result_file:
                result_file.write(f"{result}\n")
        else:
            print(f"{url} -> Status Code: {resposta.status_code}")
    except requests.RequestException as e:
        print(f"{url} -> Erro: {str(e)}")
