import requests


def buscar_clima(cidade, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt_br",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        # Levanta uma exceção para códigos de status HTTP 4xx ou 5xx
        response.raise_for_status()

        dados = response.json()

        # Filtrando informações relevantes
        temperatura = dados["main"]["temp"]
        condicao = dados["weather"][0]["description"].capitalize()
        umidade = dados["main"]["humidity"]

        print(f"--- Clima em {cidade.title()} ---")
        print(f"🌡️  Temperatura: {temperatura}°C")
        print(f"🌤️  Condição: {condicao}")
        print(f"💧 Umidade: {umidade}%\n")

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao buscar dados da cidade '{cidade}': {http_err}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão! Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("A requisição demorou muito e expirou.")
    except requests.exceptions.RequestException as err:
        print(f"Erro inesperado na requisição: {err}")


if __name__ == "__main__":
    # Substitua 'SUA_API_KEY' pela sua chave da OpenWeatherMap
    API_KEY = "SUA_API_KEY"
    cidade_usuario = input("Digite o nome de uma cidade: ")
    buscar_clima(cidade_usuario, API_KEY)