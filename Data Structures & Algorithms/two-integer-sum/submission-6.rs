impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // key is num we need and its value is the index of it
        // so we'll loop through the vector, do target-num and index the hash
        // if we find the value, then return the curr index and the found index

        let mut tracker = HashMap::new(); // needed val + index

        for i in 0..nums.len() {
            // going to do the subtraction
            // going to do match where if curr is in dict, return or pass
            let diff: i32 = target-nums[i];
            match tracker.get(&diff) {
                Some(&index) => return vec![index as i32, i as i32],
                None => {
                    tracker.insert(nums[i], i);
                }
            }
        }

        vec![]
    }
}
