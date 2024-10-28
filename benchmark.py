import pytest
import time
def test_cpu_performance(benchmark):
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    result = benchmark(fibonacci, 30)
    stats = benchmark.stats
    assert stats['min'] > 0  # Ensure that the benchmark ran successfully-

def test_memory_performance(benchmark):
    def allocate_memory(size_mb):
        return [0] * (size_mb * 1024 * 1024 // 8)

    result = benchmark(allocate_memory, 100)  # Allocate 100 MB
    stats = benchmark.stats
    assert stats['min'] > 0  # Ensure that the benchmark ran successfully