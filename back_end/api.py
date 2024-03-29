from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
from webscrapping import Model

web_model = {}

# 0 ***************************************************************************************************************************

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Cargando el modelo de web scrapping") 
    yield 
    print("Terminando la aplicación de web scrapping")

# creating the API
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to the WEB SCRAPPING project API"}

# 1 ***************************************************************************************************************************

model_router = APIRouter(prefix="/model")

@model_router.get("/hi")
async def hi_model():
    return {"message": "Hi from the model router"}

class WebModel(BaseModel):
    website_url: str
        
@model_router.post("/predict")
async def predict(request: Request, data: WebModel):
    web_model = Model()
    if web_model is None:
        return JSONResponse(status_code=404, content={"message": "Model not found"})
    prediction = web_model.predict(data.website_url)
    return JSONResponse(content={"La url ingresada es": data.website_url,
                                 "La categoria de la url es": prediction})

app.include_router(model_router)


