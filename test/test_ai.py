from __future__ import print_function
import random


class Button:
    def __init__(self, taken):
        self.taken = taken


class Game:
    def __init__(self, board):
        self.NUMS = 19
        self.buttons = {}
        self.trans = ['.', 'c', 'p']

        for i in range(self.NUMS):
            for j in range(self.NUMS):
                self.buttons[(i, j)] = Button(board[i][j])

        self.nearpos = ((1, 0), (1, 1), (0, 1), (-1, 1))

    def display(self):
        print(' ', end='')
        for j in range(self.NUMS):
            print(j % 10, end='')
        print()
        for i in range(self.NUMS):
            print(i % 10, end='')
            for j in range(self.NUMS):
                print(self.trans[self.buttons[(i, j)].taken + 1], end='')
            print()

    def compute(self, player):
        bsites=[p for p,b in self.buttons.iteritems() if b.taken == -1]
        bsites_values=[]

        choice_num = len(bsites)
        if choice_num == 0:
            print('no one wins...game over')
            return None

        for bpos in bsites:
            value = 0
            for step_pos in self.nearpos:
                _space = 0
                for i in range(1,5):
                    npos = self._add(bpos,self._mul(step_pos,i))
                    if npos is None or self.buttons[npos].taken == 1-player:
                        break
                    else:
                        _space += 1
                for i in range(1,5):
                    npos = self._add(bpos,self._mul(step_pos,-i))
                    if npos is None or self.buttons[npos].taken == 1-player:
                        break
                    else:
                        _space += 1
                if _space < 4:
                    continue

                max_step = 1
                for i in range(-1,-5,-1):
                    _t = 1
                    npos = self._add(bpos,self._mul(step_pos,i))
                    if npos is None or self.buttons[npos].taken == 1-player:
                        break
                    for j in range(5):
                        npos = self._add(npos,step_pos)
                        if npos is None or self.buttons[npos].taken == 1-player:
                            break
                        if self.buttons[npos].taken == player:
                            _t += 1
                    if _t > max_step:
                        max_step = _t
                value += 10**(max_step-1)

                npos = self._add(bpos,step_pos)
                if npos is not None :
                    if self.buttons[npos].taken == player:
                        value += 1
                npos = self._add(bpos,self._mul(step_pos,-1))
                if npos is not None :
                    if self.buttons[npos].taken == player:
                        value += 1
            if value > 0:
                bsites_values.append((bpos,value))

        _maxvalue,_maxp=0,None
        for p,v in bsites_values:
            if v > _maxvalue:
                _maxvalue,_maxp = v,p

        if _maxp == None:
         _maxp = random.choice(bsites)

        return _maxvalue,_maxp

    def _mul(self, pos1, n):
        return (pos1[0] * n, pos1[1] * n)


    def _add(self, pos1, pos2):
        npos = (pos1[0] + pos2[0], pos1[1] + pos2[1])
        if npos[0] >= self.NUMS or npos[1] >= self.NUMS or npos[0] < 0 or npos[1] < 0:
            return None
        return npos


    def check_over(self):
        # 横线
        for rows in range(self.NUMS):
            step_compute, step_person = 0, 0
            for cols in range(self.NUMS):
                npos = (rows, cols)
                if self.buttons[npos].taken == 0:
                    step_compute += 1
                    step_person = 0
                    if step_compute >= 5:
                        print('c win')
                        return True
                elif self.buttons[npos].taken == 1:
                    step_compute = 0
                    step_person += 1
                    if step_person >= 5:
                        print('p win')
                        return True
                else:
                    step_compute, step_person = 0, 0
        # 竖线
        for cols in range(self.NUMS):
            step_compute, step_person = 0, 0
            for rows in range(self.NUMS):
                npos = (rows, cols)
                if self.buttons[npos].taken == 0:
                    step_compute += 1
                    step_person = 0
                    if step_compute >= 5:
                        print('c win')
                        return True
                elif self.buttons[npos].taken == 1:
                    step_compute = 0
                    step_person += 1
                    if step_person >= 5:
                        print('p win')
                        return True
                else:
                    step_compute, step_person = 0, 0
        # 上斜线
        for pos in [(row, 0) for row in range(self.NUMS)] + [(self.NUMS - 1, col) for col in range(self.NUMS)]:
            _step = (-1, 1)
            n = 0
            step_compute, step_person = 0, 0
            while 1:
                npos = self._add(pos, self._mul(_step, n))
                if npos is None:
                    break
                if self.buttons[npos].taken == 0:
                    step_compute += 1
                    step_person = 0
                    if step_compute >= 5:
                        print('c win')
                        return True
                elif self.buttons[npos].taken == 1:
                    step_compute = 0
                    step_person += 1
                    if step_person >= 5:
                        print('p win')
                        return True
                else:
                    step_compute, step_person = 0, 0
                n += 1
        # 下斜线
        for pos in [(row, 0) for row in range(self.NUMS)] + [(0, col) for col in range(self.NUMS)]:
            _step = (1, 1)
            n = 0
            step_compute, step_person = 0, 0
            while 1:
                npos = self._add(pos, self._mul(_step, n))
                if npos is None:
                    break
                if self.buttons[npos].taken == 0:
                    step_compute += 1
                    step_person = 0
                    if step_compute >= 5:
                        print('c win')
                        return True
                elif self.buttons[npos].taken == 1:
                    step_compute = 0
                    step_person += 1
                    if step_person >= 5:
                        print('p win')
                        return True
                else:
                    step_compute, step_person = 0, 0
                n += 1
        return False

    def next(self, player):
        cv, cpos = self.compute(player)
        pv, ppos = self.compute(1-player)
        if cv > pv:
            return cpos
        else:
            return ppos



if __name__ == '__main__':
    # self.buttons[(NUMS/2,NUMS/2)].taken = 0
    a=int(input('先手请输入1，后手请输入2：'))
    board = [[-1 for _ in range(19)] for _ in range(19)]


    if a==1:
        board[9][9] = 0
        game = Game(board)
        game.display()
        #print('(9, 9)')

    while True:

        x = int(input('input x：'))
        y = int(input('input y：'))
        board[x][y] = 1
        game = Game(board)
        pos = game.next(0)
        board[pos[0]][pos[1]] = 0
        game = Game(board)
        game.display()

        if game.check_over():
            break