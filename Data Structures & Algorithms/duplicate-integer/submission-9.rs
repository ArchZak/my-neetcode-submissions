impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut tracker = HashMap::new();

        for num in &nums {
            if tracker.contains_key(num) {
                return true
            }
            tracker.insert(num, 1);
        }

        false
    }
}
