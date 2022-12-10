o Projeto consiste em extrações de dados climáticos da cidade de Boston 
API utilizada do site https://www.visualcrossing.com/

o Script Está programado para execuções semanais todas as segundas "schedule_interval='0 0 * * 1'"

Atenção: Verifiquei as tags PATH e altere de acordo com o necessário 

Requisitos:
1. Conta no site:. VisualCrossing URL:. https://www.visualcrossing.com/
    1.1 Crie uma conta
    1.2 Dentro do Usuario copie a chave de acesso (Key)
    1.3 Crie um Arquivo chamado key.txt e faça referência apasta no código linha: 22
2. Python 3.9 ou superior
3. Pip
    3.1 Virtual Env
4. Crie um Virtual Env e acessa ela ->  python3 -m venv venv
    4.1 Pandas      -> pip install pandas
    4.2 Airflow     -> pip install 'apache-airflow==2.3.2' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.2/constraints-3.9.txt"

Após intalação do airflow é necessário a exportar a variável de ambiente chamada AirflowHome
export AIRFLOW_HOME= ~/CAMINHO
Inicie o serviço
airflow standalone

O Usuário padrão: admin
a senha de acesso se encontra em um arquivo chamado standalone_admin_password.txt

Vá até o navegador e digite:
localhost:8080
acesse o airflow com o usuário e senha fornecidos pela instalação