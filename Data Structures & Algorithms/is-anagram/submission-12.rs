impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut array: [i32; 26] = [0; 26];

        for c in s.chars() {
            let ascii_c = {
                let x = c as i32;
                let y = 'a' as i32;
                x - y
            };
            array[ascii_c as usize]-=1;
        };

        for c in t.chars() {
            let ascii_c = {
                let x = c as i32;
                let y = 'a' as i32;
                x - y
            };
            array[ascii_c as usize]+=1;
        };

        for num in &array {
            if *num != 0 {
                return false
            };
        };

        return true
    }
}
