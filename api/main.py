import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import status, mode
from api.routes import actions, context

from core.config import settings
from core.errors import handle_exception  # ✅ NEW

logger = logging.getLogger(__name__)

app = FastAPI(title="Execra API", version="0.1.0", description="Execra backend API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Startup event
@app.on_event("startup")
async def startup_event():
    try:
        logger.info("Execra API starting...")
    except Exception as e:
        handle_exception(e)


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    try:
        logger.info("Execra API shutting down...")
    except Exception as e:
        handle_exception(e)


# Root endpoint
@app.get("/")
def read_root():
    try:
        return {
            "status": "success",
            "data": {
                "message": "Execra is running",
                "version": "0.1.0"
            }
        }
    except Exception as e:
        return handle_exception(e)


# Routes (wrapped safely)

try:
    app.include_router(status.router, prefix="/api/v1")
    app.include_router(mode.router, prefix="/api/v1")
    app.include_router(actions.router, prefix="/api/v1")
    app.include_router(context.router, prefix="/api/v1")

except Exception as e:
    handle_exception(e)


# from api.routes import users
# app.include_router(users.router)