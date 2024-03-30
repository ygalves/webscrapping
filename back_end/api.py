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
    web_model['web'] = Model()

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
    query_params = dict(request.query_params)
    model_name = query_params.get("model_name")
    model = web_model.get(model_name, None)
    
    if model is None:
        return JSONResponse(status_code=404, content={"message": "Model not found"})
    title, description, domain, icon, siteimage, prediction = model.predict(data.website_url)
    return JSONResponse(content={"Título": title,
                                 "Descripción": description,
                                 "Url": domain,
                                 "Icon": icon,
                                 "Site_image": siteimage, 
                                 "Categoría": prediction})

app.include_router(model_router)


