# Slow Query Log<a name="en-us_topic_slow_query_log"></a>

Slow query logs record statements whose execution period exceeds the value of  **slowms**  \(100 ms by default\), allowing you identify and optimize slowly executed statements.

## Procedure<a name="section5651101513599"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Slow Query Logs**.
4.  On the displayed page, click  **Slow Query Logs**. Then, view the log details.
    -   Log records of all shards of a cluster instance
    -   Log records of all nodes of a replica set instance
    -   Log records of a node in different time periods
    -   Statements of the following level
        -   All statement type
        -   INSERT
        -   QUERY
        -   UPDATE
        -   REMOVE
        -   GETMORE
        -   COMMAND



