# coding=utf-8
 
class RMM(object):
    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        with open(dic_path, 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)
    def cut(self, text):
        result = []
        index = len(text)
        while index > 0:
            for size in range(self.maximum, 0, -1):
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    result.append(piece)
                    index -= size
                    break
            if piece is None:
                index -= 1
        return result[::1]
def main():
    text = '南京市长江大桥'
    tokenizer = RMM('./data.utf8')
    print(tokenizer.cut(text))
main()
