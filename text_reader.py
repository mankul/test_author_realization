###############
##
#suggestions for storage of data
#store data in dictionary,
#store data alphabatically, such that searching will be linear
#store data in dictinaries or tabulate the data
#reading the text file data, and creating the hashmap for the data


def main():
    f= open("/home/mankul/text_reader/Karma-Yoga-by-Swami-Vivekananda.txt",'r')
    
    #stop words file 
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
    print stop_words

 ##### list of special symbols and articles           
    special_symb=[',','.',' ','-','?','\'','\"','\n',':',';','//','`','!']
    articles=['a','an','the']
    s=f.read()
   # //print f
    #//print s
    
##############
####### 
    dict_words = {}
    dict_articles={'a':0,'an':0,'the':0}
    
    common_words={'a','an','and','the','that','they','of','to','in','all','he','she','this','as','you','me','we','not','be','or'}
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
                
                if t in dict_words.keys():
                    dict_words[t]=dict_words[t]+1
                else:
                    dict_words[t]=1
                t=""
            continue
        else:
            t=t+i
    cn=0
    for i in sorted(dict_words):
        
        print i,"\t\t",dict_words[i]
        cn=cn+dict_words[i]
    print "\n",cn
    print "\n",dict_articles
    list_of_top20=[]
    count=0
    for key, value in sorted(dict_words.items(), key=lambda (k,v): (v,k) ,reverse=True):
        # //print key,"\t",value
        if count<20 :
           if  key in common_words:
               continue
           else:
            count=count+1
            list_of_top20.append((key,value))
        else:
            break
    print list_of_top20  

if __name__ == "__main__" : main()




