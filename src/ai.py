from groq import Groq
from pydantic import BaseModel
from py_dotenv import read_dotenv
import os, sys

read_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

def prompt(prompt: str, model: str, documents: any) -> BaseModel:
    client = Groq()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""You are a helpful tutor, aiming to help people get better with their academic scores.
                                Your objective is to generate practice questions when asked, questions that involve calculating something, or explaining terms.
                                Use terms that are used in the document provided.
                                If the subject seems like it is math, physics or chemistry, only give questions that adhere to math (i.e. calculating something, tricky questions).
                                If the subject seems english, only give questions that adhere to english. (i.e. answering what a term means, finishing part of a story).
                                Lastly, only give questions from the document, if absolutely needed, make up questions only with information from the document
                                Here is the content of the document: {documents}"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=model
    )
    
    return chat_completion

# if __name__ == "__main__":
#     print(prompt(sys.argv[1], sys.argv[2]).choices[0].message.content)