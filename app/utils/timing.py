import time
from app.utils.logger import logger
from app.utils.metrics import track_latency, increment_usage

def timing(metric_name: str = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start

            name = metric_name or func.__name__

            # Log with file + func name now handled by logger
            logger.info(f"{name} took {duration:.2f}s")

            # Track latency in metrics
            track_latency(name, duration)
            increment_usage(metric_name)

            return result
        return wrapper
    return decorator