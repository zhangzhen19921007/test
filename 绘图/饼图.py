import matplotlib.pyplot as plt
#slices中所有的值加起来为分母，其中任意值/分母为百分比
slices = [10,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
plt.title('Interesting Graph\nCheck it out')
plt.show()