from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message":"Good Evening Rajeev"}

@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status":"healthy"}