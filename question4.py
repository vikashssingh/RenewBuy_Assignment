# Create a function that takes a list of football clubs with properties: name, wins,
# loss, draws, scored, conceded, and returns the team name with the highest
# number of points. If two teams have the same number of points, return the
# team with the largest goal difference.
# How to Calculate Points and Goal Difference
# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
# "conceded": 20 }
# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68


#Solution



def RankTeams(arr):
	for i in range(len(arr)):
		if(arr[i][0] == arr[i][1]):
			print("Invalid")
			return
		arr[i][2] = int(arr[i][2])
		arr[i][3] = int(arr[i][3])


	table = {}
	
	for i in range(len(arr)):
	

		li1 = [0] * 4
		li2 = [0] * 4
		if arr[i][0] in table:
			li1 = table[arr[i][0]]
			
		if arr[i][1] in table:
			li2 = table[arr[i][1]]
		li1[2] += arr[i][2]
		li1[3] += arr[i][3]
		li2[2] += arr[i][3]
		li2[3] += arr[i][2]
		li1[1] = li1[2] - li1[3]
		li2[1] = li2[2] - li2[3]
		if(arr[i][2] == arr[i][3]):
			li1[0] += 1
			li2[0] += 1

		elif(arr[i][2] > arr[i][3]):
			li1[0] += 2
		elif(arr[i][2] < arr[i][3]):
			li2[0] += 2
		table[arr[i][0]] = li1
		table[arr[i][1]] = li2

	for key, value in sorted(table.items(),
							key = lambda r: (-r[1][0],
											-r[1][1],
											-r[1][2],
											r[0])):
		print(key, end ='\n')
arr = [['Manchester United', 'England', '3', '0']]
RankTeams(arr)




