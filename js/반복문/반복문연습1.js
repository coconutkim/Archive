// 1부터 10까지 찍기
// 중괄호를 꼭 해준다

// 초기화, 조건, 증가
// for(ㅁㅁㅁ){
// }

// 누적합
let tot = 0;
for (let i=1;i<=10;i++){
    tot = tot+i;
}
console.log(tot)

// 홀짝
for(let i=1;i<=10;i++){
        console.log(`${i} is even number`)
    }else{
        console.log(`${i} is odd number`)
    }

// 구구단
    for(let i = 2;i<=9;i++){
        for (let j = i;j<=9;j++){
            console.log(`${i}x${j} = ${i*j}`)
        }
    }


// 배열을 반복문으로 돌리기1
// let arr = ['apple','banana','candy']
// for(let i = 0;i<arr,length;i++){
//     console.log(arr[i]);
// }

// 배열을 반복문으로 돌리기2
// let arr = ['apple','banana','candy']
// for(let i in arr){
//     console.log(arr[i]);
// }

// 배열을 반복문으로 돌리기3
let arr = ['apple','banana','candy']
for(let obj of arr){
    console.log(obj);
}