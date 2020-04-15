# Deleting a Tag<a name="EN-US_TOPIC_0183019671"></a>

If you no longer need a tag, delete it in any of the following ways:

-   [Deleting a Tag on the Page Providing Details About an ECS](#section8763326153815)
-   [Deleting a Tag on the TMS Console](#section167319315388)
-   [Batch Deleting Tags on the TMS Console](#section13142241209)

## Deleting a Tag on the Page Providing Details About an ECS<a name="section8763326153815"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **Tags**  tab. Locate the row containing the tag to be deleted and click  **Delete**  in the  **Operation**  column. In the  **Delete Tag**  dialog box, click  **Yes**.

## Deleting a Tag on the TMS Console<a name="section167319315388"></a>

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Tag Management Service**.
3.  In the upper right corner of the page, click the username and select  **Tag Management**  from the drop-down list.
4.  On the  **Resource Tags**  page, set the search criteria for ECSs and click  **Search**.
5.  In the  **Search Result**  area, click  **Edit**  to make the resource tag list editable.

    If the key of a tag you want to delete is not contained in the list, click  ![](figures/icon-set-2.png)  and select the tag key from the drop-down list. You are advised to select at most 10 keys to display.

6.  Locate the row containing the target ECS and click  ![](figures/icon-delete.png).
7.  \(Optional\) Click  ![](figures/icon-refresh.png)  in the upper right of the  **Search Result**  area.

    The resource list is refreshed and the refresh time is updated.


## Batch Deleting Tags on the TMS Console<a name="section13142241209"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Exercise caution when deleting tags in a batch. After you delete the tags, they will be removed from all the associated ECSs and cannot be recovered.  

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Tag Management Service**.
3.  On the  **Resource Tags**  page, set the search criteria for ECSs and click  **Search**.
4.  Select the target ECSs.
5.  Click  **Manage Tag**  in the upper left corner of the list.
6.  In the displayed  **Manage Tag**  dialog box, click  **Delete**  in the  **Operation**  column. Click  **OK**.
7.  \(Optional\) Click  ![](figures/icon-refresh.png)  in the upper right of the  **Search Result**  area.

    The resource list is refreshed and the refresh time is updated.


