import turtle
from config import fractals
from choose import choose
import random


TRACER_ON = True
#TRACER_ON = False


class LSystem:
    def __init__(self, t, axiom, angle, width=2, len=5, num_iter=3, start_point=(0,0), start_angle = 0):
        self.axiom = axiom   # аксиома
        self.state = axiom
        self.width = width   # толщина линии рисования
        self.len = len       # длина одного сегмента кривой
        self.angle = angle   # угол поворота(фиксированный)
        self.t = t           # сама черепашка
        self.rules : dict = {}      # хранение правил
        self.start_point = start_point
        self.start_angle = start_angle
        self.t.pensize(self.width)
        self.num_iter = num_iter
    
    @classmethod
    def from_description(cls, turtle, descr: dict):
        lsystem = cls(
            turtle,
            axiom=descr['axiom'] or "F",
            angle=descr['angle'],
            width=descr.get('width') or 2,
            start_angle=descr.get('start_angle') or 0,
            start_point=descr.get('start_point') or (0,0),
            len=descr['len'] or 5,
            num_iter=descr['num_iter'] or 3,
        )
        
        lsystem.add_rules(descr['rules'])
    
        return lsystem

    
    def add_rules(self, rules):
        if isinstance(rules, (set, list)):
            for key, value in rules:
                self.rules[key] = value
        elif isinstance(rules, dict):
            self.rules = rules
        elif isinstance(rules, tuple):
            self.rules[rules[0]] = rules[1]
        else:
            raise ValueError("Bad Rules")


    def generate(self, num_iter=None):
        if num_iter is None:
            num_iter = self.num_iter

        for i in range(num_iter):
            new_state = []
            for symbol in self.state:
                if symbol in self.rules:
                    if isinstance(self.rules[symbol], list):  # правила с вероятностями
                        rule = choose(self.rules[symbol])
                    elif isinstance(self.rules[symbol], str): # детерминированное правило
                        rule = self.rules[symbol]
                    
                    
                    new_state.append(rule)
                
                else:
                    new_state.append(symbol)
            
            self.state = "".join(new_state)

    
    def set_turtle(self, koord):
        self.t.up()
        self.t.goto(koord[0], koord[1]) # перенос в нужные координаты
        self.t.seth(koord[2]) # устанавливаем нужный угол поворота
        self.t.down()

    def draw_turtle(self, start_point=None, start_angle=None, add_randomness=False):
        turtle.tracer(TRACER_ON)
        self.t.up()
        if start_point is None:
            start_point = self.start_point
            t.setpos(start_point)
        if start_angle is None:
            start_angle = self.start_angle
            t.seth(start_angle)
        
        self.t.down()
        stack = []

        for move in self.state:
            if move == 'F':
                step = self.len
                if add_randomness:
                    r1 = random.randint(-self.len // 4, +self.len // 4)
                    step = r1 + self.len
                self.t.forward(step)
            elif move == '+':
                angle = self.angle
                if add_randomness:
                    angle = self.angle + random.randint(-self.angle // 2, +self.angle // 2)
                self.t.left(angle)
                        
            elif move == '-':
                angle = self.angle
                if add_randomness:
                    angle = self.angle + random.randint(-self.angle // 2, +self.angle // 2)
                self.t.right(angle)
            elif move == '[':
                if add_randomness:
                    self.t.right(random.randint(-self.angle//5, +self.angle//5))
                stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize())) #добавляем в стэк (текущую координату по х и по y, текущий угол поворота, и толщину линии )
            elif move == ']':
                xcor, ycor, head, w = stack.pop()
                self.set_turtle((xcor, ycor, head)) # c помощью этого устанавливаем черепашку в соотв.координаты
                self.width = w
                self.t.pensize(self.width)
        
        turtle.done()


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()



    sys = LSystem.from_description(t, fractals['derevo_prob'])
    sys.generate()
    print(sys.state)
    sys.draw_turtle(add_randomness=False)
    #sys.len = 10
    #print(sys.state)
    #sys.draw_turtle((0,-200), 0)
    