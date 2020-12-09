class Constraint():
    """约束处理"""

    def __init__(self, variables):
        # 受约束的对象（例澳大利亚着色受约束对象为两相邻州所组成的列表对象）
        self.variables = variables

    def satisfied(self, assignment):
        pass


class CSP:
    def __init__(self, variables: list, domins: dict):
        # 需处理的全部对象集（例八皇后的8个皇后）
        self.variables = variables
        # 每个对象的值域对应键值对
        self.domins = domins
        # 每个对象及其约束集对应键值对
        self.contraints = {}
        for variable in self.variables:
            self.contraints[variable] = []
            if variable not in self.domins:
                raise LookupError(f'{variable}不在domins内')

    def add_constraint(self, constraint):
        """ 为增加约束
        :param constraint:
        :return:
        """
        for variable in constraint.variables:
            if variable in self.variables:
                self.contraints[variable].append(constraint)
            else:
                raise LookupError(f'{variable}变量不在csp对象集内')

    def is_consistent(self, variable, assignment):
        """判断一对象是否满足其全部约束"""
        for constrain in self.contraints[variable]:
            if not constrain.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: dict):
        """
        :param assignment: 已处理完毕的对象及分配结果键值对（例{皇后3：位置}
        :return:
        """
        unassigned = [v for v in self.variables]

        def dfs(assignment):
            # dfs要点：保存已处理过的结果（assignment）
            nonlocal unassigned
            if len(assignment) == len(self.variables):
                return assignment
            unassigned = [v for v in self.variables if v not in assignment]
            unassigned_variable = unassigned[0]
            # unassigned_variable = unassigned.pop()

            # 取一个未处理的对象进行处理
            for value in self.domins[unassigned_variable]:
                # 为对象设定状态，若该状态满足约束，则进行递归处理其他未处理的元素
                # 若所有状态均不满足约束，则进行回溯，回到当前上一点选择其他路径
                local_assignment = assignment.copy()
                local_assignment[unassigned_variable] = value
                if self.is_consistent(unassigned_variable, local_assignment):

                    result = dfs(local_assignment)
                    if result:
                        return result

            # 无法处理返回None
            return None

        return dfs(assignment)
