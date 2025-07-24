from collections import defaultdict

# Track how many times each chain is called
usage_counter = defaultdict(int)

# Track total latency for each chain
latency_total = defaultdict(float)
latency_count = defaultdict(int)

def increment_usage(chain_name: str):
    usage_counter[chain_name] += 1

def track_latency(chain_name: str, duration: float):
    latency_total[chain_name] += duration
    latency_count[chain_name] += 1

def get_metrics():
    return {
        "usage": dict(usage_counter),
        "latency_avg": {
            k: latency_total[k] / latency_count[k] if latency_count[k] else 0.0
            for k in latency_total
        }
    }
