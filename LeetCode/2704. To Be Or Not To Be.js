/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    
    if (expect===val) {
        return {"value": true}
    } else {
        return {"error": "Not Equal"}
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
