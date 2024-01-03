import json
import pandas as pd
import tiktoken

def load_json(path):
    with open(path,"r", encoding="utf8") as f:
        return json.load(f)
    
def open_txt(file):
    with open(file,"r", encoding="utf8") as f:
        return f.read()

def default_excel(df, resultFile):
    with pd.ExcelWriter(resultFile) as writer:
        df.to_excel(writer,  sheet_name='Sheet1') 
        writer.book.formats[0].set_text_wrap()

def save_json(result_file_json, json_data):
    with open(result_file_json, "w", encoding="utf8") as fp:
        json.dump(json_data , fp, ensure_ascii=False) 

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def utf8len(s):
    return len(s.encode('utf-8'))