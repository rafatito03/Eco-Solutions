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

Foi criado um diagrama de atividades que detalha o fluxo de interação entre os usuários e o sistema, cobrindo desde o login até o gerenciamento de inventários e visualização dos pontos de coleta. O diagrama está disponível para consulta. 

### Fluxograma:
![image](https://github.com/user-attachments/assets/1838c98a-c6d4-4515-8096-967c9d2f81d4)

## Atualização do Bugtracker
Problema de Django não Reconhecendo a Pasta Static

Issue: O Django não estava reconhecendo os arquivos na pasta static, resultando em falhas ao carregar CSS e JavaScript no frontend.

Causa: A configuração para servir arquivos estáticos em modo de desenvolvimento estava incompleta. O Django não sabia onde buscar os arquivos estáticos devido à ausência da definição correta no arquivo settings.py, além da configuração da URL para arquivos estáticos no arquivo urls.py.

Solução: Corrigimos o problema adicionando a configuração correta para STATIC_URL e STATICFILES_DIRS no settings.py, garantindo que o Django soubesse o caminho para a pasta static. Também foi necessário verificar se a URL para servir os arquivos estáticos estava configurada corretamente no urls.py ao incluir from django.conf import settings e from django.conf.urls.static import static, seguido de urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT).

Esse ajuste permitiu que os arquivos CSS e JavaScript fossem servidos corretamente, resolvendo o problema de renderização de estilo no frontend.

Problema com o Leaflet.js Não Reconhecendo Classes CSS Passadas pelo Django
Issue: As classes CSS aplicadas aos mapas Leaflet.js, que foram geradas dinamicamente via Django, não estavam sendo reconhecidas, resultando em falhas no estilo ou na funcionalidade dos mapas.
Causa: O problema estava relacionado à maneira como as classes CSS eram passadas para o template. Algumas classes específicas, principalmente aquelas relacionadas ao estilo dinâmico dos mapas, não estavam sendo aplicadas corretamente, possivelmente devido a conflitos no escopo ou à maneira como o Django estava gerando as classes nos templates.
Solução: Para corrigir, revisamos como as classes CSS eram geradas e aplicadas aos elementos de mapa. Garantimos que todas as classes necessárias fossem passadas de forma explícita via contexto para o template Django. Além disso, verificamos se o arquivo de CSS do Leaflet.js estava sendo carregado corretamente no template.
Corrigimos o problema ao garantir que as classes CSS fossem aplicadas dinamicamente de forma adequada no HTML gerado, e revisamos a configuração do STATIC_url para carregar os estilos corretos do Leaflet.js. Isso restaurou a renderização apropriada dos estilos e funcionalidades do mapa no frontend.

### Issue Aberta:
![image](https://github.com/user-attachments/assets/38cb1ddc-bd16-49d3-99f6-607d4282b8a2)

## Deployment

As histórias implementadas foram devidamente testadas e já estão disponíveis em produção. Isso inclui as funcionalidades de visualização de inventários e pontos de coleta, que podem ser acessadas diretamente pelos usuários.

## Programação em Par

Nós, da parte de programação da Eco Storage, utilizamos a técnica de programação em par, a qual se trata de duas pessoas colaborarem no código juntas, enquanto uma escreve o código e diz as ideias para a outra, essa outra vai revisando e analisando o código para encontrar erros e possíveis melhorias.
Essa técnica foi utilizada majoritariamente em questões que pudessem ser resolvidas em um não tão longo período de tempo.
Além disso, para que pudessemos usufruir totalmente dessa técnica, utilizamos a extensão "Live Share" do VSCode, o que resultou em feedbacks rápidos e pcorreção imediata do código, já que a pessoa que estava analisando o código podia o editar por si só.

Par 00 - Raphael e Beatriz
- Coube à dupla fazer a integração do banco de dados SQLite com Django e com JSON, também a interação de template e views.

Par 01 - Rafael e Raphael
- O live Share foi utilizado nesse caso para uma correção de bug no deploy, Rafasel fez a formatação correta das pastas, mas ao encontrar erross no comnmit do github, teve o auxílio de Raphael para criar a branch de produção.

---

## Próximos Passos

- Concluir as histórias pendentes.
- Realizar testes de usabilidade nas funcionalidades implementadas.
- Implementar melhorias baseadas no feedback dos usuários e stakeholders.
