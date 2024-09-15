"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function productExceptSelf(nums) {
    const answer = [];
    const left = [];
    const right = [];
    let i = 0;
    for (const n of nums) {
        if (i === 0) {
            left.push(1);
        }
        else {
            left.push(left[i - 1] * nums[i - 1]);
        }
        i++;
    }
    i = nums.length - 1;
    const reversed = [...nums].reverse();
    for (const n of reversed) {
        if (i === nums.length - 1) {
            right[i] = 1;
        }
        else {
            right[i] = right[i + 1] * nums[i + 1];
        }
        i--;
    }
    for (i = 0; i < nums.length; i++) {
        answer[i] = left[i] * right[i];
    }
    return answer.reverse();
}
const res = productExceptSelf([1, 2, 3, 4]);
console.log(res);
