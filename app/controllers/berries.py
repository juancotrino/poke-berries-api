from fastapi import APIRouter, status

from fastapi_cache.decorator import cache

from app.services.berries import BerriesService
from app.schemas.berries import BerriesStats


TAG = 'Berries'
PREFIX = 'berries'

# Initialize AdminUser router
router = APIRouter(
    prefix='/' + PREFIX,
    tags=[TAG],
    responses={
        status.HTTP_404_NOT_FOUND: {
            'message': 'Nothing to see here'
        }
    }
)

# Endpoint to return a list of all admin users
@router.get(
    '/allBerryStats',
    response_model=BerriesStats,
    tags=[TAG]
)
@cache(namespace="berries", expire=120)
async def calculate_berries_stats():
    return await BerriesService.get_stats()
