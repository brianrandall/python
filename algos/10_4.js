// /* 
//   String: Reverse
//   Given a string,
//   return a new string that is the given string reversed
// */

// const str1 = "creature";
// const expected1 = "erutaerc";

// const str2 = "dog";
// const expected2 = "god";

// const str3 = "hello";
// const expected3 = "olleh";

// const str4 = "";
// const expected4 = "";

// /**
//  * Reverses the given str.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str String to be reversed.
//  * @returns {string} The given str reversed.
//  */
// function reverseString(str) {}

/*****************************************************************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const two_str1 = "hello";
const two_expected1 = "olleh";

const two_str2 = "hello world";
const two_expected2 = "olleh dlrow";

const two_str3 = "abc def ghi";
const two_expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
// function reverseWords(str) {
//     var result = ""
//     var temp = [];
//     for (var i = str.length - 1; i >= 0; i--) {
//         temp += str[i];
//     }

//     return temp;
// }

// console.log(reverseWords(two_str2));

function reverseWords(str) {
    var str = str + ' '
    var tempValue= ''
    var result = []
    for (let i=0;i<str.length+1;i++){
        if (str[i] != ' '){
        tempValue += str[i];
        }
        else if (str[i]== ' '){
            result.push(tempValue)
            tempValue = ''
        }
        else {
            result.push(tempValue)
            tempValue = ''
        }
    for (let j = result.length; j > 0; j--)
        
    }
    return result
}

console.log(reverseWords(two_str2));