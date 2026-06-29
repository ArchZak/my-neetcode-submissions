class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        #iterate through the word
        #if a node is there then the letter exists

        curr = self.trie
        for letter in word:
            if curr.children[ord(letter)-ord('a')]:
                curr = curr.children[ord(letter)-ord('a')]
            else:
                curr.children[ord(letter)-ord('a')] = TrieNode()
                curr = curr.children[ord(letter)-ord('a')]

        curr.end = True

    def search(self, word: str) -> bool:
        #iterate through the word
        #if a node is there then the letter exists

        curr = self.trie
        for letter in word:
            if curr.children[ord(letter)-ord('a')]:
                curr = curr.children[ord(letter)-ord('a')]
            else:
                return False
        
        return True if curr.end else False

    def startsWith(self, prefix: str) -> bool:
        #iterate through the word
        #if a node is there then the letter exists

        curr = self.trie
        for letter in prefix:
            if curr.children[ord(letter)-ord('a')]:
                curr = curr.children[ord(letter)-ord('a')]
            else:
                return False

        return True

class TrieNode:
    def __init__(self):
        self.children = [None]*26 #put more nodes in here
        self.end = False