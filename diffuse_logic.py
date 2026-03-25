import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

distance = ctrl.Antecedent(np.arange(0, 11, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 11, 1), 'speed')
crossing = ctrl.Consequent(np.arange(0, 11, 1), 'crossing')

distance['far'] = fuzz.trimf(distance.universe, [0, 0, 5])
distance['near'] = fuzz.trimf(distance.universe, [0, 5, 10])
distance['very_near'] = fuzz.trimf(distance.universe, [5, 10, 10])

speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 5])
speed['fast'] = fuzz.trimf(speed.universe, [0, 5, 10])
speed['very_fast'] = fuzz.trimf(speed.universe, [5, 10, 10])

crossing['walking'] = fuzz.trimf(crossing.universe, [0, 0, 5])
crossing['trotting'] = fuzz.trimf(crossing.universe, [0, 5, 10])
crossing['running'] = fuzz.trimf(crossing.universe, [5, 10, 10])

rule1 = ctrl.Rule(distance['far'] & speed['slow'], crossing['walking'])
rule2 = ctrl.Rule(distance['near'] & speed['fast'], crossing['running'])

control_system = ctrl.ControlSystem([rule1, rule2])
simulation = ctrl.ControlSystemSimulation(control_system)

simulation.input['distance'] = 3.5
simulation.input['speed'] = 8.2

simulation.compute()

result = simulation.output['crossing']

if result <= 2.5:
    interpretation = 'walking'
elif result <= 7.5:
    interpretation = 'trotting'
else:
    interpretation = 'running'

print('Result:', result)
print('Interpretation:', interpretation)

distance.view()
speed.view()
crossing.view()
plt.show()
