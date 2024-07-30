// 테스트라는 변수 선언, 초기화 아니므로 값은 언디파인드
let test;

// console.log(typeof(test));

// 타입이 언디파인드인데
// 내용은 언디파이드가 아니라 한다
// 그러므로 거짓을 출력한다
console.log(typeof(test) != 'undefined')

// 테스트의 타입이 언디파인드가 아니면 결과는 아니다
// 하지만 언디파인드므로 테스트 변수의 값에는 변화가 없다
typeof(test) != 'undefined' ? test:'hi'
// 테스트는 여전히 초기화 되지 않았으므로
// 언디파인드를 출력한다
console.log(test)