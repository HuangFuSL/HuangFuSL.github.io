fn main() {
    let mut b1 = 1;

    let (c1, c2) = 'outer_loop: loop {
      let mut b2 = 1;

      'inner_loop: loop {
        println!("Current Value : [{}][{}]", b1, b2);

        if b1 == 2 && b2 == 2 {
            break 'outer_loop (b1, b2); // Leave outer_loop with return value
        } else if b2 == 5 {
        	break; // Leave inner_loop by default
        }

        b2 += 1;
      }

      b1 += 1;
    };
    println!("b1 = {}, b2 = {}", c1, c2);
}
