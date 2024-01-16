fn main() {
    let x: f64 = -20.48; // float
    let x: i64 = x.floor() as i64; // int
    println!("{}", x); // -21

    let s: &str = "hello"; // &str
    let s: String = s.to_uppercase(); // String
    println!("{}", s) // HELLO
}
