// /* 
// Given an array of ints representing a line of people where the space between
// indexes is 1 foot, with 0 meaning no one is there and 1 meaning someone is in
// that space,
// return whether or not there is at least 6 feet separating every person.
// Bonus: O(n) linear time (avoid nested loops that cause re-visiting indexes).
// */

// const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

// const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected2 = true;

// const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected3 = true;

// const queue4 = [];
// const expected4 = true;

// /**
//  * Determines whether each occupied space in the line of people is separated by
//  * 6 empty spaces.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<0|1>} queue
//  * @returns {Boolean}
//  */
// function socialDistancingEnforcer(queue) {

//     console.log(queue.count(0))
    
// }



/*****************************************************************************/

/*****************************************************************************/

/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const two_nums1 = [-2, 5, 7, 0, 3];
const two_expected1 = 2;

const two_nums2 = [9, 9];
const two_expected2 = -1;

const two_num3 = [10, 3, 2, 3, 20, -8, 1, 2]
const two_expected3 = 3;

const two_num4 = [10, 3, 2, 3, 20, -8, 1, 1, 1]
const two_expected4 = 3;

const two_num5 = [10, 3, 2, 3, 20, -8, 1, 1, 4]
const two_expected5 = -1;
/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    let lsum = 0
    let rsum = 0

    if (nums.length < 3) {
        return -1;
    }
    else {
        for (let i = 0; i < nums.length; i++) {
            for (let j = 0; j < i; j++)
                lsum += nums[j];

            for (let j = nums.lenth - 1; j >= 0; j--)
                rsum += nums[j]

            if (lsum == rsum) 
                return i;
           
        }
        return -1
    }
}

console.log(balanceIndex(two_nums1))