// let array = [52,273,32,93,103];
// for (let i in array){console.log(array[i]);}

let str1 = ''
for (let i = 1; i<7; i++){
    for (let j = 6; j>i; j--);{
    str1 += '';
    }
    for (let k = 0; k<2*i-1; k++){
            str1 += '*'
    }
        str1 += '\n';
}
console.log(str1);