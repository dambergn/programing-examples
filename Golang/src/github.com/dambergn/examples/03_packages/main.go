package main

import (
	"fmt"
	"math"

	"github.com/ndamberg/examples/03_packages/strutil"
)

// go env -w GO111MODULE=off

func main() {
	fmt.Println(math.Floor(2.7))
	fmt.Println(math.Ceil(2.7))
	fmt.Println(math.Sqrt(16))
	fmt.Println(strutil.Reverse("olleh"))
}
