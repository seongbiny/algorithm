

function solution(numbers) {
  const num = numbers.split("");
  const answer = new Set(); //정답(소수)을 넣을 set 선언

  getPermutation(num, ""); //순열 함수 호출

  //완전탐색할 순열 함수
  function getPermutation(arr, fixed) {
    //매개변수 arr의 요소가 있을때까지만 반복 (사실상 이부분을 이해하는 것이 중요 -> 요소가 없다면 백트래킹이 적용되므로)
    if (arr.length > 0) {
      //arr의 각 요소에 대해
      for (let i = 0; i < arr.length; i++) {
        const newFixed = fixed + arr[i]; //기존의 고정값에 배열의 요소를 하나씩 붙이며 고정값을 늘려나감 -> 이렇게 늘려나가면서 arr.length > 0 일 때 까지 반복하는 것
        const copyArr = [...arr]; //백트래킹으로 다시 돌아오려면 arr원본이 필요하기 때문에 arr의 복사본으로 다음 진행
        copyArr.splice(i, 1); //기존 fixed에 newFixed로 붙여진 arr[i]는 제거하기 (이렇게 되면 copyArr에는 고정되지 않은 요소들이 남게됨)

        //새로운 고정값은 소수 판별 후 맞으면 정답 set에 add
        if (isPrime(parseInt(newFixed)) === true)
          answer.add(parseInt(newFixed));

        //재귀를 통해 배열의 요소가 없을 때까지 계속 고정값을 늘려가며 순열 구하기
        getPermutation(copyArr, newFixed);
      }
    }
  }

  //소수 판별 함수
  function isPrime(num) {
    if (num < 2) return false; //2보다 작은 수 중에 소수는 없다
    //2부터 num-1의 수 중에서 num으로 나누어떨어지는 수가 있다면 소수가 아니다
    for (let i = 2; i < num; i++) {
      if (num % i === 0) return false;
    }
    //그 외에는 true를 return
    return true;
  }

  return answer.size; //정답 set에 들어있는 소수들의 크기로 return
}