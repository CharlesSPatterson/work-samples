package nfl

import (
	"fmt"
	conf "sdio-go/utils"
)

// Configuration

var SPORTSDATAIO_NFL_BASE_URL string = conf.SPORTSDATAIO_BASE_URL +
	conf.SPORTSDATAIO_API_VERSION + "/nfl/"

func PrintHello() {
	fmt.Println("nfl base url: " + SPORTSDATAIO_NFL_BASE_URL)
	//fmt.Println(conf.SPORTSDATAIO_API_VERSION)
	//fmt.Println(conf.SPORTSDATAIO_BASE_URL)
}
