=========================
Operations on Containers
=========================

The requests that are sent by users to OBS must comply with REST specifications and contain required header parameters. If a request is successfully processed, OBS \(compatible with OpenStack Swift\) returns a success response. If the request fails to be processed, OBS \(compatible with OpenStack Swift\) returns a message that contains the cause of the error. This chapter describes REST operations on containers. Authentication is implemented based on IAM.

.. toctree::
   :maxdepth: 1


   show-container-details-and-list-objects.md
   create-container.md
   delete-container.md
   create-update-delete-container-metadata.md
   show-container-metadata.md
   batch-delete-containers.md
