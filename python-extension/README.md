## Extension for python's JIT interpreters

Despite the fact that most users don't care about python's performance, partly because most high-performance computing is replaced by c-extensions in python's design philosophy, and the other part because  in python's usage scenarios they don't need it anyway, but an important fact is that pros always have a desire for performance, Most modern sophisticated computer engineering techniques are tied to the need for performance.

So I really appreciate python's exploration of the python's jit interpreter, although the highly dynamic properties brings difficulties to the jit implementation, many thanks to the programmers who contributed open source code in this field. Hence it's unfair to exclude them from the benchmark, I used the same source code to add them to the test.

It is important to note that this is not a rigorous test in a rigorous environment, if you want to estimate the performance of your program, you need to always test it in conjunction with the actual environment.
