# Explanation

The Trie implementation and TrieNode are similar to problem 6.

I'm adding a fake 'root' node as the first child. It's unnecessary but makes it conceptually simpler for me.

'split_path' is a helper function whose job is to get the correct array of paths from a URL.


Eg:

'/abc//def/g/hi'   -> ["root", "def", "g", "hi"]

' /abc//def/g/hi/'   -> ["root", "def", "g", "hi"]

'/abc//def/g/hi//'   -> ["root", "def", "g", "hi"]


Like in problem 5, 'add_handler' iterates through the nodes, checking each part of the above array.

Similar to "is_word", the final node is assigned the handler.

'lookup' iterates though the nodes.

If one is found and it has a handler, this is returned, otherwise the not_found handler is returned.



# Analysis

Adding a new route to a Trie is O(n), where n is the number of segments being added.

Eg. /a/bbbbbbbbbb/cccc/d has 4 segments

Splitting a string on slashes is O(k) where 'k' is the total number of characters.

Since most urls will have human-readable parts, I think n and k will be related linearly (by the typical length of a segment)

So, O(n) = O(k)


Looking up a handler is also O(n), where n = number of segments.

This is because we split the string into 'n' parts and do 'n' dict lookups.

This is also O(k) where k = number of characters.


For storage, it depends how the routes are structured.

Eg.


/a/b/c

/a/b/d

/a/b/d

/a/b/f

These routes need 5 nodes.

But these need 12:

/a/b/c

/d/e/f

/h/i/j

/k/l/m



If there are 'n' routes added and each one has 'k' segments, the best case is O(k) (eg. if all 'n' are the same)

The worst case is O(nk) (if all are different at each step).









