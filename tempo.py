import requests

def obter_previsao_tempo(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()

    if dados["cod"] != "404":
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]
        pais = dados["sys"]["country"]

        print(f"Condições climáticas em {cidade}, {pais}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descrição: {descricao}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do vento: {vento} km/h")
    else:
        print("Cidade não encontrada.")

# Chave da API do OpenWeatherMap
chave_api = "API_KEY_OPENWEATHERAPI"

# Cidade desejada
cidade = "CIDADE_AQUI"

obter_previsao_tempo(cidade, chave_api)
input("Pressione <enter> para continuar")