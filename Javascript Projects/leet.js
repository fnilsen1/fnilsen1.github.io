
// var reverseVowels = function(s) {
// let arr = []
// let indices = []
// let vowels = ["a", "e","i", "o","u", "A", "E", "I", "O", "U"]
    
// s = s.split("")

// for(let i=0; i<s.length;i++){
// if(vowels.includes(s[i])){
// arr.push(s[i])
// indices.push(i)
// }

// }

// arr.reverse()



// for(let j=0; j<arr.length;j++){


// s[indices[j]]=arr[j]

// }
// return(s.join("")); 

// };

// console.log(reverseVowels("leetcode"));


// let arr1 = []
// let arr2 = []
// let final = []

// var shuffle = function(nums, n) {
// for(let i = 0; i<(nums.length/2); i++){
// arr1.push(nums[i])

// }

// for(let j = nums.length/2; j<nums.length; j++){
// arr2.push(nums[j])

// }

// console.log(arr1, arr2)
// for(let k = 0; k<(arr1.length); k++){
// final.push(arr1[k])
// final.push(arr2[k])
// }

// return final


// };

// console.log(shuffle([1,2,3,4,4,3,2,1], 4));


var runningSum = function(nums) {
    let arr = [...nums]    
    
    for(let i =1; i<nums.length; i++){
    for(let j = i-1; j>-1; j--){
    console.log(arr);
    arr[i]= arr[i]+nums[j]
    
    }
    }
    
    return arr
    };

console.log(runningSum([3,2,1]));