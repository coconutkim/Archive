// npm install repl

// import 'repl'

// repl 모듈을 사용하여 읽기 평가 출력 루프를 시작하는 예제

// repl 모듈을 가져와서 콘솔에 출력한다
import repl from 'repl';
console.log(repl);

// repl 인터페이스를 시작한다
repl.start({

// 프롬프트 문자열을 인풋으로 설정한다
// 사용자가 입력할 때 앞에 인풋이 표시된다
    prompt:'input',

// eval은 사용자가 입력한 명령을 평가하는 함수
// 커멘드는 문자열, 콘텍스트는 사용하지 않고,
// 파일네임은 사용하지 않고, 콜백은 평가가 완료되었을 때 호출하는 함수
    eval:(command,context,filename,callback) => {

// 입력된 문자열을 숫자로 변환하려고 한다
// 변환된 값이 nan인지 확인
// 숫자가 아닌 값인지
        let number =  Number(command);
        if(isNaN(number)){
            console.log('숫자가 아님');

// 변환된 값이 유효한 숫자이면 숫자를 출력한다
        }else{
            console.log('숫자');

// 평가가 완료되었음을 알리는 콜백함수를 호출한다
        }
        callback();
    }
    
})