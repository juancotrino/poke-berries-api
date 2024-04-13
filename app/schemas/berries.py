from pydantic import BaseModel

class BerriesStats(BaseModel):
    berries_names: list[str]
    min_growth_time: int
    median_growth_time: float
    max_growth_time: int
    variance_growth_time: float
    mean_growth_time: float
    frequency_growth_time: dict[int, int]
