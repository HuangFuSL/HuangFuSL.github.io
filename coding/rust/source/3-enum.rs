enum IpAddr {
    V4(u8, u8, u8, u8), // Tuple
    V6{ addr: String }, // Struct
    LocalHost, // Unit
}

fn main() {
    let v4 = IpAddr::V4(4, 4, 4, 4);
    let v4_invalid = IpAddr::V4(0, 0, 0, 0);
    let v6 = IpAddr::V6{ addr: String::from("::1") };
    let local = IpAddr::LocalHost;
    print_ip(v4);
    print_ip(v4_invalid);
    print_ip(v6);
    print_ip(local);
}

fn print_ip(ip: IpAddr) {
    match ip {
        IpAddr::V4(a, b, c, d) if a != 0 || b != 0 || c != 0 || d != 0
            => println!("{}.{}.{}.{}", a, b, c, d),
        IpAddr::V4(a, b, c, d)
            => println!("{}.{}.{}.{} is not an valid IPv4 address", a, b, c, d),
        IpAddr::V6{ addr } => println!("{}", addr),
        IpAddr::LocalHost => println!("localhost"),
    }
}
