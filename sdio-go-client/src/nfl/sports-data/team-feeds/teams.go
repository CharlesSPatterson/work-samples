package teams

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"sdio-go/src/nfl"
	players "sdio-go/src/nfl/sports-data/player-feeds"
	conf "sdio-go/utils"
	"strconv"
)

type Team struct {
	Key                          string
	TeamID                       int
	PlayerID                     int
	City                         string
	Name                         string
	Conference                   string
	Division                     string
	FullName                     string
	StadiumID                    int
	ByeWeek                      int
	AverageDraftPosition         float32
	AverageDraftPositionPPR      float32
	HeadCoach                    string
	OffensiveCoordinator         string
	DefensiveCoordinator         string
	SpecialTeamsCoach            string
	OffensiveScheme              string
	DefensiveScheme              string
	UpcomingSalary               string
	UpcomingOpponent             string
	UpcomingOpponentRank         int
	UpcomingOpponentPositionRank int
	UpcomingFanDuelSalary        int
	UpcomingDraftKingsSalary     int
	UpcomingYahooSalary          int
	PrimaryColor                 string
	SecondaryColor               string
	TertiaryColor                string
	QuarternaryColor             string
	WikipediaLogoUrl             string
	WikipediaWordMarkUrl         string
	GlobalTeamID                 int
	DraftKingsName               string
	DraftKingsPlayerID           int
	FanDuelName                  string
	FanDuelPlayerID              int
	FantasyDraftName             string
	FantasyDraftPlayerID         int
	YahooName                    string
	YahooPlayerID                int
	AverageDraftPosition2QB      float32
	AverageDraftPositionDynasty  float32
	StadiumDetails               Stadium
}

type Stadium struct {
	StadiumID      int
	Name           string
	City           string
	State          string
	Country        string
	Capacity       int
	PlayingSurface string
	GeoLat         float32
	GeoLong        float32
	Type           string
}

type TeamDepthChart struct {
	TeamID       int
	Offense      []OffensiveDepthChart
	Defense      []DefensiveDepthChart
	SpecialTeams []SpecialTeamsDepthChart
}

type OffensiveDepthChart struct {
	Players []DepthChartDetail
}

type DefensiveDepthChart struct {
	Players []DepthChartDetail
}

type SpecialTeamsDepthChart struct {
	Players []DepthChartDetail
}

type DepthChartDetail struct {
	DepthChartID     int
	TeamID           int
	PlayerID         int
	Name             string
	PositionCategory string
	Position         string
	DepthOrder       int
	Updated          string
}

type Injury struct {
	InjuryID            int
	SeasonType          int
	Season              int
	Week                int
	PlayerID            int
	Name                string
	Team                string
	Opponent            string
	BodyPart            string
	Status              string
	Practice            string
	PracticeDescription string
	Updated             string
	DeclaredInactive    string
	TeamID              int
	OpponentID          int
}

// Returns an array of Team objects for teams who are active
func GetActiveTeams() []Team {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Teams/" + "?key=" + conf.API_KEY

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

	var teamsArrayResponse []Team
	json.Unmarshal(responseData, &teamsArrayResponse)

	return teamsArrayResponse
}

// Returns an array of all possible Teams
func GetAllTeams() []Team {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/AllTeams/" + "?key=" + conf.API_KEY

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

	var teamsArrayResponse []Team
	json.Unmarshal(responseData, &teamsArrayResponse)

	return teamsArrayResponse
}

// Returns an array of teams playing in a particular season
// Year of the season and the season type. If no season type is provided, then the default is regular season.
// Examples: 2015REG, 2015PRE, 2015POST.
func GetTeamsBySeason(season string) []Team {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/Teams/" + season + "?key=" + conf.API_KEY

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

	var teamsArrayResponse []Team
	json.Unmarshal(responseData, &teamsArrayResponse)

	return teamsArrayResponse
}

// Returns an array of team depth charts for all NFL teams
// split by offensive, defensive, and special teams position grouping
func GetDepthCharts() []TeamDepthChart {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/DepthCharts/" + "?key=" + conf.API_KEY

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

	var depthCharts []TeamDepthChart
	json.Unmarshal(responseData, &depthCharts)

	return depthCharts
}

// Returns an array of all currently injured players
func GetInjuredPlayers() []players.Player {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"scores/json/InjuredPlayers" + "?key=" + conf.API_KEY

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

	var injuredPlayers []players.Player
	json.Unmarshal(responseData, &injuredPlayers)

	return injuredPlayers
}

// Returns an array of injuries by season and week. If no season type is provided, then the default is regular season.
// Examples: 2015REG, 2015PRE, 2015POST. Valid values for the week are as follows:
// Preseason 0 to 4, Regular Season 1 to 17, Postseason 1 to 4. Example: 1
func GetInjuriesBySeasonAndWeek(season string, week int) []Injury {

	var endpoint string = nfl.SPORTSDATAIO_NFL_BASE_URL +
		"stats/json/Injuries/" + season + "/" + strconv.Itoa(week) +
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

	var injuriesResponse []Injury
	json.Unmarshal(responseData, &injuriesResponse)

	return injuriesResponse
}
