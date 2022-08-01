def defense_rate(a, b):
    return a - a * b / 100

def is_lower_rate(d_rate):
    is_lower = 0
    
    if d_rate < 100:
        is_lower = 1
        
    return is_lower


if __name__ == "__main__":
    a, b = map(int, input().split())
    
    d_rate = defense_rate(a, b)
    
    print(is_lower_rate(d_rate))