![](../site/banner.png)

# 12 Prepare: Go Threads


## What is Go?

> The Go programming language is an open source project to make programmers more productive.> 

> Go is expressive, concise, clean, and efficient. Its concurrency mechanisms make it easy to write programs that get the most out of multicore and networked machines, while its novel type system enables flexible and modular program construction. Go compiles quickly to machine code yet has the convenience of garbage collection and the power of run-time reflection. It's a fast, statically typed, compiled language that feels like a dynamically typed, interpreted language.

Go's main website: https://golang.org/

The reason for introducing Go to this course, is that the language is built around concurrency and parallelism.

## What are Goroutines?

Please read the [following article](https://www.golang-book.com/books/intro/10)

A goroutine is a function that is capable of running concurrently with other functions.  They are like threads about lighter (meaning faster to start and take up less system resources).

The following a quotes from the [following website](http://tleyden.github.io/blog/2014/10/30/goroutines-vs-threads/)


Here are some of the advantages of Goroutines over threads:

- You can run more goroutines on a typical system than you can threads.
- Goroutines have growable segmented stacks.
- Goroutines have a faster startup time than threads.
- Goroutines come with built-in primitives to communicate safely between themselves (channels).
- Goroutines allow you to avoid having to resort to mutex locking when sharing data structures.
- Goroutines are multiplexed onto a small number of OS threads, rather than a 1:1 mapping.
- You can write massively concurrent servers without having to resort to evented programming.


### You can run more of them.

On Java you can run 1000’s or tens of 1000’s threads. On Go you can run hundreds of thousands or millions of goroutines.

Java threads map directly to OS threads, and are relatively heavyweight. Part of the reason they are heavyweight is their rather large fixed stack size. This caps the number of them you can run in a single VM due to the increasing memory overhead.

Go has a segmented stack that grows as needed. They are “Green threads”, which means the Go runtime does the scheduling, not the OS. The runtime multiplexes the goroutines onto real OS threads, the number of which is controlled by GOMAXPROCS. Typically you’ll want to set this to the number of cores on your system, to maximize potential parallelism.


https://rcoh.me/posts/why-you-can-have-a-million-go-routines-but-only-1000-java-threads/

## Running Go programs

- You can download the Go language to your computer.  There are packages to help you write Go programs in VSCode.
- You can use replit.com
- You can go to https://play.golang.org/


## Examples of Go programs

This isn't a course on Go, so we best method to learning a new computer language is to see and run examples.

I used the command line terminal window to run the following examples.  For example, the `hello.go` program below was run using `go run hello.go`

### Hello World

Notice that to display information to the console, you use the `fmt` package.

```go
package main

import "fmt"
func main() {
    fmt.Println("hello world")
}
```

Output:

```
hello world
```

---
### Variables

Variables are defined with the `var` statement.  Go is a strongly typed language meaning that you need to define a variables' type. (ie., `var gpa float32`).  Here are the [basic types](https://tour.golang.org/basics/11).  For formatting strings for output, Go uses the `Printf()` statement like C language.

The **:=** statment

the `:=` short assignment statement can be used in place of a var declaration with implicit type.  The variable `g` below is an example of using `:=`.

```go
package main

import "fmt"

func main() {

    var a = "initial"
    fmt.Println(a)

    var b, c int = 1, 2
    fmt.Println(b, c)

    var d = true
    fmt.Println(d)

    var e int
    fmt.Println(e)

    // Same as:  var f string = "apple"
    f := "apple"
    fmt.Println(f)

    g := 2.345
    fmt.Printf("%f\n", g)
}
```

Output:

```
initial
1 2
true
0
apple
2.345000
```

---
### If Else statements

Basic If/Else statements.  In this example, `if num := 9; num < 0 {` is different in that the variable `num` is created and set to the value of 9 in the `if` statement.

```go
package main

import "fmt"

func main() {

    if 7 % 2 == 0 {
        fmt.Println("7 is even")
    } else {
        fmt.Println("7 is odd")
    }

    if 8 % 4 == 0 {
        fmt.Println("8 is divisible by 4")
    }

    if num := 9; num < 0 {
        fmt.Println(num, "is negative")
    } else if num < 10 {
        fmt.Println(num, "has 1 digit")
    } else {
        fmt.Println(num, "has multiple digits")
    }
}
```

Output:

```
7 is odd
8 is divisible by 4
9 has 1 digit
```

---
### For loops

The for loops are similar to the C for loops.

```go
package main

import "fmt"

func main() {
    for j := 7; j <= 9; j++ {
        fmt.Println(j)
    }

    for {
        fmt.Println("loop")
        break
    }

    for n := 0; n <= 5; n++ {
        if n%2 == 0 {
            continue
        }
        fmt.Println(n)
    }

    // Look through an array of integers
    array := [10]int{12, 23, 34, 45, 56, 67, 78, 89, 90, 100}
    sum := 0
    for _, v := range array {
        sum += v
    }
    fmt.Println("Sum of the array is", sum)
}
```

Output:

```
7
8
9
loop
1
3
5
Sum of the array is 594
```

---
### While Loops

There isn't a `while` statement in Go, but there is something like it using the `for` statement.

```go
package main

import "fmt"
func main() {
    i := 1
    for i <= 3 {
        fmt.Println(i)
        i = i + 1
    }
}
```

Output:

```
1
2
3
```

---
### Functions

[Web page article on Functions](https://www.golang-book.com/books/intro/7)

Functions in Go must also be strongly typed - meaning you must type of the arguments and any returned values.

```go
package main

import "fmt"

func plus(a int, b int) int {
    return a + b
}

func plusPlus(a, b, c int) int {
    return a + b + c
}

func main() {

    res := plus(1, 2)
    fmt.Println("1 + 2 =", res)

    res = plusPlus(1, 2, 3)
    fmt.Println("1 + 2 + 3 =", res)
}
```

Output:

```
1 + 2 = 3
1 + 2 + 3 = 6
```

---
### Functions returning multiple values

Just as you can do in Python, functions in Go can return multiple values.  Notice the use of the `_` character below (Meaning that we don't care to keep the value returned by the function).

```go
package main

import "fmt"

func vals() (int, int) {
    return 3, 7
}

func main() {

    a, b := vals()
    fmt.Println(a)
    fmt.Println(b)

    _, c := vals()
    fmt.Println(c)
}
```

Output:

```
3
7
7
```


---
### Map

Maps are like Python's dictionaries.  You create a map in Go by using the `make` statement.  For example: `m := make(map[string]int)` creates a map of key (string) and value (int)

```go
package main

import "fmt"

func main() {

    m := make(map[string]int)

    m["k1"] = 7
    m["k2"] = 13

    fmt.Println("map:", m)

    v1 := m["k1"]
    fmt.Println("v1: ", v1)

    fmt.Println("len:", len(m))

    delete(m, "k2")
    fmt.Println("map:", m)

    _, prs := m["k2"]
    fmt.Println("prs:", prs)

    // make is not required as we are assigning the map values at creation
    n := map[string]int{"foo": 1, "bar": 2}
    fmt.Println("map:", n)
}
```

Output:

```
map: map[k1:7 k2:13]
v1:  7
len: 2
map: map[k1:7]
prs: false
map: map[bar:2 foo:1]
```

---
### Arrays

Arrays are created using `[]` when you define the variable.  For example: `var a [5]int` creates an array of 5 integers. `var twoD [2][3]int` creates a 2D array in integers.

```go
package main

import "fmt"

func main() {

    var a [5]int
    fmt.Println("emp:", a)

    a[4] = 100
    fmt.Println("set:", a)
    fmt.Println("get:", a[4])

    fmt.Println("len:", len(a))

    b := [5]int{1, 2, 3, 4, 5}
    fmt.Println("dcl:", b)

    var twoD [2][3]int
    for i := 0; i < 2; i++ {
        for j := 0; j < 3; j++ {
            twoD[i][j] = i + j
        }
    }
    fmt.Println("2d: ", twoD)
}
```

Output:

```
emp: [0 0 0 0 0]
set: [0 0 0 0 100]
get: 100
len: 5
dcl: [1 2 3 4 5]
2d:  [[0 1 2] [1 2 3]]
```

---
### Goroutines

A goroutine is a function that is capable of running concurrently with other functions. To create a goroutine we use the keyword go followed by a function invocation.

In this example, the function `say` is called from main normally and as a goroutine.  If you look at the output, you will see that each function of `say` is trying to display their string.

```go
package main

import (
    "fmt"
    "time"
)

func say(s string) {
    for i := 0; i < 5; i++ {
        time.Sleep(100 * time.Millisecond)
        fmt.Println(s)
    }
}

func main() {
    go say("world")
    say("hello")
}
```

Output:

```
world
hello
hello
world
world
hello
world
hello
world
hello
```

Another example where one of the goroutines using a lamda function.

```go
package main

import (
    "fmt"
    "time"
)

func f(from string) {
    for i := 0; i < 3; i++ {
        fmt.Println(from, ":", i)
    }
}

func main() {

    f("direct")

    go f("goroutine")

    go func(msg string) {
        fmt.Println(msg)
    }("going")

    time.Sleep(time.Second)
    fmt.Println("done")
}
```

Output:

```
direct : 0
direct : 1
direct : 2
going
goroutine : 0
goroutine : 1
goroutine : 2
done
```

---
### Channels

In Python, we could use Queue, Pipe, Shared Memory to pass data between threads/processes.  Go uses a channel which is close to a Pipe in Python.  A goroutine can add data to a channel and another goroutine can read from it.

Channels are created with the `chan` keyword.  For example: `c := make(chan int)` creates a channel of integers.

You add data to the channel using `<-`.  The statement `c <- 55` places 55 onto the channel.  The statement `<-c` reads a value from the channel.

```go
package main

import "fmt"

func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // send sum to c
}

func main() {
    s := []int{7, 2, 8, -9, 4, 0}

    c := make(chan int)
    go sum(s[:len(s)/2], c)     // Slice the array
    go sum(s[len(s)/2:], c)     // Slice the array
    x, y := <-c, <-c            // receive from c

    fmt.Println(x, y, x+y)
}
```

Output:

```
-5 17 12
```

---
### Using for range with a channel

In this example, the goroutine `fibonacci()` will place values in a channel.  The main function will use a `for range` statement to go through each value in the channel.  

Note that the goroutine `fibonacci()` closes the channel when it is finished.  This is important for the `for range` statement in main as the `for` loop would not know when the channel is finished being used.

```go
package main

import (
    "fmt"
)

func fibonacci(n int, c chan int) {
    x, y := 0, 1
    for i := 0; i < n; i++ {
        c <- x
        x, y = y, x+y
    }
    close(c)
}

func main() {
    c := make(chan int, 10)
    go fibonacci(cap(c), c)
    for i := range c {
        fmt.Println(i)
    }
}
```

Output:

```
0
1
1
2
3
5
8
13
21
34
```

---
### Work Pool

There are `thread` or work pools in Go. In this example, channels are used to allow 3 workers to process values from the channel.

```go
package main

import (
    "fmt"
    "time"
)

func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        fmt.Println("worker", id, "started  job", j)
        time.Sleep(time.Second)
        fmt.Println("  worker", id, "finished job", j)
        results <- j * 2
    }
}

func main() {

    const numJobs = 5
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)

    //  Create 3 workers - they will wait until values are in the channel
    for w := 1; w <= 3; w++ {
        go worker(w, jobs, results)
    }

    // Place 5 values in the channel - this will start the workers
    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    // Very important to close the channel so that the
    // workers can know when to finish
    close(jobs)

    // Get the results from a channel
    for a := 1; a <= numJobs; a++ {
        <-results
    }
}
```

Output:

```
worker 3 started  job 1
worker 1 started  job 2
worker 2 started  job 3
  worker 2 finished job 3
worker 2 started  job 4
  worker 1 finished job 2
worker 1 started  job 5
  worker 3 finished job 1
  worker 2 finished job 4
  worker 1 finished job 5
```

---
### Producer Consumer Problem

Here is the classic Producer/Consumer program in Go.  The `sync.WaitGroup` variable is used as a barrier so main() will know when the goroutines are finished.

```go
package main

import (
    "fmt"
    "sync"
)

func producer(wg *sync.WaitGroup, count int, ch chan int) {
    for i := 1; i <= count; i++ {
        ch <- i
    }
    ch <- -1
    fmt.Println("Producer Done!")
    wg.Done()
}

func consumer(wg *sync.WaitGroup, ch chan int) {
    valuesToGet := true
    for valuesToGet {
        value := <-ch
        if value == -1 {
            valuesToGet = false
        } else {
            fmt.Println(value)
        }
    }
    fmt.Println("Consumer Done!")
    wg.Done()
}

func main() {
    // "barrier"
    var wg sync.WaitGroup

    // Pipe from prod to consumer
    ch := make(chan int, 10)

    go producer(&wg, 15, ch)
    go consumer(&wg, ch)
    wg.Add(2)

    wg.Wait()
    fmt.Println("All done!")
}
```

Output:

```
1
2 
3 
4 
5 
6 
7 
8 
9 
10
11
12
13
14
15
Consumer Done!
Producer Done!
All done!
```

## Links

- Great free online book on the Go Language: https://www.golang-book.com/books/intro
