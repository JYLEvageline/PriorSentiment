import priorsentiment.priorsentiment as pr

f = open('pos.txt','r')
d1 = f.readlines()
f1 = open('negative.txt')
d2 = f.readlines()
test = pr.SO(d1,d2)
f2 = open('test.txt','r')
d3 = f2.readlines()
for sen in d3:
    test.cal_sen(sen)
f.close()
f1.close()
f2.close()
print("positive: ",test.posl,"negative: ",test.negl,"neutral: ",test.neul)