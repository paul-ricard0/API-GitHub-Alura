import requests
import pandas as pd
import os, dotenv
dotenv.load_dotenv()
import base64


class DadosRepositorios:

    def __init__(self, owner:str):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        self.access_token = os.getenv("TOKEN_GITHUB")
        self.headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'X-GitHub-Api-Version': '2022-11-28'
        }

    def lista_repositorios(self)-> list:
        repos_list = []
        for page_num in range(1, 50):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except Exception as e:
                print(f"Ocorreu um erro ao buscar repositórios da página {page_num}: {str(e)}")
                repos_list.append(None)
        return repos_list


    def extract_repo_info(self, repos_list:list)-> list:
        repo_data = []
        for page in repos_list:
            for repo in page:
                    repo_data.append({"repository_name": repo["name"], "language": repo["language"]})
        return repo_data


    def cria_df_linguagens(self) -> pd.DataFrame:
        repositorios = self.lista_repositorios()
        data= self.extract_repo_info(repositorios)

        df = pd.DataFrame(data)
        return df
    


class ManipulaRepositorios:

    def __init__(self, username: str):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        self.access_token=os.getenv("TOKEN_GITHUB")
        self.headers = {'Authorization':"Bearer " + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}

    def cria_repo(self, nome_repo: str, description: str = '', private: bool = False) -> int:
        data = {
            "name": nome_repo,
            "description": description,
            "private": private
        }
        response = requests.post(f"{self.api_base_url}/user/repos", json=data, headers=self.headers)

        print(f'status_code criação do repositório: {response.status_code}')
        return response.status_code

    def add_arquivo(self, nome_repo: str, arquivo_no_github: str, arquivo_local: str, description: str):

        # Codificando o arquivo
        with open(arquivo_local, "rb") as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
        url = f"{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{arquivo_no_github}"
        data = {
            "message": description,
            "content": encoded_content.decode("utf-8")
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'status_code upload do arquivo: {response.status_code}')
