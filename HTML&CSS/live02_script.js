console.log("hello world")

const number = document.querySelector("#number")
const btn = document.querySelector("#button")

// addEventListener는 2개의 전달인자를 갖는다.
// 1. 이벤트 종류
// 2. 실행할 함수

btn.addEventListener("click", function() {
    console.log("click!")
    number.textContent = Number(number.textContent) + 1;
})

btn.addEventListener("click", ()=>{
    console.log("hihihi~")
})

// 매개변수: parameter
// 전달인자: argument


function sayHi(x) {
    console.log(`${x} :b`)
}

document.querySelector(".mysubmit").addEventListener("click", (event)=> {
    event.preventDefault();
    alert("정상적으로 제출되었습니다.")
})