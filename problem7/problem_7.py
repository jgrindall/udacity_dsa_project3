class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.handler_name = None
        
    def has(self, segment):
        return segment in self.children
    
    def get_child(self, char):
        return self.children[char]

    def insert(self, segment):
        # Add a child node in this Trie
        self.children[segment] = TrieNode(segment)

    
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler_name = "root handler", notfound_handler_name = "not found helper"):
        self.root = TrieNode("root")
        self.root.handler_name = root_handler_name
        self.notfound_handler_name = notfound_handler_name

    def add_handler(self, route, handler_name):
        if len(route) == 0 or route[0] != "/":
            raise ValueError("Invalid route")
        parts = self.split_path(route)
        node = self.root
        for part in parts:
            if node.has(part):
                node = node.get_child(part)
            else:
                node.insert(part)
                node = node.get_child(part)
        node.handler_name = handler_name

    def lookup(self, route):
        parts = self.split_path(route)
        node = self.root
        for part in parts:
            if node.has(part):
                node = node.get_child(part)
            else:
                return self.notfound_handler_name
        return node.handler_name

    def split_path(self, path):
        parts = path.split("/")
        remove_slashes = list(filter(lambda x: len(x) >= 1, parts))
        remove_slashes.insert(0, "root")
        return remove_slashes