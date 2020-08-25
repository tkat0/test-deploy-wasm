from time import time
import numpy as np


def benchmark(name, f, args=None, n=10):
    elapseds = []
    for _ in range(n):
        if args:
            start = time()
            f(*args)
            end = time()
        else:
            start = time()
            f()
            end = time()
        elapsed = end - start
        elapseds.append(elapsed)
    elapseds = np.asarray(elapseds)
    print(f"{name}: {elapseds.mean():.2f} sec, std: {elapseds.std():.2f}")
    return elapsed


if __name__ == '__main__':
    import benchmark_pyo3
    from benchmark_wasm import instance

    # DEBUG = True
    DEBUG = False

    conds = [16000] if not DEBUG else [10]
    for size in conds:
        args = (size,)
        benchmark(f"pyo3/mandelbrot/{size}", benchmark_pyo3.mandelbrot, args)
        benchmark(f"wasm/mandelbrot/{size}", instance.exports["mandelbrot"], args)

    conds = [50000000] if not DEBUG else [10]
    for n in conds:
        args = (n,)
        benchmark(f"pyo3/n_body/{n}", benchmark_pyo3.n_body, args)
        benchmark(f"wasm/n_body/{n}", instance.exports["n_body"], args)

