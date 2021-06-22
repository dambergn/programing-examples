package main

import "fmt"

func main() {
	// Arrays (fixed length)
	var fruitArr [2]string

	// Assign Values
	fruitArr[0] = "Apple"
	fruitArr[1] = "Orange"

	fmt.Println(fruitArr)
	fmt.Println(fruitArr[1])

	// Declare and assign
	vegArr := [2]string{"Carrot", "Potato"}
	fmt.Println(vegArr)

	// Slice
	fruitSlice := []string{"Apple", "Orange", "Grape", "Cherry"}

	fmt.Println(fruitSlice)
	fmt.Println(len(fruitSlice))
}
