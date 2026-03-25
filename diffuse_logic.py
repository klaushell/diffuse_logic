import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

distance = ctrl.Antecedent(np.arange(0, 11, 1), 'distance')
speed = ctrl.Antecedent(np.arange(0, 11, 1), 'speed')
crossing = ctrl.Consequent(np.arange(0, 11, 1), 'crossing')

# Low x = close, high x = far (peaks match the linguistic labels)
distance['very_near'] = fuzz.trimf(distance.universe, [0, 0, 5])
distance['near'] = fuzz.trimf(distance.universe, [0, 5, 10])
distance['far'] = fuzz.trimf(distance.universe, [5, 10, 10])

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

# Illustrative tip % (0–30) from the same crisp output for linguistic bands
tip = result * 3.0
if tip <= 10:
    tip_interpretation = 'low tip'
elif tip <= 20:
    tip_interpretation = 'medium tip'
else:
    tip_interpretation = 'high tip'

print('Result:', result)
print('Interpretation:', interpretation)
print('Tip (%):', tip)
print('Tip interpretation:', tip_interpretation)

# Pass the real simulation — otherwise skfuzzy uses an empty ControlSystem and
# plots never reflect your inputs or aggregated output.
distance.view(simulation)
speed.view(simulation)
crossing.view(simulation)
plt.show()
