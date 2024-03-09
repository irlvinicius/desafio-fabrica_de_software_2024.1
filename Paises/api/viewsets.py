from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from .serializers import PaisSerializer

from ..models import Pais

import requests


class PaisViewSet(ModelViewSet):
    serializer_class = PaisSerializer
    queryset = Pais.objects.all()

    def create(self, request):
        pais = request.data.get('name', '')
        
        url = f"https://restcountries.com/v2/name/{pais}" #Cria uma URL usando o nome do país para consultar a API de informações de países. A URL é formatada com base no nome do {pais}.

        requisicao = requests.get(url) #Faz uma requisição GET à API externa usando a url.
        json_data = requisicao.json() #Converte a resposta da requisição para um objeto JSON.


        #Nessa questão do if tive auxiilio do ChaTGPTxd. 
        #Enfrentei uma dificuldade com o request da API em questão, pois seu JSON estão dentro de uma lista, de forma que o GET não funcionava. 
        if isinstance(json_data, list) and json_data: #Verifica se os dados retornados são uma lista e se ela não está vazia.
            country_info = json_data[0] #Se a condição anterior for verdadeira, assume-se que a primeira entrada na lista contém as informações do país. Essas informações são extraídas para a variável country_info.  
            name = country_info.get('name','')
            capital = country_info.get('capital','')
            subregion = country_info.get('subregion','')
            population = country_info.get('population','')
            region = country_info.get('region','')

        dadosrecebidos = { #As informações extraídas são armazenadas nesse dicionario
            "name": f'{name}',
            "capital": f'{capital}',
            "subregion": f'{subregion}',
            "population": f'{population}',
            "region": f'{region}',
        }
        

        meuserializer = PaisSerializer(data=dadosrecebidos)

        if meuserializer.is_valid():
            name_pesquisado = Pais.objects.filter(name=name) #Consulta o banco de dados para verificar se já existe um país com o mesmo nome.
            name_pesquisado_existe = name_pesquisado.exists() #Verifica se o país já existe no banco de dados.

            if name_pesquisado_existe: #Se o país já existe, retorna uma mensagem de aviso...
                return Response({"AVISO":"Seu País já existe no bando de dados"})
            
            meuserializer.save() #...Se não, salva os dados no banco de dados e retorna os dados serializados em formato JSON.
            return Response(meuserializer.data)
            
        else:
            return Response({"AVISO: Algo deu errado"})