# Explanation

TrieNode contains a value (a character), a boolean 'is_word' and a dictionary of children.

eg. {'a' -> node, 'b'->node}


'get_suffixes' is a function that can be called on a node and it will return all continuations that end in words.

For example, a node that has the value 'a' and two children {b -> {is_word:false},   m -> {is_word: true}} will return ['m']



The class Trie contains three methods - insert, find and get_suffixes.

'insert' just iterates through the characters and gets the relevant child nodes if they exist.

When a child no longer exists, it inserts a new Node with 'is_word':= true.

'find' does something similar, going through children one by one until we reach null or exhaust the characters (we found the word)

'get_suffixes' is a helper function that returns 'prefix_node.get_suffixes()' if the node is found and [] otherwise.


# Analysis

Building a tree using words with a total of 'n' characters is O(n) because we iterate through each character in each word and insert into the dict.

Eg. ['a', 'apple', 'ant'] -> n = 9

'get_suffixes' for a word with 'k' characters is O(k), because we iterate through each character, choosing the relevant child.

Storage is harder to calculate because it depends on the number of nodes and the structure of words in the language. 

I suspect English and Chinese would have very different storage.

For the top 100 words in English, I get 217 nodes
For the top 1000 words in English, I get 3045 nodes
For the top 3000 words in English, I get 9127 nodes

(see the tests in tests.txt).

This suggests that the number of nodes is about O(3n) where 'n' is the number of words.

The average word length in English is about 5, so this is O(0.6k) where 'k' is the number of characters.

It seems to be linear anyway.


![graph](/img.jpg)




