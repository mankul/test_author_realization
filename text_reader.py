###############
##
#suggestions for storage of data----done
#store data in dictionary,-------done
#store data alphabatically, such that searching will be linear-------done
#store data in dictinaries or tabulate the data---------done
#reading the text file data, and creating the hashmap for the data-------done
#make the words list for each author, with a)high frequeny, b) high frequency with stop words, c) high frequency without stop words
#plotting graph between the various frequencies of results.

import sys
import os

def main():
    ############## the directory name is text_of_authors
    os.system("mkdir ./text_data")
    directory_name="/home/mankul/text_reader/text_of_authors"
    dir_file=os.listdir(directory_name)
    for filename in dir_file :
        file_for(filename)

########################################################################################### poppulating the file
        
def file_for(filename):
    stor_dir="/home/mankul/text_reader/text_data"
    
    
    if filename == "Bhagavad-gita_As_It_Is_plaintxt.txt":
        file_name= stor_dir + "swami_prabhupad.txt"
        
    elif filename == "Freedom_from_the_Known.txt":
        file_name= stor_dir + "sri_aurobindo_ghosh.txt"
        
    elif filename == "Karma-Yoga-by-Swami-Vivekananda.txt":
        file_name= stor_dir + "swami_vivekanada.txt"
        
    else :
        file_name = "not_pr"
        exit()
    f= open(filename,'rb')#("/home/mankul/text_reader/text_data/"+file_name,'rb')
    fp= open(file_name,w)
    #st_new=file_name[:-4].strip()
    #fp= open(st_new+".txt",w)
    ######stop words file read
    sw=open("/home/mankul/text_reader/stop_words.txt",'rb')
    stop_words=[]
    stop_w=sw.read()
    word=""
    for sr in stop_w :
        if sr in ["(",")",",","."," ","\"","\'"]:
            if word != "":
                stop_words.append(word)
                word=""
            continue
        else:
            word=word+sr
    #print stop_words
    
    ##### list of special symbols and articles           
    special_symb=[',','.',' ','-','?','\'','\"','\n',':',';','\\','/','`','!','(',')','{','}',0,1,2,3,4,5,6,7,8,9]
    articles=['a','an','the']
    s=f.read()
    
    # //print f
    #//print s
    
    ##############
    ####### 
    dict_words = {}
    dict_words_with_numerals = {}
    dict_articles={'a':0,'an':0,'the':0}
    list_20_stop_words=[]
    list_20_without_stop_words=[]
    list_of_top20=[]
    #common_words={'a','an','and','the','that','they','of','to','in','all','he','she','this','as','you','me','we','not','be','or'}
    # past={'had'}
    # present={'is','am','are','ing'}
    # future={'will','shall','would','should'}
    #####
    t=""
    for i in s:
        if(i in special_symb):
            if(t!=""):
                ##################################   commmented articles code
                #             if t in dict_articles.keys():
                ##                dict_articles[t]=dict_articles[t]+1
                ###### dictionary logic here #######
                #
                if t.lower() in dict_words.keys():
                    dict_words[t.lower()]=dict_words[t.lower()]+1
                else:
                    dict_words[t.lower()]=1
                t=""
            continue
        else:
            t=t+i

            
    ###########################
    #cn=0
    #for i in sorted(dict_words):
    #   
    #    print i,"\t\t",dict_words[i]
    #    cn=cn+dict_words[i]
    #######print "\n",cn
    #######print "\n",dict_articles
    ##print dict_words
    count=0
    count_1=0
    count_2=0
    for key, value in sorted(dict_words.items(), key=lambda (k,v): (v,k) ,reverse=True):
        # //print key,"\t",value
        if count<20:
            list_of_top20.append((key,value))
            count=count+1
        if count_1<20 or count_2<20:
            if  key in stop_words and count_2 < 20:
                count_2=count_2+1
                list_20_stop_words.append((key,value))
            else:
                if count_1<20:
                    count_1=count_1+1
                    list_20_without_stop_words.append((key,value))
            
        else:
            break
    

    print "\n\nmost_frequent_words\n",list_of_top20,"\n\n\nmost_repetitive_stop_words\n",list_20_stop_words,"\n\n\nmost_words_without_stop_words\n ",list_20_without_stop_words,"\n\n"
    fp.write("\n")
    for nm in ["list_of_top20","list_20_stop_words","list_20_without_stop_words"] :
        fp.write("\n")
        for (k,v) in nm :
            fp.write(k,v)
            fp.write("\n")
    f.close()
    sw.close()
    fp.close()

if __name__ == "__main__" : main()




