"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function lengthOfLongestSubstring(s) {
    let maxLengthFound = 0;
    let currentMaxString = [];
    for (const char of s) {
        console.log(`Evaluating ${char}`);
        if (currentMaxString.includes(char)) {
            const indexOfChar = currentMaxString.indexOf(char);
            currentMaxString = currentMaxString.slice(indexOfChar + 1);
            currentMaxString.push(char);
            console.log(`If branch ${currentMaxString} - ${maxLengthFound}`);
        }
        else {
            currentMaxString.push(char);
            console.log(`Else branch ${currentMaxString} - ${maxLengthFound}`);
        }
        maxLengthFound =
            maxLengthFound < currentMaxString.length
                ? currentMaxString.length
                : maxLengthFound;
    }
    return maxLengthFound;
}
const result = lengthOfLongestSubstring("abcabcbb");
console.log(result);
