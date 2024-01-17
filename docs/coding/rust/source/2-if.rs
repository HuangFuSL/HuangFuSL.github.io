fn main() {
    let (a, b) = (5, 3);
    println!("max({}, {}) = {}", a, b, if a > b { a } else { b });
    if a < b {
        println!("min({}, {}) = {}", a, b, a);
    } else {
        println!("min({}, {}) = {}", a, b, b);
    }
}
