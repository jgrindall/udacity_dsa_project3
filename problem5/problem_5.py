"""
Before we start let us reiterate the key components of a Trie or Prefix Tree.
A trie is a tree-like data structure that stores a dynamic set of strings
Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
"""


## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value):
        # map char to nodes
        # eg. {'a' -> node, 'b'->node}
        self.value = value
        self.children = {}
        self.is_word = False
        
    def has(self, char):
        return char in self.children
    
    def get_child(self, char):
        return self.children[char]

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode(char)

    def get_suffixes(self):
        path = []
        continuations = []
        def visit(node):
            path.append(node.value)
            if node.is_word:
                continuations.append("".join(path))
            for char in node.children:
                visit(node.children[char])
            path.pop()
        visit(self)
        
        suffices = []
        
        for c in continuations:
            c = c[1::]
            if len(c) >= 1:
                suffices.append(c)
        
        return suffices


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        # Add a word to the Trie
        
        node = self.root
        for char in word:
            if node.has(char):
                node = node.get_child(char)
            else:
                node.insert(char)
                node = node.get_child(char)
        node.is_word = True

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if node.has(char):
                node = node.get_child(char)
            else:
                return None
        return node




