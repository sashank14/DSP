from __future__ import division
import matplotlib.pyplot as plt
import math

#provide function definition here
#############################################################################################################################
## Exponential Decay. The discrete time exponential decay. The Exponential Decay is defined as (a**n) * u[n]
## The exponential decay is, as we will see, the free response of a discrete time first order recursive fiter. 
## Exponential sequences are well behaved only for values of a less than 1 in magnitude; sequences in which mod(a) > 1 are unbounded 
## and represent and unstable behavior (their energy and power are both infinite).
## It is produced by running this program
#############################################################################################################################
def f(x):
     return math.e**(-1*x)

def g(x):
   return 0

def fillYaxis1(xList):  ## returns real number list
    aList = []
    for iter in range(len(xList)):
      aList.append(f(xList[iter]))
    
    return aList

def fillYaxis2(xList):  ## returns complex number list
    aList = []
    for iter in range(len(xList)):
      aList.append(g(0))
    
    return aList

def TickLabels(iList):
    oList = []
    for iter in range(len(iList)):
        oList.append(""+str(iList[iter])+"")
    
    return oList


def plotGraph():
  plt.title('x vs f(x)   \n')
  x_axis = range(0,15) #[1,2,3,4,5]
  x_tick_labels = TickLabels(x_axis)
  plt.xlim(x_axis[0],x_axis[-2])
  plt.xticks(x_axis[0:-1], x_tick_labels[0:-1], rotation='horizontal' , fontsize='10')
  plt.xlabel('\n X  -- > ', fontsize=14, color='blue')
  plt.ylabel('Y  -- > \n', fontsize=14, color='blue',rotation='vertical' )
  #plt.yticks(y_axis, y_tick_labels, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  ###f(x)
  y_axis1 =  fillYaxis1(x_axis)
  ###g(x)
  y_axis2 =  fillYaxis2(x_axis)
  plt.ylim(min(y_axis1+y_axis2), max(y_axis1+y_axis2)) ## + concatenates the list
  y_tick_labels1 = TickLabels(y_axis1)
  y_tick_labels2 = TickLabels(y_axis2)
  ###########################################################################
  ####### 
  ###########################################################################
  y_axis_all = y_axis1+y_axis2
  y_tick_labels_ALL = y_tick_labels1+y_tick_labels2
  ###########################################################################
  ####### 
  ###########################################################################
  plt.yticks(y_axis_all, y_tick_labels_ALL, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  #line1, = plt.plot(x_axis,y_axis1,linestyle = "-", color = "b", marker = "d", markerfacecolor = "b", markersize=10) 
  markerline, stemlines, baseline = plt.stem(x_axis, y_axis1, '-.', bottom=0,zorder =3)
  line2, = plt.plot(x_axis,y_axis2,linestyle = "-", color = "k", marker = None, markerfacecolor = "g", markersize=10,zorder =2)
  #plt.grid(True, which ="major")
  #plt.grid(True, which ="minor")
  ax = plt.axes()
  #ax.xaxis.grid(True)
  plt.legend((markerline,line2),("f(x) = Exponential Decay = (a**n) * u[n] = math.e**(-1*x) ","g(x) = 0"),loc="upper left")
  plt.show()

plotGraph()

