from fastapi import FastAPI
import logging

from core.engine import CoreEngine
from core.logging import setup_logging
from config.settings import PROJECT_NAME

logger = setup_logging()

app = FastAPI(title=PROJECT_NAME)

engine = CoreEngine()

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    await engine.start()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")
    await engine.halt()

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "engine_state": engine.state,
    }
