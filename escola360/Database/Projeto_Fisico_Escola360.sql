
-- ==========================================================
-- UNIVERSIDADE FEDERAL DO CARIRI - UFCA
-- CURSO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
-- DISCIPLINA - PROJETO INTEGRADO II
-- ENTREGÁVEL PARCIAL II
-- ==========================================================


-- ==========================================================
-- APP Escola360 - Projeto Físico (PostgreSQL)
-- ==========================================================




-- Cria o banco de dados escola360

CREATE DATABASE escola360;

-- ==============================
-- 1) USUÁRIOS
-- ==============================
CREATE TABLE usuarios (
  id_usuario      SERIAL PRIMARY KEY,
  email           VARCHAR(100) NOT NULL UNIQUE,
  senha           VARCHAR(255) NOT NULL,
  data_criacao    DATE NOT NULL DEFAULT CURRENT_DATE,
  tipo_usuario    VARCHAR(20) NOT NULL,

  -- Tipos de usuários permitidos
  CONSTRAINT ck_usuarios_tipo
    CHECK (tipo_usuario IN ('ALUNO', 'PROFESSOR', 'GESTOR', 'RESPONSAVEL')),

  -- Validação de formado do email
  CONSTRAINT email_formato
    CHECK (email ~* '^.+@.+\..+$')
);

-- ==============================
-- 2) ESTRUTURA ACADÊMICA
-- ==============================

-- 2.1 TABELA: TURMAS
CREATE TABLE turmas (
  id_turma      SERIAL PRIMARY KEY,
  nome_turma    VARCHAR(50) NOT NULL,
  turno         VARCHAR(20) NOT NULL,
  ano_letivo    INTEGER NOT NULL,
  quant_alunos  INTEGER NOT NULL DEFAULT 0,

  CONSTRAINT ck_turmas_turno
    CHECK (turno IN ('Matutino', 'Vespertino', 'Noturno')),

  CONSTRAINT ck_turmas_ano
    CHECK (ano_letivo BETWEEN 1900 AND 2200),

  CONSTRAINT ck_turmas_quant_alunos
    CHECK (quant_alunos >= 0)
);

-- 2.2 TABELA: DISCIPLINAS
CREATE TABLE disciplinas (
  id_disciplina    SERIAL PRIMARY KEY,
  nome_disciplina  VARCHAR(100) NOT NULL UNIQUE,
  carga_horaria    INTEGER,

  CONSTRAINT ck_disciplinas_carga
    CHECK (carga_horaria > 0)
);

-- ==============================
-- 3) PERFIS DE USUÁRIOS
-- ==============================

-- 3.1 TABELA: ALUNOS
CREATE TABLE alunos (
  id_aluno         SERIAL PRIMARY KEY,
  id_usuario       INTEGER NOT NULL UNIQUE,
  id_turma         INTEGER,
  matricula        VARCHAR(20) NOT NULL UNIQUE,
  nome             VARCHAR(100) NOT NULL,
  cpf              VARCHAR(14) UNIQUE,
  data_nascimento  DATE,
  telefone         VARCHAR(20),
  endereco         TEXT,

  CONSTRAINT fk_alunos_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_alunos_turma
    FOREIGN KEY (id_turma)
    REFERENCES turmas (id_turma)
    ON DELETE SET NULL
    ON UPDATE CASCADE,

  CONSTRAINT ck_alunos_data_nasc
    CHECK (data_nascimento <= CURRENT_DATE)
);

-- 3.2 TABELA: PROFESSORES
CREATE TABLE professores (
  id_professor        SERIAL PRIMARY KEY,
  id_usuario          INTEGER NOT NULL UNIQUE,
  matricula_funcional VARCHAR(20) NOT NULL UNIQUE,
  nome                VARCHAR(100) NOT NULL,
  cpf                 VARCHAR(14) UNIQUE,
  data_nascimento     DATE,
  formacao            VARCHAR(100),
  telefone            VARCHAR(20),
  endereco            TEXT,

  CONSTRAINT fk_professores_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_professores_data_nasc
    CHECK (data_nascimento <= CURRENT_DATE)
);

-- 3.3 TABELA: GESTORES
CREATE TABLE gestores (
  id_gestor           SERIAL PRIMARY KEY,
  id_usuario          INTEGER NOT NULL UNIQUE,
  matricula_funcional VARCHAR(20) NOT NULL UNIQUE,
  nome                VARCHAR(100) NOT NULL,
  cpf                 VARCHAR(14) UNIQUE,
  data_nascimento     DATE,
  cargo               VARCHAR(50),
  telefone            VARCHAR(20),
  endereco            TEXT,

  CONSTRAINT fk_gestores_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_gestores_data_nasc
    CHECK (data_nascimento <= CURRENT_DATE)
);

