const { performance } = require('perf_hooks')
const iters = Number(process.argv[2])
const algo = Number(process.argv[3])

let start
let end
let j

switch(algo) {
  case 1:
    start = performance.now()
    j = [...new Array(iters).keys()] // ~6762 milli
    end = performance.now()
    break
  case 2:
    start = performance.now()
    j = [] // ~2760 milli
    for(let i = 0; i < iters; i++) {
      j.push(i)
    }
    end = performance.now()
    break
  case 3:
    start = performance.now()
    const range = function* (n) { for (let i = 0; i < n; i++) { yield i } }
    j = [...range(iters)]
    end = performance.now()
    break
  case 4:
    start = performance.now()
    j = new Array(iters).fill(0).map((x, i) => i)
    end = performance.now()
    break
  default:
    break
}
console.log((end - start)/1000) // Convert it to seconds
