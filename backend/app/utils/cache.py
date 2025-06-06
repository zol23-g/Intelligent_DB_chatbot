# app/utils/cache.py
import redis.asyncio as redis
from app.config import settings
from fastapi import Depends
import json
import logging

logger = logging.getLogger(__name__)

# Redis connection pool
redis_client = None

async def get_redis() -> redis.Redis:
    """Dependency for getting Redis client"""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
    return redis_client

async def get_cache(key: str) -> any:
    """Get cached data by key"""
    try:
        redis = await get_redis()
        value = await redis.get(key)
        return json.loads(value) if value else None
    except Exception as e:
        logger.error(f"Cache get failed for key {key}: {e}")
        return None

async def set_cache(key: str, value: any, ttl: int = 3600) -> bool:
    """Set cached data with TTL (seconds)"""
    try:
        redis = await get_redis()
        await redis.set(
            key, 
            json.dumps(value),
            ex=ttl
        )
        return True
    except Exception as e:
        logger.error(f"Cache set failed for key {key}: {e}")
        return False

async def clear_cache(key: str) -> bool:
    """Clear cached data by key"""
    try:
        redis = await get_redis()
        await redis.delete(key)
        return True
    except Exception as e:
        logger.error(f"Cache clear failed for key {key}: {e}")
        return False