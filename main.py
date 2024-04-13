import os
from contextlib import asynccontextmanager

import uvicorn

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from dotenv import load_dotenv

from docs import info
from app.controllers import berries

load_dotenv()

# Instantiate redis at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(os.getenv("REDIS_HOST"))
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

# Initialize API
app = FastAPI(
    title=info['title'],
    description=info['description'],
    version=info['version'],
    contact=info['contact'],
    openapi_tags=info['tags_metadata'],
    swagger_ui_parameters={
        "useUnsafeMarkdown": True
    },
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan
)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Change /docs favicon
@app.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=info['title'],
        swagger_favicon_url="/static/images/logo-app.png"
    )

# Change /redoc favicon
@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(
        openapi_url="/openapi.json",
        title=info['title'],
        redoc_favicon_url="/static/images/logo-app.png"
    )

# Add berries router
app.include_router(berries.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
