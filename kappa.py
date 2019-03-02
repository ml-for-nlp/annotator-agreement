from nltk.metrics import agreement, ConfusionMatrix
import itertools
import sys
import os

test_data = [['kim', 'Washington', 'PER'],['sandy', 'Washington', 'LOC'],['kim', 'Italy', 'ORG'],['sandy', 'Italy', 'LOC'],['kim', 'Einstein', 'PER'],['sandy', 'Einstein', 'PER'],['kim', 'Rovereto', 'LOC'],['sandy', 'Rovereto', 'LOC'],['kim','Google','ORG'],['sandy', 'Google', 'ORG'],['kim', 'Jupiter', 'LOC'],['sandy','Jupiter','LOC']]

def load_coders():
    coders = [f[:-4] for f in os.listdir('./annotations/') if os.path.isfile(os.path.join('./annotations/', f)) and f[-4:] == ".txt"]
    return coders

def load_data(coders):
    data = []

    for username in coders:
        input_file = "./annotations/"+username+".txt"
        f = open(input_file,'r')
        for l in f:
            l = l.rstrip('\n')
            datapoint = l.split("::")[0]
            answer = l.split("::")[1]
            data.append([username,datapoint,answer])
    return data

def get_coder_answers(coder_name, datapoints):
    #print("Getting coder answers for",coder_name,"...")
    coder_answers = []
    for i,answers in datapoints.items():
        for coder, answer in answers.items():
            if coder == coder_name:
                coder_answers.append(answer)
    return coder_answers

def get_datapoints(data):
    datapoints = {}
    for i in data:
        if i[1] not in datapoints:
            datapoints[i[1]] = {}
        datapoints[i[1]][i[0]] = i[2]
    return datapoints

def get_test_coders(data):
    return list(set([d[0] for d in data]))

def get_disagreements(datapoints):
    disagreements = {}
    for i,answers in datapoints.items():
        answered_categories = answers.values()
        if len(set(answers.values())) > 1:
            disagreements[i] = answers
    return disagreements

coders = []
data = []

if len(sys.argv) > 1:
    if sys.argv[1] == "--test":
        print("Running test kappa...")
        coders = get_test_coders(test_data)
        print(coders)
        data = test_data
        #print(data)
    else:
        print("I don't know this argument. Try again.")
        exit() 

if len(sys.argv) == 1:
    coders = load_coders() 
    #print(coders)
    data = load_data(coders)
    #print(data)

num_coders = len(coders)
datapoints = get_datapoints(data)

task = agreement.AnnotationTask(data=data)
for pair in itertools.combinations(coders, 2):
    print("\n\n*** Coders",pair[0],pair[1]," ***")
    print("\nObserved agreement:",task.Ao(pair[0],pair[1]))
    print("Expected agreement:",task.Ae_kappa(pair[0],pair[1]))
    print("Pairwise kappa:",task.kappa_pairwise(pair[0],pair[1]))
    a1 = get_coder_answers(pair[0], datapoints)
    a2 = get_coder_answers(pair[1], datapoints)
    cm = ConfusionMatrix(a1,a2)
    print("\n",cm)

print("Average kappa for this task:")
print(task.kappa())


#for i,answers in datapoints.items():
#    print(i,answers)

print("\n\nNow printing disagreements:")

disagreements = get_disagreements(datapoints)

for d,answers in disagreements.items():
    print(d,answers)
