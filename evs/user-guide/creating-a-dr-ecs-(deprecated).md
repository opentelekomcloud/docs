# Creating a DR ECS \(Deprecated\)<a name="evs_01_0024"></a>

## Scenarios<a name="section44945912112556"></a>

Before you create an EVS replication pair, create a DR ECS in the secondary AZ for the production ECS. The DR ECS parameters must be consistent with those of the production ECS. The parameters include the ECS specifications and the parameters of the production ECS's EVS disks, subnet, and security group.

If a large number of physical resources in the primary AZ are faulty due to force majeure, you can attach DR disks in the secondary AZ to DR ECSs and use DR disks to ensure the service availability and continuity.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Procedure<a name="section5471394711362"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  Click the name of the production ECS.

    The ECS details page is displayed.

5.  Take note of the production ECS information, including the ECS specifications, details of the EVS disks attached to the ECS, private IP address, and security group, as shown in  [Table 1](#table8510771171728).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The listed parameter values are for reference only.  

    **Table  1**  Information to be collected

    <a name="table8510771171728"></a>
    <table><thead align="left"><tr id="row63085598171728"><th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.1"><p id="p19829764171728"><a name="p19829764171728"></a><a name="p19829764171728"></a>Production Resource</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.449999999999996%" id="mcps1.2.4.1.2"><p id="p62707018171728"><a name="p62707018171728"></a><a name="p62707018171728"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.2.4.1.3"><p id="p46103697171728"><a name="p46103697171728"></a><a name="p46103697171728"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12280092171728"><td class="cellrowborder" rowspan="7" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="p55163399171728"><a name="p55163399171728"></a><a name="p55163399171728"></a>ECS</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.449999999999996%" headers="mcps1.2.4.1.2 "><p id="p39050310171728"><a name="p39050310171728"></a><a name="p39050310171728"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.3 "><p id="p8958530171728"><a name="p8958530171728"></a><a name="p8958530171728"></a>vpc-001</p>
    </td>
    </tr>
    <tr id="row43745607171756"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p57980369171855"><a name="p57980369171855"></a><a name="p57980369171855"></a>ECS type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p26696093171924"><a name="p26696093171924"></a><a name="p26696093171924"></a>General-purpose</p>
    </td>
    </tr>
    <tr id="row29405508171759"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p58665222171759"><a name="p58665222171759"></a><a name="p58665222171759"></a>Specification</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p54262556171759"><a name="p54262556171759"></a><a name="p54262556171759"></a>s2.xlarge.2</p>
    </td>
    </tr>
    <tr id="row133175017182"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1346087817182"><a name="p1346087817182"></a><a name="p1346087817182"></a>vCPU</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1658929617182"><a name="p1658929617182"></a><a name="p1658929617182"></a>4 cores</p>
    </td>
    </tr>
    <tr id="row17521825171836"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3210113171836"><a name="p3210113171836"></a><a name="p3210113171836"></a>Memory</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p58692590171836"><a name="p58692590171836"></a><a name="p58692590171836"></a>8 GB</p>
    </td>
    </tr>
    <tr id="row9698958171840"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15662736171840"><a name="p15662736171840"></a><a name="p15662736171840"></a>Image</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p60722118171840"><a name="p60722118171840"></a><a name="p60722118171840"></a>CentOS 7.2 64bit</p>
    </td>
    </tr>
    <tr id="row65993885171950"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p66602652171950"><a name="p66602652171950"></a><a name="p66602652171950"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p26105695171950"><a name="p26105695171950"></a><a name="p26105695171950"></a>AZ1</p>
    </td>
    </tr>
    <tr id="row19169185172116"><td class="cellrowborder" rowspan="5" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="p9200184172116"><a name="p9200184172116"></a><a name="p9200184172116"></a>EVS disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.449999999999996%" headers="mcps1.2.4.1.2 "><p id="p7017402172116"><a name="p7017402172116"></a><a name="p7017402172116"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.3 "><a name="ul45343600172232"></a><a name="ul45343600172232"></a><ul id="ul45343600172232"><li>System disk: 1</li><li>Data disk: 1</li></ul>
    </td>
    </tr>
    <tr id="row51002542172137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p22886168172137"><a name="p22886168172137"></a><a name="p22886168172137"></a>Capacity</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul65338516172237"></a><a name="ul65338516172237"></a><ul id="ul65338516172237"><li>System disk: 500 GB</li><li>Data disk: 2000 GB</li></ul>
    </td>
    </tr>
    <tr id="row42862631172144"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p41236582172144"><a name="p41236582172144"></a><a name="p41236582172144"></a>Disk type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul4761466817235"></a><a name="ul4761466817235"></a><ul id="ul4761466817235"><li>System disk: common I/O</li><li>Data disk: ultra-high I/O</li></ul>
    </td>
    </tr>
    <tr id="row62502604172144"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p64588969172144"><a name="p64588969172144"></a><a name="p64588969172144"></a>Disk sharing</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul29341473172329"></a><a name="ul29341473172329"></a><ul id="ul29341473172329"><li>System disk: non-shared disk</li><li>Data disk: non-shared disk</li></ul>
    </td>
    </tr>
    <tr id="row18536682172148"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p24360096172148"><a name="p24360096172148"></a><a name="p24360096172148"></a>Device type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul2336131517249"></a><a name="ul2336131517249"></a><ul id="ul2336131517249"><li>System disk: VBD</li><li>Data disk: SCSI</li></ul>
    </td>
    </tr>
    <tr id="row39298945172148"><td class="cellrowborder" rowspan="3" valign="top" width="28.07%" headers="mcps1.2.4.1.1 "><p id="p18146190172148"><a name="p18146190172148"></a><a name="p18146190172148"></a>Others</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.449999999999996%" headers="mcps1.2.4.1.2 "><p id="p60555252172148"><a name="p60555252172148"></a><a name="p60555252172148"></a>Private IP address</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.4.1.3 "><p id="p6028379172148"><a name="p6028379172148"></a><a name="p6028379172148"></a>192.168.12.2</p>
    </td>
    </tr>
    <tr id="row13247577172148"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p60916412172148"><a name="p60916412172148"></a><a name="p60916412172148"></a>Security group</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p35282360172148"><a name="p35282360172148"></a><a name="p35282360172148"></a>Sys-default</p>
    </td>
    </tr>
    <tr id="row12460051172148"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p23680882172148"><a name="p23680882172148"></a><a name="p23680882172148"></a>Virtual IP address</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p39103261172148"><a name="p39103261172148"></a><a name="p39103261172148"></a>192.168.12.23</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Create the DR ECS using the information of the production ECS.

    For details, see  **Creating an ECS**  in the  _Elastic Cloud Server User Guide_.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >Check the parameter values carefully and ensure that information of the DR ECS and production ECS is consistent.  

7.  After the DR ECS has been created, locate the DR ECS and stop it.

    Stopping the DR ECS prevents it from being incorrectly used.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When the DR ECS is not stopped and its system disk is used to create an EVS replication pair, the DR ECS status will change to  **REBUILDING**. In this state, you cannot stop the DR ECS, detach EVS disks from it, or expand its EVS disks.  


