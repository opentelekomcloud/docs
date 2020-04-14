# Deploying ECSs on DeHs<a name="EN-US_TOPIC_0046252763"></a>

## Scenarios<a name="section25191858103313"></a>

If you have a DeH, you can create ECSs of the supported flavors on the DeH.

## Prerequisites<a name="section68934418496"></a>

Before creating an ECS on a DeH, ensure that the following tasks have been completed:

-   A DeH has been allocated.
-   You have created a security group in the target region and added security group rules that meet your service requirements if you do not use the default security group that is automatically created by the system.
-   You have created a key pair in the target region if you select the key pair login mode when creating an ECS.

## Procedure<a name="section48682314158"></a>

1.  Log in to the management console.
2.  Click  ![](figures/9.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Dedicated Host**.

    The  **Dedicated Host**  page is displayed.

4.  In the list of DeHs, locate the DeH on which an ECS will be located and click  **Create ECS**  in the  **Operation**  column.

    The  **Create ECS**  page is displayed.

    For details, see "[Creating an ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0021831611.html)".

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   To create an ECS without specifying a DeH, click  **Create ECS**  in the upper right corner of the page. In this case, ensure that the auto placement function is enabled on at least one DeH.  
    >-   When selecting an ECS type, pay attention to mapping between the ECS type and the DeH type. If no matched DeH resources exist, ECSs cannot be created.  


## Results<a name="section1841119233819"></a>

Click  **Back to ECS List**  and wait until the ECS is created. You can view information about the newly created ECS, including the name/ID, specifications, and IP address.

## Related Operations<a name="section1011321010483"></a>

-   [Querying ECSs on DeHs](querying-ecss-on-dehs.md)
-   [Modifying Specifications of ECSs on DeHs](modifying-specifications-of-ecss-on-dehs.md)

