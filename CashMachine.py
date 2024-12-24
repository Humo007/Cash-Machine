def CashMachine(a: str, b: str):
    x = 3
    y = 3
    for a1, b1 in zip(a, b):
        if a1 == 'share' and b1 == 'share':
            x += 2
            y += 2
        elif a1 == 'steal' and b1 == 'share':
            x += 3
            y -= 1
        elif a1 == 'share' and b1 == 'steal':
            x -= 1
            y += 3    
        elif a1 == 'steal' and b1 == 'steal':
            x += 0
            y += 0        
            
    return [x, y]



list1 = input("Enter first player's action (share or steal): ").strip().lower().split(', ')
list2 = input("Enter second player's action (share or steal): ").strip().lower().split(', ')

print(CashMachine(list1, list2))