fn main() {
    let (a, b) = (2, 1);
    let add = |a, b| a + b;
    println!("{} + {} = {}", a, b, add(a, b));
    println!("{} - {} = {}", a, b, |a, b| -> i32 { return a - b; }(a, b));
}
