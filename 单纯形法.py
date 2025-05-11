from pulp import *

# 1. 建立问题
prob = LpProblem("Problem", LpMaximize)

# 2. 建立变量
x1 = LpVariable("x1",lowBound=0)
x2 = LpVariable("x2",lowBound=0)
x3 = LpVariable("x3",lowBound=0)

# 3. 设置目标函数 z
prob += x1 + x2 + x3

# 4. 施加约束
prob += x1 + 2*x3 <= 1, "constraint1"
prob += 2*x1 + x2 <= 1, "constraint2"
prob += x2 + 2*x3 <= 1, "constraint3"

# 5. 求解
prob.solve()

# 6. 打印求解状态
print("Status:", LpStatus[prob.status])

# 8. 打印最优解的目标函数值
print("z= ", value(prob.objective))

# 7. 打印出每个变量的最优值
for v in prob.variables():
    print(v.name, "=", v.varValue)

