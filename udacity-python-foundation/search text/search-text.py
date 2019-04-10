#searching text for curse words
import urllib
text_path = 'quotes.txt'


def read_text(path):
   with open(path, "r") as text:
        contents_of_file = text.read()
        check(contents_of_file)


def check(text):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text)
    import pdb; pdb.set_trace()
    output = connection.read()
    connection.close()
    if "false" in output:
        print('No curse words found :)')
    elif "true" in output:
        print('Curse words alert!')


read_text('quotes.txt')
