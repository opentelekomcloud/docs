# Why Do Some Operation Records Occur Twice in the Trace List?<a name="cts_faq_012"></a>

For an asynchronously invoked trace, two records with the same trace name, resource type, and resource name will be generated. In the trace list, two records are displayed for the same trace, for example, the  **deleteDesktop**  trace of Workspace. The two records are associated, but have different content because they are not invoked at the same time. Details are as follows:

-   The first record contains the request of a user to perform an operation.
-   The second record contains the response to the user request and operation result, and is usually several minutes later than the first record.

The two records together indicate the operation result.

