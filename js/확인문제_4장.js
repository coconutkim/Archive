// 배열의 가장 작은 수와 큰 수 구하기

let array = [273,52,103,57,271];

let min = Number.MAX_VALUE
let max = Number.MIN_VALUE

for (let i = 0;i<array.length;i++){
    if (array[i]>max){
        max = array[i];
    }
    if (array[i]<min){
        min = array[i];
    }
}
console.log(`the biggest num: ${max}`);
console.log(`the smallest number: ${min}`);

// ========================================================

// 어레이 요소 역순으로 나오게 하기

// let array = [52,71,32,103,273,93];


// for (let i=array.length-1;i>=0;i--){
//     console.log(array[i]);
// }