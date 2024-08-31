def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    words = file_contents.split()
    counted_words = count_words(words)
    print(counted_words)

    lowered_string = file_contents.lower()
    counted_chars = count_chars(lowered_string)
    counted_chars.sort(reverse=True, key=sort_on)
    
    info = print_info(counted_words, counted_chars)

    print(info)

    


def count_words(words):
  return len(words)


def count_chars(string):
  letter_count = {}
  letter_list = []

  for letter in string:
    if letter not in letter_count and letter.isalpha():
      letter_count[letter] = 1
    elif letter in letter_count and letter.isalpha():
      letter_count[letter] += 1
    
  for key in letter_count:
    dict = {}

    dict["char"] = key
    dict["count"] = letter_count[key]
    letter_list.append(dict)

  return letter_list

def sort_on(dict):
  return dict["count"]

def print_info(words_int, letters_list):
  report = "--- Begin report of books/frankenstein.txt ---\n"
  report += f"{words_int} words found in the document\n\n"

  for i in range(len(letters_list)):
    report += f"The '{letters_list[i]['char']}' character was found {letters_list[i]['count']} times\n"

  report += "--- End of report ---"
  return report


main()