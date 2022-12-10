from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
import pendulum
from os.path import join
import pandas as pd

with DAG(
        "dados_climaticos",
        start_date=pendulum.datetime(2022, 10, 22, tz="UTC"),
        schedule_interval='0 0 * * 1', # Minuto e hora | Dia do mẽs e mẽs | Dia da semana
) as dag:
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        #PATH
        bash_command = 'mkdir -p "/home/mayron/Workstation/Airflow/VisualCrossing/Extraction/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'
    )
    
    def extrai_dados(data_interval_end):
        def ler_chave(): #PATH
            arquivo = open('/home/mayron/Workstation/Airflow/VisualCrossing/key.txt','r')
            key = arquivo.read()
            arquivo.close()
            return key

        city = 'Boston'
        key = ler_chave()

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                    f'{city}/{data_interval_end}/{ds_add(data_interval_end,7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)
        #PATH
        file_path = f'/home/mayron/Workstation/Airflow/VisualCrossing/Extraction/semana={data_interval_end}/'

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )
    
    tarefa_1 >> tarefa_2