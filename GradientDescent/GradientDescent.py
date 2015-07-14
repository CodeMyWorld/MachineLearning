__author__ = 'alex'


class HypothesisFunction(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_value(self, c, b):
        return c + b * self.x

data = []
preResult = 0

threshold = 0.01
# learning rate
a = 0.007
w0 = 0
w1 = 0
m = 0

dataFile = open("data.txt")

for line in dataFile:
    lineList = line.split()
    m += 1
    data.append(HypothesisFunction(float(lineList[0]), float(lineList[1])))

while True:
    sum_w0 = 0
    sum_w1 = 0

    for i in range(m):
        sum_w0 += (data[i].get_value(w0, w1) - data[i].y)
        sum_w1 += (data[i].get_value(w0, w1) - data[i].y)*data[i].x

    w0 -= a*sum_w0/m
    w1 -= a*sum_w1/m
    print "%f %f" % (w0, w1)

    this_result = 0
    for i in range(m):
        this_result += (data[i].get_value(w0, w1) - data[i].y) * (data[i].get_value(w0, w1) - data[i].y)

# the condition is wrong maybe  is something like w0_pre - wo_current < threshold?
    if abs(this_result/(2*m) - preResult) < 1:
        break
    preResult = this_result
print w0
print w1
