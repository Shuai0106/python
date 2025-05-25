import jieba
import logging
import csv
import statistics
from collections import Counter

jieba.setLogLevel(logging.INFO)
data = []
ex = ['不错', '比较', '可以', '感觉', '没有', '我们', '就是', '还是', '非常', '但是', '不过', '有点', '一个', '一般',
      '下次', '携程', '不是', '晚上', '而且', '他们', '什么', '不好', '时候', '知道', '这样', '这个', '还有', '总体',
      '位置', '客人', '因为', '如果', '这里', '很多', '选择', '居然', '不能', '实在', '不会', '这家', '结果', '发现',
      '竟然', '已经', '自己', '问题', '不要', '地方', '只有', '第二天', '酒店', '房间', '虽然']
# [['1', '距离川沙公路较近,但是公交指示不对,如果是"蔡陆线"的话,会非常麻烦.建议用别的路线.房间较为简单.'],
with open('step1/comment.csv', 'r', encoding='GBK') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        data.append(row)
ff_good = []
ff_baad = []
goods = {}
good = [x[1] for x in data if x[0] == '1']
baad = [x[1] for x in data if x[0] == '0']
n = input()
if n == '总评':
    print(f'总评论: {len(data)}')
    print(f'好评: {len(good)}')
    print(f'差评: {len(baad)}')
elif n == '平均':
    lene = [len(x[1]) for x in data]
    ave = statistics.mean(lene)#读取数据返回浮点数，需要round四舍五入
    print(round(ave))
elif n == '好评':
    for ch in good:
        f_good = jieba.lcut(ch)
        ffgood = [x for x in f_good if (x not in ex and len(x) >= 2 and not x.isdigit())]
        for ch in ffgood:
            ff_good.append(ch)
    counter1 = Counter(ff_good)
    sorted_counter = (counter1.most_common())[:15]#使用Counter统计元素出现的次数，再使用most.cpmmon返回排序后的元组为元素的列表
    for ch in sorted_counter:
        print(f'{ch[0]}: {ch[1]}')
elif n == '差评':
    for ch in baad:
        f_baad = jieba.lcut(ch)
        ffbaad = [x for x in f_baad if (x not in ex and len(x) >= 2 and not x.isdigit())]
        for ch in ffbaad:
            ff_baad.append(ch)
    counter2 = Counter(ff_baad)
    sorted_counter = (counter2.most_common())[:15]
    for ch in sorted_counter:
        print(f'{ch[0]}: {ch[1]}')
else:
    print('无数据')
