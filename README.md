# test-deploy-wasm

build rust code as wasm and deploy as python package.

```bash
$ cargo make setup
$ cargo make all
# benchmark result
pyo3/mandelbrot/16000: 4.30 sec, std: 0.08
wasm/mandelbrot/16000: 13.87 sec, std: 0.15
pyo3/n_body/50000000: 2.38 sec, std: 0.03
wasm/n_body/50000000: 8.69 sec, std: 0.05

# binary size
1.6M ./target/wheels/benchmark_pyo3-0.1.0-cp36-cp36m-manylinux1_x86_64.whl
1.6M ./target/wheels/benchmark_pyo3-0.1.0-cp38-cp38-manylinux1_x86_64.whl
428K ./wasm/dist/benchmark_wasm-0.1.0-py3-none-any.whl
```

