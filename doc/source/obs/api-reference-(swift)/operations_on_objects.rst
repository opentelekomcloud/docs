======================
Operations on Objects
======================


The requests that are sent by users to OBS \(compatible with OpenStack Swift\) must comply with REST specifications and contain required header parameters. If a request is successfully processed, OBS \(compatible with OpenStack Swift\) returns a success response. If the request fails to be processed, OBS \(compatible with OpenStack Swift\) returns a message that contains the cause of the error. This chapter describes REST operations on objects. Authentication is implemented based on IAM.

.. image:: /images/icon-note.gif

**NOTE:**
In the event of invoking OBS APIs, if the value of  **Content-Length**  in a request is not a correct digital text, OBS \(compatible with OpenStack Swift\) will attempt to parse the content text and use it as the value of  **Content-Length**. For example,  **-H"Content-Length:26abc"**  is equivalent to  **-H"Content-Length:26"**. OpenStack Swift, however, returns the error code 400 \(Bad Request\).

.. toctree::
   :maxdepth: 1

   get-object-content-and-metadata.md
   create-or-replace-object.md
   copy-object.md
   delete-object.md
   show-object-metadata.md
   create-update-delete-object-metadata.md
