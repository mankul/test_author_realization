


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

