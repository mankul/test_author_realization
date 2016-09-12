import matplotlib.pyplot as plt
import sys
import os



labels={}
#def main():

def plot_and_filter(directory_n):
    #directory_name="/home/mankul/text_reader/"+sys.argv[1]
    directory_name= directory_n
    print directory_n, directory_name
    s=os.listdir(directory_name)
    print s
    escape_chars=[" ","\n","\t","\'","\"","\\","/"]
    auth_dict={}
    all_labels_list=[]
    for filename in s:
        fp=open(directory_name+"/"+filename,"rb")
        print filename
        file_name=filename[:-4].split()[0]
        if filename[:4].split()[0] != ".txt":
            continue;
        print filename,"\n",file_name
        dict_of_words={}
        data=fp.read()
        word=""
        key_r=0
        key_var=""
        val_var=""
        for chare in data:
            if chare in escape_chars:
                continue
            elif chare == "[" :
                dict_list=word
                dict_of_words[dict_list]={}
                word=""
            elif chare=="," and key_r==1:
                key_var=word
                word=""
                val_var=""
                key_r=0
            elif chare == "(":
                key_r=1
            elif chare == ",":
                continue
            elif chare == ")" :
                val_var=word
                word=""
                print val_var
                dict_of_words[dict_list][key_var]=val_var
                key_var=""
            elif chare == "]":
                word=""
            else:
                word=word+chare
        auth_dict[file_name]=dict_of_words
        
    for f_name in auth_dict.keys():
        file_name=auth_dict[f_name]
        for lister in file_name.keys():
            listes=file_name[lister]
            list1=[]
            for key in listes.keys():
                list1.append(key)
            all_labels_list=set().union(all_labels_list,list1)

    k=1
    ##labels as keys are labels and values are integers
    for lab in all_labels_list:
        labels[lab]=k
        k=k+1
        
    plt.xticks(rotation='vertical')###################try this
    #plt.setp(axes,xticks=labels.values(),xticklabels=labels.keys(),rotation='vertical')###################try this
    plotting_graph(auth_dict,directory_name+"/")
    comparision_plotter(auth_dict,directory_name+"/")



    
def plotting_graph(auth_dict,directory_name):
    ##########plotting the individual graph for every possible collection of words saturated in the dictionary in the given folder.....
    #####################################    opening a file for writing
    fp=open("author's_database.txt","w")
    fp.close()
    #
    #
    colors={0:'r',1:'b',3:'g',2:'y',4:'c'}
    markers={0:"^",1:"*",2:"+",3:'*',4:"o"}
    num=0
    full_fig, full_ax = plt.subplots(figsize=(20,10))
    for f_name in auth_dict.keys():
        #print f_name
        file_name=auth_dict[f_name]
        for lister in file_name.keys():
            part_fig,part_ax= plt.subplots(figsize=(20,5))
            plt.xticks(rotation = 90)
            plt.setp(part_ax,xticks=labels.values(),xticklabels=labels.keys())#,rotation=45)###################try this
            print lister,"lister"
            listes=file_name[lister]
            y=[]
            x=[]
            coord={}
            for key in listes.keys():
                val=listes[key]
                x.append(float(labels[key]))
                y.append(float(val))
                #coord[int(labels[key])]=float(val)
                #coord=sorted(coord)
            # 
            #art_ax.xticks(x,labels,rotation='vertical')
            part_ax.plot(x, y,'ro', color=colors[num], marker=markers[num], markersize=9, mew =2, linewidth=2)
            #art_ax.xlabel("frequency")
            #art_ax.ylabel(lister)
            st=f_name+lister+".png"
            part_ax.set_title(f_name+lister)
            part_fig.savefig(directory_name+st)
            #
            #ull_ax.xticks(x,labels,rotation='vertical')
            #
            full_ax.plot(x, y, 'ro', color=colors[num], marker=markers[num], markersize=9, mew =2, linewidth=2)
            #
            #ull_ax.xlabel("frequency")
            #ull_ax.ylabel(lister)
            #plotter(x,y,num,labels,colors,markers,lister,f_name)
            #
            num=(num+1)%5
            #
        full_fig.savefig(directory_name+"full_img.png")
    #plt.show()


    
    
def comparision_plotter(auth_dict,directory_name):
    ##########################comparision plotting on the various seperated values
    colors={0:'r',1:'b',3:'g',2:'y',4:'c'}
    markers={0:"^",1:"*",2:"+",3:'*',4:"o"}
    num=0
    comparision_dict={}
    ##############filtering data from the dictionary made in main function, over various parameters, with every parameter contains various authors data
    for f_name in auth_dict.keys():
        #print f_name
        file_name=auth_dict[f_name]
        for lister in file_name.keys():
            listes=file_name[lister]
            if lister in comparision_dict.keys():
                comparision_dict[lister][f_name]=file_name[lister]
            else:
                new_dict={}
                new_dict[f_name]=file_name[lister]
                comparision_dict[lister]=new_dict
    print comparision_dict
    #
    #
    for lister in comparision_dict.keys():
        listes=comparision_dict[lister]
        colors={0:'r',1:'b',3:'g',2:'y',4:'c'}
        markers={0:"^",1:"*",2:"+",3:'*',4:"o"}
        num=0
        #        
        part_fig,part_ax= plt.subplots(figsize=(20,5))
        for f_name in listes.keys():
            file_name=listes[f_name]
            y=[]
            x=[]
            coord={}
            for key in file_name.keys():
                val=file_name[key]
                x.append(float(labels[key]))
                y.append(float(val))
                #coord[int(labels[key])]=float(val)
                #coord=sorted(coord)
            #print x
            #print y
            plt.xticks(rotation = 90)
            plt.setp(part_ax,xticks=labels.values(),xticklabels=labels.keys())#,rotation=45)###################try this
            part_ax.plot(x,y,"ro",color=colors[num],marker=markers[num], markersize=9, mew =2, linewidth=2)
            num=(num+1)%5
            st=lister+".png"
            part_fig.savefig(directory_name+st)

            
#if __name__=="__main__": main()
