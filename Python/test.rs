fn main() {
    let mut sum: u64 = 0;

    for i in 1..=1_000_000_000 {
        sum += i;
    }

    println!("Sum of numbers from 1 to 1 billion: {}", sum);
}