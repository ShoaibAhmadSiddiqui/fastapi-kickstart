from logging import Logger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import CONFIG
from routes import router


origins = [CONFIG.FRONTEND.FRONTEND_BASE_URL]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

logger = Logger("api")


@app.get("/")
async def root_hello():
    logger.info("Hello from root")
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    print("Starting the app")

    uvicorn.run(app, host=CONFIG.UVICORN.HOST, port=CONFIG.UVICORN.PORT)
