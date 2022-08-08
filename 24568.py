def cupcake_party(regular_box, small_box):
    whole_cupcake = regular_box * 8 + small_box * 3
    
    answer = whole_cupcake - 28
    
    if answer < 0:
        answer = 0
    
    return answer


if __name__ == "__main__":
    regular_box = int(input())
    small_box = int(input())
    
    print(cupcake_party(regular_box, small_box))
