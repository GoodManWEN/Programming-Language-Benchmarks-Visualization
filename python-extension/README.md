## Extension for python's JIT interpreters

Despite the fact that most users don't care about python's performance, partly because most high-performance computing is replaced by c-extensions in python's design philosophy, and the other part because  in python's usage scenarios they don't need it anyway, but an important fact is that pros always have a desire for performance, Most modern sophisticated computer engineering techniques are tied to the need for performance.

So I really appreciate python's exploration of the python's jit interpreter, although the highly dynamic properties brings difficulties to the jit implementation, many thanks to the programmers who contributed open source code in this field. Hence it's unfair to exclude them from the benchmark, I used the same source code to add them to the test.

It is important to note that this is not a rigorous test in a rigorous environment, if you want to estimate the performance of your program, you need to always test it in conjunction with the actual environment.

### Details

All test items and scripts are placed in the `/python-extension/script` directory, and they are obtained in the same way as for all other languages from [The Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python.html). Actions is tasked with running test scripts to test the speed in every 1-3 days, the JIT interpreter and CPython interpreter are executed in the same environment to estimate their speedup times. Since Github Actions does not provide an exclusive(stable) running environment, this may result in slight variations between executions, so the test results are taken as the nearest moving average to minimize the error. If a version upgrade is encountered, it will usually increase the number of executions to ensure that the moving average results are updated to the latest.

The specific tests are executed by the script in `/python-extension/timer`, the most recent execution results can be found in `python-extension/result/result.json` which to avoid overly long files does a timed rollover, but usually you can find at least the last few dozen historical results in it. Each test also logs the interpreter version in `python-extension/result/version.json`, In which recorded, from top to bottom, the Linux distribution versions, the kernel version, CPython's version, pypy's version & pyston's version.
