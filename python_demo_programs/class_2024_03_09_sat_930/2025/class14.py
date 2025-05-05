'''
File handling
Read and write file in python
'''
# i = 0
# with open('resources/note.txt', 'r') as file:
#     # context = file.read()
#     for line in file:
#         print(i, line)
#         i += 1

# print(context)

# note = input('Write a note to save:')
# note1 = 'line first'
# note2 = 'line second'
# note3 = 'line third'
# with open('note.txt', 'w') as file:
#     file.write(note1+'\n')
#     file.write(note2+'\n')
#     file.write(note3+'\n')

'''
use input() to gather user typing, for each typing writes it
into note.txt, if people type 'exit', finish the program
'''
# with open('note.txt', 'w') as file:
#     while True:
#         user_input = input('Type something or type exit to quit')
#         if user_input == 'exit':
#             break
#
#         file.write(user_input + '\n')

'''
Personal Diary
let user write a diary entry and save it to a file. The user can also read past entries
'''
def write_entry():
    entry = input('Write your diary entry:\n')
    with open('diary.text', 'a') as file:
        file.write(entry + '\n')
    print('Your entry has been saved!')

def read_entries():
    print('\nYour Diary Entries:')
    with open('diary.txt', 'r') as file:
        for line in file:
            print('- ' + line.strip())