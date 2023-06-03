


// list = []
// for(i=0; i<100; i++){
// list.push(false)
// }
// // console.log(list);
// let number = 0
// for(k=1;k<101;k++){
// // number++
// for(j=1; j<101; j++){


// if(j%k==0){
// list[j-1]= !list[j-1]
// // console.log(list[j]%k)
// }


// }



// }

// console.log(list);

// for(i of list){
// if(i == true){
// const newDiv = document.createElement("div")
// newDiv.classList.add("divs")
// newDiv.classList.add("red")
// document.getElementById("master").append(newDiv)
// }

// else{
// const newDiv = document.createElement("div")
// newDiv.className="divs"
// document.getElementById("master").append(newDiv)
// }


// }

// function getRandomIntInclusive(min, max) {
//     min = Math.ceil(min);
//     max = Math.floor(max);
//     return Math.floor(Math.random() * (max - min + 1) + min);
//   }
// let list = []
// let money = 0
// console.log(getRandomIntInclusive(1,2));
// // while(true){

// // }
// let count = 0
// for(i=0;i<100000;i++){
// money = 0
// console.log(getRandomIntInclusive(1,4));
// // for(j=0;j<10000;j++){
// // money +=getRandomIntInclusive(1,4)

// // }

// // list.push(money)

// }


// var counts = 0;
// for(var i = 0; i < list.length; ++i){
//     if(list[i] == 25000)
//         counts++;
// }
// console.log(counts);

function generateArrayWithAvg(targetAvg, length) {
    const arr = [];
    
    // Calculate the sum required for the target average
    const targetSum = targetAvg * length;
    
    // Generate random numbers until the sum matches the target sum
    let sum = 0;
    for (let i = 0; i < length; i++) {
      const randNum = Math.random() * 6; // Generate a random number between 0 and 6
      arr.push(randNum);
      sum += randNum;
    }
    
    // Adjust the sum by subtracting the excess amount and adding the shortfall amount
    const excess = sum - targetSum;
    const adjustment = excess / length;
    
    for (let i = 0; i < length; i++) {
      arr[i] -= adjustment;
    }
    
    return arr;
  }
  
  // Generate an array with 1000000 elements and an average of 3
  const arr = generateArrayWithAvg(3, 1000000);
  
  // Calculate the actual average of the array
  const actualAvg = arr.reduce((sum, num) => sum + num, 0) / arr.length;
  
  console.log(`Target average: 3`);
  console.log(`Actual average: ${actualAvg}`);