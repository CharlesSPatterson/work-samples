data = {
    "Teams":{
        1:{
            "name": "Lakers",
            "city": "Los Angeles",
            "full_name": "Los Angeles Lakers",
            "abbrev": "LAL"
        },
        2:{
            "name": "Cavaliers",
			"city": "Cleveland",
			"full_name": "Cleveland Cavaliers",
			"abbrev": "CLE"
        },
        3:{
            "name": "Clippers",
			"city": "Los Angeles",
			"full_name": "Los Angeles Clippers",
			"abbrev": "LAC"
        },
		4:{
            "name": "Warriors",
			"city": "Golden State",
			"full_name": "Golden State Warriors",
			"abbrev": "GSW"
        },
        5:{
            "name": "Hawks",
			"city": "Atlanta",
			"full_name": "Atlanta Hawks",
			"abbrev": "ATL"
        },
        6:{
            "name": "Raptors",
			"city": "Toronto",
			"full_name": "Toronto Raptors",
			"abbrev": "TOR"
        },
    },    
    "Players":{
		1:{
			"name": "Nick Young",
			"team_id": 1
		},
		2:{
			"name": "Lou Williams",
			"team_id": 1
		},
		3: {
			"name": "Lebron James",
			"team_id": 2
		},
		4: {
			"name": "Kyrie Irving",
			"team_id": 2
		},
		5: {
			"name": "Chris Paul",
			"team_id": 3
		},
		6: {
			"name": "Blake Griffin",
			"team_id": 3
		},
		7: {
			"name": "Kevin Durant",
			"team_id": 4
		},
		8: {
			"name": "Stephen Curry",
			"team_id": 4
		},
		9: {
			"name": "Dwight Howard",
			"team_id": 5
		},
		10: {
			"name": "Kyle Korver",
			"team_id": 5
		},
		11: {
			"name": "Kyle Lowry",
			"team_id": 6
		},
		12: {
			"name": "DeMar DeRozan",
			"team_id": 6
		}
	},
    "Games":{
		1: {
			"home_team_id": 1,
			"away_team_id": 2,
			"date": "1/1/2016"
		},
		2: {
			"home_team_id": 3,
			"away_team_id": 4,
			"date": "1/1/2016"
		},
		3: {
			"home_team_id": 5,
			"away_team_id": 6,
			"date": "1/1/2016"
		},
		4: {
			"home_team_id": 2,
			"away_team_id": 3,
			"date": "1/2/2016"
		},
		5: {
			"home_team_id": 1,
			"away_team_id": 4,
			"date": "1/3/2016"
		},
	},
    "Player Stats":{
		1:{
			"game_id": 1,
			"player_id": 1,
			"team_id": 1,
			"points": 20,
			"assists": 10,
			"rebounds": 2,
			"nerd": 10
		},
		2: {
			"game_id": 1,
			"player_id": 2,
			"team_id": 1,
			"points": 15,
			"assists": 2,
			"rebounds": 2,
			"nerd": -1
		},
		3: {
			"game_id": 1,
			"player_id": 3,
			"team_id": 2,
			"points": 10,
			"assists": 2,
			"rebounds": 20,
			"nerd": 20
		},
		4: {
			"game_id": 1,
			"player_id": 4,
			"team_id": 2,
			"points": 5,
			"assists": 1,
			"rebounds": 2,
			"nerd": -10
		},
		5: {
			"game_id": 2,
			"player_id": 5,
			"team_id": 1,
			"points": 23,
			"assists": 10,
			"rebounds": 2,
			"nerd": 2.7
		},
		6: {
			"game_id": 2,
			"player_id": 6,
			"team_id": 1,
			"points": 12,
			"assists": 2,
			"rebounds": 2,
			"nerd": -8.9
		},
		7: {
			"game_id": 2,
			"player_id": 7,
			"team_id": 2,
			"points": 11,
			"assists": 2,
			"rebounds": 20,
			"nerd": 15.2
		},
		8: {
			"game_id": 2,
			"player_id": 8,
			"team_id": 2,
			"points": 15,
			"assists": 1,
			"rebounds": 2,
			"nerd": 13
		},
		9: {
			"game_id": 3,
			"player_id": 9,
			"team_id": 1,
			"points": 19,
			"assists": 10,
			"rebounds": 2,
			"nerd": -2
		},
		10: {
			"game_id": 3,
			"player_id": 10,
			"team_id": 1,
			"points": 7,
			"assists": 2,
			"rebounds": 2,
			"nerd": -17
		},
		11: {
			"game_id": 3,
			"player_id": 11,
			"team_id": 2,
			"points": 20,
			"assists": 2,
			"rebounds": 20,
			"nerd": 21
		},
		12: {
			"game_id": 3,
			"player_id": 12,
			"team_id": 2,
			"points": 1,
			"assists": 1,
			"rebounds": 2,
			"nerd": 21
		},
		13: {
			"game_id": 4,
			"player_id": 3,
			"team_id": 2,
			"points": 5,
			"assists": 11,
			"rebounds": 12,
			"nerd": 3
		},
		14: {
			"game_id": 4,
			"player_id": 5,
			"team_id": 3,
			"points": 9,
			"assists": 1,
			"rebounds": 12,
			"nerd": -12
		},
		15: {
			"game_id": 4,
			"player_id": 6,
			"team_id": 3,
			"points": 17,
			"assists": 12,
			"rebounds": 12,
			"nerd": -7
		},
		16: {
			"game_id": 4,
			"player_id": 4,
			"team_id": 2,
			"points": 2,
			"assists": 12,
			"rebounds": 2,
			"nerd": 2
		},
		17: {
			"game_id": 5,
			"player_id": 8,
			"team_id": 4,
			"points": 25,
			"assists": 14,
			"rebounds": 6,
			"nerd": 9
		},
		18: {
			"game_id": 5,
			"player_id": 1,
			"team_id": 1,
			"points": 9,
			"assists": 3,
			"rebounds": 7,
			"nerd": -21
		},
		19: {
			"game_id": 5,
			"player_id": 2,
			"team_id": 1,
			"points": 27,
			"assists": 4,
			"rebounds": 9,
			"nerd": 7
		},
		20: {
			"game_id": 5,
			"player_id": 7,
			"team_id": 4,
			"points": 2,
			"assists": 8,
			"rebounds": 12,
			"nerd": 15
		}
	},
    "Game States":{
		1: {
			"game_id": 1,
			"home_team_score": 78,
			"away_team_score": 77,
			"broadcast": "ESPN",
			"quarter": 4,
			"time_left_in_quarter": "10:20",
			"game_status": "IN PROGRESS"
		},
		2: {
			"game_id": 2,
			"home_team_score": 10,
			"away_team_score": 20,
			"broadcast": "TNT",
			"quarter": 2,
			"time_left_in_quarter": "1:00",
			"game_status": "IN PROGRESS"
		},
		3: {
			"game_id": 3,
			"home_team_score": 100,
			"away_team_score": 99,
			"broadcast": "TNT",
			"quarter": 4,
			"time_left_in_quarter": "0:00",
			"game_status": "FINAL"
		},
		4: {
			"game_id": 4,
			"home_team_score": 20,
			"away_team_score": 30,
			"broadcast": "ROOT",
			"quarter": 4,
			"time_left_in_quarter": "10:20",
			"game_status": "IN PROGRESS"
		},
		5: {
			"game_id": 5,
			"home_team_score": 120,
			"away_team_score": 100,
			"broadcast": "ESPN3",
			"quarter": 4,
			"time_left_in_quarter": "0:00",
			"game_status": "FINAL"
		},
	}
}