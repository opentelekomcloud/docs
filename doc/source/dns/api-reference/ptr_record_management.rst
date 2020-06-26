=====================
PTR Record Management
=====================

PTR records are region-level tenant resources. The system will isolate and manage them based on projects.

Before creating, querying, or unsetting PTR records, specify a project in  **X-Project-Id**  in the request header to perform the operations. If you do not specify one, the default project of the token will be used.

.. image:: /images/icon-note.gif

**NOTE:**
 For details about  **X-Project-Id**, see  `Constructing a Request`_.

The ap-sg region does not support PTR records, and therefore APIs in this section are not applicable.

.. _Constructing a Request: https://docs.otctest.t-systems.com/en-us/api/apiug/apig-en-api-180328010.html?tag=API%20Documents

.. toctree::
   :maxdepth: 1


   description-on-ptr-record-apis.md
   creating-ptr-record.md
   configuring-a-ptr-record.md
   querying-a-ptr-record.md
   querying-all-ptr-records.md
   unsetting-a-ptr-record.md
   modifying-a-ptr-record.md




