#evens_odds

def evens(n):
    evens_list = []

    for i in range(1, n + 1):
        evens_list.append(2 * i)
    return evens_list

def odds(n):
    odds_list = []

    for i in range(n):
        odds_list.append(2 * i + 1)
    return odds_list

print(evens(4))
print(odds(7))
