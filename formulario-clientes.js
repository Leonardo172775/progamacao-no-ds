<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Clientes com SQLite em JS</title>

  <!-- Importa a biblioteca sql.js, que permite usar SQLite diretamente no navegador -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.6.2/sql-wasm.js"></script>
</head>
<body>
  <!-- Seção para buscar cliente -->
  <h2>Buscar Cliente</h2>
  <input type="number" id="idBuscar" placeholder="ID do cliente">
  <button onclick="buscarCliente()">Buscar</button>
  <div id="resultado"></div>

  <!-- Seção para excluir cliente -->
  <h2>Excluir Cliente</h2>
  <input type="number" id="idExcluir" placeholder="ID do cliente">
  <button onclick="excluirCliente()">Excluir</button>
  <div id="exclusao"></div>

  <script>
    let db; // Variável que vai armazenar o banco de dados em memória

    // Inicializa a biblioteca SQL.js e cria o banco de dados
    initSqlJs({
      locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.6.2/${file}`
    }).then(SQL => {
      // Cria uma instância do banco de dados SQLite em memória
      db = new SQL.Database();

      // Cria a tabela "Clientes" com colunas Id, Nome e Email
      db.run(`CREATE TABLE Clientes (
        Id INTEGER PRIMARY KEY,
        Nome TEXT,
        Email TEXT
      );`);

      // Insere um cliente de exemplo na tabela
      db.run(`INSERT INTO Clientes (Id, Nome, Email)
              VALUES (1, 'Ana', 'ana@email.com');`);
    });

    // Função para buscar cliente pelo ID
    function buscarCliente() {
      // Pega o valor digitado no campo de busca
      const id = document.getElementById('idBuscar').value;

      // Prepara a consulta SQL com parâmetro (?)
      const stmt = db.prepare("SELECT * FROM Clientes WHERE Id = ?");
      stmt.bind([id]); // Substitui o ? pelo valor digitado

      let result = '';

      // Executa a consulta e percorre os resultados
      while (stmt.step()) {
        const row = stmt.getAsObject(); // Converte a linha em objeto JS
        result = `Nome: ${row.Nome}, Email: ${row.Email}`; // Monta o texto de resultado
      }

      stmt.free(); // Libera os recursos da consulta

      // Exibe o resultado ou mensagem de "não encontrado"
      document.getElementById('resultado').innerText =
        result || 'Cliente não encontrado.';
    }

    // Função para excluir cliente pelo ID
    function excluirCliente() {
      // Pega o valor digitado no campo de exclusão
      const id = document.getElementById('idExcluir').value;

      // Executa o comando SQL para excluir o cliente
      db.run("DELETE FROM Clientes WHERE Id = ?", [id]);

      // Exibe mensagem de sucesso
      document.getElementById('exclusao').innerText =
        'Cliente excluído com sucesso!';
    }
  </script>
</body>
</html>

