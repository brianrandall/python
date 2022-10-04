/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 * 
 * - create a function that takes in a string
 * - create a tempValue
 * - iterate through the string starting at the end
 *      - set tempValue to be tempValue + current char
 * - return tempValue
 */

function reverseString(str) {
    var reverse = "";
    for (var i = str.length -1; i >=0; i--) {
        reverse+=str[i];
    }
    return reverse;
}

reverseString("hello");

/*****************************************************************************/

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const two_str1 = "object oriented programming";
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";

//read string as input
//split string into individual words
//create tempVal empty array
//iterate through new array
    //iterate through and return first value of each subarray
    //push to tempVal array
//return new array


/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * 
 *
 * 
 * @returns {string} The acronym.
 * 
 * 
 */
function acronymize(str) {
    var words = str.split(" ");
    let newString = "";
    for (let i = 0; i < words.length; i++) {
        if (words[i] != "") {
            newString += words[i].charAt(0).toUpperCase();
        }
    }
    return newString;
}