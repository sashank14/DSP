from __future__ import division
import matplotlib.pyplot as plt
import math

#provide function definition here
#############################################################################################################################
## The product of two sequences x[n] and w[n] is their term by term product:
## y[n] = x[n] * w[n]
## 
## 
#############################################################################################################################
def f(x):
   return math.sin(x) 

def g(x):
   return math.cos(x)

def h(x):
   return math.sin(x)*math.cos(x)

def fillYaxis1(xList):  ## returns real number list
    aList = []
    for iter in range(len(xList)):
      aList.append(f(xList[iter]))
    
    return aList

def fillYaxis2(xList):  ## returns complex number list
    aList = []
    for iter in range(len(xList)):
      aList.append(g(xList[iter]))
    
    return aList

def fillYaxis3(xList):  ## returns complex number list
    aList = []
    for iter in range(len(xList)):
      aList.append(h(xList[iter]))
    
    return aList

def TickLabels(iList):
    oList = []
    for iter in range(len(iList)):
        oList.append(""+str(iList[iter])+"")
    
    return oList


def plotGraph():
  plt.title('x vs f(x)   \n')
  #x_axis = range(-15,15+1) #[1,2,3,4,5]
  x_axis = []
  for iter in range(100):
    x_axis.append(iter*0.1)
  x_tick_labels = TickLabels(x_axis)
  plt.xlim(x_axis[0],x_axis[-2])
  #plt.xticks(x_axis[0:-1], x_tick_labels[0:-1], rotation='horizontal' , fontsize='10')
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
  ###h(x)
  y_axis3 =  fillYaxis3(x_axis)
  plt.ylim(min(y_axis1+y_axis2+y_axis3), max(y_axis1+y_axis2+y_axis3)) ## + concatenates the list
  y_tick_labels1 = TickLabels(y_axis1)
  y_tick_labels2 = TickLabels(y_axis2)
  y_tick_labels3 = TickLabels(y_axis3)
  ###########################################################################
  ####### 
  ###########################################################################
  y_axis_all = y_axis1+y_axis2+y_axis3
  y_tick_labels_ALL = y_tick_labels1+y_tick_labels2+y_tick_labels3
  ###########################################################################
  ####### 
  ###########################################################################
  #plt.yticks(y_axis_all, y_tick_labels_ALL, rotation='horizontal' , fontsize='10')
  ###########################################################################
  ####### 
  ###########################################################################
  line1, = plt.plot(x_axis,y_axis1,linestyle = "-", color = "b", marker = ".", markerfacecolor = "b", markersize=10,zorder =1) 
  #markerline, stemlines, baseline = plt.stem(x_axis, y_axis1, '-.', bottom=0,zorder =3)
  line2, = plt.plot(x_axis,y_axis2,linestyle = "-", color = "g", marker = ".", markerfacecolor = "g", markersize=10,zorder =2)
  line3, = plt.plot(x_axis,y_axis3,linestyle = "-", color = "r", marker = ".", markerfacecolor = "r", markersize=10,zorder =3)
  #plt.grid(True, which ="major")
  #plt.grid(True, which ="minor")
  ax = plt.axes()
  #ax.xaxis.grid(True)
  plt.legend((line1,line2,line3),("f(x) = sin(x)","g(x) = cos(x)","h(x) = sin(x)*cos(x)"),loc="upper left")
  plt.show()

plotGraph()

