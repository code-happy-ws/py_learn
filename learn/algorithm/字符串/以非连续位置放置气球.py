class BalloonPutError(Exception):
    """无法以非连续位置放置气球异常"""

    def __str__(self):
        return '无法以非连续位置放置气球'


class BalloonPutNotInSequence:
    """放置非连续位置气球"""

    def __init__(self, balloon: dict):
        """
        :param balloon: 气球颜色及对应数量信息
        """
        self.balloon = balloon

    def put(self) -> str:
        """在墙上非连续位置摆放气球
        :return:
            可以非连续位置摆放：返回摆放位置
            不可非连续位置摆放：抛出异常
        """
        temp = []
        balloon_count = sum(self.balloon.values())
        position = [0] * balloon_count

        # 将气球按数量排序
        balloon_in_order = sorted(self.balloon.items(), key=lambda x: x[1])

        for color, count in balloon_in_order:
            # 若某气球数量超过总数量一半，则无法以非连续位置摆放
            if float(count) > balloon_count // 2:
                raise BalloonPutError
            temp.extend(color * count)

        # 确定非连续摆放位置
        position[::2] = temp[balloon_count // 2:]
        position[1::2] = temp[:balloon_count // 2]

        return ''.join(position)


if __name__ == '__main__':
    # y-yellow; r-red; w-white; g-green; p-pink
    # 正常情况
    balloon_info = {'y': 2, 'r': 6, 'w': 2, 'g': 1, 'p': 1}
    # 异常情况
    # balloon_info = {'y': 20, 'r': 6, 'w': 2, 'g': 1, 'p': 1}
    BALLOON = BalloonPutNotInSequence(balloon_info)
    balloon_position = BALLOON.put()
    print(balloon_position)
