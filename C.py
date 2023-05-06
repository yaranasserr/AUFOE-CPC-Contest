V, A, B, C = map(int, input().split())
while True:
    
    V -= A  # Takahashi's father uses shampoo
    if V < 0:  # check if he ran out of shampoo
        print("F")
        break

    V -= B  # Takahashi's mother uses shampoo
    if V < 0:  # check if she ran out of shampoo
        print("M")
        break

    V -= C  # Takahashi uses shampoo
    if V < 0:  # check if he ran out of shampoo
        print("T")
        break