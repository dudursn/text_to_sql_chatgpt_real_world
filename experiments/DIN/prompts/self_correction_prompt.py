self_correction_prompt = """
#### For the given question, use the provided tables, columns, foreign keys, and primary keys to fix the given Oracle SQL QUERY for any issues. If there are any problems, fix them. If there are no issues, return the Oracle SQL QUERY as is.
#### Use the following instructions for fixing the SQL QUERY:
1) Use the database values that are explicitly mentioned in the question.
2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
3) Use DESC and DISTINCT when needed.
4) Pay attention to the columns that are used for the GROUP BY statement.
5) Pay attention to the columns that are used for the SELECT statement.
6) Only change the GROUP BY clause when necessary (Avoid redundant columns in GROUP BY).
7) Use GROUP BY on one column only.
8) Use FETCH FIRST <NUMBER> ROWS ONLY when needed

{schema}
Foreign_keys = {foreign_keys}
Primary_keys = {primary_keys}
#### Question: {question}
#### {dialect} SQL QUERY
{query}
#### {dialect} FIXED SQL QUERY
SELECT
"""