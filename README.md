# LLM-driven Data Engineering

## Getting Started

Make an OpenAI account [here](https://platform.openai.com/) and then generate an API Key.

- You will need to supply a credit card but you will also get $5 in free credit which is more than enough for this lab and tomorrow's lab.

The live Zoom classes will be held here:
- [Day 1 (LLM-driven data engineering)](https://us06web.zoom.us/meeting/register/tZ0pcuqppjopHNFyy-G52Hh2jKdRlePT66oe#/registration)
- [Day 2 (LLM dev with LangChain)](https://us06web.zoom.us/meeting/register/tZYude6grj8pEt23y6J1rhHcXL2ytMX8IRzy#/registration)

Store the API key as an environment variable like:
`export OPENAI_API_KEY=<your_api_key>`
Or set it in Windows

Run the command `pip install -r requirements.txt` to get the OpenAI and Pandas libraries

## Lab

We'll be using the schemas from Dimensional Data Modeling Week 1 and generating the queries from the homework and labs except this time we'll do it via LLMs