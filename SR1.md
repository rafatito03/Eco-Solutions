## Índice
- [Links](#links)
- [Objetivos do Projeto](#Objetivos-do-Projeto)
- [Histórias de Usuário](#Histórias-de-usuário)
- [Detalhamento das Histórias](#Detalhamento-das-Histórias)
- [Diagrama de Atividades](#Diagrama-de-Atividades)
- [Atualização do Bugtracker](#Atualização-do-bugtracker)
- [Deployment](#Deployment)
- [Programação em Par](#Programação-em-Par)
- [Próximos passos](#Próximos-Passos)


## Links
- [TRELLO](https://drive.google.com/file/d/1kQ6dO-DEH4K1aShqM6Eu_-71e0VDUZxx/view?usp=drive_link)
- [Screencast Protótipo](https://drive.google.com/file/d/1_To07M6iXKal6sByfs84ZTFmZgKrUXRv/view?usp=sharing)
- [Screencast Azure](https://youtu.be/A_Wpf8nVrlk)

## Objetivos do Projeto

Este projeto visa criar uma plataforma de gestão de resíduos que permita a ONGs e empresas parceiras gerenciar inventários de resíduos e visualizar pontos de coleta. O progresso atual do projeto inclui histórias de usuário concluídas e implementadas, além de diagramas de atividades e a experiência com programação em par.

## Histórias de Usuário

### Histórias Pendentes

1. **Adicionar inventário de resíduos (ONG)**
   - **Descrição**: Como ONG, gostaria de adicionar uma lista de inventário de resíduos, para poder registrar os materiais recicláveis disponíveis.
   - **Critérios de Aceitação**:
     - A ONG pode acessar um formulário para adicionar novos itens ao inventário.
     - O inventário deve ser atualizado em tempo real após a adição de um novo item.

2. **Visualizar inventário de resíduos (ONG)**
   - **Descrição**: Como ONG, gostaria de visualizar a lista de um inventário de resíduos, para acompanhar os materiais disponíveis para doação ou coleta.
   - **Critérios de Aceitação**:
     - A ONG pode acessar uma página de visualização do inventário.
     - A lista deve exibir detalhes como nome, tipo, e quantidade dos resíduos.

3. **Remover itens do inventário de resíduos (ONG)**
   - **Descrição**: Como ONG, gostaria de remover itens da lista de inventário de resíduos, para manter a lista atualizada conforme os resíduos são coletados.
   - **Critérios de Aceitação**:
     - A ONG pode selecionar itens para remover da lista.
     - A remoção deve ser refletida imediatamente no inventário.

### Histórias Concluídas

1. **Visualizar inventário de ONGs parceiras (Administradora)**
   - **Descrição**: Como administradora de empresas, gostaria de visualizar a lista de inventário de resíduos das ONGs parceiras, para poder planejar a logística de coleta.
   - **Critérios de Aceitação**:
     - A administradora pode visualizar os inventários de ONGs cadastradas.
     - A visualização inclui detalhes como data de atualização e tipos de resíduos disponíveis.

2. **Saber pontos de coleta de resíduos (Administradora e Usuário)**
   - **Descrição**: Como administradora da empresa e como usuário, gostaria de saber os pontos de coleta de resíduos, para facilitar o planejamento e entrega dos materiais recicláveis.
   - **Critérios de Aceitação**:
     - Um mapa interativo que mostra os pontos de coleta disponíveis.
     - Detalhes como endereço e horários de funcionamento dos pontos.

## Detalhamento das Histórias

- **Storyboards e Sketches**: Cinco histórias de usuário foram detalhadas com sketches e storyboards que podem ser acessados através do [README](https://github.com/rafatito03/Eco-Solutions/blob/main/README.md).
- **Histórias Implementadas**: Até o momento, duas histórias foram completamente implementadas e testadas, focando na visualização do inventário de ONGs e nos pontos de coleta de resíduos.

## Diagrama de Atividades

Foi criado um diagrama de atividades que detalha o fluxo de interação entre os usuários e o sistema, cobrindo desde o login até o gerenciamento de inventários e visualização dos pontos de coleta. O diagrama está disponível para consulta [aqui](#).

## Atualização do Bugtracker

Todas as issues relacionadas aos bugs encontrados até o momento foram documentadas e atualizadas no Bugtracker. Foram criados novos relatórios de bugs e atualizações de progresso em cada uma das issues.

## Deployment

As histórias implementadas foram devidamente testadas e já estão disponíveis em produção. Isso inclui as funcionalidades de visualização de inventários e pontos de coleta, que podem ser acessadas diretamente pelos usuários.

## Programação em Par

Nós, da parte de programação da Eco Storage, utilizamos a técnica de programação em par, a qual se trata de duas pessoas colaborarem no código juntas, enquanto uma escreve o código e diz as ideias para a outra, essa outra vai revisando e analisando o código para encontrar erros e possíveis melhorias.
Essa técnica foi utilizada majoritariamente em questões que pudessem ser resolvidas em um não tão longo período de tempo.
Além disso, para que pudessemos usufruir totalmente dessa técnica, utilizamos a extensão "Live Share" do VSCode, o que resultou em feedbacks rápidos e pcorreção imediata do código, já que a pessoa que estava analisando o código podia o editar por si só.

---

## Próximos Passos

- Concluir as histórias pendentes.
- Realizar testes de usabilidade nas funcionalidades implementadas.
- Implementar melhorias baseadas no feedback dos usuários e stakeholders.
