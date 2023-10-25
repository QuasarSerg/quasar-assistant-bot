from fastapi import FastAPI

import g4f

app = FastAPI()


@app.get("/")
async def root():
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": "What is the holiday in Russia today?"}],
    )

    return {"message": response}


if __name__ == '__main__':
    pass

