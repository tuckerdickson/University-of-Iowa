import mathimport pylab def hawkID():    return("ntdickson") # try plotSquares(7), ... 100, 1000#def plotSquares(maxNum=20):    pylab.clf()    xlist, ylist = [], []    for x in range(1,maxNum+1):        xlist.append(x)        ylist.append(x*x)    pylab.plot(xlist, ylist)    pylab.show()# plot linear, n log n, and quadratic functions on the same chart# try plotThree()# def plotThree(maxNum=200):    pylab.clf()    xlist, linlist, nlognlist, sqlist = [], [], [], []    for x in range(1,maxNum+1):        xlist.append(x)        linlist.append(50*x)        nlognlist.append(25 * x * math.log(x,2))        sqlist.append(x*x)    pylab.plot(xlist, linlist, linestyle = '-', color = 'b')    pylab.plot(xlist, nlognlist, linestyle = '--', color = 'r')    pylab.plot(xlist, sqlist, linestyle = ':', color = 'g')    pylab.savefig('plotTwoImage')    pylab.show() # a simple bar chartdef barChartTest():    pylab.clf() # clears the current chart    pylab.bar([0,1,2,3], [5,10,12,2])    # use xticks to specify bar labels    pylab.xticks([v + 0.45 for v in range(4)], ('A', 'B', 'C', 'D') )    pylab.show()        def plotCommonComplexities(maxNum=10):        pylab.clf()    xlist, constlist, linlist, lognlist, nlognlist, sqlist, explist = [], [], [], [], [], [], []        for x in range(1,maxNum+1):        constlist.append(1)        xlist.append(x)        linlist.append(x)        lognlist.append(math.log(x,2))        nlognlist.append(x * math.log(x,2))        sqlist.append(x*x)        explist.append(0.1 * 2**x)            #pylab.semilogy(basey = 2)            pylab.plot(xlist, constlist, linestyle = '-', color = 'b', label='constant')  # constant    pylab.plot(xlist, lognlist, linestyle = '-.', color = 'r', label='logn')  # logn    pylab.plot(xlist, linlist, linestyle = '--', color = 'g', label = 'linear')   # linear    pylab.plot(xlist, nlognlist, linestyle = ':', color = 'c', label = 'nlogn') # nlogn    pylab.plot(xlist, sqlist, linestyle = 'dotted', color = 'm', label = 'squared') # squared    pylab.plot(xlist, explist, linestyle = 'dashdot', color = 'y', label = 'exponential')    pylab.savefig('plotTwoImage')    pylab.legend()    pylab.show() def pieChart():        pylab.clf()        spendingPercent = [30, 7, 23, 4, 10, 19, 7]    items = ['chicken', 'eggs', 'cottage cheese', 'peanut butter', 'bananas', 'apples', 'meal bars']    colors = ['c', 'r', 'g', 'y', 'k', 'b', 'm']        pylab.pie(spendingPercent, labels = items, colors = colors)    pylab.title('Grocery Spending')    pylab.show()        def spiral(r = 1, thetaRange = 100):        pylab.clf()    xlist, ylist = [], []        for theta in range(1, thetaRange+1):        xlist.append(r*math.cos(theta))        ylist.append(r*math.sin(theta))            pylab.plot(xlist, ylist)    pylab.show()