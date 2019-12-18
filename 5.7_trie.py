# 任务：开发一颗字典树
# 描述：有一个文件，每行一个英文字符串（英文单词），要求将这些单词存储于如下所述的树形结构中，并编写查询函数，输入一个字符串，判断该字符串是否存在于这棵树中
# 单词列表：what,rank,range,water,want,ranker,rant
# 树形结构：
#                  (root)
#                /       \
#               w          r
#             /   \         \
#            h     a          a
#          /      / \          \
#         a      t   n          n
#        /      /      \      / | \
#       t*     e      t*     k* g  t*
#             /             /   |
#            r*            e    e*
#                         /
#                        r*
# (其中，标记为星号的节点为数据节点，表示从root节点到该节点的这条路径，经过的所有节点的字符连接起来，可以组成一个单词。)

# 字母共有 26 个，故除了根节点外，其他每个节点到下一节点均有 25 条可走路径，根节点有 26 条路径



class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.next = []
        self.isword = False


class TrieTree:
    def __init__(self):
        self.root = TreeNode('root')

    def insert(self, word):
        currentNode = self.root

        for w in word:
            exist = False
            for node in currentNode.next:
                if w == node.val:
                    exist = True
                    currentNode = node
                    break
            if not exist:
                tmp = TreeNode(w)
                currentNode.next.append(tmp)
                currentNode = tmp
        currentNode.isword = True

    def search(self, word):
        currentNode = self.root

        for w  in word:
            exist = False
            for node in currentNode.next:
                if w == node.val:
                    exist = True
                    currentNode = node
                    break
            if not exist:
                return False
        if currentNode.isword:
            return True
        else:
            return False

    def delete(self, word):
        currentNode = self.root

        for w in word:
            exist = False
            for node in currentNode.next:
                if w == node.val:
                    exist = True
                    currentNode = node
                    break
            if not exist:
                return f'............{word} not in the trie tree'

        if currentNode.isword:
            currentNode.isword = False


if __name__ == '__main__':
    trie = TrieTree()

    for word in 'what,rank,range,water,want,ranker,rant,english,me,python'.split(','):
        trie.insert(word)

    print('search wha: ', trie.search('wha'))
    print('search what: ', trie.search('what'))
    print('search abc: ', trie.search('abc'))
    print('search python: ', trie.search('python'))
    print('search ok: ', trie.search('ok'))

    print('delete what: ', trie.delete('what'))
    print('search what: ', trie.search('what'))
    
    print('delete we: ', trie.delete('we'))
