package players

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"sdio-go/src/nfl"
	conf "sdio-go/utils"
	"strconv"
)

type Player struct {
	PlayerID                            int
	Team                                string
	Number                              uint8
	FirstName                           string
	LastName                            string
	Position                            string
	Status                              string
	Height                              string
	Weight                              uint8
	BirthDate                           string
	College                             string
	Experience                          uint8
	FantasyPosition                     string
	Active                              bool
	PositionCategory                    string
	FullName                            string
	Age                                 uint8
	ExperienceString                    string
	BirthDateString                     string
	PhotoURL                            string
	ByeWeek                             uint8
	UpcomingGameOpponent                string
	UpcomingGameWeek                    uint8
	ShortName                           string
	AverageDraftPosition                float32
	DepthPositionCategory               string
	DepthPosition                       string
	DepthOrder                          uint8
	DepthDisplayOrder                   uint8
	CurrentTeam                         string
	CollegeDraftTeam                    string
	CollegeDraftYear                    uint16
	CollegeDraftRound                   uint8
	CollegeDraftPick                    uint8
	IsUndraftedFreeAgent                bool
	HeightFeet                          uint8
	HeightInches                        uint8
	UpcomingOpponentRank                uint8
	UpcomingOpponentPositionRank        uint8
	CurrentStatus                       string
	UpcomingSalary                      int
	FantasyAlarmPlayerID                int
	SportRadarPlayerID                  string
	RotoworldPlayerID                   int
	RotoWirePlayerID                    int
	StatsPlayerID                       int
	SportsDirectPlayerID                int
	XmlTeamPlayerID                     int
	FanDuelPlayerID                     int
	DraftKingsPlayerID                  int
	YahooPlayerID                       int
	InjuryStatus                        string
	InjuryBodyPart                      string
	InjustStartDate                     string
	InjuryNotes                         string
	FanDuelName                         string
	DraftKingsName                      string
	YahooName                           string
	FantasyPositionDepthOrder           uint8
	InjuryPractice                      string
	InjuryPracticeDescription           string
	DeclaredInactive                    bool
	UpcomingFanDuelSalary               int
	UpcomingDraftKingsSalary            int
	UpcomingYahooSalary                 int
	TeamID                              uint8
	GlobalTeamID                        uint8
	FantasyDraftPlayerID                int
	FantasyDraftName                    string
	UsaTodayPlayerID                    int
	UsaTodayHeadshotURL                 string
	UsaTodayHeadshotNoBackgroundURL     string
	UsaTodayHeadshotNoBackgroundUpdated string
	PlayerSeason                        string   // API type unclear
	LatestNews                          []string // API type unclear, possibly need new struct
}

// Returns an array of Player objects for players who are available to play
func GetAvailablePlayers() []Player {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Players/" + "?key=" + conf.API_KEY

	response, err := http.Get(endpoint)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("error not nil")
		log.Fatal(err)
	}

	var playersArrayResponse []Player
	json.Unmarshal(responseData, &playersArrayResponse)

	return playersArrayResponse
}

// Returns an array of Player objects for players who are free agents
func GetFreeAgents() []Player {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/FreeAgents/" + "?key=" + conf.API_KEY

	response, err := http.Get(endpoint)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("error not nil")
		log.Fatal(err)
	}

	var playersArrayResponse []Player
	json.Unmarshal(responseData, &playersArrayResponse)

	return playersArrayResponse
}

// Returns an array of Player objects for players in a given draft year
func GetPlayersByRookieDraftYear(rookieYear int) []Player {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Rookies/" + strconv.Itoa(rookieYear) +
		"?key=" + conf.API_KEY

	response, err := http.Get(endpoint)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("error not nil")
		log.Fatal(err)
	}

	var playersArrayResponse []Player
	json.Unmarshal(responseData, &playersArrayResponse)

	return playersArrayResponse
}

// Returns a Player object using the SportsDataIO player ID
func GetPlayer(playerID int) Player {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Player/" + strconv.Itoa(playerID) +
		"?key=" + conf.API_KEY

	response, err := http.Get(endpoint)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("error not nil")
		log.Fatal(err)
	}

	var returnedPlayer Player
	json.Unmarshal(responseData, &returnedPlayer)

	return returnedPlayer
}

// Returns an array of Player objects based on team abbreviation (i.e. 'WAS', 'PHI')
func GetPlayerDetailsByTeam(teamAbbreviation string) []Player {

	// TODO: API does not check abbreviation validity, check against set of constants

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Players/" + teamAbbreviation +
		"?key=" + conf.API_KEY

	response, err := http.Get(endpoint)
	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println("error not nil")
		log.Fatal(err)
	}

	var playersArrayResponse []Player
	json.Unmarshal(responseData, &playersArrayResponse)

	return playersArrayResponse
}
