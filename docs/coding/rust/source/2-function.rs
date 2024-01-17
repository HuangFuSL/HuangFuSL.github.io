fn add(a: i32, b: i32) -> i32 {
    a + b // Return by expression
}
fn sub(a: i32, b: i32) -> i32 {
    return a - b; // Return by return keyword
}

fn main() {
    let (a, b) = (2, 1);
    println!("{} + {} = {}", a, b, add(a, b));
    println!("{} - {} = {}", a, b, sub(a, b));
}
