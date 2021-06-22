package main

import "fmt"

func main() {
	x := 5
	y := 10

	// If else
	if x < y {
		fmt.Printf("%d is less Than %d\n", x, y)
	} else {
		fmt.Printf("%d is less Than %d\n", y, x)
	}

	// else if
	color := "red"

	if color == "red" {
		fmt.Println("1 Color is red")
	} else if color == "blue" {
		fmt.Println("1 color is blue")
	} else {
		fmt.Println("1 color is neiter red nor blue")
	}

	// Switch
	switch color {
	case "red":
		fmt.Println("2 Color is red")
	case "blue":
		fmt.Println("2 color is blue")
	default:
		fmt.Println("2 Color is not blue nor red")
	}
}
