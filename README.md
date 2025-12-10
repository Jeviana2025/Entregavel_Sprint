# Entregavel_Sprint
# Escola360 – Sistema Escolar
O Sistema Escola 360 é uma estrutura orientada a objetos em Python destinada ao gerenciamento de usuários em um ambiente escolar.
Este projeto implementa um modelo simples de sistema escolar, baseado no diagrama de classes fornecido.  
O objetivo é demonstrar o uso de **Orientação a Objetos em Python**, seguindo boas práticas de modelagem.
<img width="749" height="503" alt="image" src="https://github.com/user-attachments/assets/b4077a2f-4892-46a9-92fa-1457b703cb93" />
# O sistema implementa:
Uma interface de autenticação, uma classe base abstrata para usuários, quatro subclasses especializadas,métodos específicos para cada papel, encapsulamento forte e princípios de herança e polimorfismo.

# ClassDiagram
<img width="1536" height="1024" alt="ChatGPT Image 9 de dez  de 2025, 21_30_32" src="https://github.com/user-attachments/assets/af5dc1cc-7a8a-40fb-9bc1-ddfb45052f2f" />



# Objetivo principal
 O objetivo é servir como base para sistemas escolares, acadêmicos ou educacionais que envolvem login, perfis e ações específicas de cada tipo de usuário.
Uso POO, implentação das classes funcional e o relacionamentos entre objetos.
# Explicação do funcionamento
A princípio aplica-se o conceito de Herança, a classe Usuario é “pai”,  e dela herdam as classes: Professor,Gestor, Responsável.
Todos eles possuem: email, senha, cpf, telefone, métodos de login e isso vai evitar repetição do codigo.

A implementação do Sistema Escola 360 utilizou de forma consistente diversos princípios e práticas fundamentais da programação, entre os principais, destacam se:
# Abstração
As classes foram modeladas a partir de entidades reais do contexto escolar, cada classe representa apenas os atributos e comportamentos essenciais do domínio, ocultando detalhes internos e proporcionando uma visão simplificada do sistema.
# Encapsulamento
A proteção dos dados é garantida por meio de atributos privados\protegidos e pela utilização de @properties para validação e acesso controlado, isso assegura a integridade das informações, como validação automática de emails, nota entre 0 e 10 e status de frequência.
# Herança
Neste requisito foi criada uma classe abstrata UsuarioAutenticavel, da qual derivam Gestor, Professor, Responsavel e Aluno. Essa estrutura evita repetição de código e promove reuso, permitindo que todas as subclasses herdam atributos comuns (id, email, senha, CPF, telefone, endereço) e o método fazer_login.
# Polimorfismo 
A herança permite que métodos comuns sejam chamados de forma uniforme, independentemente do tipo específico de usuário. A existência de um método abstrato para login, por exemplo, possibilita que cada tipo de usuário possa futuramente implementar variações específicas sem alterar a interface geral.
# Composição
O projeto faz uso de composição para representar relações entre os objetos.
um Aluno possui uma coleção interna de Nota e Frequencia;
uma Disciplina contém suas respectivas avaliações;
uma Frequencia referencia aluno, professor e disciplina simultaneamente, a relação entre Responsavel e Aluno também ocorre por composição. 
Essas estruturas tornam o modelo mais fiel ao funcionamento real de uma instituição escolar.
# Relacionamentos bidirecionais
Quando um professor registra uma nota ou frequência, as informações são automaticamente vinculadas ao aluno e à disciplina, mantendo coerência entre os módulos. Essa prática evita inconsistências e reflete a natureza integrada dos dados.
#Separação em módulos (modularização)
A organização do sistema em arquivos como usuarios.py, aluno.py, avaliacao.py e disciplinas.py favorece manutenção, reutilização e clareza do código, contribuindo para um design mais limpo e sustentável.
# Validação e integridade dos dados
As @properties com validação reforçam boas práticas de desenvolvimento orientado a objetos, garantindo que cada classe seja responsável por manter válidos os próprios dados.
# Possíveis usos da nossa solução
Gestão escolar mais organizada

A ferramenta poderá ser utilizada por escolas públicas ou privadas para centralizar informações de alunos, professores, notas, presenças e disciplinas, reduzindo processos manuais e aumentando a produtividade da equipe gestora.

Acompanhamento mais eficiente da aprendizagem

Professores poderão registrar avaliações e frequência de forma padronizada, gerando um histórico completo de cada estudante. Isso facilitará a identificação de dificuldades de aprendizagem e apoiaria intervenções pedagógicas mais assertivas.
Fortalecimento da comunicação entre responsáveis e escola

Responsáveis terão acesso rápido às informações acadêmicas de seus filhos, como notas atualizadas e registros de faltas, aumentando a participação da família no processo educativo.

Automação de relatórios e indicadores educacionais

O sistema pode ser expandido para gerar relatórios automáticos para uso interno ou envio aos órgãos educacionais, diminuindo o tempo gasto com documentos burocráticos.

Base para soluções comerciais

Empresas de tecnologia educacional poderiam utilizar essa estrutura como ponto de partida para criar produtos mais robustos, incluindo dashboards, apps móveis e integração com outros sistemas escolares.

Ferramenta de apoio para professores iniciantes

Estudantes de licenciatura ou profissionais em formação continuada poderiam usar o sistema para simular rotinas de registro escolar, adicionando como notas e frequências na sua organização no dia a dia de uma escola.




