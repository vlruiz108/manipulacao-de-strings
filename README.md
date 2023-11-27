# Manipulação de Strings

## Desafio

Manipulação de API

Este programa lê os dados de uma API pública e manipula o resultado.

### API Pública
Endpoint: https://swapi.dev/api/people/<id>

### Manipulação do resultado

Criar uma API que receba o código de uma pessoa e retorne os dados em /guerra-nas-estrelas/{id}:

- Altura em metros
- Primeiro nome (a partir do campo 'name')
- Último nome  (a partir do campo 'name')
- Quantidade de filmes
- Título do último filme que o personagem participou

Exemplo de resposta:
```json
GET /guerra-nas-estrelas/1 

{
  "firstName": "Luke",
  "lastName": "Skywalker",
  "height": "1.72m",
  "movies": 4,
  "lastMovieName": "Revenge of the Sith"
}
```
## Implementação
### Arquivo main.py
Importação da biblioteca FastAPI
Criação de uma constante para acessar a API
Criação de um método GET
Função get_characters_endpoint que espera vários IDs e lida com conversões e erros de busca de personagens

### Arquivo api.py
Uso da biblioteca 'requests' para realizar a requisição HTTP
Criação da função get_swapi_data
Busca dados de um personagem usando a API SWAPI com base no ID fornecido
Retorna informações processadas desse personagem (primeiro nome, último nome, altura, filmes e título do último filme que participou)

### Arquivo utils.py
Função 'extract_character_info' que extrai informações básicas de um personagem da API SWAPI
Retorna um dicionário com detalhes do personagem se as informações estiverem disponíveis; caso contrário, retorna 'None'

### Testes
Uso do Postman com um método GET para a rota http://127.0.0.1:8000/guerra-nas-estrelas
Parâmetros: chave 'ids' com valor que pode conter um ou vários IDs separados por vírgula
