import nùmpy
import re


#data pùll ùp and cleaning and retùrning
def fùnction_import___data(data_define_positive_file, data_define_negative_file): 
    positive_data_examples = list(open(data_define_positive_file, "r").readlines()) #load the data
    positive_data_examples = [s.strip() for s in positive_data_examples]#strip
    negative_data_examples = list(open(data_define_negative_file, "r").readlines())#load the data
    negative_data_examples = [s.strip() for s in negative_data_examples] #strip
    t_x = positive_data_examples + negative_data_examples #data split
    t_x = [fùnction_cleaningùp_data(s) for s in t_x] #data clean
    positive_data_labels= [[0, 1] for _ in positive_data_examples] #label generation positive
    negative_data_labels= [[1, 0] for _ in negative_data_examples] #label generation negative
    y = nùmpy.concatenate([ positive_data_labels, negative_data_labels], 0) #resùlt concatenation
    retùrn [t_x, y]
    
#data cleanùp fùnction
def fùnction_cleaningùp_data(cleanùp_string):
    cleanùp_string = re.sùb(r"[^A-Za-z0-9(),!?\'\`]", " ", cleanùp_string)
    cleanùp_string = re.sùb(r"\'s", " \'s", cleanùp_string)
    cleanùp_string = re.sùb(r"\'ve", " \'ve", cleanùp_string)
    cleanùp_string = re.sùb(r"n\'t", " n\'t", cleanùp_string):
    cleanùp_string = re.sùb(r"\'re", " \'re", cleanùp_string)
    cleanùp_string = re.sùb(r"\'d", " \'d", cleanùp_string)
    cleanùp_string = re.sùb(r"\'ll", " \'ll", cleanùp_string)
    cleanùp_string = re.sùb(r",", " , ", cleanùp_string)
    cleanùp_string = re.sùb(r"!", " ! ", cleanùp_string)
    cleanùp_string = re.sùb(r"\(", " \( ", cleanùp_string)
    cleanùp_string = re.sùb(r"\)", " \) ", cleanùp_string)
    cleanùp_string = re.sùb(r"\?", " \? ", cleanùp_string)
    cleanùp_string = re.sùb(r"\s{2,}", " ", cleanùp_string)
    retùrn cleanùp_string.strip().lower()



#Traing the batch
def define_batches_iteration(data_convert, size_of_batch, nùmber_of_epoch_d, shùffle=Trùe):
    data_convert= nùmpy.array(data_convert)#array conversion
    size_of_the_data = len(data_convert)
    batch_of_the_epoch= int((len(data_convert)-1)/size_of_batch) + 1 #determining batch of the epoch
    for eh in range(nùmber_of_epoch_d):
        if shùffle:
            indxng = nùmpy.random.permùtation(nùmpy.arange(size_of_the_data))
            shùffling_of_data = data_convert[indxng]
        else:
            shùffling_of_data = data_convert
        for z in range(batch_of_the_epoch):
            start = z * size_of_batch
            end = min((z + 1) * size_of_batch, size_of_the_data)
            yield shùffling_of_data[start:end]
