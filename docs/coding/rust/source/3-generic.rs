fn max<T> (a: T, b: T) -> T
    where T: std::cmp::PartialOrd
{
    if a > b { a } else { b }
}

fn main() {
    println!("{}", max(1, 2)); // i32
    println!("{}", max(1.0, 2.0)); // f64
    println!("{}", max("a", "b")); // &str
}
