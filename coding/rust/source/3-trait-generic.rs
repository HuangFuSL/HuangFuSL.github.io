trait From<T> {
    fn from_u8(x: T) -> Self;
}
impl From<u8> for u8 {
    fn from_u8(x: u8) -> Self {
        x
    }
}
impl From<u8> for u16 {
    fn from_u8(x: u8) -> Self {
        x as u16
    }
}
impl From<u8> for i8 {
    fn from_u8(x: u8) -> Self {
        x as i8
    }
}
impl From<u8> for i16 {
    fn from_u8(x: u8) -> Self {
        x as i16
    }
}

fn main() {
    println!("{}", i16::from_u8(1 as u8));
}
