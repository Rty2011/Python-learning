import random

# 선수 리스트
players = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Hazard", "Salah", "De Bruyne", "Lewandowski", "Van Dijk", "Kane"]

# 골키퍼 리스트
goalkeepers = ["Neuer", "De Gea", "Courtois", "Allison", "Ederson", "Buffon", "Ter Stegen", "Navas", "Lloris", "Oblak"]

# 슛 결과 리스트
shoot_results = ["Goal!", "Saved by the goalkeeper", "Missed the goal"]

# 랜덤으로 선수와 골키퍼 선택
player = random.choice(players)
goalkeeper = random.choice(goalkeepers)

# 결과 출력
print("Player:", player)
print("Goalkeeper:", goalkeeper)

# 슛 결과 랜덤 선택
shoot_result = random.choice(shoot_results)

# 슛 결과 출력
print("Shoot result:", shoot_result)
