# Tagging Overview<a name="dws_01_0104"></a>

A tag is a key-value pair customized by users and used to identify cloud resources. It helps users to classify and search for cloud resources.

Tags are composed of key-value pairs.

-   A key in a tag can have multiple values.
-   A cloud resource must have a unique key.

On DWS, after creating a cluster, you can add identifiers to items such as the project name, service type, and background information using tags. If you use tags in other cloud services, you are advised to create the same tag key-value pairs for cloud resources used by the same business to keep consistency.

DWS supports the following two types of tags:

-   Resource tags

    Non-global tags created on DWS


-   Predefined tags

    Predefined tags created on Tag Management Service \(TMS\). Predefined tags are global tags.

    For details about predefined tags, see the  _Tag Management Service User Guide_.


On DWS, tags can be added to the following resources:

-   Cluster

    Tags can be added to a cluster when the cluster is being created or after it is successfully created. You can search for the cluster in the cluster list using tags.

    Each cluster can have a maximum of 10 tags added to it.

    After you add tags to a cluster and then create a snapshot for the cluster, the tags cannot be restored if you use the snapshot to restore the cluster. Instead, you need to add tags again.

    When a cluster is deleted, non-predefined tags associated with the cluster are also deleted. Predefined tags need to be deleted on TMS.


