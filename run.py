import gym
import numpy as np
from cartpole import ContinuousCartPoleEnv
from collections import defaultdict
from rules_3 import angle_rules, position_rules
from matplotlib import pyplot as plt

class TriangularMembershipFunction:
    def __init__(self, a, b, c, name, inf_a=False, inf_c=False):
        assert a <= b and b <= c
        self.a = a
        self.b = b
        self.c = c
        self.name = name
        self.inf_a = inf_a
        self.inf_c = inf_c
    
    def __call__(self, x):
        if x < self.a:
            if self.inf_a:
                return 1
            return 0
        elif x > self.c:
            if self.inf_c:
                return 1
            return 0
        elif x == self.b:
            return 1
        elif self.a <= x and x < self.b:
            m = self.a
            n = self.b
            # p.x + q
            p = -1/(m-n)
            q = m/(m-n)
            return p*x + q
        elif self.b < x and x <= self.c:
            m = self.c
            n = self.b
            p = -1/(m-n)
            q = m/(m-n)
            return p*x + q

class Variable:
    def __init__(self, gain=1, inf_out=True):
        self.mem_funcs = dict()
        self.list_sets = []
        self.inf_out = inf_out
        self.gain = gain

    def auto_devide(self, num_devide=7, names = ['NL', 'NM', 'NS', 'ZE', 'PS', 'PM', 'PL'], min_a=-1, max_c=1):
        if min_a is None:
            min_a = -np.inf
        if max_c is None:
            max_c = np.inf
        lin = np.linspace(min_a, max_c, num_devide)
        a = [lin[0], *lin[:-1]]
        b = lin
        c = [*lin[1:], lin[-1]]
        for i in range(num_devide):
            self.add_func(a[i], b[i], c[i], names[i], inf_a=(i==0 and self.inf_out), inf_c=(i==num_devide-1 and self.inf_out))


    def add_func(self, a, b, c, name='None', inf_a=False, inf_c=False):
        fun = TriangularMembershipFunction(a, b, c, name, inf_a, inf_c)
        self.mem_funcs[name] = fun
        self.list_sets.append(name)
        
    def mu_all(self, x):
        x = self.gain*x
        result = dict()
        for _, fun in self.mem_funcs.items():
            result[fun.name] = fun(x)
        return result

    def mu(self, name, x):
        x = self.gain*x
        return self.mem_funcs[name](x)

    def plot(self, min_range, max_range):
        fig = plt.figure()
        ax = fig.subplots()
        xs = np.arange(min_range, max_range, 0.005)
        for _, fun in self.mem_funcs.items():
            mu = [fun(x) for x in xs]
            ax.plot(xs, mu, c='b')
        return fig

    def weight_average_defuzzification(self, alphas):
        numerator = 0
        denomirator = 0
        #print(alphas)
        for key, fun in self.mem_funcs.items():
            numerator += alphas[key]*fun.b
            denomirator += alphas[key]
        if np.isnan(numerator/denomirator):
            print(numerator, denomirator)
        return numerator/denomirator


class MamdaniController:
    def __init__(self, input_variables, output_variable, rulesets, name):
        self.rulesets = rulesets
        self.input_variables = input_variables
        self.output_variable = output_variable
        self.or_agg = np.min
        self.and_agg = np.max
        self.name = name

    def control(self, *inputs):
        memberships = []
        alphas = defaultdict(float)
        for idx, inp in enumerate(inputs):
            m_input = self.input_variables[idx].mu_all(inp)
            memberships.append(m_input)

        for key, val in self.rulesets.items():
            rule_ms = []
            for idx, var_name in enumerate(key):
                rule_ms.append(memberships[idx][var_name])
            alphas[val] += self.or_agg(rule_ms)
        
        return self.output_variable.weight_average_defuzzification(alphas)
    
    
def main(pa_gain, pv_gain, cp_gain, cv_gain, aa_gain, ca_gain):
    pole_angle = Variable(gain=pa_gain)
    pole_angle.auto_devide()
    pole_velocity = Variable(gain=pv_gain)
    pole_velocity.auto_devide()

    cart_position = Variable(gain=cp_gain)
    cart_position.auto_devide()
    cart_velocity = Variable(gain=cv_gain)
    cart_velocity.auto_devide()

    action = Variable()
    action.auto_devide()

    angle_controller = MamdaniController([pole_angle, pole_velocity], action, angle_rules, 'angle')  
    position_controller = MamdaniController([cart_position, cart_velocity], action, position_rules, 'position')

    env = ContinuousCartPoleEnv()

    cart_position_val, cart_velocity_val, pole_angle_val, pole_velocity_val = env.reset(0.1)
    done = False
    time_step = 0
    results = []
    while not done:
        angle_action = np.array([angle_controller.control(pole_angle_val, pole_velocity_val)])
        cart_action = np.array([position_controller.control(cart_position_val, cart_velocity_val)])
        action = (aa_gain*angle_action + ca_gain*cart_action)/(aa_gain+ca_gain)
        # print('Cart:', cart_position_val, cart_velocity_val, cart_action[0] )
        # print('Pole:', pole_angle_val, pole_velocity_val, angle_action[0])
        # print('Action:', action)
        state, reward, done, _ = env.step(action)
        cart_position_val, cart_velocity_val, pole_angle_val, pole_velocity_val = state
        env.render()
        time_step += 1
    return time_step
    
        

if __name__ == '__main__':
    pa_gain = 10
    pv_gain = 10
    cp_gain = 0.5
    cv_gain = 0.5
    aa_gain = 1
    ca_gain = 1
    main(pa_gain, pv_gain, cp_gain, cv_gain, aa_gain, ca_gain)
