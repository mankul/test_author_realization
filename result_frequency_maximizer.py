


def frequency_matcher_and_maximizer(r,file_name):
    #print "\n\n\n\n\nthe r is \n",r,"\n\n\n"
    #print file_name
    new_dict={}
    for data in r.keys():
        datum=r[data]
        #print "the data is \n",data
        for authors in datum:
            #print "\n\n\n\nthe data is \t",authors
            print "\n\n\n\n\n",authors
            product=1
            for set_constraints in datum[authors].values(): 
                #print "\nthese are set constraints:",set_constraints
                product=product* float(set_constraints)*100
            new_dict[data]=product
    print file_name, new_dict
    val,aut,normalized_val=maximum_frequency(new_dict)
    print "this file",file_name," matches to the author ",aut," with index value =", val,"\t and the normalized value is", normalized_val
    


def maximum_frequency(new_dict):
    l1=new_dict.keys()
    l2=new_dict.values()
    t1=max(l2)
    t3=sum(l2)
    t2=l1[l2.index(t1)]
    return t1,t2,t1/t3