-- 3.4 TABELA: RESPONSÁVEIS
CREATE TABLE responsaveis (
  id_responsavel   SERIAL PRIMARY KEY,
  id_usuario       INTEGER NOT NULL UNIQUE,
  nome             VARCHAR(100) NOT NULL,
  cpf              VARCHAR(14) UNIQUE,
  data_nascimento  DATE,
  telefone         VARCHAR(20),
  endereco         TEXT,
  parentesco       VARCHAR(50),

  CONSTRAINT fk_responsaveis_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_responsaveis_data_nasc
    CHECK (data_nascimento <= CURRENT_DATE)
);

-- ==============================
-- 4) RELACIONAMENTOS
-- ==============================

-- 4.1 RESPONSÁVEL x ALUNO
CREATE TABLE responsavel_aluno (
  id_vinculo            SERIAL PRIMARY KEY,
  id_responsavel        INTEGER NOT NULL,
  id_aluno              INTEGER NOT NULL,
  responsavel_principal BOOLEAN NOT NULL DEFAULT FALSE,

  CONSTRAINT fk_ra_responsavel
    FOREIGN KEY (id_responsavel)
    REFERENCES responsaveis (id_responsavel)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_ra_aluno
    FOREIGN KEY (id_aluno)
    REFERENCES alunos (id_aluno)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT uk_responsavel_aluno
    UNIQUE (id_responsavel, id_aluno)
);

-- 4.2 LOTAÇÃO PROFESSOR x TURMA x DISCIPLINA
CREATE TABLE prof_turma_lotacao (
  id_lotacao            SERIAL PRIMARY KEY,
  id_professor          INTEGER NOT NULL,
  id_turma              INTEGER NOT NULL,
  id_disciplina         INTEGER NOT NULL,
  carga_horaria_lotacao INTEGER,

  CONSTRAINT fk_lotacao_professor
    FOREIGN KEY (id_professor)
    REFERENCES professores (id_professor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_lotacao_turma
    FOREIGN KEY (id_turma)
    REFERENCES turmas (id_turma)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_lotacao_disciplina
    FOREIGN KEY (id_disciplina)
    REFERENCES disciplinas (id_disciplina)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_lotacao_ch
    CHECK (carga_horaria_lotacao IS NULL OR carga_horaria_lotacao > 0),

  CONSTRAINT uk_lotacao
    UNIQUE (id_professor, id_turma, id_disciplina)
);

-- ==============================
-- 5) REGISTROS ACADÊMICOS
-- ==============================

-- 5.1 TABELA: NOTAS
CREATE TABLE notas (
  id_nota         SERIAL PRIMARY KEY,
  id_aluno        INTEGER NOT NULL,
  id_disciplina   INTEGER NOT NULL,
  id_professor    INTEGER NOT NULL,
  valor_nota      NUMERIC(4,2) NOT NULL,
  data_lancamento DATE NOT NULL DEFAULT CURRENT_DATE,

  CONSTRAINT fk_notas_aluno
    FOREIGN KEY (id_aluno)
    REFERENCES alunos (id_aluno)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_notas_disciplina
    FOREIGN KEY (id_disciplina)
    REFERENCES disciplinas (id_disciplina)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_notas_professor
    FOREIGN KEY (id_professor)
    REFERENCES professores (id_professor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_notas_valor
    CHECK (valor_nota BETWEEN 0 AND 10),

  CONSTRAINT ck_notas_data
    CHECK (data_lancamento <= CURRENT_DATE),

  CONSTRAINT uk_notas
    UNIQUE (id_aluno, id_disciplina)
);

-- 5.2 TABELA: FREQUÊNCIAS
CREATE TABLE frequencias (
  id_frequencia     SERIAL PRIMARY KEY,
  id_aluno          INTEGER NOT NULL,
  id_disciplina     INTEGER NOT NULL,
  id_professor      INTEGER NOT NULL,
  data_aula         DATE NOT NULL,
  status_frequencia CHAR(1) NOT NULL,

  CONSTRAINT fk_freq_aluno
    FOREIGN KEY (id_aluno)
    REFERENCES alunos (id_aluno)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_freq_disciplina
    FOREIGN KEY (id_disciplina)
    REFERENCES disciplinas (id_disciplina)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_freq_professor
    FOREIGN KEY (id_professor)
    REFERENCES professores (id_professor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_freq_status
    CHECK (status_frequencia IN ('P', 'F')),

  CONSTRAINT ck_freq_data
    CHECK (data_aula <= CURRENT_DATE),

  CONSTRAINT uk_frequencia
    UNIQUE (id_aluno, id_disciplina, data_aula)
);

-- 5.3 TABELA: AVISOS
CREATE TABLE avisos (
  id_aviso        SERIAL PRIMARY KEY,
  id_usuario      INTEGER NOT NULL,
  titulo          VARCHAR(200) NOT NULL,
  conteudo        TEXT NOT NULL,
  data_publicacao DATE NOT NULL DEFAULT CURRENT_DATE,

  CONSTRAINT fk_avisos_usuario
    FOREIGN KEY (id_usuario)
    REFERENCES usuarios (id_usuario)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT ck_avisos_data
    CHECK (data_publicacao <= CURRENT_DATE)
);


-- Fim do script SQL

-- Editado por: Francisco Sávio Sousa da Cunha - Mat. nº 2025013352