use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn n_body(n: i32) -> PyResult<()> {
    benchmark::n_body::run(n);
    Ok(())
}

#[pyfunction]
fn mandelbrot(size: usize) -> PyResult<()> {
    benchmark::mandelbrot::run(size);
    Ok(())
}

/// A Python module implemented in Rust.
#[pymodule]
fn benchmark_pyo3(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(n_body))?;
    m.add_wrapped(wrap_pyfunction!(mandelbrot))?;

    Ok(())
}
