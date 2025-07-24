import pytest
from app.utils import metrics


def test_increment_usage():
    chain_name = "test_chain"

    metrics.usage_counter.clear()
    
    metrics.increment_usage(chain_name)
    metrics.increment_usage(chain_name)

    result = metrics.get_metrics()
    assert result["usage"][chain_name]==2

def test_track_latency():
    chain_name = "test_chain_latency"

    metrics.latency_total.clear()
    metrics.latency_count.clear()

    metrics.track_latency(chain_name, 1.5)
    metrics.track_latency(chain_name, 0.5)

    result = metrics.get_metrics()

    assert result['latency_avg'][chain_name] == 1.0


def test_get_metrics_empty():
    metrics.latency_total.clear()
    metrics.usage_counter.clear()
    metrics.latency_count.clear()

    result = metrics.get_metrics()

    assert result['usage'] == {}
    assert result["latency_avg"] == {}
