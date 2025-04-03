DROP TABLE demo;

-- Criação da tabela Aluno
CREATE TABLE Aluno (
    id_aluno INT PRIMARY KEY, -- Identificação única do aluno
    nome VARCHAR(50),
    idade INT
);

-- Criação da tabela Professor
CREATE TABLE Professor (
    id_professor INT PRIMARY KEY, -- Identificação única do professor
    nome_professor VARCHAR(50),
    cpf_professor VARCHAR(11) -- CPF do professor com tamanho padrão de 11 caracteres
);

-- Criação da tabela Escola
CREATE TABLE Escola (
    id_escola INT PRIMARY KEY, -- Identificação única da escola
    nome_escola VARCHAR(50),
    cnpj_escola VARCHAR(14) -- CNPJ da escola com tamanho padrão de 14 caracteres
);
SELECT * FROM Aluno;
