# MasterPoint Admin

Esse projeto foi desenvolvido em Python com framework Django e suas diversas ferramentas de ecossistema, visando apresentar habilidades de desenvolvimento backend.

A idéia é ser um sistema Fullstack de Cadastro de usuários e registros de pontos eletrônicos.

Frontend: (https://github.com/seltonkdd/MasterPoint-app)

# Funcionalidades:

- Um sistema backoffice (Django Admin) para administradores cadastrarem manualmente usuários, funcionários e seus respectivos pontos.
- Autenticação de Usuários com Simple-JWT
- API REST para consumo do aplicativo mobile MasterPoint
- Uso de API externa do Google Maps
- Cada ponto guarda a ultima localização de quem registrou.
- Conteinerização com Docker e PostgresSQL
  
# Uso

> ## Pré requisitos

#### Clone o projeto:
    git clone https://github.com/seltonkdd/api-MasterPoint

Entre no diretório do projeto

#### Para rodar localmente com Docker, necessário ter o Docker e o Docker Compose
    docker-compose up --build

Você deve criar um superusuário `python manage.py createsuperuser` no container da sua aplicação para poder entrar no Admin do DJango

Acesse `localhost:8000/`

# Documentação da API

A rota padrão da API é `api/v1` e a documentação estará disponivél em `/docs/`, `/schema/` ou `/redoc/`.

Essa API será consumida pelo frontend, que é o app mobile MasterPoint

> As rotas são privadas e só podem ser acessadas via token JWT (simple_jwt)

#### Geração de token para autenticação

    POST /auth/token/

| Body   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `email` | `string` | **Obrigatório**. email do Usuário para requisição | 
| `password` | `string` | **Obrigatório**. Senha do Usuário para |

Retorna um JSON com token `refresh` e `access`

    POST /auth/refresh/

| Body   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `refresh` | `string` | **Obrigatório**. Token `refresh`|

Retorna um novo token válido

#### Cadastro de funcionários
    POST /employees/

| Body   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `user` | `integer` | **Opcional**. ID do Usuário associado a esse Funcionário | 
| `name` | `string` | **Obrigatório**. Nome do Funcionário |
| `cpf` | `string` | **Opcional**. CPF do Funcionário |
| `phone` | `string` | **Opcional**. Telefone do Funcionário |

Cada Funcionário tem uma relação `OneToTone` com o Usuário do Django
Apenas Usuários com permissão podem adicionar Funcionários

#### Consulta de funcionários
    GET /employees/

Retorna uma lista de todos os funcionários cadastrados. Apenas Usuários com permissão podem acessar essa rota

#### Editar e deletar funcionários
    PUT PATCH DELETE /employees/{id}

Apenas Usuários com permissão podem deletar ou editar Funcionários

#### Registro de pontos por funcionário
    POST /clocks/

| Body   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `punch` | `datetime` | **Obrigatório**. Data e hora do ponto | 
| `latitude` | `string` | **Opcional**. Latitude do funcionário |
| `longitude` | `string` | **Opcional**. Longitude do funcionário |
| `employee` | `integer` | **Opcional**. ID do funcionário relacionado ao ponto |
| `email` | `string` | **Read-Only**. Email do Usuário relacionado ao funcionário |

O campo `employee` é preenchido automaticamente com o Funcionário associado ao Usuário da requisição
O campo `email` é preenchido automaticamente com o email do Usuário da requisição

Apenas Funcionários podem adicionar pontos, ou Usuários para um funcionário específico

#### Consulta de pontos por funcionário
    GET /clocks/

Retorna uma lista de pontos APENAS daquele funcionário

#### Editar, Deletar pontos
    PUT PATCH DELETE /clocks/{id}

Apenas Usuários com permissão podem editar ou deletar pontos

#### Uso da API do google maps
Em `.env` coloque sua chave de api do google maps

    GET /get_maps_image/{latitude}/{longitude}/

Retorna uma imagem de GPS da localização fornecida, essa rota é requisitada pelo frontend.

# Screenshots
![Captura de Tela (11)](https://github.com/user-attachments/assets/69f11a13-26af-499b-b341-f3fa6c5eafcb)

