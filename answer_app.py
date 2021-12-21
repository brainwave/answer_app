import argparse
import os
import sys
import pandas as pd

parser = argparse.ArgumentParser(description = 'Show answers in selected range')

parser.add_argument('answer_key_path', metavar='answer_key_path', type=str, help='path to answer key csv file')

parser.add_argument('start_qno', metavar='starting_question_number', type=int, help='which question number to start displaying answers')

parser.add_argument('end_qno', metavar='ending_question_number', type=int, help='which question number to end displaying answers')

args = parser.parse_args()

#print(args)



if os.path.isfile(args.answer_key_path):
    answer_key = pd.read_csv(args.answer_key_path, header=None)
    #print(max(answer_key.iloc[:,0].values), 'Max Answer No')
    #print(min(answer_key.iloc[:,0].values), 'Min Answer No')
    if (args.start_qno < min(answer_key.iloc[:,0].values)) or (
                args.end_qno > max(answer_key.iloc[:,0].values)):
        print('provided start and end question numbers beyond range in answer key, please re-check file and input values')
        print(max(answer_key.iloc[:,0].values))
        print(min(answer_key.iloc[:,0].values))
        sys.exit()
    else: 
        print(*answer_key[answer_key.iloc[:,0].isin(range(args.start_qno, args.end_qno+1))].values, sep="\n")
        #print('csv file read and provided start and end question numbers are valid')
else:
    print('csv file does not exist')


