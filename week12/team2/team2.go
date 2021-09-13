/* ---------------------------------------
Course: CSE 251
Lesson Week: ?12
File: team.go
Author: Brother Comeau

Purpose: team activity - finding primes

Instructions:

- Process the array of numbers, find the prime numbers using goroutines

worker()

This goroutine will take in a list/array/channel of numbers.  It will place
prime numbers on another channel


readValue()

This goroutine will display the contents of the channel containing
the prime numbers

--------------------------------------- */
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func isPrime(n int) bool {
	// Primality test using 6k+-1 optimization.
	// From: https://en.wikipedia.org/wiki/Primality_test

	if n <= 3 {
		return n > 1
	}

	if n%2 == 0 || n%3 == 0 {
		return false
	}

	i := 5
	for (i * i) <= n {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func worker() {
	// TODO - process numbers on one channel and place prime number on another
}

func readValues() {
	// TODO -Display prime numbers from a channel
}

func main() {

	workers := 10
	numberValues := 100

	// create workers
	for w := 1; w <= workers; w++ {
		go worker() // Add any arguments
	}

	rand.Seed(time.Now().UnixNano())
	for i := 0; i < numberValues; i++ {
		// ch <- rand.Int()
	}

	go readValues() // Add any arguments

	fmt.Println("All Done!")
}
