use pyo3::prelude::*;
use chrono::offset::{Local, FixedOffset};

/// Formats the sum of two numbers as string.
#[pyfunction]
pub fn rs_sys_tz() -> FixedOffset {
    println!("Look mah, 2 + 2 = {}!", lyrs::add(2, 2));
    Local::now().offset().to_owned()
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyrs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rs_sys_tz, m)?)?;
    Ok(())
}
