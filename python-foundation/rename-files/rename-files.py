import os


def rename_files():
    file_list = os.listdir('prank')
    #print(file_list)

    first_path = os.getcwd()
    print(first_path)

    os.chdir('prank')
    for file_name in file_list:
        new_file_name = file_name.translate(None, '1234567890')
        print('old file name: '+file_name)
        print('new file name: '+new_file_name)
        os.rename(file_name, new_file_name)
    os.chdir(first_path)


rename_files()
#print(os.listdir('prank'))
