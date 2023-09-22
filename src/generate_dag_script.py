import openai
import os
from util import get_api_key
openai.api_key = get_api_key()

schema_files = os.listdir('schemas')

all_schemas = {}

for file in schema_files:
    opened_file = open('schemas/' + file, 'r')
    all_schemas[file] = opened_file.read()

system_prompt = """
            You are a data engineer looking to generate an Airflow pipeline DAG skeleton 
            without the SQL details
            """

user_prompt = f"""
                Generate a cumulative Airflow DAG that transforms 
                {all_schemas['player_seasons.sql']}
                into {all_schemas['players.sql']}
                use markdown for output and Postgres for queries
                The DAG depends on last season data from players table 
                and the DAG depends on past is true
                Make sure each run scans only one season and does a 
                FULL OUTER JOIN with the previous seasons data
                Use the {{ ds }} airflow parameter to filter season 
                All create table statements should include IF NOT EXISTS
            """

print(system_prompt)
print(user_prompt)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0
)
answer = response.choices[0].message.content

if not os.path.exists('output'):
    os.mkdir('output')

output = filter(lambda x: x.startswith('python'), answer.split('```'))
# Open the file with write permissions
with open('output/airflow_dag.py', 'w') as file:
    # Write some data to the file
    file.write('\n'.join(output))


