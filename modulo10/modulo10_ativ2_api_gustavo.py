import requests


def buscar_filme(nome_filme, api_key):
    url_busca = "https://api.themoviedb.org/3/search/movie"
    url_generos = "https://api.themoviedb.org/3/genre/movie/list"

    params_busca = {"api_key": api_key, "query": nome_filme, "language": "pt-BR"}

    params_generos = {"api_key": api_key, "language": "pt-BR"}

    try:
        # Busca lista de gêneros para mapear os IDs
        res_generos = requests.get(
            url_generos, params=params_generos, timeout=10
        )
        res_generos.raise_for_status()
        mapa_generos = {
            g["id"]: g["name"] for g in res_generos.json().get("genres", [])
        }

        # Busca os filmes correspondentes ao termo digitado
        res_filme = requests.get(url_busca, params=params_busca, timeout=10)
        res_filme.raise_for_status()
        resultados = res_filme.json().get("results", [])

        if not resultados:
            print(f"Nenhum filme encontrado para '{nome_filme}'.")
            return

        primeiro_filme = resultados[0]

        titulo = primeiro_filme.get("title", "Sem título")
        sinopse = primeiro_filme.get(
            "overview", "Sinopse não disponível em português."
        )
        genre_ids = primeiro_filme.get("genre_ids", [])
        generos_nomes = [
            mapa_generos.get(gid, "Desconhecido") for gid in genre_ids
        ]

        print(f"🎬 Título: {titulo}")
        print(
            f"🏷️  Gênero(s): {', '.join(generos_nomes) if generos_nomes else 'Não informado'}"
        )
        print(
            f"📝 Sinopse: {sinopse if sinopse else 'Sem sinopse disponível.'}\n"
        )

    except requests.exceptions.RequestException as err:
        print(f"Erro ao conectar com a API do TMDB: {err}")


if __name__ == "__main__":
    # Substitua 'SUA_API_KEY_TMDB' pela sua chave do TMDB
    API_KEY_TMDB = "SUA_API_KEY_TMDB"
    filme_usuario = input("Digite o nome de um filme: ")
    buscar_filme(filme_usuario, API_KEY_TMDB)