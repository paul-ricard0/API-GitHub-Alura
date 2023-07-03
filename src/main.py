from api_github import DadosRepositorios
from api_github import ManipulaRepositorios


def main1():
    amazon_repo = DadosRepositorios('amzn')
    amazon_df = amazon_repo.cria_df_linguagens()

    netflix_repo = DadosRepositorios('netflix')
    netflix_df = netflix_repo.cria_df_linguagens()

    spotify_repo = DadosRepositorios('spotify')
    spotify_df = spotify_repo.cria_df_linguagens()

    path = r'C:\Users\paulo\Documents\Cursos\Alura\Engenharia-de-Dados\projeto-requests\data'
    amazon_df.to_csv(f'{path}\linguagens_amazon.csv', index=False)
    netflix_df.to_csv(f'{path}\linguagens_netflix.csv', index=False)
    spotify_df.to_csv(f'{path}\linguagens_spotify.csv', index=False)


def main2():
    # instanciando um objeto
    new_repo = ManipulaRepositorios('paul-ricard0')

    # Criando o repositório
    name_repo = 'linguagens-repositorios-empresas'
    new_repo.cria_repo(name_repo, description='Teste socorrroooo!!', private=False)

    # Adicionando arquivos salvos no repositório criado
    path = r'C:\Users\paulo\Documents\Cursos\Alura\Engenharia-de-Dados\projeto-requests\data'
    new_repo.add_arquivo(name_repo, 'linguagens_amzn.csv', arquivo_local=f'{path}\linguagens_amazon.csv',  description='TESTE03')
    new_repo.add_arquivo(name_repo, 'linguagens_netflix.csv', arquivo_local=f'{path}\linguagens_netflix.csv',  description='TESTE02')
    new_repo.add_arquivo(name_repo, 'linguagens_spotify.csv', arquivo_local=f'{path}\linguagens_spotify.csv', description='TESTE01')

if __name__ == "__main__":
    main1()
    main2()
