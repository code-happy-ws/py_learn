""" 解释器模式：定义一个语言的文法，并且建立一个解释器来解释该语言中的句子，
              这里的“语言”是指使用规定格式和语法的代码；
    例如：机器人控制指令“down run 10 and left move 20”

"""
from abc import ABC, abstractmethod

"""抽象表达式"""


class AbstractNode(ABC):

    @abstractmethod
    def interpret(self):
        pass


"""终结符表达式"""


class DirectionNode(AbstractNode):
    """方向解释"""

    def __init__(self, direction):
        self.direction = direction

    def interpret(self):
        if self.direction == 'up':
            return '向上'
        elif self.direction == 'down':
            return '向下'
        elif self.direction == 'left':
            return '向左'
        elif self.direction == 'right':
            return '向右'
        else:
            return '无效指令'


class ActionNode(AbstractNode):
    """行为解释"""

    def __init__(self, action):
        self.action = action

    def interpret(self):
        if self.action == 'move':
            return '移动'
        elif self.action == 'run':
            return '快速移动'
        else:
            return '无效指令'


class DistanceNode(AbstractNode):
    """距离解释"""

    def __init__(self, distance):
        self.distance = distance

    def interpret(self):
        return self.distance


"""非终结符表达式"""


class AndNode(AbstractNode):
    """And解释：非终结符表达式"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + '再' + self.right.interpret()


class SentenceNode(AbstractNode):
    """简单句子解释：非终结符表达式"""

    def __init__(self, direction, action, distance):
        self.direction = direction
        self.action = action
        self.distance = distance

    def interpret(self):
        return self.direction.interpret() + self.action.interpret() + self.distance.interpret()


"""环境类"""


class InstructionHandle:

    @staticmethod
    def handle(instruction):
        # 解析例如'down run 10 and left move 20'指令
        stack = []
        words = instruction.split()
        index = 0
        while index < len(words) - 1:
            if words[index] == 'and':
                left = stack.pop()
                word1 = words[index + 1]
                word2 = words[index + 2]
                word3 = words[index + 3]
                direction = DirectionNode(word1)
                action = ActionNode(word2)
                distance = DistanceNode(word3)
                right = SentenceNode(direction, action, distance)

                stack.append(AndNode(left, right))
                index += 4
            else:
                word1 = words[index]
                word2 = words[index + 1]
                word3 = words[index + 2]
                direction = DirectionNode(word1)
                action = ActionNode(word2)
                distance = DistanceNode(word3)
                left = SentenceNode(direction, action, distance)
                stack.append(left)
                index += 3
        sentence = [s.interpret() for s in stack]
        return ''.join(sentence)


if __name__ == '__main__':
    command = 'up move 5 and down run 6 and left move 7'
    HANDLE = InstructionHandle()
    result = HANDLE.handle(command)
    print(result)
