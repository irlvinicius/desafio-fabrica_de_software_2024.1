
# Desafio referente a Fábrica de Software (Back-End) - UNIPÊ 2024.1 
### OBJETIVO DO DESAFIO :anger: (OPÇÃO 1):
Consumir una **API** de sua livre escolha (Tema Livre) e retornar em sua API.
#### REQUISITOS FUNCIONAIS
  
  - [x] Consumir una API diferente da apresentada (ViaCEP), Realizar as quatro operaçóes, POST, GET (ou PATCH), DELETE através do INSOMNIA.
  - [x] Deve sem bem documentado, contendo Requirenents.txt e README.md.
  - [x] Sobrescrever o método create para salvar no banco dados da API. (Receber os dados de um API EXTERNA, na SUA API e salvar no SEU Banco de Dados e Exibir automaticamente).
            
#### REQUISITOS NÃO FUNCIONAIS

  - [x] Indentação do Código.
  - [x] Estruturação do Código (Pastas, Classes e Arquivos con nomes concisos e referentes).

#### PONTUAÇÃO EXTRA
- [] Relação entre dois bancos — Foreingkey, One-To-One...
- [] Usar banco de dados externo (MySQL, PostGreSQL)
- [] Acessar um Dicionário Dentro do JSON
- [] Autenticação com Token do Django Res
- [x] Commits Semânticos

## Requerimentos
1. asgiref
2. certifi
3. charset-normalizer
4. Django
5. djangorestframework
6. requests
7. mais sobre no próprios arquivo requirements.txt...

# Para rodar :dizzy:
É necessário fazer algumas ações. Certifique-se de ter o Python e instalados. Em seguida, crie um novo ambiente virtual ```py -m venv {nome_da_venv}```, e __entre nela__ ```.\{nome_da_venv}\Scripts\activate```.
<br><br>
Em seguinda instale as __dependências:__
```
pip install django
pip install django djangorestframework
pip install requests
```





# Escolha da API
A princípio, minha prioridade era escolher uma API simples, que me retornasse dados de maneira limpa e que de certa forma fossem fáceis de manipular. A API em questão foi a [REST COUNTRIES](https://restcountries.com/), que me retorna qualquer informação acerca de um país do mundo.

# Acesso a API

Antes de qualquer coisa é necessario dar os seguintes comandos no terminal(dentro da venv): ```py manage.py makemigrations```, depois o ```py manage.py migrate```. Agora ao dar o ```py manage.py runserver```, é predefinido um IP local: “http://127.0.0.1:8000/”. Com base nisso, deve-se adicionar os endereçamento correto levando para o CRUD ligado a API em questão. Link esse definido no .Paises/api/urls.py, sendo ele: “http://127.0.0.1:8000/api/paises/”. O usuário deve usar esse link para qualquer tarefa. 

# Métodos POST, GET (ou PATCH), DELETE através do INSOMNIA
Uma vez configurada no .Paises/api/viewsets.py, a função “create()” tem esse papel sob a API em si. 
<br>
__OBS:__ Utilizando integralmente ```import requests```.

É definido um valor padrão a variável país, levando em consideração ao input do usuário, no momento do POST.
```
pais = request.data.get('name', '')
```


Defini uma variável "url" usando o nome do {país} como endpoint em cima da API de informações de países. Em sequência, a variável “requisicao”, faz a requisição GET com base na URL, sendo a API. Juntamente ao “json-data” que apenas converte essa resposta a um objeto JSON. 
```
url = f"https://restcountries.com/v2/name/{pais}"
requisicao = requests.get(url)
json_data = requisicao.json()
```

__OBS:__ Ao executar o código não consegui ter um retorno direto da API, foi quando notei que toda estrutura JSON estava dentro de uma lista. Contornei essa situação com o auxílio do Chat GPT :zipper_mouth_face:, que me deu a seguinte solução:
```
if isinstance(json_data, list) and json_data: #Verifica se os dados retornados são uma lista e se ela não está vazia.
            country_info = json_data[0] #Se a condição anterior for verdadeira, assume-se que a primeira entrada na lista contém as informações do país. Essas informações são extraídas para a variável country_info.  
            name = country_info.get('name','')
            capital = country_info.get('capital','')
            subregion = country_info.get('subregion','')
            population = country_info.get('population','')
            region = country_info.get('region','')
```

Por sequência, inicia-se um dicionário onde vai armazenar todas as informações necessárias para o armazenamento no Banco de Dados.
```
        dadosrecebidos = {             
            "name": f'{name}',
            "capital": f'{capital}',
            "subregion": f'{subregion}',
            "population": f'{population}',
            "region": f'{region}',
        }
```

Por fim um algoritmo que exerce a função na administração dos requests, levando em consideração o estado atual do banco de dados, se tem devido elemento, ou se está repetido.
```
meuserializer = PaisSerializer(data=dadosrecebidos)

        if meuserializer.is_valid():
            name_pesquisado = Pais.objects.filter(name=name)
            name_pesquisado_existe = name_pesquisado.exists()

            if name_pesquisado_existe:
                return Response({"AVISO":"Seu País já existe no bando de dados"})
            
            meuserializer.save()
            return Response(meuserializer.data)
            
        else:
            return Response({"AVISO: Algo deu errado"})
```


 #### Agradecimentos especiais(euacho):
- João Pedro: Deixa de dormir para ajudar o próximo :zzz:
- Natan: Enxergou que ninguém nunca ia enxergar :eye_speech_bubble:
- Lucas: Uma didatica foda, sabe oque ta fazendo :nerd_face:
- Raphinha: cep :wrestling:














