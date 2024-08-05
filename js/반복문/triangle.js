let str1 = '';
let n = 6; // 삼각형의 높이

for (let i = 1; i <= n; i++) {
    // 앞부분에 공백 추가
    for (let j = n; j > i; j--) {
        str1 += ' ';
    }
    // 별(*) 추가
    for (let k = 0; k < 2 * i - 1; k++) {
        str1 += '*';
    }
    // 줄 바꿈
    str1 += '\n';
}

console.log(str1);
