
#[no_mangle]
pub extern "C" fn n_body(n: i32) {
    benchmark::n_body::run(n);
}

#[no_mangle]
pub extern "C" fn mandelbrot(size: usize) {
    benchmark::mandelbrot::run(size);
}

#[no_mangle]
pub extern "C" fn add(a: i32, b: i32) -> i32 {
    let c = a + b;
    println!("{} + {} = {}", a, b, c);
    c
}