from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/home/{id}")
def home_page(id: int):
    return {"message": f"welcome home, {id}"}

stu =[]

@app.put("/home/putin/{id}")
def update(id:int):
    stu.append(id)
    return {"message":stu}
