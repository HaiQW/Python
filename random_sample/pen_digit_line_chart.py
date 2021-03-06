import matplotlib.pyplot as plt
if __name__ == '__main__':
    # Customize font style
    font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 18,
        }
    # Glass
    # first line is data is from RS algorithm
    rs_class_num = [1,2,3,4,5,6,7,8,9,10]
    rs_query_times = [1,3,4,8,11,13,14,36,55,106]
    rs_line, = plt.plot(rs_query_times,rs_class_num, '-',color = 'green',
                        linewidth = 2,label=r'$RS$',
                        marker='*', markeredgecolor = 'green',
                        markerfacecolor ='white',markersize = 10,
                        markerfacecoloralt ='green',markeredgewidth = 2)

    # data from NNDM algorithm
    nndm_class_num = [1,2,3,4,5,6,7,8,9,10]
    nndm_query_times = [1,18,19,32,52,58,62,68,136,163]
    nndm_line, = plt.plot(nndm_query_times,nndm_class_num, '-.',linewidth = 2,
                          marker='<', label=r'$NNDM$',color = 'blue',
                          markeredgecolor = 'blue',markerfacecolor ='white',
                          markersize = 10,markerfacecoloralt ='green',
                          markeredgewidth = 2)

    # data from CLOVER algorithm
    clover_class_num = [1,2,3,4,5,6,7,8,9,10]
    clover_query_times = [1,48,53,58,59,63,67,70,75,76]
    clover_line, = plt.plot(clover_query_times,clover_class_num, ':',
                            linewidth = 2,marker='s', label=r'$CLOVER$',
                            color = 'black', markeredgecolor = 'black',
                            markerfacecolor ='white', markersize = 10,
                            markerfacecoloralt ='black',markeredgewidth = 2)

    # data from LOF algorithm
    lof_class_num = [1,2,3,4,5,6,7,8,9,10]
    lof_query_times = [1,2,4,17,53,62,73,110,121,209]
    lof_line, = plt.plot(lof_query_times,lof_class_num, '--',
                            linewidth = 2,marker='p', label=r'$LOF$',
                            color = 'cyan', markeredgecolor = 'cyan',
                            markerfacecolor ='white', markersize = 10,
                            markeredgewidth = 2)

    # data from RCD-Forest algorithm
    rcd_class_num = [1,2,3,4,5,6,7,8,9,10]
    rcd_query_times = [1,2,5,6,7,10,23,30,44,45]
    lof_line, = plt.plot(rcd_query_times,rcd_class_num, '-.',
                            linewidth = 2,marker='o', label=r'$RCD-Forest$',
                            color = 'red', markeredgecolor = 'red',
                            markerfacecolor ='white', markersize = 10,
                            markeredgewidth = 2)
    plt.xlabel(r"$Number$ $of$ $Queries$",fontdict = font)
    plt.ylabel(r"$Classes$ $Discovered$",fontdict = font,)
    plt.legend(loc = 4)

#plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
plt.show()
