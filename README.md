
# Text-to-SQL Meets the Real-World

Text-to-SQL refers to the task defined as “given a relational database D and a natural language sentence S that describes a question on D, generate an SQL query Q over D that expresses S”.  This repository contains the experiments described in the paper "Text-to-SQL Meets the Real-World" in mondial database. It explores how a selected set of LLM-based text-to-SQL tools perform over two challenging databases, an openly available database, Mondial, and a proprietary industrial database, IndDB. The paper also proposes a new LLM-based text-to-SQL tool that combines features from tools that performed well over the Spider and BIRD benchmarks. Then, the paper describes how the selected tools and the proposed tool, running under GPT-3.5 and GPT-4, perform over the Mondial and the IndDB databases over a suite of 100 carefully defined natural language questions that are closely related to those observed in practice. 

## Strategies

- Keyword Search Tool 
    - Danke
- Manual Prompt + Danke
- Langchain
    - SQLQueryChain
    - SQLDatabaseSequentialChain
    - SQLAgent
- DIN (https://github.com/MohammadrezaPourreza/Few-shot-NL2SQL-with-prompting)
- C3 (https://github.com/bigbigwatermalon/C3SQL)
- C3-DIN Combining

## Dataset information
- [Link](/datasets/mondial/README.md)
