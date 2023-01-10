import os
import string

class DataStream:
    def __init__(self, data_dir: str, stopwords_path: str):
        self.files = []
        self.stopwords = []
        self.punctuation = string.punctuation
        self.load_data(data_dir, stopwords_path)
        self.current_line = None

    def load_data(self, data_path: str, stopwords_path: str):
        self.files = [open(data_path)]
        with open(stopwords_path, 'r') as s:
            self.stopwords = [line.strip() for line in s.readlines()]

    def parse_line(self, line: str):
        line = line.lower().translate(str.maketrans('','', self.punctuation))
        for w in self.stopwords:
            line = line.replace(w, "")
        line = ''.join(line.split())
        return line

    def get_next(self):
        while True:
            if not self.files:
                return None

            nxt = next(self.files[0], None)
            if nxt is None:
                del self.files[0]
                continue

            if (len(nxt.strip()) == 0):
                continue
            return self.parse_line(nxt)

    def next_token(self):
        if not self.current_line:
            next_line = self.get_next()
            if not next_line:
                return None
            self.current_line = next_line

        token = self.current_line[0]
        self.current_line = self.current_line[1:]
        return token
