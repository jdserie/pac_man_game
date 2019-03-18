# I realized I did this the hard way when I was nearly done
# I am curious where I went wrong... I want this to work



points = 5000
tmp_points = 5000

f = open("game.txt", "r")
x = f.read().split(",")


def start():
    lives = 3
    while lives > 3:
        for i in x:
            if i == "VulnerableGhost":
                points += 200
                tmp_points += 200
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
                elif i == "VulnerableGhost":
                    points += 400
                    tmp_points += 400 
                    if tmp_points >= 10000:
                        lives += 1
                        points += tmp_points
                        tmp_points -= 10000
                    elif i == "VulnerableGhost":
                        points += 800
                        tmp_points += 800 
                        if tmp_points >= 10000:
                            lives += 1
                            points += tmp_points
                            tmp_points -= 10000
                        elif i == "VulnerableGhost":
                            points += 1600
                            tmp_points += 1600
                            if tmp_points >= 10000:
                                lives += 1
                                points += tmp_points
                                tmp_points -= 10000
                        else:
                            break
                    else:
                        break
                else:
                    break
            elif i == "Dot":
                points += 10
                tmp_points += 10 
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Melon":
                points += 1000
                tmp_points += 1000
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Cherry":
                points += 100
                tmp_points += 100 
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Strawberry":
                points += 300
                tmp_points += 300
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Orange":
                points += 500
                tmp_points += 500
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Apple":
                points += 700
                tmp_points += 700 
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Galaxian":
                points += 2000
                tmp_points += 2000 
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Bell":
                points += 3000
                tmp_points += 3000
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "Key":
                points += 5000
                tmp_points += 5000 
                if tmp_points >= 10000:
                    lives += 1
                    points += tmp_points
                    tmp_points -= 10000
            elif i == "InvincibleGhost":
                lives -= 1
                break
            else:
                lives = 0
                break

start()
print(f'{points}')





