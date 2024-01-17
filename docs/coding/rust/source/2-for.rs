fn main() {
    let group : [&str; 4] = ["Mark", "Larry", "Bill", "Steve"];

    for n in 0..group.len() { // group.len() = 4 -> 0..4 👎 check group.len()on each iteration
    println!("Current Person : {}", group[n]);
    }

    for person in group.iter() { // 👍 group.iter() turn the array into a simple iterator
    println!("Current Person : {}", person);
    }
}
