======================
Operations on Objects
======================


The requests that are sent to OBS by users must comply with REST specifications and contain required header parameters. If a request is successfully processed, OBS returns a success response. If the request fails to be processed, OBS returns a message that contains the reason of the error. This chapter describes REST operations on objects using the common header authorization. You can also use temporarily authorized requests described in section  [V2 Temporarily Authorized Request](v2-temporarily-authorized-request.md).


.. toctree::
   :maxdepth: 1


   put-object.md
   post-object.md
   get-object.md
   put-object---copy.md
   delete-object.md
   delete-multiple-objects.md
   head-object.md
   put-object-acl.md
   get-object-acl.md
   initiate-multipart-upload.md
   upload-part.md
   upload-part---copy.md
   list-parts.md
   complete-multipart-upload.md
   abort-multipart-upload.md
   options-object.md
   post-object-restore.md
