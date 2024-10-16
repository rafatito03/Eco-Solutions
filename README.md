# Eco-Solutions

Este projeto é uma plataforma web que permite a localização de doações de tecidos para ONGs. Ele apresenta um mapa interativo onde os usuários podem visualizar, cadastrar e buscar por pontos de coleta de tecidos, facilitando a distribuição e reutilização de materiais para projetos sociais e ambientais.

## Índice
- [Link SR1](#link-sr1)
- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Links](#links)
- [Licença](#licença)

## Link SR1
- [SR1](https://github.com/rafatito03/Eco-Solutions/blob/main/SR1.md)

## Descrição do Projeto

O **Eco Solutionss** tem como objetivo conectar doadores e ONGs que precisam de tecidos para desenvolver seus trabalhos. Através de um mapa interativo, doadores podem encontrar pontos de coleta perto de suas casas e ONGs podem divulgar as suas necessidades de material. O projeto foi desenvolvido para promover a sustentabilidade e a solidariedade, evitando o desperdício de tecidos e apoiando causas sociais.

## Funcionalidades

- **Mapa Interativo:** Visualização de pontos de coleta de doações de tecidos geolocalizados.
- **Informações Detalhadas:** Cada ponto de coleta possui detalhes como horário de funcionamento, tipos de tecidos aceitos e informações de contato.

## Tecnologias Utilizadas

- **Frontend:**
  - HTML5
  - TailwindCSS
  - JavaScript
  - Leaflet.js
  - JSON
  
- **Backend:**
  - Django 
  - SQLite

- **Outras Ferramentas:**
  - Ambiente Virtual (venv)

## Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:

   ```
   git clone https://github.com/rafatito03/Eco-Solutions/
   ```
2. Acesse o diretório do projeto:
   ```
   cd Eco-Solutions
   ```

3. Crie e ative um ambiente virtual:
    ```
    python -m venv venv
    source venv/bin/activate   # Linux/MacOS
    venv\Scripts\Activate      # Windows
    ```

4. Inicie o servidor de desenvolvimento:
    ```
    python manage.py runserver
    ```

5. Acesse o projeto no navegador:
    ```
    http://localhost:8000
    ```

## Como Usar

  Cadastro de ONGs: ONGs podem se cadastrar e informar os locais de coleta de tecidos.
  Cadastro de Doações: Usuários podem cadastrar suas doações, informando o tipo de tecido, quantidade e localização.
  Busca: Utilize o mapa ou a barra de busca para encontrar pontos de coleta ou ONGs específicas.
  Filtros: Filtre os resultados por tipo de tecido ou proximidade geográfica.

## Links

  - TRELLO: https://drive.google.com/file/d/1kQ6dO-DEH4K1aShqM6Eu_-71e0VDUZxx/view?usp=drive_link
  - SR1.md: wip

## Licença
  
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
