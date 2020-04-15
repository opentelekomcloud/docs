# Creating a Replication Pair<a name="sdrs_ug_pi_0003"></a>

## Scenarios<a name="section19872813193710"></a>

You can create replication pairs for desired disks and add the replication pairs to a specified protection group. When you create a replication pair:

-   If the protection group is in the  **Available**  state, protection is disabled. The production site disk and DR site disk have formed a replication pair, but data synchronization is not started. To start data synchronization, enable protection.
-   If the protection group is in the  **Protecting**  state, protection is enabled. After you create a replication pair, data synchronization is automatically started.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>After a replication pair is created, the default name of the DR site disk is the same as the name of the production site disk, but their IDs are different.  
>To modify a disk name, click the disk name on the replication pair details page to switch to the disk details page and modify it.  

## **Prerequisites**<a name="section1528842413918"></a>

-   The protection group is in the  **Available**  or  **Protecting**  state.
-   If  **Server Type**  of the protection group is  **ECS**, the disks used to create the replication pair are in the  **Available**  state.

## Procedure<a name="section1243511993716"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which replication pairs are to be added, click  **Replication Pairs**.

    The operation page for the protection group is displayed.

4.  On the  **Replication Pairs**  tab, click  **Create Replication Pair**.

    The  **Create Replication Pair**  page is displayed.

    **Figure  1**  Creating a replication pair<a name="fig259912464915"></a>  
    ![](figures/creating-a-replication-pair.png "creating-a-replication-pair")

5.  Configure the basic information about the replication pair listed in  [Table 1](#table14113172215131).

    **Table  1**  Parameter description

    <a name="table14113172215131"></a>
    <table><thead align="left"><tr id="row711682216134"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p111164221133"><a name="p111164221133"></a><a name="p111164221133"></a><strong id="b842352706211121"><a name="b842352706211121"></a><a name="b842352706211121"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5116172261316"><a name="p5116172261316"></a><a name="p5116172261316"></a><strong id="b84235270611218"><a name="b84235270611218"></a><a name="b84235270611218"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1211612224133"><a name="p1211612224133"></a><a name="p1211612224133"></a><strong>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16116152218134"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1111622216136"><a name="p1111622216136"></a><a name="p1111622216136"></a>Protection Group Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12116112241316"><a name="p12116112241316"></a><a name="p12116112241316"></a>Indicates the name of the protection group to which the replication pair to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11826105813010"><a name="p11826105813010"></a><a name="p11826105813010"></a>Protection-Group-test</p>
    </td>
    </tr>
    <tr id="row13973165510190"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29731755161918"><a name="p29731755161918"></a><a name="p29731755161918"></a>Protection Group ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9973155518194"><a name="p9973155518194"></a><a name="p9973155518194"></a>Specifies the ID of a protection group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1997315541911"><a name="p1997315541911"></a><a name="p1997315541911"></a>619c57e9-3927-48f8-ad14-3e293260b8a0</p>
    </td>
    </tr>
    <tr id="row2116722191312"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p121161122161311"><a name="p121161122161311"></a><a name="p121161122161311"></a>DR Direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p121169227135"><a name="p121169227135"></a><a name="p121169227135"></a>Indicates the replication direction of the protection group to which the replication pair to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11826358193017"><a name="p11826358193017"></a><a name="p11826358193017"></a>eu-de-01 -&gt; eu-de-02</p>
    </td>
    </tr>
    <tr id="row10720384287"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1673163813283"><a name="p1673163813283"></a><a name="p1673163813283"></a>Production Site</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1773113862815"><a name="p1773113862815"></a><a name="p1773113862815"></a>Specifies the AZ of the production site. </p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p101401053173316"><a name="p101401053173316"></a><a name="p101401053173316"></a>eu-de-01</p>
    </td>
    </tr>
    <tr id="row0405151012192"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7405810191910"><a name="p7405810191910"></a><a name="p7405810191910"></a>Production Site Disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p692281643110"><a name="p692281643110"></a><a name="p692281643110"></a>This parameter is mandatory.</p>
    <p id="p1292241693116"><a name="p1292241693116"></a><a name="p1292241693116"></a>Select a disk.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1928814226494"><a name="p1928814226494"></a><a name="p1928814226494"></a>volume-01</p>
    </td>
    </tr>
    <tr id="row1498954271619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p398964210165"><a name="p398964210165"></a><a name="p398964210165"></a>Replication Pair Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5904190816573"><a name="p5904190816573"></a><a name="p5904190816573"></a>Indicates the replication pair name. This parameter is mandatory.</p>
    <p id="p6161512716573"><a name="p6161512716573"></a><a name="p6161512716573"></a>Configure this parameter when you create a replication pair. Then, you can use this name to classify and search this replication pair.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19989164261619"><a name="p19989164261619"></a><a name="p19989164261619"></a>replication_001</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**.
7.  On the  **Confirm**  page, you can confirm the replication pair information.
    -   If you do not need to modify the information, click  **Submit**.
    -   If you need to modify the information, click  **Previous**.

8.  Click  **Back to Protection Group Details Page**  and query the replication pairs of the protection group.

    If the replication pair status changes to  **Available**  or  **Protecting**, the replication pair has been created successfully.


