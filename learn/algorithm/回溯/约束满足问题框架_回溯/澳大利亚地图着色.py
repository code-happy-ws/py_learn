"""
用三种颜色为澳大利亚7个州着色，要求相邻州不能同色
"""
from csp import Constraint, CSP


class MapColoringConstraint(Constraint):
    def __init__(self, place1, place2):
        super().__init__([place1, place2])
        self.place1 = place1
        self.place2 = place2

    def satisfied(self, assignment: dict):
        """根据已经处理的结果判断受约束的对象是否满足约束（相邻州不能同色）
        针对本问题，受约束的对象包括相邻的两个州1、2，若其中一个州还未着色，则一定可以满足约束
        """
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]


if __name__ == '__main__':
    assignment = {}
    variables = ['We', 'No', 'So', 'Qu', 'Ne', 'Vi', 'Ta']
    domins = {}
    for variable in variables:
        domins[variable] = ['red', 'green', 'blue']
    csp: CSP = CSP(variables, domins)
    neighbour = [('We', 'No'), ('We', 'So'), ('So', 'No'),
                 ('Qu', 'No'), ('Qu', 'So'), ('Qu', 'Ne'), ('Ne', 'So'),
                 ('Vi', 'So'), ('Vi', 'Ne'), ('Vi', 'Ta')]
    for elem in neighbour:
        csp.add_constraint(MapColoringConstraint(*elem))
    solution = csp.backtracking_search(assignment)
    print(solution)
    # {'We': 'red', 'No': 'green', 'So': 'blue', 'Qu': 'red', 'Ne': 'green', 'Vi': 'red', 'Ta': 'green'}

