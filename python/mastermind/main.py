import random
colors = ['R','G','B','Y','W','O']
tries = 10
code_length = 4

def gen_code():
    code = []

    for i in range(code_length):
        color = random.choice(colors)
        code.append(color)

    return code

def guess_code():
    while True:

        guess = input("Guess the code : ").upper().split(" ")

        if len(guess) != code_length:
            print(f"You must guess {code_length} colors")
            continue
        
        for color in guess:
            if color not in colors:
                print(f"This {color} is not exist")
                break
        
        else:
            break

    return guess

def check_code(guess,gened_code):
    color_c = {}
    true_pos = 0
    false_pos = 0

    for color in gened_code:
        if color not in color_c:
            color_c[color] = 0
        color_c[color] += 1

    for g,c in zip(guess,gened_code):
    # guess = ['A','B'] gened_code = ['C','D']
    # zip = [('A','B'),('C','D')]
        if g == c:
            true_pos += 1
            color_c[g] -= 1
    
    for g,c in zip(guess,gened_code):
        if g in color_c and color_c[g] > 0:
            false_pos += 1
            color_c[g] -= 1
    
    return true_pos, false_pos

def game():
    print (f"Welcome to master mind, you have {tries} to guess the code")
    print (f"Avalible code : {colors}")
    print("Guess format : X X X X")
    code = gen_code()
    print(code)
    for attempts in range(1,tries+1):
        guess = guess_code()
        true_pos, false_pos = check_code(guess,code)

        if true_pos == code_length:
            print(f"You guessed code in {attempts} tries")
            break

        print(f"Correct Pos: {true_pos} | Incorrect Pos: {false_pos}")
        
    else:
        print(F"Game over! , the code was {code}")

if __name__ == "__main__":
    game()