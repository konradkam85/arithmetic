import random

def addition(x,y):
    print(f'{x} + {y} = ')
    return x + y

c = None    # chart in while loop condition

# Loop untill pressing 'q'
while c != 'q':
    x = random.randrange(0,20,1)
    y = random.randrange(0,10,1)

    result = addition(x,y)
    answer = input()

    ## Test if the input is an integer
    try:
        answer=int(answer)
    except ValueError:
        try:
            answer = float(answer)
            print('This is a float. Should be an integer.') 
        except ValueError:
            print(f'{answer} is not a number.')
    
    ## Check if the answer is correct
    if result == answer:
        print('Success!')
    else:
        print('Try again...')

    c = input('Press ENTER for next or q to quit: ')
