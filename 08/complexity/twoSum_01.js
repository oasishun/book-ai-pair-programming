function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [[i, j], [nums[i], nums[j]]];
            }
        }
    }
    return null; // 정답이 반드시 존재한다고 가정하므로 이 줄은 실행되지 않음
}

// 예제 테스트
const nums = [2, 7, 11, 15];
const target = 9;
const result = twoSum(nums, target);
console.log(result); // 출력: [[0, 1], [2, 7]]