# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:24:42 2019

@author: BHN
"""
import pandas as pd
import itertools

def Deal_data():

    df=pd.read_csv(r'C:\Users\DioChen\Desktop\Python-Learning\watermelon.csv',encoding='utf-8')

    answer = {}
    for class_num,a in enumerate(list(df.columns[1:-1])): 
        one_class_label = list(set(df[a].values))

        single_class_conditional_attribute_set = []
        for b in one_class_label:
            single_class_conditional_attribute_set.append(set(df[df[a] == b].ID.values))
        answer[str(class_num)]=single_class_conditional_attribute_set
    
    answer_decision = {}
    one_class_label = list(set(df[df.columns[-1]].values))
    single_class_conditional_attribute_set = []
    for b in one_class_label:
        single_class_conditional_attribute_set.append(set(df[df[df.columns[-1]] == b].ID.values))
    answer_decision['0']=single_class_conditional_attribute_set
    return answer,answer_decision
        
def liang_zu_guan_xi_de_deng_jia_lei(list_a,list_b):
    answer = []
    for A in list_a:
        for B in list_b:
            tmp = A&B
            if tmp != set():
                answer.append(tmp)
    return answer

def Pos_2_attributes(C,D):
    answer = []
    for A in C:
        for B in D:
            if A.issubset(B):
                answer.append(A)

    if answer != []:
        union = answer[0]
        for a in answer:
            union = union|a

    else:
        union = set()
    return union
        
    
if __name__ =='__main__':
    conditional_attribute_set,decision_attribute_set = Deal_data()
    equivalence_class_count = len(conditional_attribute_set)
    for level in range(2,equivalence_class_count+2):
        for class_combination in itertools.combinations(range(equivalence_class_count), level):

            combination_id = "".join([str(o) for o in class_combination])
            previous_equivalence_class_id = combination_id[:-1]
            latter_equivalence_class_id = combination_id[-1]
            conditional_attribute_set[combination_id] = \
            liang_zu_guan_xi_de_deng_jia_lei(\
                                             conditional_attribute_set[previous_equivalence_class_id],\
                                             conditional_attribute_set[latter_equivalence_class_id])

                
    decision_attribute_number = 0
    for a in decision_attribute_set['0']:
        decision_attribute_number = decision_attribute_number + len(a)
        
    for key in conditional_attribute_set:
        union = Pos_2_attributes(conditional_attribute_set[key],decision_attribute_set['0'])
        if len(union) == decision_attribute_number:
            print(key)
       