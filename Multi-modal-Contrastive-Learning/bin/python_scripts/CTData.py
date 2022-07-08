#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 13:11:51 2022

@author: shruthi
"""

import pandas as pd
import os, glob, shutil

class CTData():
    def separateCTData(self):
    
        # get the files which have CT in the captions
        
        file = '/Users/shruthi/Downloads/release/data.csv'
        data = pd.read_csv(file)
        captions = data[['pdf_hash','s2orc_caption']]
        captionsNoNA = captions.dropna().reset_index(drop=True)
        
        CT = captionsNoNA[captionsNoNA['s2orc_caption'].str.contains('CT')].reset_index(drop=True)
        prefix = '/Users/shruthi/Downloads/release/figures/'
        new_folder = '/Users/shruthi/Downloads/release/CT/'
        #copied_items = '\t'.join(glob.glob(new_folder + "*.png"))
        
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)
            
        for i in CT['pdf_hash']:
            files = glob.glob(prefix + i + "*.png")
            for file in files:
                shutil.copy(file, new_folder)
        
            
if __name__ == '__main__':
    CTObj = CTData()
    CTObj.separateCTData()

