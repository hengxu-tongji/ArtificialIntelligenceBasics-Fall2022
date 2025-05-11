import numpy as np

#定义每局游戏的遗憾值
def yihanzhi(action_opponent,action_agent):
    return 1-payoff[action_agent][action_opponent]

payoff = [#石头  剪刀  布
           [0,   1,  -1], # 石头
           [-1,   0,  1], # 剪刀
           [1,   -1,  0]  # 布
        ]
#假设对手采取以1/3概率出石头、剪刀和布
p1=(1/3,1/3,1/3)

#定义遗憾矩阵
A=np.array([0, 0, 0]) 
for i in range(1000):
    action_agent=np.argmin(A)
    action_opponent=np.random.choice(3, 1, p1).item(0)
    A[action_agent]=yihanzhi(action_opponent,action_agent)+A[action_agent]
ans=sum(A)
A=A/ans
print("采取石头、剪刀、布的概率依次为：")
print(A)