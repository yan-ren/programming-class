'''
*****
 ****
  ***
   **
    *
'''
for row in range(5):
    for col in range(5):
        if col < row:
            print(' ', end='')
        else:
            print('*', end='')
    print()