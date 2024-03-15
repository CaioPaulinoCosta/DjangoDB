# 📜 README

Este repositório contém um exercício prático de programação em Python, no qual foi utilizado o framework Django para criar um sistema de cadastro de clientes.

## Descrição do Código

### Arquivos HTML na pasta "templates"

- **register.html**: Contém um formulário para preenchimento dos dados do cliente.
- **users.html**: Apresenta uma tabela mostrando todos os usuários já cadastrados.

### `views.py`

- **index**: Função que renderiza a página principal, mostrando todos os clientes cadastrados.
- **register_page**: Função que renderiza a página de cadastro de novos clientes.
- **ClienteForm**: Função que processa o formulário de cadastro de clientes e exibe a lista atualizada de clientes.

### `models.py`

Define o modelo de dados para o cliente, incluindo campos como nome, idade, e-mail, telefone e endereço.

### `urls.py`

Gerencia as rotas da aplicação, associando cada URL a uma view específica.

### `settings.py`

Configurações gerais do projeto, como permissões de hosts permitidos.

## Como Executar

1. Certifique-se de ter o Python e o Django instalados em sua máquina.
2. Clone este repositório em seu ambiente de desenvolvimento.
3. Abra um terminal na raiz do projeto.
4. Execute o comando `python manage.py runserver` para iniciar o servidor de desenvolvimento do Django.
5. Acesse o sistema em seu navegador através do endereço fornecido pelo servidor.

## Observações

- **csrf_exempt**: Foi utilizada a decoradora `csrf_exempt` para lidar com questões de segurança CSRF ao lidar com formulários.
- **Calcular Idade**: Implementou-se uma função para calcular a idade com base na data de nascimento fornecida.

Este projeto é parte de um exercício acadêmico e destina-se apenas a fins educacionais.

## Exibição do código em funcionamento
<h3>Register.html</h3>
<img src="https://media.discordapp.net/attachments/1209500402865803355/1218282620241055744/image.png?ex=6607191b&is=65f4a41b&hm=bcec31b16504115997467cc6d861e3268c4ad9f59f663c8e9b2cfbda8b589454&=&format=webp&quality=lossless&width=1296&height=676">
<h3>Users.html</h3>
<img src="https://media.discordapp.net/attachments/1209500402865803355/1218285641578713138/image.png?ex=66071beb&is=65f4a6eb&hm=3103a0b3945943520483ca6a7c271ba0450502b9f1c9ea66bdb96fa15769cbd4&=&format=webp&quality=lossless&width=1303&height=676">
