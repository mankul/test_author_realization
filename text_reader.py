###############
##
#suggestions for storage of data----done
#store data in dictionary,-------done
#store data alphabatically, such that searching will be linear-------done
#store data in dictinaries or tabulate the data---------done
#reading the text file data, and creating the hashmap for the data-------done
#make the words list for each author, with a)high frequeny, b) high frequency with stop words, c) high frequency without stop words
#plotting graph between the various frequencies of results.
#
#
###input files stored in test_of_authors.
###the data is retrieved and saved in text_data folder, with graphs of frequency.
###the testing files are stored in testing_data folder, and various techniques are applied on the files in testing_data folder.



import sys
import os
import plotting_graph

def main():
    ############## the directory name is text_of_authors........ uncomment it........
    #os.system("mkdir ./text_data")
    directory_name="./text_of_authors"
    directory_data="./text_data"
    testing_data="./testing_data"
    dir_file=os.listdir(directory_name)
    
    #################################################### data seet created in ./test_data folder, so code commented to reduce processing
    #############                                        uncomment in full running.
    #for filename in dir_file :
    #    print filename
    #    file_for(filename,directory_name)
    #plotting_graph.plot_and_filter(directory_data)
    #
    testing_file=os.listdir(testing_data)
    
    ####################################################testing data created in ./testing_data/testfiles folder
    #########     uncomment when runnnig from scratch.
    #os.system("mkdir ./testing_data/testfiles")
    testfiles=testing_data + "/" + "testfiles"
    #for f_name in testing_file:
    #    print f_name
    #    testing_method(testing_data, f_name, testfiles , directory_data + "/")

    #################################################testing the test data against the code
    file_dir= os.listdir(testfiles)
    directory_files=os.listdir(directory_data)
    data_list_of_dict=[]
    for files in directory_files:
        data_dict={}
        m=files[-4:].split()[0]
        if m == ".txt":
            data_dict=tokenizer(directory_data + "/" + files,files)
            data_list_of_dict.append(data_dict)
    
    for file_name in file_dir:
        m=file_name[-4:].split()[0]
        if m == ".txt":
            verifier(file_name,testfiles,data_list_of_dict)###directory_data)
            

    
##################################################################################### verifier method


def verifier(file_name, test_files,data_list_of_dict):#directory_data):
    list_of_frequency_match=[]
    test_dict={}
    test_dict=tokenizer(test_files + "/" + file_name,file_name)
    print file_name,"\n"
    finding_frequency(test_dict,data_list_of_dict)
    print "\n\n\n\n"

####################################################  matching frequency of test data with testing data,, test data ie, test_dict with list of dictinary of testing data, ie data_list_of_dict,,, for each file is calculated...


def finding_frequency(test_dict,data_list_of_dict):
    resulting_matching_frequency={}
    for data_key in data_list_of_dict:
         for clusteres in data_key.keys():
             #print clusteres,"\n",data_key[clusteres],"\n\n\n"
             resulting_matching_frequency[clusteres]=matching_frequency_method(test_dict,data_key[clusteres])
    print resulting_matching_frequency
             
    


    
##########################################################


def matching_frequency_method(test_dict, data_dict):
    resulting_dict={}
    for list1 in test_dict.values():
        temp_dict={}
        for test_top_20_choices in list1:
            temp_dict[test_top_20_choices]=indexing_and_matching_frequency(list1[test_top_20_choices],data_dict[test_top_20_choices])
    return temp_dict

def indexing_and_matching_frequency(dict_test,dict_data):
    count1,count2=0,0
    index_of_test_in_data_set={}
    for keys in dict_test.keys():
        count1=count1+(int)(dict_test[keys])
    for keys in dict_data.keys():
        count2=count2+(int)(dict_data[keys])
    count=count1*count2
    list_of_data_keys=dict_data.keys()
    for keys in dict_test.keys():
        if keys in list_of_data_keys:
            index_of_test_in_data_set[keys]=(float(int(dict_test[keys])* int(dict_data[keys])))/count
    return index_of_test_in_data_set

    
################################################################################# tokenizer method

def tokenizer(filename,file_name):
    fp=open(filename,'r')
    escape_chars=[" ","\n","\t","\'","\"","\\","/"]
    
    auth_dict={}
    all_labels_list=[]
    
    file_name=file_name[:-4].split()[0]
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
            dict_of_words[dict_list][key_var]=val_var
            key_var=""
        elif chare == "]":
            word=""
        else:
            word=word+chare
    fp.close()
    auth_dict[file_name]=dict_of_words
    return auth_dict


########################################################################################### poppulating the file
        
def file_for(filename,read_dir):
    stor_dir="./text_data/"
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
    
    ##### list of special symbols and articles           
    special_symb=[',','.',' ','-','?','\'','\"','\n',':',';','\\','/','`','!','(',')','{','}',0,1,2,3,4,5,6,7,8,9]
    articles=['a','an','the']
    s=f.read()

    
    ##############
    
    dict_words = {}
    dict_words_with_numerals = {}
    dict_articles={'a':0,'an':0,'the':0}
    list_20_stop_words=[]
    list_20_without_stop_words=[]
    list_of_top20=[]
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
    tmp_dict={}
    tmp_dict["most_frequent_words"]=list_of_top20
    tmp_dict["most_repetitive_stop_words"]=list_20_stop_words
    tmp_dict["most_words_without_stop_words"]=list_20_without_stop_words
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


##################################################################################

def testing_method(testing_data,file_name, testfiles, testing_dir):
    #print file_name
    #print testing_dir
    #cmdstr="mkdir %stestfiles" % (testing_dir)
    #os.system(cmdstr)
    filter_seperator(file_name,file_name,testing_data,testfiles)



###########################################################################################3

if __name__ == "__main__" : main()




