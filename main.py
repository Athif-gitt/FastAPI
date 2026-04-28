from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello FastAPI"}

@app.get('/sayhello')
def sayhello():
    return{"message": "Helllloooo!"}

@app.get("/users")
def get_users():
    return ["Athif", "John"]