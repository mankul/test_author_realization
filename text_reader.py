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
import filter_sep
import tokener

def main():
    ############## the directory name is text_of_authors........ uncomment it........

    os.system("mkdir ./text_data")

    directory_name="./text_of_authors"
    directory_data="./text_data"
    testing_data="./testing_data"
    dir_file=os.listdir(directory_name)
    
    #################################################### data seet created in ./test_data folder, so code commented to reduce processing
    #############                                        uncomment in full running.

    for filename in dir_file :
    #    print filename
        filter_sep.file_for(filename,directory_name,directory_data)
    plotting_graph.plot_and_filter(directory_data)
    #
    testing_file=os.listdir(testing_data)

    
    ####################################################testing data created in ./testing_data/testfiles folder
    #########     uncomment when runnnig from scratch.

    os.system("mkdir ./testing_data/testfiles")
    testfiles=testing_data + "/" + "testfiles"
    for f_name in testing_file:
    #    print f_name
        testing_method(testing_data, f_name, testfiles , directory_data + "/")

    #################################################testing the test data against the code

    file_dir= os.listdir(testfiles)
    directory_files=os.listdir(directory_data)
    data_list_of_dict=[]
    for files in directory_files:
        data_dict={}
        m=files[-4:].split()[0]
        if m == ".txt":
            data_dict=tokener.tokenizer(directory_data + "/" + files,files)
            data_list_of_dict.append(data_dict)
    
    for file_name in file_dir:
        m=file_name[-4:].split()[0]
        if m == ".txt":
            verifier(file_name,testfiles,data_list_of_dict)###directory_data)
            

    
##################################################################################### verifier method


def verifier(file_name, test_files,data_list_of_dict):#directory_data):
    list_of_frequency_match=[]
    test_dict={}
    test_dict=tokener.tokenizer(test_files + "/" + file_name,file_name)
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
        for test_top_k_choices in list1:
            temp_dict[test_top_k_choices]=indexing_and_matching_frequency(list1[test_top_k_choices],data_dict[test_top_k_choices])
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

##################################################################################

def testing_method(testing_data,file_name, testfiles, testing_dir):
    #print file_name
    #print testing_dir
    cmdstr="mkdir %stestfiles" % (testing_dir)
    os.system(cmdstr)
    filter_seperator(file_name,file_name,testing_data,testfiles)



###########################################################################################3

if __name__ == "__main__" : main()




