#Chris Plowman
#PA3
#CS151
#10/28/21

def getChoice():
    return input("What statistic would you like to find? (Football/Quidditch/Gymnastics): ").strip().lower()

def getCompleteions():
    return int(input("Enter the # of completeions made: "))

def getAttempts():
    return int(input("Enter the # of attempts made: "))

def getPassingYards():
    return int(input("Enter the # of passing yards: "))

def getTDPasses():
    return int(input("Enter the # of touch down passes: "))

def getInterceptions():
    return int(input("Enter the # of interceptions: "))

def getQBRating(completions,attempts,passing_yards,TDpasses,interceptions):
    return 100 * (5 * (completions/attempts - 0.3) + 0.25 * (passing_yards/attempts - 3) + 20 * (TDpasses/attempts) + 2.375 - (25 * interceptions/attempts)) / 6

def getGoals():
    return int(input("Enter the # of goals scored by the team: "))

def getCatches():
    return int(input("How many goals were catches: "))

def getScore(catches, goals):
    return (goals * 10) + (catches * 30)

def getDifScore():
    return int(input("What is the difficulty score of the apparatus: "))

def getScoring(DifScore):
    Total_Score = 0
    count = 1
    while count < 6:
        points = int(input("Enter the score: "))
        Total_Score += points
        count += 1
    return (Total_Score / 5) + DifScore


def main():

    choice = getChoice()

    if choice == 'football':

        completions = getCompleteions()
        attempts = getAttempts()
        passing_yards = getPassingYards()
        TDpasses = getTDPasses()
        interceptions = getInterceptions()
        QB_Rating = getQBRating(completions,attempts,passing_yards,TDpasses,interceptions)
        QB_Rating = (round(QB_Rating, 2))
        print(QB_Rating)
        if QB_Rating > 158.3:
            print("This player has a perfect rating or higher!")

    elif choice == 'quidditch':
        goals = getGoals()
        catches = getCatches()
        score = getScore(catches, goals)
        print("The score of that team is: ", score)


    elif choice == 'gymnastics':
        DifScore = getDifScore()
        scoring = getScoring(DifScore)
        print ("The final score of the apparatus is: ",(round(scoring, 2)))

    else:
        print("Invalid statistic selection")

main()

