/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const final_arr = []
    for(let i = 0; i<arr.length; i++) {
        final_arr[i] = fn(arr[i], i)
    }
    return final_arr
};
