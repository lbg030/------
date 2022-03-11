
def solution(attack, recovery, hp):
    count = 0
    while(True):
        count += 1
        hp -= recovery
        if hp <= 0:
            break
        hp += recovery
    return count
