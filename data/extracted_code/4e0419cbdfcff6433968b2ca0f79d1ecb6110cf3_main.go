package main

import (
	"fmt"
	"strconv"
)

// Day 20: Type casting
// Type casting means converting one data type to another
// eg. int to string or int to float
// https://golangdocs.com/type-casting-in-golang

func stringToInt() {
	var s string = "4000"
	v, _ := strconv.Atoi(s)
	fmt.Println("--- String to Int ---")
	fmt.Printf("The type is %T, %v\n", s, s)
	fmt.Printf("The type is %T, %v\n", v, v)
}

func intToString() {
	var i int = 42
	s := strconv.Itoa(i)
	fmt.Println("\n--- Int to String ---")
	fmt.Printf("The type is %T, %v\n", i, i)
	fmt.Printf("The type is %T, %v\n", s, s)
}

func floatToInt() {
	f := 12.56784242
	i := int(f)
	fmt.Println("\n--- Float to Int ---")
	fmt.Printf("The type is %T, %v\n", f, f)
	fmt.Printf("The type is %T, %v\n", i, i)
}

func stringToBytes() {
	s := "Hello, Gophers!"
	b := []byte(s)
	fmt.Println("\n--- String to Bytes ---")
	fmt.Printf("The type is %T, %v\n", s, s)
	fmt.Printf("The type is %T, %v\n", b, b)
	// can also convert back to string with b
	ss := string(b)
	fmt.Printf("The type is %T, %v\n", ss, ss)
}

func main() {
	stringToInt()
	intToString()
	floatToInt()
	stringToBytes()
}