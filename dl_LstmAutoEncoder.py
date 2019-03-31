#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:43:07 2018

@author: Shariful
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras_anomaly_detection.library.plot_utils import visualize_reconstruction_error
from keras_anomaly_detection.library.recurrent import LstmAutoEncoder


def main():
    train_path = '/Users/Shariful/Documents/GitHubRepo/Datasets/ADFA-LD/n-gram/5-gram/train/5_gram.csv'
#    attack test path
#    test_path = '/Users/Shariful/Documents/GitHubRepo/Datasets/ADFA-LD/n-gram/5-gram/5_gram_attack_16.csv'
#    normal test path
    
    data_dir_path = '/Users/Shariful/Documents/DataCamp/ADFA-LD(tf-idf)'
    model_dir_path = '/Users/Shariful/Documents/DataCamp/models/'

##    ecg_data = pd.read_csv(data_dir_path + '/train_normal.csv', header=None)
#    ecg_data = pd.read_csv(train_path, header = None, skiprows = 1)
#    ecg_data = ecg_data.drop(ecg_data.columns[0], axis = 1)  
#    print(ecg_data.head())
#    
#    ecg_np_data = ecg_data.as_matrix()
#    scaler = MinMaxScaler()
#    ecg_np_data = scaler.fit_transform(ecg_np_data)
#    print(ecg_np_data.shape)
#
    ae = LstmAutoEncoder()
##
#    # fit the data and save model into model_dir_path
#    ae.fit(ecg_np_data, model_dir_path=model_dir_path, estimated_negative_sample_ratio=0.9)
##    ae.fit(ecg_np_data, model_dir_path=model_dir_path, estimated_negative_sample_ratio=0.9)

    # load back the model saved in model_dir_path detect anomaly
    ae.load_model(model_dir_path)
#    load test set
#    test_atk = pd.read_csv(data_dir_path + '/test_attack.csv', header=None)
#    test_nml = pd.read_csv(data_dir_path + '/test_normal.csv', header=None)
#    df_test = pd.concat([test_atk, test_nml])
#    lab_test = pd.concat([pd.DataFrame([1] * len(test_atk)), \
#                          pd.DataFrame([0] * len(test_nml))], ignore_index=True)
    
    test_idx_path = '/Users/Shariful/Documents/GitHubRepo/Datasets/ADFA-LD/n-gram/5-gram/5_gram_test_idx.csv'
    df_test_idx = pd.read_csv(test_idx_path, header = None, skiprows = 1)
    test_path = '/Users/Shariful/Documents/GitHubRepo/Datasets/ADFA-LD/n-gram/5-gram/5_gram_test.csv'
    df_test = pd.read_csv(test_path, header = None, skiprows = 1)
#    df_test = df_test.drop(df_test.columns[0], axis = 1)
    df_test = df_test.loc[:127949,:]
    
#    anomaly samples 4373-4433
    df_test = df_test.as_matrix()
    scaler = MinMaxScaler()
    df_test = scaler.fit_transform(df_test)
    
       
    anomaly_information = ae.anomaly(df_test)
    anomaly_information = list(anomaly_information)
    
    for idx_seq in range(0, 121): #len(df_test_idx)
        
        start_idx = df_test_idx.loc[idx_seq,0]
        end_idx = df_test_idx.loc[idx_seq,1]
        
        predict_label = 'normal'
        for idx in range(start_idx, end_idx+1):
            if anomaly_information[idx][0]:
                predict_label = 'abnormal'
                break
        print(predict_label)
            
    
##    reconstruction_error = []
#    for idx, (is_anomaly, dist) in enumerate(anomaly_information):
#        print('# ' + str(idx) + ' is ' + ('abnormal' if is_anomaly else 'normal') + ' (dist: ' + str(dist) + ')')
##        reconstruction_error.append(dist)
#
##    visualize_reconstruction_error(reconstruction_error, ae.threshold)


if __name__ == '__main__':
    main()