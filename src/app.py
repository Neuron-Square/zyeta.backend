"""
This module contains the main application setup.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.__base.manager import Manager


@asynccontextmanager
async def lifespan(app: FastAPI):
  # Startup
  yield
  # Shutdown


app = FastAPI(lifespan=lifespan)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Allow specific origins
  allow_credentials=True,
  allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
  allow_headers=["*"],  # Allow all headers
)


manager = Manager(app)
manager.register_middlewares()
manager.register_services()
