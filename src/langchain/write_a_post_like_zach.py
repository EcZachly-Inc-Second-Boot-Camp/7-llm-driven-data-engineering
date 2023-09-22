from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import re
import csv


with open('data/zachs_posts.csv') as f:
    reader = csv.DictReader(f)
    topic = 'data'
    all_lines = ""
    for line in reader:
        if topic.lower() in line['ShareCommentary'].lower():
            all_lines += (' ' + re.sub(r'[^a-zA-Z0-9 ]', '', line['ShareCommentary']))
    llm = OpenAI(temperature=0, model_name='gpt-4')
    template = """
            Here are all of Zach Wilson's LinkedIn posts {lines}: 
            Write a new LinkedIn post about {{topic}} in Zach Wilson's voice"""\
    .format(lines=all_lines)
    prompt = PromptTemplate(
        input_variables=["topic"],
        template=template,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    print(chain.run(topic=topic))
