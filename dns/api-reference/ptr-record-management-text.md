

PTR records are region-level tenant resources. The system will isolate and manage them based on projects.

Before creating, querying, or unsetting PTR records, specify a project in  **X-Project-Id**  in the request header to perform the operations. If you do not specify one, the default project of the token will be used.

> ![](/images/icon-note.gif) **NOTE:** 

> For details about  **X-Project-Id**, see  [Constructing a Request](https://docs.otctest.t-systems.com/en-us/api/apiug/apig-en-api-180328010.html?tag=API%20Documents).

> The ap-sg region does not support PTR records, and therefore APIs in this section are not applicable.