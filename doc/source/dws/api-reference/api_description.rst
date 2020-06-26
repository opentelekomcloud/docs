================
API Description
================


Cluster Management APIs
=========================


A data warehouse cluster is the smallest management unit in DWS. A cluster is a data warehouse that runs independently. You can manage the cluster life cycle in DWS.


.. toctree::
   :maxdepth: 1

   creating-a-cluster.md
   querying-the-cluster-list.md
   querying-cluster-details.md
   querying-the-supported-node-types.md
   deleting-a-cluster.md


Snapshot Management APIs
=========================


A DWS snapshot is a complete backup of a cluster. Snapshots are stored in the storage space of Object Storage Service \(OBS\). A snapshot can be used to restore a cluster to a newly created one that has the same flavor. Currently, you can only restore a cluster to a new one.


.. toctree::
   :maxdepth: 1

   creating-a-snapshot.md
   querying-the-snapshot-list.md
   querying-snapshot-details.md
   deleting-a-snapshot.md
   restoring-a-cluster.md


Tag Management APIs
====================


.. toctree::
   :maxdepth: 1


   tagging.md
   adding-a-resource-tag.md
   adding-or-deleting-resource-tags-in-batches.md
   querying-resources-by-tag.md
   querying-resource-tags.md
   querying-tags-in-a-specified-project.md
   deleting-a-resource-tag.md

