import uvicorn  #servidor web
import os

if __name__ == "__main__":
    uvicorn.run(
        "api:app", 
        host="0.0.0.0", 
        reload=True, 
        port=int(os.environ.get("PORT", 8070)) 
    )