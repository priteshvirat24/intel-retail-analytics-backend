import pytest
from app.orchestrator.retry import RetryPolicy
from app.models.failure import SpecificReason


def test_retry_policy_transient_vs_permanent():
    policy = RetryPolicy(max_retries=3)

    # 429 Rate limited -> should retry
    assert policy.should_retry(1, 429, SpecificReason.HTTP_429_RATE_LIMITED) is True

    # 503 Server error -> should retry
    assert policy.should_retry(2, 503, SpecificReason.HTTP_5XX_SERVER_ERROR) is True

    # 404 Not Found -> should NOT retry
    assert policy.should_retry(1, 404, SpecificReason.HTTP_404_NOT_FOUND) is False

    # Max retries exceeded -> should NOT retry
    assert policy.should_retry(3, 500, SpecificReason.HTTP_5XX_SERVER_ERROR) is False
