from fastapi import FastAPI
# import g4f

from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()


@app.get("/")
async def root():
    # response = g4f.ChatCompletion.create(
    #     model=g4f.models.gpt_4,
    #     messages=[{"role": "user", "content": "What is the holiday in Russia today?"}],
    # )
    response = os.getenv('TELEGRAM_BOT_API_TOKEN')

    return {"message": response}


if __name__ == '__main__':
    pass
