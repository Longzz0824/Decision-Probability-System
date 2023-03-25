'''import calculation
import graph_matrix
import graphs
import heuristic
import brute_force
g1 = graph_matrix.random_graph_generate(8)

#print(g1.ability_matrix)
#print(g1.adjacency_matrix)

calculation.print_special_states(g1)
print('the probability if all the transitions are activated: ')
calculation.print_result(g1)
print('\nthe result of deactivate all useless transitions :')
heuristic.deactivate_all_useless_transitions(g1)
print('\nthe result of dijkstra :')
heuristic.dijkstra(g1)
heuristic.brute_force_after_daut(g1)
brute_force.brute_force(g1)'''
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置主题风格
sns.set_theme(style="whitegrid")

# 加载内置的企鹅数据集
penguins = pd.DataFrame({
    '职称': {0:"正教授", 1:"副教授", 2:"助理教授"},
    '频数': {0:151, 1:131, 2:58}
})

# 绘制分组柱状图，按物种和性别分组，显示体重均值和标准差
g = sns.barplot(
    data=penguins,
    x="职称",
    y="频数",

)

# 添加标题和坐标轴标签
g.set_title("Penguin body mass by species and sex")
g.set_xlabel("Species")
g.set_ylabel("Body mass (g)")

# 显示图形
plt.show()

'''
transition_probs = {
    's0': [('s1', 0.5, True), ('s1', 0.5, True)],
    's2': [('s4', 0.98, False), ('s3', 0.02, False)],
    's1': [('s3', 0.01, False), ('s4', 0.99, True)],
    's4': [('s4', 1, True)]}
print("Length : %d" % len (transition_probs))
for state, transitions in transition_probs.items():
    print(state)
    print(transitions)