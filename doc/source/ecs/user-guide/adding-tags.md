# Adding Tags<a name="EN-US_TOPIC_0183019669"></a>

Tags are used to identify cloud resources, such as ECSs, images, and disks. If you have multiple types of cloud resources which are associated with each other, you can add tags to the resources to classify and manage them easily. For more details, see  [Overview](tag-management-overview.md).

You can add tags to ECSs in any of the following ways:

-   [Adding Tags When Creating an ECS](#section619816351650)
-   [Adding Tags on the Page Providing Details About an ECS](#section15164103015253)
-   [Adding Tags on the TMS Console](#section115321623241)

For details about how to use predefined tags, see  [Using Predefined Tags](#section648015120456).

## Adding Tags When Creating an ECS<a name="section619816351650"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  Click  **Create ECS**.
5.  Configure ECS parameters.

    Select  **Configure now**  for  **Advanced Options**. Then, add a tag key and tag value. For the tag key and tag value requirements, see  [Table 1](tag-management-overview.md#table197401426182516).

    >![](/images/icon-note.gif) **NOTE:**   
    >-   For details about other parameters, see "Purchasing an ECS with Customized Configurations".  


## Adding Tags on the Page Providing Details About an ECS<a name="section15164103015253"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **Tags**  tab and then  **Add Tag**. In the displayed dialog box, enter the tag key and tag value. For the tag key and tag value requirements, see  [Table 1](tag-management-overview.md#table197401426182516).

    You can change the tag value after the tag is added.


## Adding Tags on the TMS Console<a name="section115321623241"></a>

>![](/images/icon-note.gif) **NOTE:**   
>This method is suitable for adding tags with the same tag key to multiple resources.  

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Tag Management Service**.
3.  On the displayed  **Resource Tags**  page, select the region where the resource is located, select  **ECS**  for  **Resource Type**, and click  **Search**.

    All ECSs matching the search criteria are displayed.

4.  In the  **Search Result**  area, click  **Create Key**. In the displayed dialog box, enter a key \(for example  **project**\) and click  **OK**.

    After the tag is created, the tag key is added to the resource list. If the key is not displayed in the resource list, click  ![](figures/icon-set-2.png)  and select the created key from the drop-down list.

    By default, the value of the tag key is  **Not tagged**. You need to set a value for the tag of each resource to associate the tag with the resource.

5.  Click  **Edit**  to make the resource list editable.
6.  Locate the row containing the target ECS, click  ![](figures/icon-plus.png), and enter a value \(for example  **A**\).

    After a value is set for a tag key, the number of tags is incremented by 1. Repeat the preceding steps to add tag values for other ECSs.


## Using Predefined Tags<a name="section648015120456"></a>

If you want to add the same tag to multiple ECSs or other resources, you can create a predefined tag on the TMS console and then select the tag for the ECSs or resources. This frees you from having to repeatedly enter tag keys and values. To do so, perform the following operations:

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Tag Management Service**.
3.  In the navigation pane on the left, choose  **Predefined Tags**. In the right pane, click  **Create Tag**  enter a key \(for example  **project**\) and a value \(for example  **A**\) in the displayed dialog box.
4.  Choose  **Service List**  \>  **Computing**  \>  **Elastic Cloud Server**, and select the predefined tag by following the procedure for adding a tag.

