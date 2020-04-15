# Viewing Patch Information About an Active Cluster<a name="EN-US_TOPIC_0125375709"></a>

You can view patch information about cluster components. If a cluster component, such as Hadoop or Spark, is abnormal, download the patch. Then choose  **Clusters \> Active Clusters**. Select a cluster and click its name to switch the cluster details page to upgrade the component to resolve the problem.

The  **Patch Information**  is displayed on the basic information page only when patch information exists in the database.

If the cluster version is  **MRS 1.6.3**  or earlier, patch information contains the following parameters:

-   Patch Name: patch name
-   Patch Path: location where the patch is stored in OBS
-   Patch Description: patch description

If the cluster version is  **MRS 1.7.2**  or later, patch information contains the following parameters:

-   Patch Name: patch name
-   Status: patch status
-   Patch Description: patch description
-   Operation: install patch or uninstall patch

