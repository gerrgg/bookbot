book_dir = 'books'

def main(filename):
  path = f"{book_dir}/{filename}"
  content = get_book_text(path)
  wc = get_word_count(content)
  char_count = get_char_count(content)
  report(path, wc, char_count)

def get_book_text(path):
  with open(path, 'r') as file:
    content = file.read()
    return content

def get_word_count(content):
  return len(content.split())

def get_char_count(content):
  chars = list(content)
  char_dict = {}
  for char in chars:
    lowercase = char.lower()
    if lowercase not in char_dict:
      char_dict[lowercase] = 1
    else:
      char_dict[lowercase] += 1

  return char_dict    

def report(path, wc, char_count):
  lowercase_chars = [chr(i) for i in range(ord('a'), ord('z')+1)];

  print(f"--- Begin report of {path} ---")
  print(f"{wc} words found in the document \n")

  for char in lowercase_chars:
    print(f"The '{char}' character was found {char_count[char]} times")

  print('--- End report ---')
    
main('frankenstein.txt')