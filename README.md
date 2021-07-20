`eval-rabbitmq-py/README.md` - Evaluation RabbitMQ with Python

## 1. Introdução

Este repositório contém os artefatos do projeto **eval-rabbitmq-py** que consiste em uma avaliação dos mecanismos básicos da ferramenta de messaging RabbitMQ utilizando linguagem de programação Python.

* Tabela de Conteúdo
  * Introdução
  * Documentação
    * Diagrama de Caso de Uso (Use Case Diagram)
    * Diagrama de Implantação (Deploy Diagram)
  * Projeto
    * Pré-Requisitos, Pré-Condições e Premissas
    * Guia do Desenvolvedor e Administrador
    * Guia de Implantação, Configuração e Instalação
    * Guia de Execução, Demonstração e Cenários de Teste
	* Guia de Estudo
    * Design Patterns, Standard, Conventions and Best Practices
  * I - Referências


## 2. Documentação

### 2.1. Diagrama de Caso de Uso (Use Case Diagram)

![UseCaseDiagram-Context.png](./doc/uml-diagrams/UseCaseDiagram-Context.png) 


### 2.2. Diagrama de Implantação (Deploy Diagram)

![DeployDiagram-Context.png](./doc/uml-diagrams/DeployDiagram-Context.png) 


## 3. Projeto

### 3.1. Pré-Requisitos, Pré-Condições e Premissas

#### a. Tecnologias e ferramentas

* Python 3.8
* Venv
* Docker or Kubernetes or VirtualBox or On-Premisse infrastructure (Deployment Infraestructure)


#### b. Ferramental de apoio

* Ferramenta: [Draw.IO](https://app.diagrams.net/) (only for diagrams design and documentation)


### 3.2. Guia do Desenvolvedor e Administrador

* Faça um clone do projeto `git clone`. Use o _branch_ `master` se o _branch_ `develop` não estiver disponível
* Leia as documentações disponíves em "2. Documentação"  and "3.x. Design Patterns, Standard, Conventions and Best Practices"


### 3.3. Guia de Implantação, Configuração e Instalação

#### a. RabbitMQ

* Run Docker container for RabbitMQ

```cmd
C:\..\eval-rabbitmq> 
docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:3-management
```

* Login RabbitMQ
  * url: `http://localhost:8080`
  * username: `user`
  * password: `password`

![screenshot-01-rabbitmq-login.png](./doc/images/screenshot-01-rabbitmq-login.png) 

* Expected dashboard painel

![screenshot-02-rabbitmq-dashboard-painel.png](./doc/images/screenshot-02-rabbitmq-dashboard-painel.png) 

* Add a new queue - name: `queue-eval`, durability: `Durable`, auto-delete: `No`

![screenshot-03-rabbitmq-new-queue.png](./doc/images/screenshot-03-rabbitmq-new-queue.png) 


### 3.4. Guia de Demonstração e Teste

* n/a


### 3.5. Guia de Estudo

* n/a


## I - Referências

* https://hub.docker.com/_/rabbitmq
* Github README.md writing sintax
  * [Basic Github Markdown Writing Format](https://docs.github.com/pt/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax)  
  * [Github Markdown Chead Sheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
  * [Github Mastering Markdown](https://guides.github.com/features/mastering-markdown/#what)
