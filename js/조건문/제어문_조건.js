// 홀짝 프로그램

// let n=2;
// if(n%2==0){
//     console.log('even')
// }else{
//     console.log('odd')
// }

// 성적 프로그램

// let score=79;
// if (score >=90&&score <=100){
//     console.log('a')
// }
// else if(score>=80&&score<90){
//     console.log('b')
// }
// else{
//     console.log('c')
// }

// 과일가게 키오스크
// 1번 누르면 사과, 2번 누르면 바나나, 3번 누르면 포도, 4번 딸기

let menu = 1;
switch (menu) {
    case 1:
        console.log('apple')
        break;
    case 2:
        console.log('banana')
        break;
    case 3:
        console.log('grape')
        break;
    case 4:
        console.log('berry')
        break;
    default:
        console.log('choose among of them')
        break;
}




let withdraw = 1;
switch (withdraw) {
    case 1:
        console.log('입금')
        break;
    case 2:
        console.log('출금')
        break;

    default:
        console.log('end')
        break;
}