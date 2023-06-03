

// var singleNumber = function(nums) {
//     let obj = {}

// for(i=0; i<nums.length; i++){
// if(obj[nums[i]]==undefined){
// obj[nums[i]]=1
// }
// else{
// obj[nums[i]]++
// }



// }   
// console.log(obj);

// console.log(Object.keys(obj));
// for(j=0; j<Object.keys(obj).length; j++){
// if(parseInt(obj[Object.keys(obj)[j]])==1){
// return (Object.keys(obj)[j]); 

// }
// }
// };



// let obj = {}

// var singleNumber = function(nums) {

// for(i=0; i<nums.length; i++){
// if(obj[nums[i]]==undefined){
// obj[nums[i]]=1
// }
// else{
// obj[nums[i]]++
// }

// }   

// for(key in obj){
// if(obj[key]==1){
// console.log(key); 

// }
// }
// };


// singleNumber([1])

// const nums = [1, 2, 3, 4, 5];
// for (let n in nums) {
//   console.log(n);
// }

// let numsob={
// 3: "yes",
// 2: 2,
// "yes": 4

// }
// for(key in numsob) {
// console.log(key);
// }
var singleNumber = function(nums) {
    let obj = {}
    
    for(i of nums){
    if(nums.length==0){
    return nums[0]
    }
    
    if(obj[i]){
    obj[i]++
    }
    else{
    
    obj[i]=1
    }
    
    }   
    


    for(key in obj){
    if(obj[key]==1){
    console.log(key); 
    
    }
    }
    };
singleNumber([-1,-1,-2])