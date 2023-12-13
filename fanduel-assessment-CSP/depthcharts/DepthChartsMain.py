from Players import Player
from DepthCharts import DepthChart

Bob = Player(1, "Bob")
Alice = Player(2, "Alice")
Charlie = Player(3, "Charlie")

dc = DepthChart()
dc.addPlayerToDepthChart(Bob, "WR", 0)
dc.addPlayerToDepthChart(Alice, "WR", 0)
dc.addPlayerToDepthChart(Charlie, "WR", 2)
dc.addPlayerToDepthChart(Bob, "KR")

dc.getFullDepthChart()

dc.getPlayersUnderPlayerInDepthChart(Alice, "WR")