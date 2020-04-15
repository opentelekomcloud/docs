# Step 1: Create a Protection Group<a name="EN-US_TOPIC_0108180805"></a>

## Scenarios<a name="section1266142102019"></a>

You can specify two AZs as the source and target AZs, and create a protection group. Then, you can create protected instances and replication pairs in this protection group.

Verify the servers at the production and DR sites before you create a protection group. In this version, only the VPC migration deployment model is supported. Specifically, the servers at the production and DR sites must be in different AZs but in the same VPC. 

**Figure  1**  Creating a protection group<a name="fig9364464217"></a>  
![](figures/creating-a-protection-group.png "creating-a-protection-group")

## Procedure<a name="section684619122203"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  Click  **Create Protection Group**.

    The  **Create Protection Group**  page is displayed.

    **Figure  2**  Creating a protection group<a name="fig1677474514378"></a>  
    ![](figures/creating-a-protection-group-0.png "creating-a-protection-group-0")

4.  Configure the basic information about the protection group listed in  [Table 1](#table0120161710336). 

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >All the parameters in the following table are mandatory.  

    **Table  1**  Parameter description

    <a name="table0120161710336"></a>
    <table><thead align="left"><tr id="row10120117163319"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1012041715334"><a name="p1012041715334"></a><a name="p1012041715334"></a><strong id="b842352706211121"><a name="b842352706211121"></a><a name="b842352706211121"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1312018173335"><a name="p1312018173335"></a><a name="p1312018173335"></a><strong id="b842352706211125"><a name="b842352706211125"></a><a name="b842352706211125"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p312061716330"><a name="p312061716330"></a><a name="p312061716330"></a><strong>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4120201713314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p112031713310"><a name="p112031713310"></a><a name="p112031713310"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1041215984713"><a name="p1041215984713"></a><a name="p1041215984713"></a>A region is a geographic area where resources used by servers are located.</p>
    <p id="p34476578162953"><a name="p34476578162953"></a><a name="p34476578162953"></a>If the region is incorrect, click the drop-down list for correction.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p129831635135611"><a name="p129831635135611"></a><a name="p129831635135611"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row101221617153317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p99001313420"><a name="p99001313420"></a><a name="p99001313420"></a>DR Direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><a name="ul13691336183613"></a><a name="ul13691336183613"></a><ul id="ul13691336183613"><li>Production site: Select the AZ of the production site server.</li><li>DR site: Select the AZ of the DR site server.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p0229123912587"><a name="p0229123912587"></a><a name="p0229123912587"></a>Production site: az-01</p>
    <p id="p11988134874711"><a name="p11988134874711"></a><a name="p11988134874711"></a>DR site: az-02</p>
    </td>
    </tr>
    <tr id="row14577105111253"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1057819516252"><a name="p1057819516252"></a><a name="p1057819516252"></a>Deployment Model</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p147501443112510"><a name="p147501443112510"></a><a name="p147501443112510"></a>Currently, only the VPC migration model is supported. All resources at the production and DR sites belong to the same VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25789514251"><a name="p25789514251"></a><a name="p25789514251"></a>VPC migration</p>
    </td>
    </tr>
    <tr id="row41343352614"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15134631261"><a name="p15134631261"></a><a name="p15134631261"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1213413152610"><a name="p1213413152610"></a><a name="p1213413152610"></a>Specifies the VPC where the protection group is located.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61341316261"><a name="p61341316261"></a><a name="p61341316261"></a>vpc-test</p>
    </td>
    </tr>
    <tr id="row7122131763316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p69405172348"><a name="p69405172348"></a><a name="p69405172348"></a>Protection Group Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6161512716573"><a name="p6161512716573"></a><a name="p6161512716573"></a>Enter the protection group name. It is used for group classification and search.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2122161717335"><a name="p2122161717335"></a><a name="p2122161717335"></a>protection_group_001</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Create Now**.
6.  Click  **Back to Protection Group List**  to return to the SDRS homepage and query the protection group status.

    If the protection group is displayed in the  **Storage Disaster Recovery Service**  page and its status is  **Available**  \(![](figures/23.png)\), the protection group has been created successfully.


