import matplotlib.pyplot as plt
if __name__ == '__main__':
    # Customize font style
    font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 18,
        }
    # Ecoli
    # first line is data is from RS algorithm
    rs_class_num = [1,2,3,4,5,6]
    rs_query_times = [1,3,4,6,27,51]
    rs_line, = plt.plot(rs_query_times,rs_class_num, '-',color = 'green',
                        linewidth = 2,label=r'$RS$',
                        marker='*', markeredgecolor = 'green',
                        markerfacecolor ='white',markersize = 10,
                        markerfacecoloralt ='green',markeredgewidth = 2)

    # data from NNDM algorithm
    nndm_class_num = [1,2,3,4,5,6]
    nndm_query_times = [1,3,5,27,28,34]
    nndm_line, = plt.plot(nndm_query_times,nndm_class_num, '-.',linewidth = 2,
                          marker='<', label=r'$NNDM$',color = 'blue',
                          markeredgecolor = 'blue',markerfacecolor ='white',
                          markersize = 10,markerfacecoloralt ='green',
                          markeredgewidth = 2)

    # data from CLOVER algorithm
    clover_class_num = [1,2,3,4,5,6]
    clover_query_times = [1,7,13,14,17,18]
    clover_line, = plt.plot(clover_query_times,clover_class_num, ':',
                            linewidth = 2,marker='s', label=r'$CLOVER$',
                            color = 'black', markeredgecolor = 'black',
                            markerfacecolor ='white', markersize = 10,
                            markerfacecoloralt ='black',markeredgewidth = 2)

    # data from LOF algorithm
    lof_class_num = [1,2,3,4,5,6]
    lof_query_times = [1,2,3,7,8,11]
    lof_line, = plt.plot(lof_query_times,lof_class_num, '--',
                            linewidth = 2,marker='p', label=r'$LOF$',
                            color = 'cyan', markeredgecolor = 'cyan',
                            markerfacecolor ='white', markersize = 10,
                            markeredgewidth = 2)

    # data from RCD-Forest algorithm
    rcd_class_num = [1,2,3,4,5,6]
    rcd_query_times = [1,2,4,5,6,10]
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
