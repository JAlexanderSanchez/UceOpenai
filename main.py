import uvicorn
from fastapi import FastAPI
from uce.ai.openai import Document, process_inference

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/inference", status_code=200)
def inference(doc: Document):
    response = process_inference(doc.item)
    return {
        'Respuesta': response[0],
        'El numero de tokens consumidos es: ': response[1]
    }


#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=9015)

