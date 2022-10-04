/* 
Zip Arrays into Map


Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
Associative arrays are sometimes called maps because a key (string) maps to a value 
*/

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];

const expected1 = {
abc: 42,
3: "wassup",
yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};


const keys3 = ["abc", 3, ['animal', 'treat']];
const vals3 = [42, "wassup", true];

const expected3 = {
    abc: 42,
    3: "wassup",
    'animal': true,
    'treat': true
};

const keys4 = ["abc", 3, 'yo'];
const vals4 = [42, "wassup"];

const expected4 = {
    abc: 42,
    3: "wassup",
    'yo': null
};

const keys5 = ["abc", 3];
const vals5 = [42, "wassup", true];

const expected5 = false

function combo (arr1, arr2) {
    newObject = {};

    if (arr1.length < arr2.length) {
        return false
    }

    for (i = 0; i < arr1.length; i++) {
        var key = arr1[i]; 
        var val = arr2[i];
        newObject[key] = val;
        
    }
    return newObject;
}

console.log("1 - ", combo(keys1, vals1))
console.log("2 - ", combo(keys2, vals2))
console.log("3 - ", combo(keys3, vals3))
console.log("4 - ", combo(keys4, vals4))
console.log("5 - ", combo(keys5, vals5))


// /**
//  * Converts the given arrays of keys and values into an object.
//  * - Time: O(?).
//  * - Space: O(?).
// //  * @param {Array<string>} keys
// //  * @param {Array<any>} values
// //  * @returns {Object} The object with the given keys and values.
// //  */
// // function zipArraysIntoMap(keys, values) {
// // }
// /* 
// Invert Hash
// A hash table / hash map is an obj / dictionary
// Given an object / dict,
// return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
// */

// const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
// const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// const two_obj2 = { name: "Zaphod", charm: "high", morals: ["dicey", 'something'] };
// const two_expected2 = { Zaphod: "name", high: "charm", dicey: "morals", something:"morals" };

// const two_obj3 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey" };
// const two_expected3 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"]};

// /**
//  * Inverts the given object's key value pairs so that the original values
//  * become the keys and the original keys become the values.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Object<string, any>} obj
//  * @return The given object with key value pairs inverted.
//  */
// function invertObj(obj) {

//     newObject = {};

//     if (arr1.length < arr2.length) {
//         return false
//     }

//     for (i = 0; i < arr1.length; i++) {
//         var key = arr1[i]; 
//         var val = arr2[i];
//         newObject[key] = val;
        
//     }
//     return newObject;


// }

// function combo (arr1, arr2) {
//     newObject = {};

//     if (arr1.length < arr2.length) {
//         return false
//     }

//     for (i = 0; i < arr1.length; i++) {
//         var key = arr1[i]; 
//         var val = arr2[i];
//         newObject[key] = val;
        
//     }
//     return newObject;
// }

// console.log(combo(keys3, vals3))