from table_recall_module import table_recall_main
from column_recall_module import column_recall_main

SQL_GENERATE_PROMPT = """
### Complete oracle SQL query only and with no explanation, and do not select extra columns that are not explicitly requested in the query. 
### Oracle SQL tables, with their properties: 
#
{schema}
#
### {question}
SELECT"""

def generate_clear_prompting(question, db, llm, c3_representation_prompt = True, add_fk = False, callback=None):
    
    if c3_representation_prompt:
        table_schema = db.get_schema_openai_prompt()
    else:
        table_schema = db.get_table_info()
    tables_ori = db.get_table_names()
    table_list = table_recall_main(table_schema, tables_ori, question, llm, callback= callback)
    
    if c3_representation_prompt:
        specific_tables_schema = db.get_schema_openai_prompt(table_list)
        tables_cols_ori = db.get_schema_json(table_list)
        foreign_keys_prompt = ""
        if add_fk:
            foreign_keys_prompt = db.get_foreign_keys_openai_prompt(table_list)

        schema_result = column_recall_main(specific_tables_schema, tables_cols_ori, question, llm, foreign_keys_prompt, callback=callback)
        
        if schema_result is not None:
            schema_result_prompt = get_schema_to_clear_prompt(schema_result, foreign_keys_prompt)
        else:
            schema_result_prompt = db.get_schema_openai_prompt(table_list) + foreign_keys_prompt
        
    else:
        schema_result_prompt = db.get_table_info(table_list)
        
    clear_prompt_template = SQL_GENERATE_PROMPT.format(schema=schema_result_prompt, question=question)
    
    return clear_prompt_template

def get_schema_to_clear_prompt(schema_result, foreign_keys_prompt):
    schema_result_pompt = ""
    for tbl, columns in schema_result.items():
        schema_result_pompt += f"# {tbl} ({', '.join([c for c in columns])})\n"
    
    schema_result_pompt += foreign_keys_prompt
        
    return schema_result_pompt

