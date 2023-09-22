# LLM-driven Data Engineering

## Getting Started

Make an OpenAI account [here](https://platform.openai.com/) and then generate an API Key.

- You will need to supply a credit card but you will also get $5 in free credit which is more than enough for this lab and tomorrow's lab.

The live Zoom classes will be held here:
- [Day 1 (LLM-driven data engineering)](https://us06web.zoom.us/meeting/register/tZ0pcuqppjopHNFyy-G52Hh2jKdRlePT66oe#/registration)
  - Lecture Video is [here](https://www.dataengineer.io/course/large-language-models-day-1-lecture)
  - Lab video is [here](https://www.dataengineer.io/course/large-language-models-day-1-lab)
- [Day 2 (LLM dev with LangChain)](https://us06web.zoom.us/meeting/register/tZYude6grj8pEt23y6J1rhHcXL2ytMX8IRzy#/registration)


## Setup

Store the API key as an environment variable like:
`export OPENAI_API_KEY=<your_api_key>`
Or set it in Windows

Run the command `pip install -r requirements.txt` to get the OpenAI and Pandas libraries

## Day 1 Lab

We'll be using the schemas from Dimensional Data Modeling Week 1 and generating the queries from the homework and labs except this time we'll do it via LLMs


## Day 2 Lab

We'll be using Langchain to auto generate SQL queries for us based on tables and writing LinkedIn posts in Zach Wilson's voice
### Setup

If you are watching live, you will be given a cloud database URL to use.
`export LANGCHAIN_DATABASE_URL=<value zach gives in Zoom>`

If you aren't watching live, you'll need to use the `halo_data_dump.dump` file located in the `data` folder

Running `pg_restore` with your local database should get you up and running pretty quickly. 

- example command, assuming you got Postgres up and running either via Homebrew or Docker:
 - `pg_restore -h localhost -p 5432  -d postgres -U <your laptop username> halo_data_dump.dump`