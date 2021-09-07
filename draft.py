def parse(str_arr):
    arr = str_arr.split('\n')
    arr = [e.strip().replace(',', '.') for e in arr]
    arr = [float(e) for e in arr]
    return arr


concentrations = parse("""0,002
0,02
0,03
0,2
0,3
0,4
1""")
od605 = parse("""0,0008
0,0016
0,0033
0,01385
0,0374
0,0424
0,1258""")
# LINEAR REGRESSION
import numpy as np

od605 = np.array(od605)
concentrations = np.array(concentrations).reshape(-1, 1)

x = np.linalg.solve(concentrations.T @ concentrations, concentrations.T @ od605)
equation=f'OD-605 = Concentration of 6 * {x[0]:.4f} = 1000/6 * concentration * {x[0]:.4f}'
print(equation)
# PLOT
predicted = concentrations @ x
import matplotlib.pyplot as plt

plt.plot(concentrations, od605, marker='o')
plt.plot(concentrations, predicted, color='red')
plt.title(equation)
plt.show()
