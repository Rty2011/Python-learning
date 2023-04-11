import random

# 게임 초기화
score = [0, 0]
team1 = input("Enter name for team 1: ")
team2 = input("Enter name for team 2: ")

# 게임 루프
while True:
    attacking_team = random.choice([team1, team2])
    defending_team = team2 if attacking_team == team1 else team1
    print(f"{attacking_team} is attacking! {defending_team} is defending!")
    input("Press enter to shoot...")

    # 골인 여부 결정
    if random.random() < 0.3:
        print(f"GOAL!!! {attacking_team} scores!")
        score[0 if attacking_team == team1 else 1] += 1
    else:
        print(f"{attacking_team}'s shot missed the goal!")
    print(f"Score: {team1} {score[0]} - {score[1]} {team2}")

    # 게임 종료 조건
    if score[0] >= 3 or score[1] >= 3:
        print("Game over!")
        winner = team1 if score[0] > score[1] else team2
        print(f"{winner} wins!")
        break