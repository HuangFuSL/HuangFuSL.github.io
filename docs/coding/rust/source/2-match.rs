fn main() {
    let marks_paper_a: u8 = 25;
    let marks_paper_b: u8 = 30;

    let output = match (marks_paper_a, marks_paper_b) {
        (50, 50) => "Full marks for both papers",
        (50, _) => "Full marks for paper A",
        (_, 50) => "Full marks for paper B",
        (x, y) if x > 25 && y > 25 => "Good",
        (_, _) => "Work hard"
    };

    println!("{}", output); // Work hard
}
