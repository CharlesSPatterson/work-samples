package main

import (
	"fmt"
	"sdio-go/src/nfl"
	players "sdio-go/src/nfl/sports-data/player-feeds"
	//"sync"
	//"time"
	//"math/rand"
)

func executeDraft(teamCount int) {
	//var draft sync.WaitGroup

}

func main() {
	//var draft sync.WaitGroup
	fmt.Println("Rockbot go sample start")
	nfl.PrintHello()
	// players.GetPlayerDetailsByAvailable()
	//players.GetPlayer(732)
	//result = players.GetPlayerDetailsByTeam("WAS")
	fmt.Println(players.GetPlayer(12))
}
