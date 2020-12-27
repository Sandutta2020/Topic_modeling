import pandas as pd
import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning)
import os
from src.data_preprocessing import data_preprocessing
from src.utilities import read_yaml


def main_funct(df: pd.DataFrame, def_flag: bool = False):
    if def_flag:
        conf = read_yaml("params.yaml")
        srcFile = conf["srcFile"]
        columnName = conf["columnName"]
        Limit = conf["Limit"]
        df = pd.read_csv(srcFile)
        df_short = df.loc[1:Limit, [columnName]]
    else:
        df_short = df

    data_preprocessing(df_short)
    os.system("python src/hyper_tuning_model.py")
    os.system("python src/generate_report.py")


if __name__ == "__main__":
    def_flag = True
    df =pd.DataFrame
    start =read_yaml("params.yaml","startTopic")
    end =read_yaml("params.yaml","endTopic")
    main_funct(df,def_flag)
