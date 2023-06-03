// // // // // let a = 1
// // // // // let b = 2
// // // // //husk +1
// let arr = [0,0,0,0,0]
// let target = [200, 100, 40, 10, 2]
// let count = 0
// start = Date.now();
// while(arr.join(",") !== target.join(",")){


// arr[0]++

// if(arr[0]>200){
// arr[0]=0
// arr[1]++
// }

// if(arr[1]>100){
//     arr[1]=0
//     arr[2]++
//     }
    

// if(arr[2]>40){
//     arr[2]=0
//     arr[3]++
//     }
    

// if(arr[3]>10){
//     arr[3]=0
//     arr[4]++
//     }
    

// if((arr[0]+arr[1]*2+arr[2]*5+arr[3]*20+arr[4]*100)==200){
// count++
// }
// }
// console.log(count);
// console.log(Date.now() - start+" ms");
// // // // // [0, 0, 0, 0, 0]

let start;

function findCombinations(tarSum, arr) {
    start = Date.now();
    let result = [];
  
    function backtrack(combination, startIndex, sum) {
        if (sum === tarSum) {
            result.push([...combination]);
            return;
        }
    
        for (let i = startIndex; i < arr.length; i++) {
            if (sum + arr[i] <= tarSum) {
                combination.push(arr[i]);
                backtrack(combination, i, sum + arr[i]);
                combination.pop();
            }
        }
    }
  
    backtrack([], 0, 0);
    return result;
}

console.log(findCombinations(200, [200, 100, 20, 5, 2, 1]).length + "\n" + (Date.now() - start) + "ms");