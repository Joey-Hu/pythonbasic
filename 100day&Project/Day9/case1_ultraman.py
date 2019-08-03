# @author: huhao
# @file: case1_ultraman.py
# @time: 2019/7/17 11:45
# @Document：https://www.python.org/doc/
# @desc:


from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if hp >= 0:
            self._hp = hp
        else:
            self._hp = 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        # param other: 被攻击的对象
        pass


class Ultraman(Fighter):

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other._hp -= randint(15, 25)

    def hard_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other._hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other._hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp._hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值: %d\n' % self._hp + \
               '魔法值: %d\n' % self._mp


class Monster(Fighter):
    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


'''
Don't Cry

Singer: Guns N' Roses

Talk to me softly
There is something in your eyes
Don't hang your head in sorrow
And please don't cry
I know how you feel inside now 
I've been there before
Something's changing inside you
And don't you know
Don't you cry tonight
I still love you baby
Don't you cry tonight
Don't you cry tonight
There's a heaven above you baby
And don't you cry tonight
Give me a whisper
And give me a sigh
Give me a kiss before you
Tell me goodbye
Don't you take it so hard now
And please don't take it so bad
I'll still be thinking of you
And the times we had...baby
And don't you cry tonight
Don't you cry tonight
Don't you cry tonight
There's a heaven above you baby
And don't you cry tonight
And please remember
That I never lied
And please remember
How I felt inside now baby
You gotta make it your own way
But you'll be alright now sugar
You'ii feel better tomorrow
Come the morning light now baby
And don't you cry tonight
And don't you cry tonight
And don't you cry tonight
There's a heaven above you baby
And don't you cry tonight
Don't you ever cry
Don't you ever cry tonight
Baby maybe someday
Don't you cry
Don't you ever cry
Don't you cry
Tonight


'''


def main():
    u = Ultraman('胡浩', 1000, 120)
    m1 = Monster("蛇精", 250)
    m2 = Monster("一只耳", 500)
    m3 = Monster("蝎子精 ", 750)
    ms = [m1, m2, m3]
    fight_round = 1

    while u.alive and is_any_alive(ms):
        print("========Round %02d========" % fight_round)
        m = select_alive_one(ms)    # 选中一只小怪兽
        skill = randint(1,10)   # 通过随机数选择使用哪种技能
        if skill <= 6:      # 60%的几率使用普通攻击
            print("%s使用普通攻击打了%s" %(u._name, m._name))
            u.attack(m)
            print("%s回复了%d点魔法值" %(u._name, u.resume()))
        elif skill <= 9:    # 30%的几率使用魔法攻击（可能因为魔法点不足而失败）
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u._name)
            else:
                print('%s使用魔法失败.' % u._name)
        else:   # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.hard_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u._name, m._name))
            else:
                print('%s使用普通攻击打了%s.' % (u._name, m._name))
                print('%s的魔法值恢复了%d点.' % (u._name, u.resume()))
        if m.alive > 0:     # 如果选中的小怪兽没有死就回击奥特曼
            print("%s回击了%s" %(m._name, u._name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print("========Fight is over!========")
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')

if __name__ == '__main__':
    main()
