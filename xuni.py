import numpy as np

#定义玩家1与玩家2的收益矩阵分别为u0,u1
u0=np.array( [#石头  剪刀  布
     [0,   1,  -1], # 石头
     [-1,   0,  1], # 剪刀
     [1,   -1,  0]  # 布
     ])
u1=-u0
A0=np.array([0,0,0]) #用于存放玩家1的历史策略
A1=np.array([0,0,0]) #用于存放玩家2的历史策略
a0=np.random.choice(3, 1).item(0)
a1=np.random.choice(3, 1).item(0)
A0[a0]=1
A1[a1]=1
B0=A0 #用于存放玩家1的历史平均策略
B1=A1 #用于存放玩家2的历史平均策略
#进行虚拟博弈
for i in range(10000):
    #根据2的历史平均策略，计算出玩家1当前最优的决策
    earn = B1*np.reshape(u0,(3,3))
    money_sum = np.sum(earn, axis=1)
    a0= np.argmax(money_sum)
    #根据1的历史平均策略，计算出玩家2当前最优的决策
    earn = B0*u1.T
    money_sum = np.sum(earn, axis=1)
    a1= np.argmax(money_sum)
    #对玩家1、2的策略集进行更新
    A0[a0]=A0[a0]+1
    A1[a1]=A1[a1]+1
    B0=A0/sum(A0)
    B1=A1/sum(A1)
print("10000次虚拟博弈后，玩家1、2的选择石头、剪刀、布的概率依次为") 
print(B0)
print(B1)
