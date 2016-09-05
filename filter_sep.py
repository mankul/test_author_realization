



############ poppulating the file
        
def file_for(filename,read_dir,stor_dir):
    #stor_dir="./text_data" #### no need to uncomment
    read_dir=read_dir 
    print filename
    
    if filename == "Bhagavad-gita_As_It_Is_plaintxt.txt":
        file_name=  "swami_prabhupad.txt"
        
    elif filename == "Freedom_from_the_Known.txt":
        file_name=  "sri_aurobindo_ghosh.txt"
        
    elif filename == "Karma-Yoga-by-Swami-Vivekananda.txt":
        file_name=  "swami_vivekanada.txt"
        
    else :
        file_name = "not_pr"
        return
    filter_seperator(file_name, filename,read_dir,stor_dir)





########################################################################################## seperating the code for reusing in 2 files.
    
def filter_seperator(file_name,filename,read_dir,stor_dir):
    f= open(read_dir + "/" +filename,'r')################("/home/mankul/text_reader/text_data/"+file_name,'rb')
    fp= open(stor_dir + "/" + file_name,'w')
    
    #st_new=file_name[:-4].strip()
    #fp= open(st_new+".txt",w)
    ######stop words file read
    
    sw=open("./stop_words.txt",'rb')
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
    
    ##### list of special symbols and articles           
    special_symb=[',','.',' ','-','?','\'','\"','\n',':',';','\\','/','`','!','(',')','{','}',0,1,2,3,4,5,6,7,8,9]
    articles=['a','an','the']
    s=f.read()

    
    ##############
    
    dict_words = {}
    dict_words_with_numerals = {}
    dict_articles={'a':0,'an':0,'the':0}
    list_k_stop_words=[]
    list_k_without_stop_words=[]
    list_of_top_k=[]
    ########################################################################################
    #common_words={'a','an','and','the','that','they','of','to','in','all','he','she','this','as','you','me','we','not','be','or'}
    # past={'had'}
    # present={'is','am','are','ing'}
    # future={'will','shall','would','should'}
    ########################################################################################
    
    t=""
    for i in s:
        if(i in special_symb):
            if(t!=""):
                ##################################   commmented articles code removed...
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

            
    #################################
    #cn=0
    #for i in sorted(dict_words):
    #   
    #    print i,"\t\t",dict_words[i]
    #    cn=cn+dict_words[i]
    #######print "\n",cn
    #######print "\n",dict_articles
    ##print dict_words
    #################################

    k=20
    count=0
    count_1=0
    count_2=0
    for key, value in sorted(dict_words.items(), key=lambda (k,v): (v,k) ,reverse=True):
        # //print key,"\t",value
        if count<20:
            list_of_top_k.append((key,value))
            count=count+1
        if count_1<k or count_2<k:
            if  key in stop_words and count_2 < k:
                count_2=count_2+1
                list_k_stop_words.append((key,value))
            else:
                if count_1<k:
                    count_1=count_1+1
                    list_k_without_stop_words.append((key,value))
            
        else:
            break
    

    print "\n\nmost_frequent_words\n",list_of_top_k,"\n\n\nmost_repetitive_stop_words\n",list_k_stop_words,"\n\n\nmost_words_without_stop_words\n ",list_k_without_stop_words,"\n\n"
    fp.write("\n")
    tmp_dict={}
    tmp_dict["most_frequent_words"]=list_of_top_k
    tmp_dict["most_repetitive_stop_words"]=list_k_stop_words
    tmp_dict["most_words_without_stop_words"]=list_k_without_stop_words
    fp.write("\n")
    for nm in tmp_dict.keys():
        fp.write("\n")
        fp.write(nm)
        fp.write("\n")
        fp.write(str(tmp_dict[nm]))
        fp.write("\n")
        #for k,v in nm :
        #    fp.write((k,v))
        #    fp.write("\n")
    f.close()
    sw.close()
    fp.close()

