## Índice
- [Links](#links)
- [Bug Tracker](#Bug-Tracker)
- [Diagrama de Atividades](#Diagrama-de-Atividades)
- [Deployment](#Deployment)
- [Extreme Programming](#Extreme-Programming)
- [Histórias de Usuário](#Histórias-de-Usuário)

## Links
- [Screencast CI/CD G09](https://youtu.be/eFDLo6aWeGg)
- [Screencast testes G09](https://youtu.be/-sc3ooL2jvI)
- [Screencast Protótipo de média fidelidade](https://youtu.be/ngcamw3nYnw)
- [Protótipo de média fidelidade](https://www.figma.com/design/MbJEOcZNmzkNZshfwB1Tgr/lowfi-ecostorage-gogo?node-id=0-1&node-type=canvas&t=7ohRnEn0rMPRHHFA-0)
- [Diagrama de Atividades](https://drive.google.com/file/d/1aFjQFdqnjbixS3VZI18kmLsCGPx637HP/view?usp=drive_link)


## Bug Tracker

### Bugs Abertos
- Páginas de mapa não responsiva no celular, cadastro não é visível
![image](https://github.com/user-attachments/assets/43c34ec2-e4f6-47a8-af6a-c3493e211b35)

### Bugs Fechados
- Reviews multiplicando inventário de uma ong: https://github.com/rafatito03/Eco-Solutions/issues/4
- Verificar_ong e ong_details: https://github.com/rafatito03/Eco-Solutions/issues/3
- Apagando outros marcadores: https://github.com/rafatito03/Eco-Solutions/issues/2
- Problema com Caminho da Pasta Static: https://github.com/rafatito03/Eco-Solutions/issues/1
![image](https://github.com/user-attachments/assets/fc803e36-9164-45c5-b64c-03a753f45e43)

## Diagrama de Atividades

### Fluxograma
![image](https://github.com/user-attachments/assets/1448aaac-c1ba-4358-9dde-a02d8b5f7551)

## Deployment
O site pode ser acessado por esse link: [Azure Site](https://ecosolutions.azurewebsites.net/)

## Extreme Programming
Nós da Eco Storage fizemos utilização do pair programming durante o processo de desenvolvimento do Site
Par 00 - Rafael e Raphael:
- Rafael e Raphael fizeram os testes E2E utilizando Cypress e também fizeram o deploy, dizem eles que a experiência foi tranquila e conseguiram aprender durante o processo, por mais que tenha sido longo e frustrante em certos momentos.

## Histórias de Usuário

### Histórias concluídas:

**1. Como usuário, gostaria de avaliar ONGs**

- **Independent:** Sim, essa funcionalidade é independente e não depende de outras histórias para ser implementada.
- **Negotiable:** Sim, os critérios de avaliação podem ser ajustados com base nos requisitos do sistema ou do feedback dos usuários.
- **Valuable:** Sim, permite que os usuários contribuam para a melhoria das ONGs e ajudem outros usuários a tomar decisões informadas.
- **Estimable:** Sim, é possível estimar o esforço para implementar a funcionalidade de avaliação.
- **Small:** Sim, é uma funcionalidade específica que pode ser desenvolvida em uma sprint curta.
- **Testable:** Sim, pode ser testada verificando se o sistema permite avaliar e registrar feedback para as ONGs.

**2. Como usuário, gostaria de saber a rota até a ONG pelo Waze**

- **Independent:** Sim, essa funcionalidade é independente e não depende de outras histórias para ser implementada.
- **Negotiable:** Sim, o botão, link e formato de interação podem ser negociados.
- **Valuable:** Sim, permite que os usuários se localizem e possam buscar o que é de interesse deles diretamente na ONG.
- **Estimable:** Sim, é possível estimar o esforço para implementar a rota do Waze.
- **Small:** Sim, é uma funcionalidade específica que pode ser desenvolvida em uma sprint curta.
- **Testable:** Sim, pode ser testada verificando se o link está redirecionando o usuário corretamente.


**3. Como usuário, gostaria de falar direto com a ONG pelo WhatsApp**

- **Independent:** Sim, é uma funcionalidade independente que pode ser desenvolvida separadamente.
- **Negotiable:** Sim, os detalhes como botão de acesso, formato da interação e integrações podem ser negociados.
- **Valuable:** Sim, facilita a comunicação direta entre usuários e ONGs, tornando o sistema mais útil e acessível.
- **Estimable:** Sim, é possível estimar o esforço necessário para implementar essa integração com o WhatsApp.
- **Small:** Sim, é uma tarefa objetiva e com escopo bem definido.
- **Testable:** Sim, pode ser testada verificando se o botão ou link de contato direciona corretamente para o WhatsApp da ONG.


**4. Como ONG, gostaria de adicionar lista de um inventário de resíduos**

- **Independent:** Sim, é uma funcionalidade que pode ser desenvolvida de forma isolada.
- **Negotiable:** Sim, a descrição permite alterações e negociação de requisitos específicos.
- **Valuable:** Sim, agrega valor ao permitir o registro de resíduos pela ONG.
- **Estimable:** Sim, é possível estimar o esforço necessário para implementá-la.
- **Small:** Sim, a tarefa parece suficientemente pequena para ser concluída em um curto prazo.
- **Testable:** Sim, pode ser testada verificando se a lista é adicionada corretamente.

**5. Como ONG, gostaria de visualizar a lista de um inventário de resíduos**

- **Independent:** Sim, pode ser desenvolvida separadamente de outras histórias.
- **Negotiable:** Sim, é possível ajustar a forma de exibição com base nos requisitos.
- **Valuable:** Sim, facilita o acesso à informação para a ONG.
- **Estimable:** Sim, pode-se estimar o esforço necessário para implementar essa funcionalidade.
- **Small:** Sim, parece ser uma tarefa pequena e objetiva.
- **Testable:** Sim, pode ser testada verificando se a lista é exibida corretamente.

**6. Como ONG, gostaria de remover a lista de um inventário de resíduos**

- **Independent:** Sim, é independente de outras funcionalidades.
- **Negotiable:** Sim, os detalhes sobre a remoção podem ser ajustados.
- **Valuable:** Sim, permite manter o inventário atualizado, o que é valioso para a ONG.
- **Estimable:** Sim, o esforço para implementar essa funcionalidade é estimável.
- **Small:** Sim, é uma tarefa pequena e bem delimitada.
- **Testable:** Sim, pode ser testada ao verificar se a lista é removida conforme esperado.

**7. Como Admin, gostaria de remover ONGs existentes**

- **Independent:** Sim, a história é independente, pois a ação de remover ONGs não depende de outras ações, como editar ou adicionar ONGs, podendo ser implementada de forma autônoma.
- **Negotiable:** Sim, pode-se discutir aspectos como exigir confirmação antes da remoção, tipos de validações necessárias ou permitir recuperação dos dados removidos.
- **Valuable:** Sim, é valiosa, pois mantém a integridade dos dados da plataforma, permitindo ao admin gerenciar as ONGs de forma eficaz, excluindo aquelas que não devem mais estar disponíveis.
- **Estimable:** Sim, o esforço necessário para implementar a funcionalidade de exclusão de ONGs, incluindo interface, confirmações e integração com o banco de dados, é previsível.
- **Small:** Sim, a história é pequena, já que a exclusão de ONGs é uma funcionalidade específica, com escopo limitado.
- **Testable:** Sim, cenários de teste podem incluir: tentar excluir ONGs com/sem vínculos, verificar a remoção de dados no banco de dados, e a confirmação ou rejeição de exclusão.

**8. Como Admin, gostaria de adicionar ONGs novas**

- **Independent:** Sim, a história é independente. Adicionar ONGs novas não depende de outras funcionalidades, como editar ou excluir ONGs. Pode ser implementada separadamente.
- **Negotiable:** Sim, é negociável. Pode-se ajustar os detalhes, como quais campos são necessários para o cadastro das ONGs ou o fluxo de adição (formulário simples ou em etapas).
- **Valuable:** Sim, é valiosa, pois permite que novas ONGs e seus dados sejam inseridos na plataforma, expandindo a utilidade e relevância do sistema e melhorando a experiência do usuário.
- **Estimable:** Sim, é possível calcular o esforço necessário para criar uma interface de cadastro, validações e a integração com o banco de dados.
- **Small:** Sim, a história é pequena, pois trata de uma funcionalidade bem definida e de escopo limitado.
- **Testable:** Sim, pode-se criar cenários de teste para verificar o cadastro de ONGs, como entrada de dados válidos/inválidos, validação de campos obrigatórios e feedback ao usuário.

**9. Como Admin, gostaria de modificar ONGs existentes**

- **Independent:** Sim, a história pode ser implementada de forma independente, sem depender diretamente de outras funcionalidades, como criação ou exclusão de ONGs.
- **Negotiable:** Sim, é negociável. Pode-se ajustar os detalhes, como o tipo de campos que serão editáveis ou as permissões para ações.
- **Valuable:** Sim, é valiosa, pois permite que o admin mantenha os dados das ONGs atualizados, o que é crucial para a funcionalidade da plataforma.
- **Estimable:** Sim, é possível estimar o esforço necessário para implementar a funcionalidade, desde a interface de edição até as validações e atualizações no banco de dados.
- **Small:** Sim, a história é pequena, pois trata de uma única ação, que é bem delimitada e de fácil implementação.
- **Testable:** Sim, pode-se criar cenários de teste para verificar se o admin consegue editar as ONGs, com validações para campos obrigatórios, permissões e feedback de sucesso ou erro.
