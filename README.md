# 🔐 Sistema de Login com Flask e SQLite

## 📌 Sobre o Projeto

Este é um sistema de login simples, desenvolvido com **Flask** e **SQLite**, projetado para ser um ponto de partida para aplicações web que precisam de autenticação de usuários. Ele permite cadastrar usuários, armazenar senhas de forma segura com **hash SHA-256**, e gerenciar o banco de dados de maneira intuitiva.

## 🚀 Funcionalidades

- Cadastro de usuários com **armazenamento seguro da senha** (SHA-256).
- Login básico com redirecionamento para uma página protegida.
- Gerenciamento de banco de dados SQLite via `db.py`.
- Testes e manipulação do banco via `teste_db.py`.

## 📂 Estrutura do Projeto

```
login/
│
├── static/                # Arquivos estáticos (CSS, JS, imagens)
│
├── templates/             # Arquivos HTML
│   ├── login.html         # Página de login
│   ├── home.html          # Página principal pós-login
│
├── database.db            # Banco de dados SQLite
│
├── db.py                  # Módulo de gerenciamento do banco de dados
│
├── main.py                # Arquivo principal que roda o Flask
│
├── routes.py              # Rotas da aplicação
│
├── teste_db.py            # Script para testar funcionalidades do banco
│
└── README.md              # Documentação do projeto
```

## 🛠️ Configuração e Execução

### 1️⃣ **Pré-requisitos**

Antes de rodar o projeto, certifique-se de ter o **Python** instalado.

Instale as dependências necessárias:

```bash
pip install flask
```

### 2️⃣ **Rodando o sistema**

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Acesse no navegador:

```
http://127.0.0.1:5000/
```

### 3️⃣ **Testando o banco de dados**

O arquivo `teste_db.py` pode ser usado para manipular usuários e testar operações no banco. Para rodá-lo:

```bash
python teste_db.py
```

## 🔐 Segurança

- Senhas armazenadas usando **hash SHA-256** para maior segurança.
- Banco de dados SQLite leve e fácil de gerenciar.

## 📌 Melhorias Futuras

- Implementar autenticação com sessão.
- Criar um sistema de permissões de usuário.
- Melhorar a interface com CSS/JS.

## 🤝 Contribuição

Este projeto é um ponto de partida. Se quiser contribuir, sinta-se à vontade para abrir **pull requests** ou relatar problemas.

---

📌 **Autor**: José Paz
