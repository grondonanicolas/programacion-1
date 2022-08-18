## This is a example
def calculate_animals(total_heads, total_legs):
    CHICKEN_LEGS = 2
    RABBIT_LEGS = 4
    for i in range(total_heads + 1):
        chicken_quantity_candidate = total_heads - i
        rabbit_quantity_candidate = i
        total_legs_candidate = chicken_quantity_candidate * CHICKEN_LEGS + rabbit_quantity_candidate * RABBIT_LEGS
        if total_legs_candidate == total_legs:
            return chicken_quantity_candidate, rabbit_quantity_candidate
    print("incoppatible animals and heads")
    return 0,0

print(calculate_animals(35,94))