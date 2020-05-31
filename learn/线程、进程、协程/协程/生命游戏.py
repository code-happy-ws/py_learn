from collections import namedtuple, UserList

Query = namedtuple('Query',('y','x'))
Transition = namedtuple('Transition',('y','x','state'))

ALIVE = '*'
EMPTY = '-'

def count_neighbors(y,x):
    """获取邻居存活数量"""
    n_= yield Query(y+1,x+0) # North
    ne = yield Query(y+1,x+1) # northeast
    s_= yield Query(y-1,x+0) # south
    se = yield Query(y-1,x+1) # southeast
    w_= yield Query(y+0,x-1) # west
    nw = yield Query(y+1,x-1) # northwest
    e_= yield Query(y+0,x+1) # east
    sw = yield Query(y-1,x-1) # southwest
    neighbor_states=[n_,ne,e_,se,s_,sw,w_,nw]
    count =0
    for state in neighbor_states:
        if state == ALIVE:
            count +=1
    return count

def game_logic(state,neighbors):
    """规定游戏逻辑"""
    if state == ALIVE:
        if neighbors!=3:
            return EMPTY
    else:
        if neighbors==3:
            return ALIVE
        else:
            return EMPTY

def step_cell(y,x):
    """把本细胞下一轮所应有的状态，告诉外部代码"""
    state= yield Query(y,x)
    neighbors=yield from count_neighbors(y,x)
    next_state = game_logic(state,neighbors)
    yield Transition(y,x,next_state)

TICK = object()
def simulate(height,width):
    """处理网格中所有细胞，
       处理完毕后产生TICK对象，表示当前这一代处理完毕"""
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y,x)
        yield TICK

class Grid:
    """单个网格管理"""
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY]*self.width)

    def query(self,y,x):
        return self.rows[y%self.height][x%self.width]

    def assign(self,y,x,state):
        self.rows[y%self.height][x%self.width]=state

    def __repr__(self):
        grid=''
        for row in self.rows:
            row_show=''.join(row)+'\n'
            grid+=row_show
        return f'gtid:\n{grid}'

def live_a_generation(grid,sim):
    """把网格所有细胞往前推进一步，与外部环境交互操作"""
    grid=Grid(grid.height,grid.width)
    item=next(sim)
    while item is not TICK:
        if isinstance(item,Query):
            state = grid.query(item.y,item.x)
            item = sim.send(state)
        else:
            grid.assign(item.y,item.x,item.state)
    return grid

class ColumnPrinter(UserList):
    pass
    #
    def __repr__(self):
        return '\n\n'.join(self.__iter__())
        # for grid in self.__class__():



grid=Grid(6,6)
grid.assign(0,3,ALIVE)
grid.assign(1,4,ALIVE)
grid.assign(2,3,ALIVE)
grid.assign(2,4,ALIVE)
grid.assign(2,5,ALIVE)

columns=ColumnPrinter()
sim=simulate(grid.height,grid.width)
for i in range(5):
    print('start')
    columns.append(str(grid))
    grid=live_a_generation(grid,sim)

print(columns)


# if __name__ == '__main__':
    # columns=ColumnPrinter()
    # for i in range(5):
    #     columns.append(str(i))
    # print(columns)
    # it = step_cell(10,5)
    # q0 = next(it)
    # print('me :',q0)
    # q1 = it.send(ALIVE)
    # print('1 yield:',q1)
    # q2=it.send(ALIVE)
    # print('2 yield:',q2)
    # q3=it.send(ALIVE)
    # print('3 yield:',q3)
    # q4=it.send(ALIVE)
    # print('4 yield:',q4)
    # q5=it.send(ALIVE)
    # print('5 yield:',q5)
    # q6=it.send(ALIVE)
    # print('6 yield:',q6)
    # q7=it.send(ALIVE)
    # print('7 yield:',q7)
    # q8=it.send(ALIVE)
    # print('8 yield:',q8)
    # t1=it.send('empty')
    # print('outcome:',t1)
    # grid=Grid(5,9)
    # grid.assign(0,3,ALIVE)
    # print(grid)