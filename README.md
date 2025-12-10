

# Escola360 - Dashboard de Acompanhamento Escolar

O Sistema Escola 360 é uma aplicação de gestão escolar que modela o ecossistema de uma instituição de ensino. Desenvolvido com foco em boas práticas de programação, extensibilidade e manutenibilidade, o sistema busca oferecer uma base sólida para o gerenciamento acadêmico.

Características principais:

 - Gestão de múltiplos tipos de usuários (professores, alunos, responsáveis, gestores)

 - Controle completo de notas e frequência

 - Sistema de disciplinas curriculares

 - Geração de relatórios

 - Arquitetura modular e extensível

**OBS -*** <ins>Sistema na fase inicial de desenvolvimento.</ins>

Nesta etapa foi implementado apenas o básico do Backend do sistema.

## Visão Geral do Projeto

O projeto está organizado em módulos, cada um representando uma parte do domínio:

 **usuarios.py:**
  + Classes base (Usuario, Autenticavel, GeradorRelatorio) e papéis de gestão, ensino e acompanhamento  (Professor, Gestor, Responsavel).

 **aluno.py**
  + Implementação da classe Aluno e seus métodos de consulta de dados acadêmicos.

 **disciplinas.py**
  + Implementação da classe Disciplina e seu registro de notas/frequências.

 **avaliacao.py**
  + Classes que representam registros acadêmicos (Nota e Frequencia).

 **relatorios.py**
  + Classe simples para o objeto Relatorio, usado pelo Gestor.

 **main.py**
  + Script de demonstração para testar as funcionalidades e relações entre as classes.



## Como Executar

Certifique-se de ter o Python 3.10+ instalado.

Garanta que todos os arquivos estejam na mesma pasta:

    usuarios.py

    aluno.py

    disciplinas.py

    avaliacao.py

    relatorios.py

    main.py

No terminal, navegue até a pasta do projeto e execute:
```python
python main.py
```



Você deverá ver uma saída semelhante a:
````
--- 1. CRIAÇÃO DE ENTIDADES ---
Professor criado: João Silva (ID: 10)
----------------------------------------
--- 2. TESTES DE AUTENTICAÇÃO ---
Login de João Silva: SUCESSO.
Login de João Silva: FALHA (esperado).
----------------------------------------
--- 3. LANÇAMENTO DE NOTAS E VALIDAÇÃO ---
Nota 9.0 em Matemática lançada com sucesso.
Nota 7.5 em Português lançada com sucesso.
Teste de Erro de Nota: SUCESSO. Erro capturado: valor da nota deve estar entre 0 e 10
----------------------------------------
--- 4. TESTES DE FREQUÊNCIA E CÁLCULOS ---
Total de Aulas de Matemática: 5
Presenças: 3 | Faltas: 2
Porcentagem de Frequência: 60.00%
----------------------------------------
--- 5. TESTES DE RELACIONAMENTO ---
Notas registradas para Ana Pereira:
  > Matemática: 9.0 (Prova Mensal)
  > Português: 7.5 (Trabalho)
Notas registradas em Matemática:
  > Aluno: Ana Pereira, Nota: 9.0
````
(Os textos exatos podem variar ligeiramente conforme adaptações/alterações no arquivo main.py.)

## Conceitos de design e boas práticas utilizadas
Este projeto foi pensado como um modelo de domínio didático, aplicando boas práticas de Programação Orientada a Objetos (POO):

> Herança e polimorfismo

Usuario é a classe base abstrata, enquanto Gestor, Professor, Responsavel e Aluno especializam seu comportamento.

Interfaces (Autenticavel, GeradorRelatorio) definem contratos claros.

> Encapsulamento

Atributos privados (__nome, __notas, __frequencias etc.) e properties expõem apenas o que é necessário.

As coleções são retornadas como cópias, evitando modificação externa direta.

> Validação de regras de negócio

Notas limitadas entre 0 e 10.

Status de frequência limitado a “P” ou “F”.

E-mail com formato mínimo.

ID positivo, CPF não vazio.

> Consistência do modelo

Quando o professor lança uma nota ou registra uma frequência, o código atualiza as listas do Professor, do Aluno e da Disciplina, garantindo que todos os lados do relacionamento se mantenham sincronizados.

## Possíveis usos do Escola360
Embora o projeto seja pequeno e construido para fins didáticos, ele já representa um núcleo que poderia facilmente ser expandido em várias direções. Vejamos algumas possibilidades:

1. Backend de um sistema escolar web ou mobile
   - Servir como camada de domínio em uma API (Flask, FastAPI ou Django), expondo endpoints para:
     - Cadastro de usuários, alunos, disciplinas.
     -	Lançamento de notas e registro de frequência.
     -	Geração de relatórios consolidados para gestores, professores, etc..
       
2. Ferramenta de acompanhamento pedagógico
   - Professores/Gestores poderiam usar uma aplicação simples, baseada nesse modelo, para:
     - Registrar avaliações e presenças em tempo real.
     - Gerar relatórios por aluno, por turma ou por disciplina.
     - Exportar dados em CSV/JSON para outros sistemas.
       
3. Criação de Portal de Pais e Alunos
   - Essa estrutura pode ser facilmente convertida em uma API para alimentar um portal onde responsáveis e alunos acessam suas informações em tempo real, como:
     - Notificações de Ocorrências.
     - Agendamento de Reuniões.
     - Visualização/acompanhamento de atividades escolares.
       
4. Protótipo para integração com ERPs escolares
  - O modelo poderia ser integrado a sistemas maiores, atuando como:
    - Módulo de “vida acadêmica” (notas, frequências, boletins).
    - Fonte de dados para dashboards de desempenho e evasão.
## Estrutura de pastas (módulos)
seu_projeto/
│
├── main.py
│
├── usuarios/
│   ├── __init__.py
│   ├── usuarios.py   ← aqui estão Gestor, Professor, Responsavel, Usuario
│
├── relatorios/
│   ├── __init__.py
│   ├── relatorios.py ← classe Relatorio
│
├── avaliacao/
│   ├── __init__.py
│   ├── avaliacao.py  ← classes Nota e Frequencia
│
└── disciplinas/
    ├── __init__.py
    ├── disciplinas.py ← classe Disciplina

