import os


# Gets the API key from the environment
def get_api_key():
    API_KEY = os.environ.get("OPENAI_API_KEY")
    if API_KEY is None:
        raise ValueError("You need to specify OPENAI_API_KEY environment variable!")
    return API_KEY