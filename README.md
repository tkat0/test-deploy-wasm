# test-deploy-wasm

build rust code as wasm and deploy as python package.

## Usage

```bash
$ cargo install cargo-make
$ cargo make setup
$ cargo make all
# benchmark result
pyo3/mandelbrot/16000: 4.23 sec, std: 0.11
wasm/mandelbrot/16000: 14.51 sec, std: 0.75
pyo3/n_body/50000000: 2.43 sec, std: 0.09
wasm/n_body/50000000: 8.90 sec, std: 0.17

# binary size
741K ./target/wheels/benchmark_pyo3-0.1.0-cp36-cp36m-manylinux1_x86_64.whl
741K ./target/wheels/benchmark_pyo3-0.1.0-cp38-cp38-manylinux1_x86_64.whl
428K ./wasm/dist/benchmark_wasm-0.1.0-py3-none-any.whl
```

## Repository Structure

- benchmark: benchmark main code (rust)
- pyo3: benchmark pyo3 binding & python library
- wasm: benchmark wasm binding & python library
