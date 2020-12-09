"""八皇后"""
from time import time

from learn.algorithm.回溯.约束满足问题框架_回溯.csp import Constraint, CSP


class QueensConstraint(Constraint):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns = columns

    def satisfied(self, assignment):
        # 根据已处理过的结果集判断当前状态是否满足约束，受约束的对象为当前皇后
        for column1, row1 in assignment.items():
            for column2 in range(column1):
                if column2 in assignment:
                    row2 = assignment[column2]
                    if row1 == row2:
                        return False
                    if abs(row1 - row2) == abs(column1 - column2):
                        return False
        return True


if __name__ == '__main__':
    start = time()
    columns = [i for i in range(1, 8)]
    # rows = {}
    # for column in columns:
    #     rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows = {column: list(range(1, 8)) for column in columns}
    csp = CSP(variables=columns, domins=rows)
    csp.add_constraint(QueensConstraint(columns))
    assignment = {}
    result = csp.backtracking_search(assignment)
    print(result)
    end = time()
    print('during:', end - start)
