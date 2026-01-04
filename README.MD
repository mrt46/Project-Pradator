================================================
PROJECT PREDATOR – FAZ 1
CORE ENGINE SKELETON
REPO STRUCTURE + FIRST COMMIT
================================================

AMAÇ:
FAZ 1 kapsamında sistemin:
- Ayağa kalktığını
- Çökmediğini
- Deterministik davrandığını
kanıtlayan MINIMAL bir çekirdek oluşturmak.

Bu fazda:
- Trade YOK
- AI YOK
- Binance YOK
- Redis YOK

================================================
1. REPOYA EKLENECEK DİZİN YAPISI
================================================

(Mevcut .md dosyalarına DOKUNMA)

Project-Predator/
│
├── backend/
│   ├── main.py                # FastAPI entrypoint
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── engine.py          # Core engine state machine
│   │   └── logging.py         # Central logging config
│   │
│   └── config/
│       ├── __init__.py
│       └── settings.py        # Env & basic settings
│
├── docker/
│   └── Dockerfile             # Minimal backend container
│
├── docker-compose.yml         # Single service, nothing else
│
└── README.md                  # (İstersen FAZ 1 notu eklenir)

================================================
2. FAZ 1 – KOD İÇERİĞİ
================================================

------------------------------------------------
backend/core/logging.py
------------------------------------------------

import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    return logging.getLogger("predator-core")


------------------------------------------------
backend/core/engine.py
------------------------------------------------

import asyncio
from enum import Enum
import logging

logger = logging.getLogger("predator-core.engine")

class EngineState(str, Enum):
    INIT = "INIT"
    IDLE = "IDLE"
    RUNNING = "RUNNING"
    HALTED = "HALTED"

class CoreEngine:
    def __init__(self):
        self.state = EngineState.INIT
        self._running = False

    async def start(self):
        logger.info("CoreEngine starting")
        self.state = EngineState.IDLE
        self._running = True
        asyncio.create_task(self._heartbeat())

    async def _heartbeat(self):
        while self._running:
            logger.info(f"Heartbeat | state={self.state}")
            await asyncio.sleep(5)

    async def halt(self):
        logger.warning("CoreEngine halting")
        self.state = EngineState.HALTED
        self._running = False


------------------------------------------------
backend/config/settings.py
------------------------------------------------

import os

PROJECT_NAME = os.getenv("PROJECT_NAME", "PROJECT PREDATOR")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


------------------------------------------------
backend/main.py
------------------------------------------------

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


------------------------------------------------
docker/Dockerfile
------------------------------------------------

FROM python:3.11-slim

WORKDIR /app

COPY backend /app/backend

RUN pip install fastapi uvicorn

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]


------------------------------------------------
docker-compose.yml
------------------------------------------------

version: "3.9"

services:
  predator-backend:
    build:
      context: .
      dockerfile: docker/Dockerfile
    ports:
      - "8000:8000"
    restart: always


================================================
3. FAZ 1 DOĞRULAMA CHECKLIST
================================================

[ ] docker-compose up --build çalışıyor  
[ ] /health endpoint cevap veriyor  
[ ] Loglarda heartbeat görünüyor  
[ ] CTRL+C veya container stop sonrası düzgün kapanıyor  
[ ] Hiçbir trade / veri / ajan çalışmıyor  

Bu maddeler geçilmeden FAZ 2 YASAK.

================================================
4. İLK COMMIT MESAJI (AYNEN KULLAN)
================================================

feat(phase1): add core engine skeleton and deterministic heartbeat

- FastAPI application bootstrapped
- CoreEngine state machine introduced
- Deterministic heartbeat loop added
- Graceful startup and shutdown implemented
- No trading, no agents, no external integrations

Phase: FAZ 1 – Core Engine Skeleton

================================================
5. OPERASYON TALİMATI (iPad + Server)
================================================

1. Kodları repo’ya ekle
2. Commit + push
3. Server’da:
   git pull
   docker-compose up --build -d
4. iPad’den:
   - /health kontrol
   - log izle
5. Gunluk.md’ye FAZ 1 başlangıç kaydı ekle

================================================
SON NOT (BAĞLAYICI)
================================================

Bu FAZ 1 kodu:
- Sıkıcıdır
- Para kazandırmaz
- Ama sistemin omurgasıdır

Burada acele edilirse,
ileride her şey iki kat yavaşlar.

================================================
END OF FAZ 1 PREPARATION
================================================
