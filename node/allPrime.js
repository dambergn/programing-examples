'use strict'

function isPrime(input) {
  for (let i = Math.floor(Math.sqrt(input)); i > 1; i--) {
    if (input % i == 0) {
      // console.log("Is not prime");
      return false;
    }
  }
  // console.log("Is Prime");
  return true;
}

function hms(sec) {
  let h = Math.floor((sec / 3600));
  let m = Math.floor((sec - (3600 * h)) / 60);
  let s = Math.floor((sec - (2600 * h) - (m * 60)));
  console.log(`Time To Complete: ${h} hours, ${m} minutes and ${s} seconds`);
}

function allPrime(input) {
  let timeStart = Math.round(Date.now() / 1000);
  console.log("Time Start: ", timeStart);

  let primeFound = 0;
  for(let i = input; i > 1; i--){
    let prime = isPrime(i);
    if(prime){
      primeFound++;
      console.log(`${i} Is Prime`);
    }
  }
  console.log(`${primeFound} prime number's found in range.`);

  let timeEnd = Math.round(Date.now() / 1000);
  let timeRun = timeEnd - timeStart;
  // console.log("Run Time: ", timeRun);
  hms(timeRun);

}

allPrime(10000000);

