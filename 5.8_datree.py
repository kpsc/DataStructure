# reference
# https://linux.thai.net/~thep/datrie/datrie.html
# http://www.hankcs.com/program/java/%E5%8F%8C%E6%95%B0%E7%BB%84trie%E6%A0%91doublearraytriejava%E5%AE%9E%E7%8E%B0.html 
# https://www.cnblogs.com/zhangchaoyang/articles/4508266.html


class DATrie(object):

    class Node(object):

        def __init__(self, code, depth, left, right):
            self.code = code
            self.depth = depth
            self.left = left
            self.right = right

        def __str__(self):
            return "Node{" + \
                    "code=" + self.code + \
                    ", depth=" + self.depth + \
                    ", left=" + self.left + \
                    ", right=" + self.right + \
                    '}'


    def __init__(self):
        self.MAX_SIZE = 100
        self.base = [0] * self.MAX_SIZE
        self.check = [0] * self.MAX_SIZE
        self.used = [False] * self.MAX_SIZE
        self.nextCheckPos = 0
        self.size = 0  # memory used

    def resize(self, size):
        if size > self.MAX_SIZE:
            expend_size = size - self.MAX_SIZE
            self.base.extend([0] * expend_size)
            self.check.extend([0] * expend_size)
            self.used.extend([False] * expend_size)
            self.MAX_SIZE = size
    
    # 先决条件是self.words ordered 且没有重复
    # siblings至少会有一个
    def fetch(self, parent):
        depth = parent.depth

        siblings = []  # size == parent.right-parent.left, [left, right), 记录共有多少个子节点
        i = parent.left
        while i < parent.right:
            s = self.words[i][depth:]  # '.*'
            if s == '':
                siblings.append(
                    self.Node(code=0, depth=depth+1, left=i, right=i+1)) # 叶子节点
            else:
                c = ord(s[0]) + 1
                if siblings == [] or siblings[-1].code != c:   # 添加节点以及兄弟节点
                    siblings.append(
                        self.Node(code=c, depth=depth+1, left=i, right=i+1)) # 新建节点
                else:  # siblings[-1].code == c 拥有共同前缀
                    siblings[-1].right += 1
            i += 1
        # siblings
        return siblings

    # 在insert之前，认为可以先排序词汇，对base的分配检查应该是有利的
    # 先构建树，再构建DAT，再销毁树
    def build(self, words):
        words = sorted(list(set(words)))  # 去重排序
        self.words = words
        _root = self.Node(code=0, depth=0, left=0, right=len(self.words))
        self.base[0] = 1
        self.used[0] = True
        siblings = self.fetch(_root)
        self.insert(siblings)
        
        # del self.words
        print("DATrie builded.")

    def insert(self, siblings):
        begin = 0
        pos = max(siblings[0].code + 1, self.nextCheckPos) - 1   # 找到当前层下，词的位置分配点
        nonzero_num = 0
        first = 0  

        if(self.MAX_SIZE <= pos):
            self.resize(pos + 1)

        begin_flag = False  # 找合适的begin，为以其为前缀的所有子节点来进行状态转移
        while not begin_flag: 
            pos += 1        # 对应L106，为了进行偏移，若pos不加1，则L107的begin=0，但0是作为根节点使用了的
            if pos >= self.MAX_SIZE:
                # raise Exception("no room, may be resize it.")
                self.resize(pos + 1)
            if self.check[pos] != 0 or self.used[pos]: 
                nonzero_num += 1  # 已被使用
                continue
            elif first == 0:
                self.nextCheckPos = pos  # 第一个可以使用的位置
                first = 1

            begin = pos - siblings[0].code  # 对应的begin，状态转移前的下标，对应L121, 为当前节点找到连续空间

            if begin + siblings[-1].code >= self.MAX_SIZE:   # 对应L120，以code表示状态转移，begin+sibling.code是check数组的下标
                # raise Exception("no room, may be resize it.")
                self.resize(begin + siblings[-1].code + 255)

            if self.used[begin]:
                continue

            if len(siblings) == 1:
                begin_flag = True
                break

            for sibling in siblings[1:]:
                if self.check[begin + sibling.code] == 0 and self.used[begin + sibling.code] is False:  # 判断每一个是不是都能成功的进行状态转移
                    begin_flag = True
                else:
                    begin_flag = False
                    break

        # -- Simple heuristics --
        # if the percentage of non-empty contents in check between the
        # index 'next_check_pos' and 'check' is greater than some constant value
        # (e.g. 0.9), new 'next_check_pos' index is written by 'check'.
        if (nonzero_num / (pos - self.nextCheckPos + 1)) >= 0.95:
            self.nextCheckPos = pos

        self.used[begin] = True

        if self.size < begin + siblings[-1].code + 1:
            self.size = begin + siblings[-1].code + 1
        
        for sibling in siblings:
            self.check[begin + sibling.code] = begin      # 对应L119，前面已经check过了，所以这里可以直接设定值

        for sibling in siblings:  # 由于是递归的情况，需要先处理完check
            if sibling.code == 0:
                self.base[begin + sibling.code] = -1 * sibling.left - 1       # 标记叶节点
            else:
                new_sibings = self.fetch(sibling)     # 递归计算子节点的空间，广度优先遍历。。。
                h = self.insert(new_sibings)          # 插入子节点，并返回其begin值，用于填充base数组，记录状态转移
                self.base[begin + sibling.code] = h

        return begin

    def transition(self, c, b):      # 自然语言处理入门，何晗，p56
        p = self.base[b] + ord(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key):
        b = 0
        for c in key:
            p = self.transition(c, b)
            if p != -1:
                b = p
            else:
                return None

        p = self.base[b]
        n = self.base[p]
        if p == self.check[p] and n < 0:
            index = -n - 1
            return self.words[index]
        return None

    def __str__(self):
        s = ''
        for i, (a, b) in enumerate(zip(self.base, self.check)):
            if a:
                s += '\t'.join([str(i), str(a), str(b)]) + '\n'

        return s

    def get_use_rate(self):
        """ 空间使用率 """
        return self.size / self.MAX_SIZE

if __name__ == '__main__':
    words = ["一举",
            "一举一动",
            "一举成名",
            "一举成名天下知",
            "万能",
            "万能胶"
            ]

    datrie = DATrie()
    datrie.build(words)
    print(datrie)
    print('-'*10)
    print(datrie["一举"])
    print('-'*10)
    print(datrie["万能"])
    print('-'*10)
    print(datrie["万能胶"])
    print('-'*10)
    print(datrie["万能胶水"])

#     码表：
#    胶    名    动    知    下    成    举    一    能    天    万    
# 33014 21517 21160 30693 19979 25104 20030 19968 33021 22825 19975 
 
# DoubleArrayTrie{
# char =      ×    一    万     ×    举     ×    动     ×     下    名    ×    知      ×     ×    能    一    天    成    胶
# i    =      0 19970 19977 20032 20033 21162 21164 21519 21520 21522 30695 30699 33023 33024 33028 40001 44345 45137 66038
# base =      1     2     6    -1 20032    -2 21162    -3     5 21519    -4 30695    -5    -6 33023     3  1540     4 33024
# check=      0     1     1 20032     2 21162     3 21519  1540     4 30695     5 33023 33024     6 20032 21519 20032 33023
# size=66039, allocSize=2097152, key=[一举, 一举一动, 一举成名, 一举成名天下知, 万能, 万能胶], keySize=6, progress=6, nextCheckPos=33024, error_=0}
