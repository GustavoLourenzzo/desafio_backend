## Sobre a Crédito Express

A Crédito Express é uma fintech voltada para servir instituições financeiras. Nosso objetivo é levar TAXAS ATRATIVAS para as pessoas, a partir do uso de tecnologia de ponta.

VENHA FAZER PARTE DESSA REVOLUÇÃO FINANCEIRA!


## Instruções para a execução do Projeto

1. Execute o arquivo 'docker-compose.yml' na raiz do projeto.

2. Execute o comando seed para inserir os dados iniciais:
	2.1. Execute em um terminal "docker exec -t -i python_api_geral /bin/bash", este comando ira instanciar o console do container;
	2.2. No console do container execute "flask seed run".

3. Com isso o projeto esta pronto para uso.

## Instruções de uso do Projeto

* Portas e hosts utilizadas no projeto:
	1. frontend_apache :: host = 'SEU_HOST'|localhost , porta = 80 
	2. python_api_geral :: host = 'SEU_HOST'|localhost , porta = 5000
	3. python_api_identificacao :: host = 'SEU_HOST'|localhost , porta = 5010
	4. python_api_simulacao :: host = 'SEU_HOST'|localhost , porta = 5020
	5. banco_mongo :: porta = 27017
	 

* As rotas 'SEU_HOST:PORTA/' das 3 API's contem uma descrição dos parâmetros e retornos de cada método ativo;

* Caso o projeto seja executado em um ip diferente do endereço local (por exemplo em uma maquina virtual box ou afins), entrar no arquivo /front/index.html e modificar a variavel host para o novo endereço, mantendo a porta 5000.
