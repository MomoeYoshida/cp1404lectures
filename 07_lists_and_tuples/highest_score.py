"""
Activity - Create a list
Complete this program that asks the user for their
scores and adds them to the list, until they enter
a negative score, then prints their highest score.
"""

scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))
print("Your highest score is", max(scores))