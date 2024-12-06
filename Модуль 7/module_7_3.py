class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        for file in self.file_names:
            with open(file, "r", encoding="utf-8") as fl:
                string = fl.read().lower()
            for symbol in (",", ".", "=", "!", "?", ";", ":", " - ", "\n"):
                string = string.replace(symbol, " ")
            words_list = string.split()
            all_words[file] = words_list
        return all_words

    def find(self, word):
        find_dict = dict()
        for name, words in self.get_all_words().items():
            find_dict[name] = words.index(word.lower()) + 1  # потому что с нуля
        return find_dict

    def count(self, word):
        count_dict = dict()
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word.lower())
        return count_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
