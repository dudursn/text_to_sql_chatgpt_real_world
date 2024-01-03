## Dataset Information
The dataset contains 100 natural language queries related to the Mondial schema.
- Query ID (id)
- Natural language query (string)
- Number of expected results (number_of_results)
- Query type (type: simple, medium, or complex)
- Number of filters in the query (number_of_filters)
- Number of joins in the query (number_of_joins)
- Number of aggregations in the query (number_of_aggregations)
- Keywords (keywords)
- SQL query (query)

## Query Types
The queries are distributed as follows:
- 33 queries for the 'simple' type
- 33 queries for the 'medium' type
- 34 queries for the 'complex' type

## Queries were classified based on weights defined for joins, filters, aggregations, nested queries, and expert interpretation.

- Weight for joins: 0.5
- Weight for filters: 1
- Weight for aggregations: 1
- Weight for nested queries: 2
- Weight for expert interpretations: 1.5