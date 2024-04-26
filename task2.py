import re
import zipfile

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def get_sentences(self):
        sentences = re.split(r'[.?!]', self.text)
        return sentences

    def get_sentence_types(self):
        sentence_types = []
        for sentence in self.text:
            if sentence=='?':
                sentence_types.append('question')
            elif sentence=='!':
                sentence_types.append('exclamation')
            elif sentence=='.':
                sentence_types.append('statement')
        return sentence_types

    def get_average_sentence_length(self):
        words = self.get_words()
        sentences = self.get_sentences()
        return sum(len(words) for words in sentences) / len(sentences)

    def get_average_word_length(self):
        words = self.get_words()
        return sum(len(word) for word in words) / len(words)

    def get_num_words(self):
        return len(self.get_words())

    def get_num_odd_length_words(self):
        words = self.get_words()
        return len([word for word in words if len(word) % 2 == 1])

    def get_shortest_word_starting_with_i(self):
        words = self.get_words()
        return min([word for word in words if word.startswith('i')], key=len)

    def get_repeating_words(self):
        words = self.get_words()
        return [word for word in words if words.count(word) > 1]

    def get_emails(self):
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', self.text)
        return emails

    def get_names(self):
        names = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', self.text)
        return names

    def get_words(self):
        words = re.findall(r'\w+', self.text)
        return words

    def replace_v(self):
        text = re.sub(r'\$v_\(i\)', r'$v_[i]', self.text)
        return text

def function_task2():
    # Читаем текст из файла
    with open('text.txt', 'r') as f:
        text = f.read()

    # Создаем анализатор текста
    analyzer = TextAnalyzer(text)

    # Анализируем текст и получаем искомую информацию
    sentences = analyzer.get_sentences()
    sentence_types = analyzer.get_sentence_types()
    average_sentence_length = analyzer.get_average_sentence_length()
    average_word_length = analyzer.get_average_word_length()
    num_words = analyzer.get_num_words()
    num_odd_length_words = analyzer.get_num_odd_length_words()
    shortest_word_starting_with_i = analyzer.get_shortest_word_starting_with_i()
    repeating_words = analyzer.get_repeating_words()
    emails = analyzer.get_emails()
    names = analyzer.get_names()
    replaced_text = analyzer.replace_v()

    print('Number of offers:', len(sentences)-len(emails)-1)
    print('Number of narrative sentences:', sentence_types.count('statement')-len(emails))
    print('Number of interrogative sentences:', sentence_types.count('question'))
    print('Number of incentive offers:', sentence_types.count('exclamation'))
    print('Average sentence length:', average_sentence_length)
    print('Average word length:', average_word_length)
    print('Word count:', num_words)
    print('Number of words with an odd number of letters:', num_odd_length_words)
    print('The shortest word starting with a letter "i":', shortest_word_starting_with_i)
    print('Repeated words:', repeating_words)
    print('Email list:', emails)
    print('List of names:', names)
    print('Replaced text:', replaced_text)

    # Сохраняем результаты в файл
    with open('results.txt', 'w') as f:
        f.write('Number of offers: {}\n'.format(len(sentences)-len(emails)-1))
        f.write('Number of narrative sentences: {}\n'.format(sentence_types.count('statement')-len(emails)))
        f.write('Number of interrogative sentences: {}\n'.format(sentence_types.count('question')))
        f.write('Number of incentive offers: {}\n'.format(sentence_types.count('exclamation')))
        f.write('Average sentence length: {}\n'.format(average_sentence_length))
        f.write('Average word length: {}\n'.format(average_word_length))
        f.write('Word count: {}\
        n'.format(num_words))
        f.write('Number of words with an odd number of letters: {}\n'.format(num_odd_length_words))
        f.write('The shortest word starting with a letter "i": {}\n'.format(shortest_word_starting_with_i))
        f.write('Repeated words: {}\n'.format(repeating_words))
        f.write('Email list: {}\n'.format(emails))
        f.write('List of names: {}\n'.format(names))
        f.write('Replaced text: {}\n'.format(replaced_text))

    # Архивируем файл с результатами
    with zipfile.ZipFile('results.zip', 'w') as zip_file:
        zip_file.write('results.txt')

    # Получаем информацию о файле в архиве
    with zipfile.ZipFile('results.zip', 'r') as zip_file:
        file_info = zip_file.getinfo('results.txt')
        print('Archive file name:', file_info.filename)
        print('Archive file size:', file_info.file_size)
        print('Date the file was created in the archive:', file_info.date_time)