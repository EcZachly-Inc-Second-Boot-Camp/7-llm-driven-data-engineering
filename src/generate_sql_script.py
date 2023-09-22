import openai
import os
from util import get_api_key
openai.api_key = get_api_key()

schema_files = os.listdir('schemas')

all_schemas = {}

for file in schema_files:
    opened_file = open('schemas/' + file, 'r')
    all_schemas[file] = opened_file.read()

system_prompt = """You are a data engineer looking to create a slowly-changing dimension table query"""

user_prompt = f"""Using cumulative table input schema {all_schemas['players.sql']}
                    and expected output schema {all_schemas['players_scd_table.sql']} 
                    generate a query to do a slowly-changing dimension 
                    transformation tracking changes on the dimensions is_active and scoring_class, 
                    use markdown and SQL for the transformation
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
print(response)
answer = response.choices[0].message.content


if not os.path.exists('output'):
    os.mkdir('output')

# ```sql
# SELECT * FROM table
# ```

output = filter(lambda x: x.startswith('sql'), answer.split('```'))
# Open the file with write permissions
with open('output/player_scd_generation.sql', 'w') as file:
    # Write some data to the file
    file.write('\n'.join(output))


