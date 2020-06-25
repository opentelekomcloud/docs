# Development Specifications<a name="dws_01_0106"></a>

If the connection pool mechanism is used during application development, the following specifications must be met. Otherwise, connections in the connection pool have statuses, which will affect the correctness of subsequent operations on the connection pool.

-   If the GUC parameter is set in a connection, you must execute  **SET SESSION AUTHORIZATION DEFAULT;RESET ALL;**  to clear the connection status before returning the connection to the connection pool.
-   If a temporary table is used, it must be deleted before the connection is returned to the connection pool.

