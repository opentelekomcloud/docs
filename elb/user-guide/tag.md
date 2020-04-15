# Tag<a name="EN-US_TOPIC_0113507949"></a>

## Scenarios<a name="section1143912015382"></a>

If you have a large number of cloud resources, you can assign different tags to these resources to quickly identify them. You can also query, modify, or delete the tags to help manage your resources.

For ELB, you can assign tags to enhanced load balancers and their listeners.

## Add a Tag to a Load Balancer<a name="section1163718452455"></a>

You can use either of the following methods to add a tag to a load balancer:

-   Add a tag when you create a load balancer.

    For detailed operations and parameters, see  [Create an Enhanced Load Balancer](creating-a-load-balancer.md#section19343262431).

-   Add a tag to an existing load balancer.
    1.  Log in to the management console.
    2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
    3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
    4.  Locate the target load balancer and click its name.
    5.  Under  **Tags**, click  **Add Tag**.
    6.  In the  **Add Tag**  dialog box, enter a tag key and value and click  **OK**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   A maximum of 10 tags can be added to a load balancer.  
        >-   Each tag is a key-value pair, and the tag key is unique.  



## Add a Tag to a Listener<a name="section175469211735"></a>

When adding a listener, you can find the tagging function in advanced settings.

To add a tag to an existing listener, perform the following steps:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target listener, and click its name.
6.  Under  **Tags**, click  **Add Tag**.
7.  In the  **Add Tag**  dialog box, enter a tag key and value and click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   A maximum of 10 tags can be added to a listener.  
    >-   Each tag is a key-value pair, and the tag key is unique.  


## Modify a Tag<a name="section1432939104616"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Tags**, select the tag to be edited, and click  **Edit**  in the  **Operation**  column. In the  **Edit Tag**  dialog box, change the tag value.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The tag key cannot be changed.  

6.  Click  **OK**.

The preceding steps describe how to modify a load balancer tag. The operations for modifying a listener tag are basically the same.

## Delete a Tag<a name="section1864818172465"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Tags**, select the tag to be deleted, and click  **Delete**  in the  **Operation**  column.
6.  In the  **Delete Tag**  dialog box, click  **Yes**.

The preceding steps describe how to delete a load balancer tag. The operations for deleting a listener tag are basically the same.

