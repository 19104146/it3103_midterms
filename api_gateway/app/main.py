import redis.asyncio as redis
from fastapi import Depends, FastAPI
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from app.config import config
from app.routers.admin import router as admin_router
from app.routers.protected import router as protected_router
from app.routers.public import router as public_router

app = FastAPI(title=config.APP_NAME, version=config.APP_VERSION)

global_rate_limiter = RateLimiter(times=10, seconds=60)


@app.on_event("startup")
async def startup():
    redis_url = config.REDIS_URL
    redis_client = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(redis_client)


app.include_router(public_router, dependencies=[Depends(global_rate_limiter)])
app.include_router(protected_router, dependencies=[Depends(global_rate_limiter)])
app.include_router(admin_router, dependencies=[Depends(global_rate_limiter)])
