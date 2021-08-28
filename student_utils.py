import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from itertools import chain

def clean_input_csv(path):
    clean_header=["image_index","finding_labels","follow_up","patient_id",
              "patient_age","patient_gender","view_position","image_width",
              "image_height","image_pixel_spacing_x","image_pixel_spacing_y","unnamed"]
    df=pd.read_csv('/data/Data_Entry_2017.csv',header=0,names=clean_header)
    df.pop("unnamed")
    return df
def conv_finds_to_binary_cols(df):
    df=df.copy()
    df["finding_labels"]=df["finding_labels"].apply(lambda x:x.split("|"))
    findings= ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema',
       'Effusion', 'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration',
       'Mass', 'No Finding', 'Nodule', 'Pleural_Thickening', 'Pneumonia',
       'Pneumothorax']
    findings_df=pd.DataFrame(columns=findings)
    for finding in findings:
        findings_df[finding]=df["finding_labels"].agg(lambda x: 1 if finding  in x else 0)
    data_with_finding_cols_df=pd.concat([df,findings_df],axis=1)
    return data_with_finding_cols_df