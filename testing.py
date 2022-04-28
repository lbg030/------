def solve(start, end):
    result = 0
    for i in range(start, end):
        result += i

    return result


start = int(input())
end = int(input())

answer = solve(start, end)

print(f"Sum from {start} to {end} is {answer}")
