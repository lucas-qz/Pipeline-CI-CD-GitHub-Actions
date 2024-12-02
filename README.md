# <img align="left" alt="GitHub Actions" height="30" width="60" src="https://www.mabl.com/hs-fs/hubfs/CICDBlog.png?width=536&name=CICDBlog.png"> Criar Pipeline CI/CD com GitHub Actions



## 🗺️ Objetivo do Projeto:
- Criaremos um Pipeline CI/CD com GitHub Actions
- O objetivo é automatizar o processo de desenvolvimento, testes e implantação do nosso software
- Toda vez que fizermos um push para o repositório, o GitHub Actions executará o pipeline rodando os testes e fazendo o deploy da aplicação para a AWS
- Nossa aplicação é uma página simples de galeria de fotos para exemplificar a implantação de um Pipeline CI/CD com GitHub Actions

## 📊 O que o WorkFlow CI faz:
  - roda os testes do 'pytest' (se os testes falharem você é notificado por e-mail)
  - roda os testes do 'pytest-cov' e cria um txt com o resultado dos testes
  - esse arquivo txt é exportado para a area de 'Artefactos' do GitHub Actions (você consegue ver detalhes sobre os testes)
  - roda a analise de codigo com 'flake8' para verificar conformidade do codigo com a convensão python PEP8 (verifica boas práticas)
  - formata os arquivos html,css,js,json com a ferramenta 'Prettier' (garante que o codigo está com uma formatação padrão)
  - formata os arquivos .py com a ferramenta 'Black' (garante que o codigo está com uma formatação padrão)
  - Ao fazer commit a ferramenta 'pre-commit' roda 'Prettier' e 'Black' (garante que o codigo chegue no GitHub já formatado)

## 📐 O que o WorkFlow CD faz:
  - faz login no Docker Hub (login e senha ficam salvos no SECRETY do GitHub Actions)
  - faz build da imagem
  - faz deploy da imagem para o Docker Hub
  - só segue para os próximos passos se os passos acima não falharem
  - se conecta na instancia EC2 da AWS
  - cria o container da imagem na instancia EC2
  - toda vez que enviamos a aplicação para o GitHub esse pipeline é disparado atualizando a aplicação na instancia EC2
<br><br>

## 🗂️ 1 - Criando o Pipeline CI
- Dentro do seu repositório, crie o seguinte caminho:
```ShellSession
.github/workflows/ci.yml
```
Esse arquivo contem as configurações para o GitHub Actions executar os testes da aplicação
<br><br>

## 🗂️ 2 - Criando o Pipeline CD
- Dentro do seu repositório, crie o seguinte caminho:
```ShellSession
.github/workflows/cd.yml
```
Esse arquivo contem as configurações para o GitHub Actions rodar o deploy da aplicação
<br><br>

## 🛠️ Construído com
* [GitHub Actions]() - ferramenta de automação oferecida pela plataforma GitHub, que permite aos desenvolvedores criar workflows automatizados para CI/CD
* [AWS]() - plataforma de serviços de computação em nuvem oferecida pela Amazon
<br><br>

## 👨🏼 Autor - Lucas Queiróz
<div align="left"> 
<a  href="https://github.com/lucas-qz" target="_blank"><img align="left" alt="GitHub" height="30" width="30" src="https://cdn.worldvectorlogo.com/logos/github-icon-2.svg"> GitHub - Lucas Queiróz </a><br/><br/>
<a  href="https://www.linkedin.com/in/lucas-qz/" target="_blank"><img align="left" alt="Linkedin" height="30" width="30" src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"> Linkedin - Lucas Queiróz </a><br/><br/>
<a  href="http://lucasqz.com.br" target="_blank"><img align="left" alt="Portfólio" height="30" width="30" src="https://cdn-icons-png.flaticon.com/512/5602/5602732.png"> Portfólio - Lucas Queiróz </a><br/><br/>
</div>
<br/><br/>



