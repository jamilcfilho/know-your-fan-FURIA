
# Desafio 2: Know Your Fan

Projeto em desenvolvimento com foco na criação de uma solução para validação e coleta de dados de fãs de e-sports. 
O sistema simula um ambiente de cadastro e verificação de identidade através de documentos enviado via PDF, com funcionalidades de upload de documentos, além de uma interface para visualização dos dados registrados.


## 🔎 Descrição

O projeto é um sistema criado para simular um processo de coleta e validação de dados de fãs de e-sports.
A proposta do projeto é oferecer uma base para futuras integrações com bancos de dados, inteligência artificial e autenticação de perfis em plataformas do cenário competitivo. 
Atualmente, os dados são armazenados em memória (sem uso de banco de dados) e podem ser visualizados diretamente na interface.


## ✅ Funcionalidades

- Formulário de cadastro com os seguintes campos:
  - Nome completo
  - Endereço
  - CPF
  - E-mail
  - Interesses em e-sports (campo de texto livre)
  - Eventos de e-sports que participou recentemente (campo de texto livre)
  - Compras recentes relacionadas a e-sports (campo de texto livre)
  - Links de redes sociais e perfis em sites do cenário competitivo (validação básica se o link forneceido possui http:// ou https://)
  - Upload de documento em formato PDF (validação se o arquivo não for PDF ele não aceita)

- Página de visualização dos cadastros realizados


## 💻 Tecnologias utilizadas

- Python 3.12.2
- Flask
- HTML5 + CSS3 (inline nos templates)



## ⚙️ Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/know-your-fan.git
cd know-your-fan
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python app.py
```

5. Acesse no navegador:

```
http://localhost:5000
```


## 🧪 Desenvolvimento

Este projeto está em fase inicial, com foco em prototipação. Futuras melhorias planejadas incluem:

- Validação de CPF e e-mail com expressões regulares
- Leitura e verificação inteligente dos documentos PDF
- Integração com banco de dados (SQLite ou PostgreSQL)
- Validação mais robusta de URLs e perfis sociais
- Autenticação de usuários
- Introduzir mais IAs para realizar a validação dos itens e ainda utilizar machine learning para criar uma direção de qual perfil de fãs a FURIA possui


## 🧠 Contribuições e feedbacks

Sugestões, críticas e melhorias são sempre bem-vindas em um projeto dessa magnituded. 
Fique à vontade para abrir uma *issue* ou enviar um *pull request*.