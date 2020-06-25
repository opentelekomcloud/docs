# Creating an ECS<a name="EN-US_TOPIC_0068473331"></a>

## Function<a name="en-us_topic_0057972661_section31291646"></a>

This API is used to create an ECS.

This API does not support automatic rollback after creating an ECS failed. If automatic rollback is required, call the API POST /v1/\{project\_id\}/cloudservers. For details, see  [Creating an ECS](creating-an-ecs.md).

## URI<a name="en-us_topic_0057972661_section13189358"></a>

POST /v2/\{project\_id\}/servers

POST /v2.1/\{project\_id\}/servers

[Table 1](#en-us_topic_0057972661_table47145209)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972661_table47145209"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row4152081"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row11861416151631"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972661_p50425983151639"><a name="en-us_topic_0057972661_p50425983151639"></a><a name="en-us_topic_0057972661_p50425983151639"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p57972822151639"><a name="en-us_topic_0057972661_p57972822151639"></a><a name="en-us_topic_0057972661_p57972822151639"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Alias of the API for creating ECSs: /v2/\{project\_id\}/os-volumes\_boot  
>This calling mode can only be used in OpenStack Client.  

## Constraints<a name="en-us_topic_0057972661_section51595365"></a>

1.  Parameter  **port**  in the three network parameters \(**port**,  **uuid**, and  **fixed\_ip**\) has the highest priority. If parameter  **fixed\_ip**  is set, you must specify the UUID.
2.  A file injection failure will result in the ECS creation failure.
3.  The following restrictions apply when you create ECSs using an image:
    1.  You cannot create an ECS on a specified host.
    2.  If a tenant backs up a disk in an ECS, the disk can only be deleted after the tenant deletes all the snapshots of the disk.
    3.  The flavors with different resource types cannot be adjusted if you adjust the specifications of an ECS created using an image.

4.  Native APIs /v2/\{project\_id\}/servers and /v2.1/\{project\_id\}/servers provided by the public cloud platform is developed based on and compatible with the community-version native OpenStack API.

    Compared with the community-version native API, this API has the following restrictions when you create an ECS using a specified image:

    -   Community-version native OpenStack API: creates an ECS using the local disk by default.
    -   Native API provided by the public cloud platform: creates an ECS using the shared storage as the system disk.

    Specifically, when you use the native API to create an ECS:

    1.  You can query information about the disks attached to the ECS.
    2.  The ECS system disk uses the EVS disk quota.
    3.  You cannot query ECSs created based on a specified image using the image filtering function.

5.  When you create an ECS with a specified disk, ensure that the disk and the ECS are in the same AZ.
6.  The  **device\_name**  field configured in  **block\_device\_mapping\_v2**  during the ECS creation does not take effect. The system generates a device name by default.
7.  ECSs cannot be created in networks with  **provider:network\_type**  set to  **geneve**.

    >![](/images/icon-note.gif) **NOTE:**   
    >If  **provider:network\_type**  is set to  **geneve**, the internal high-speed network is used for BMSs.  

8.  During the ECS creation, multiple ports can belong to the same network only when the global configuration item  **allow\_duplicate\_networks**  is enabled.
9.  If your ECS is remotely logged in using a key, use the  **key\_name**  parameter. If your ECS is remotely logged in using a password, use the  **adminPass**  parameter. Linux ECSs support  **user\_data**  for injection. Windows ECSs support  **admin\_pass**  for injection.
10. If the image based on which the ECS is created uses the native OpenStack API, ensure that the specified AZ and system disk capacity and type used when the ECS is created are the same as those used when the image is created. Otherwise, the ECS creation will fail.

## Request<a name="en-us_topic_0057972661_section18475057"></a>

[Table 2](#en-us_topic_0057972661_table40519951)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972661_table40519951"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row35619075"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972661_p66572856"><a name="en-us_topic_0057972661_p66572856"></a><a name="en-us_topic_0057972661_p66572856"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p1467903512918"><a name="p1467903512918"></a><a name="p1467903512918"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972661_p23692278"><a name="en-us_topic_0057972661_p23692278"></a><a name="en-us_topic_0057972661_p23692278"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972661_p20908074"><a name="en-us_topic_0057972661_p20908074"></a><a name="en-us_topic_0057972661_p20908074"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row15832433"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p7358688"><a name="en-us_topic_0057972661_p7358688"></a><a name="en-us_topic_0057972661_p7358688"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p467915358917"><a name="p467915358917"></a><a name="p467915358917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p59182880"><a name="en-us_topic_0057972661_p59182880"></a><a name="en-us_topic_0057972661_p59182880"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p6993202"><a name="en-us_topic_0057972661_p6993202"></a><a name="en-us_topic_0057972661_p6993202"></a>Specifies the ECS information. See <a href="#en-us_topic_0057972661_table64008488102639">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row29578451"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p47044325"><a name="en-us_topic_0057972661_p47044325"></a><a name="en-us_topic_0057972661_p47044325"></a>os:scheduler_hints</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p4679135396"><a name="p4679135396"></a><a name="p4679135396"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p52493967"><a name="en-us_topic_0057972661_p52493967"></a><a name="en-us_topic_0057972661_p52493967"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p10232270"><a name="en-us_topic_0057972661_p10232270"></a><a name="en-us_topic_0057972661_p10232270"></a>Specifies the ECS scheduling information. See <a href="#en-us_topic_0057972661_table12534817105641">Table 8</a>. This parameter is not available in BMS scenarios.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **server**  parameters

<a name="en-us_topic_0057972661_table64008488102639"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row56993194102639"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p15357151212247"><a name="p15357151212247"></a><a name="p15357151212247"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p67554367107"><a name="p67554367107"></a><a name="p67554367107"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p19357112132415"><a name="p19357112132415"></a><a name="p19357112132415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.2.5.1.4"><p id="p3372912142414"><a name="p3372912142414"></a><a name="p3372912142414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row64892893102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p53667478102658"><a name="en-us_topic_0057972661_p53667478102658"></a><a name="en-us_topic_0057972661_p53667478102658"></a>imageRef</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p2075533681020"><a name="p2075533681020"></a><a name="p2075533681020"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p52098484102658"><a name="en-us_topic_0057972661_p52098484102658"></a><a name="en-us_topic_0057972661_p52098484102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p32710312102658"><a name="en-us_topic_0057972661_p32710312102658"></a><a name="en-us_topic_0057972661_p32710312102658"></a>Specifies the ECS image ID or URL.</p>
<a name="en-us_topic_0057972661_ul25957356102658"></a><a name="en-us_topic_0057972661_ul25957356102658"></a><ul id="en-us_topic_0057972661_ul25957356102658"><li>Example image ID: 3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2</li><li>Example image URL: http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2</li><li>If you use a specified disk as the system disk to create an ECS, this parameter is not required. If you do not use a disk to create an ECS, you must set a valid UUID. Otherwise, the API will return error code <strong id="en-us_topic_0057972661_b842352706102125"><a name="en-us_topic_0057972661_b842352706102125"></a><a name="en-us_topic_0057972661_b842352706102125"></a>400</strong>.</li></ul>
<div class="note" id="note12001550131917"><a name="note12001550131917"></a><a name="note12001550131917"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul185629592115"></a><a name="ul185629592115"></a><ul id="ul185629592115"><li>The ECSs of certain flavors do not support all public images provided on the public cloud platform. To obtain the images supported by an ECS flavor, log in to the management console, view the images displayed on the <strong id="b842352706185454"><a name="b842352706185454"></a><a name="b842352706185454"></a>Create ECS</strong> page, and obtain the image IDs on the <strong id="b842352706185522"><a name="b842352706185522"></a><a name="b842352706185522"></a>Image Management Service</strong> page.</li><li>If the creation fails, modify the parameter settings.</li></ul>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row993360102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p20533591102658"><a name="en-us_topic_0057972661_p20533591102658"></a><a name="en-us_topic_0057972661_p20533591102658"></a>flavorRef</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p2756536151015"><a name="p2756536151015"></a><a name="p2756536151015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p52608144102658"><a name="en-us_topic_0057972661_p52608144102658"></a><a name="en-us_topic_0057972661_p52608144102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p21145347102658"><a name="en-us_topic_0057972661_p21145347102658"></a><a name="en-us_topic_0057972661_p21145347102658"></a>Specifies the flavor ID or URL.</p>
<p id="p27315444412"><a name="p27315444412"></a><a name="p27315444412"></a>For example: c1.2xlarge</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row3565234102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p47028347102658"><a name="en-us_topic_0057972661_p47028347102658"></a><a name="en-us_topic_0057972661_p47028347102658"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p9756133613109"><a name="p9756133613109"></a><a name="p9756133613109"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p51199773102658"><a name="en-us_topic_0057972661_p51199773102658"></a><a name="en-us_topic_0057972661_p51199773102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p41851471102658"><a name="en-us_topic_0057972661_p41851471102658"></a><a name="en-us_topic_0057972661_p41851471102658"></a>Specifies the ECS name. The value contains 1 to 255 characters.</p>
<div class="note" id="note1631304619446"><a name="note1631304619446"></a><a name="note1631304619446"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1313546134412"><a name="p1313546134412"></a><a name="p1313546134412"></a>ECS hostnames comply with <a href="https://tools.ietf.org/html/rfc952" target="_blank" rel="noopener noreferrer">RFC952</a> and <a href="https://tools.ietf.org/html/rfc1123" target="_blank" rel="noopener noreferrer">RFC1123</a> naming rules. It is recommended that you configure hostnames using digits, letters (case sensitive), and hyphens (-). Underscores (_) are converted into hyphens (-) by default.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row59762533102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p42298537102658"><a name="en-us_topic_0057972661_p42298537102658"></a><a name="en-us_topic_0057972661_p42298537102658"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p375616363108"><a name="p375616363108"></a><a name="p375616363108"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p3629454102658"><a name="en-us_topic_0057972661_p3629454102658"></a><a name="en-us_topic_0057972661_p3629454102658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p14501627151547"><a name="en-us_topic_0057972661_p14501627151547"></a><a name="en-us_topic_0057972661_p14501627151547"></a>Specifies the ECS metadata. For details, see <a href="#en-us_topic_0057972661_table2373623012315">Table 4</a>.</p>
<a name="en-us_topic_0057972661_ul18338492151614"></a><a name="en-us_topic_0057972661_ul18338492151614"></a><ul id="en-us_topic_0057972661_ul18338492151614"><li>The key contains 1 to 255 characters.</li><li>The value contains 0 to 255 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057972661_row4553446102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p5856011102658"><a name="en-us_topic_0057972661_p5856011102658"></a><a name="en-us_topic_0057972661_p5856011102658"></a>adminPass</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p4756133619102"><a name="p4756133619102"></a><a name="p4756133619102"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p4574868102658"><a name="en-us_topic_0057972661_p4574868102658"></a><a name="en-us_topic_0057972661_p4574868102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p59981754144012"><a name="p59981754144012"></a><a name="p59981754144012"></a>Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is <strong id="b1433882092316"><a name="b1433882092316"></a><a name="b1433882092316"></a>root</strong>, and the Windows administrator is <strong id="b3338720132311"><a name="b3338720132311"></a><a name="b3338720132311"></a>Administrator</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row19678943102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p44887270102658"><a name="en-us_topic_0057972661_p44887270102658"></a><a name="en-us_topic_0057972661_p44887270102658"></a>block_device_mapping_v2</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p17569367102"><a name="p17569367102"></a><a name="p17569367102"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p11990221102658"><a name="en-us_topic_0057972661_p11990221102658"></a><a name="en-us_topic_0057972661_p11990221102658"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p16256306102658"><a name="en-us_topic_0057972661_p16256306102658"></a><a name="en-us_topic_0057972661_p16256306102658"></a>Indicates the V2 API for specifying the ECS storage device. This is an extended attribute. This is the storage resource API of the new version. You are not allowed to create ECSs in batches when the volume is specified. For details, see <a href="#en-us_topic_0057972661_table15044407105358">Table 5</a>. This parameter is not available in BMS scenarios.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row6088188102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p21642473102658"><a name="en-us_topic_0057972661_p21642473102658"></a><a name="en-us_topic_0057972661_p21642473102658"></a>config_drive</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p07561536191013"><a name="p07561536191013"></a><a name="p07561536191013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p8209879102658"><a name="en-us_topic_0057972661_p8209879102658"></a><a name="en-us_topic_0057972661_p8209879102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p43710689102658"><a name="en-us_topic_0057972661_p43710689102658"></a><a name="en-us_topic_0057972661_p43710689102658"></a>Specifies the config_drive disk to be attached to the ECS during the ECS creation for transferring information to the ECS. This is an extended attribute.</p>
<p id="en-us_topic_0057972661_p57851884102658"><a name="en-us_topic_0057972661_p57851884102658"></a><a name="en-us_topic_0057972661_p57851884102658"></a>This function is not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row38867078102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p29656925102658"><a name="en-us_topic_0057972661_p29656925102658"></a><a name="en-us_topic_0057972661_p29656925102658"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p1675653621016"><a name="p1675653621016"></a><a name="p1675653621016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p53400697102658"><a name="en-us_topic_0057972661_p53400697102658"></a><a name="en-us_topic_0057972661_p53400697102658"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p45349775152941"><a name="en-us_topic_0057972661_p45349775152941"></a><a name="en-us_topic_0057972661_p45349775152941"></a>Specifies the security group that the ECS belongs to. This parameter is an extended attribute. The default parameter value is <strong id="en-us_topic_0057972661_b543622423112926"><a name="en-us_topic_0057972661_b543622423112926"></a><a name="en-us_topic_0057972661_b543622423112926"></a>default</strong>.</p>
<p id="en-us_topic_0057972661_p53708280102658"><a name="en-us_topic_0057972661_p53708280102658"></a><a name="en-us_topic_0057972661_p53708280102658"></a>This parameter is valid when you create an ECS on a specified network. For an existing port, the requested security groups are invalid. For details, see <a href="#en-us_topic_0057972661_table16920677105453">Table 6</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row11447375102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p58493193102658"><a name="en-us_topic_0057972661_p58493193102658"></a><a name="en-us_topic_0057972661_p58493193102658"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p14756143616107"><a name="p14756143616107"></a><a name="p14756143616107"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p40328188102658"><a name="en-us_topic_0057972661_p40328188102658"></a><a name="en-us_topic_0057972661_p40328188102658"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p50103488102658"><a name="en-us_topic_0057972661_p50103488102658"></a><a name="en-us_topic_0057972661_p50103488102658"></a>Specifies information about the ECS NIC. This parameter is an extended attribute. This parameter must be specified if multiple tenant networks are used. For details, see <a href="#en-us_topic_0057972661_table9995892105551">Table 7</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row62300910102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p62687271102658"><a name="en-us_topic_0057972661_p62687271102658"></a><a name="en-us_topic_0057972661_p62687271102658"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p3756236101010"><a name="p3756236101010"></a><a name="p3756236101010"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p44504222102658"><a name="en-us_topic_0057972661_p44504222102658"></a><a name="en-us_topic_0057972661_p44504222102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p1533495102658"><a name="en-us_topic_0057972661_p1533495102658"></a><a name="en-us_topic_0057972661_p1533495102658"></a>Specifies the name of a key pair. This parameter is an extended attribute. </p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row33176070102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p44176647102658"><a name="en-us_topic_0057972661_p44176647102658"></a><a name="en-us_topic_0057972661_p44176647102658"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p16756163619108"><a name="p16756163619108"></a><a name="p16756163619108"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p21538656102658"><a name="en-us_topic_0057972661_p21538656102658"></a><a name="en-us_topic_0057972661_p21538656102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p50969357102658"><a name="en-us_topic_0057972661_p50969357102658"></a><a name="en-us_topic_0057972661_p50969357102658"></a>Specifies the user data. This parameter is an extended attribute. The character string contains 1 to 65,534 characters and must be encrypted using Base64.</p>
<p id="p151383081516"><a name="p151383081516"></a><a name="p151383081516"></a>For more information about the user data to be injected, see "Injecting User Data into ECSs" in <em>Elastic Cloud Server User Guide</em>.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row63798654102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p45459633102658"><a name="en-us_topic_0057972661_p45459633102658"></a><a name="en-us_topic_0057972661_p45459633102658"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p16756203661019"><a name="p16756203661019"></a><a name="p16756203661019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p58351639102658"><a name="en-us_topic_0057972661_p58351639102658"></a><a name="en-us_topic_0057972661_p58351639102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p9041942195215"><a name="en-us_topic_0057972661_p9041942195215"></a><a name="en-us_topic_0057972661_p9041942195215"></a>Specifies the AZ of a specified ECS. This is an extended attribute.</p>
<p id="en-us_topic_0057972661_p56149386102658"><a name="en-us_topic_0057972661_p56149386102658"></a><a name="en-us_topic_0057972661_p56149386102658"></a>This parameter is mandatory when you create an ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row14011337102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p63604766102658"><a name="en-us_topic_0057972661_p63604766102658"></a><a name="en-us_topic_0057972661_p63604766102658"></a>return_reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p13756173611019"><a name="p13756173611019"></a><a name="p13756173611019"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p51712396102658"><a name="en-us_topic_0057972661_p51712396102658"></a><a name="en-us_topic_0057972661_p51712396102658"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p49723161102658"><a name="en-us_topic_0057972661_p49723161102658"></a><a name="en-us_topic_0057972661_p49723161102658"></a>Specifies whether the reservation IDs of the ECSs created in a batch are returned. This is an extended attribute. You can query the ECSs created this time based on the returned reservation IDs.</p>
<a name="en-us_topic_0057972661_ul1627916843419"></a><a name="en-us_topic_0057972661_ul1627916843419"></a><ul id="en-us_topic_0057972661_ul1627916843419"><li><strong id="en-us_topic_0057972661_b84235270611354"><a name="en-us_topic_0057972661_b84235270611354"></a><a name="en-us_topic_0057972661_b84235270611354"></a>true</strong>: The reservation IDs are returned.</li><li><strong id="en-us_topic_0057972661_b84235270611632"><a name="en-us_topic_0057972661_b84235270611632"></a><a name="en-us_topic_0057972661_b84235270611632"></a>false</strong>: The ECS information is returned.<div class="note" id="en-us_topic_0057972661_note1151212192215"><a name="en-us_topic_0057972661_note1151212192215"></a><a name="en-us_topic_0057972661_note1151212192215"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p17513619142119"><a name="en-us_topic_0057972661_p17513619142119"></a><a name="en-us_topic_0057972661_p17513619142119"></a>When you create ECSs in a batch, this parameter is available.</p>
</div></div>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057972661_row14685215102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p17473992102658"><a name="en-us_topic_0057972661_p17473992102658"></a><a name="en-us_topic_0057972661_p17473992102658"></a>min_count</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p47571336141013"><a name="p47571336141013"></a><a name="p47571336141013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p6107265102658"><a name="en-us_topic_0057972661_p6107265102658"></a><a name="en-us_topic_0057972661_p6107265102658"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p39383468153028"><a name="en-us_topic_0057972661_p39383468153028"></a><a name="en-us_topic_0057972661_p39383468153028"></a>Specifies the minimum number of ECSs that can be created. This is an extended attribute.</p>
<p id="en-us_topic_0057972661_p1358388153054"><a name="en-us_topic_0057972661_p1358388153054"></a><a name="en-us_topic_0057972661_p1358388153054"></a>The default value is <strong id="en-us_topic_0057972661_b84235270615612"><a name="en-us_topic_0057972661_b84235270615612"></a><a name="en-us_topic_0057972661_b84235270615612"></a>1</strong>.</p>
<div class="note" id="en-us_topic_0057972661_note5101551193636"><a name="en-us_topic_0057972661_note5101551193636"></a><a name="en-us_topic_0057972661_note5101551193636"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p45913965193636"><a name="en-us_topic_0057972661_p45913965193636"></a><a name="en-us_topic_0057972661_p45913965193636"></a>When you use a specified image to create ECSs, this parameter is supported.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row33216193102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p48294822102658"><a name="en-us_topic_0057972661_p48294822102658"></a><a name="en-us_topic_0057972661_p48294822102658"></a>max_count</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p575716366106"><a name="p575716366106"></a><a name="p575716366106"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p19566505102658"><a name="en-us_topic_0057972661_p19566505102658"></a><a name="en-us_topic_0057972661_p19566505102658"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p4122565110275"><a name="en-us_topic_0057972661_p4122565110275"></a><a name="en-us_topic_0057972661_p4122565110275"></a>Specifies the maximum number of ECSs that can be created.</p>
<p id="en-us_topic_0057972661_p771939515316"><a name="en-us_topic_0057972661_p771939515316"></a><a name="en-us_topic_0057972661_p771939515316"></a>The default value of <strong id="en-us_topic_0057972661_b8289053"><a name="en-us_topic_0057972661_b8289053"></a><a name="en-us_topic_0057972661_b8289053"></a>max_count</strong> is the same as that of <strong id="en-us_topic_0057972661_b7492614"><a name="en-us_topic_0057972661_b7492614"></a><a name="en-us_topic_0057972661_b7492614"></a>min_count</strong>.</p>
<p id="en-us_topic_0057972661_p52138865153152"><a name="en-us_topic_0057972661_p52138865153152"></a><a name="en-us_topic_0057972661_p52138865153152"></a>Note:</p>
<p id="en-us_topic_0057972661_p66596602153152"><a name="en-us_topic_0057972661_p66596602153152"></a><a name="en-us_topic_0057972661_p66596602153152"></a>The <strong id="en-us_topic_0057972661_b26298136"><a name="en-us_topic_0057972661_b26298136"></a><a name="en-us_topic_0057972661_b26298136"></a>max_count</strong> value must be greater than the <strong id="en-us_topic_0057972661_b35356632"><a name="en-us_topic_0057972661_b35356632"></a><a name="en-us_topic_0057972661_b35356632"></a>min_count</strong> value.</p>
<p id="en-us_topic_0057972661_p62498506153152"><a name="en-us_topic_0057972661_p62498506153152"></a><a name="en-us_topic_0057972661_p62498506153152"></a>If both <strong id="en-us_topic_0057972661_b45314905"><a name="en-us_topic_0057972661_b45314905"></a><a name="en-us_topic_0057972661_b45314905"></a>min_count</strong> and <strong id="en-us_topic_0057972661_b5180964"><a name="en-us_topic_0057972661_b5180964"></a><a name="en-us_topic_0057972661_b5180964"></a>max_count</strong> are specified, the number of ECSs that can be created depends on host resources. If host resources permit, you can create a maximum number of ECSs ranging from <strong id="en-us_topic_0057972661_b46628683"><a name="en-us_topic_0057972661_b46628683"></a><a name="en-us_topic_0057972661_b46628683"></a>min_count</strong> to <strong id="en-us_topic_0057972661_b17004965"><a name="en-us_topic_0057972661_b17004965"></a><a name="en-us_topic_0057972661_b17004965"></a>max_count</strong> values.</p>
<div class="note" id="en-us_topic_0057972661_note20928070193644"><a name="en-us_topic_0057972661_note20928070193644"></a><a name="en-us_topic_0057972661_note20928070193644"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p54134906193644"><a name="en-us_topic_0057972661_p54134906193644"></a><a name="en-us_topic_0057972661_p54134906193644"></a>When you use a specified image to create ECSs, this parameter is supported.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row29652792102639"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p36386296102658"><a name="en-us_topic_0057972661_p36386296102658"></a><a name="en-us_topic_0057972661_p36386296102658"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p7757123671012"><a name="p7757123671012"></a><a name="p7757123671012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p61608878102658"><a name="en-us_topic_0057972661_p61608878102658"></a><a name="en-us_topic_0057972661_p61608878102658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p19164491102658"><a name="en-us_topic_0057972661_p19164491102658"></a><a name="en-us_topic_0057972661_p19164491102658"></a>Specifies the disk configuration mode. The value can be <strong id="b131704233710139"><a name="b131704233710139"></a><a name="b131704233710139"></a>AUTO</strong> or <strong id="b185300378710139"><a name="b185300378710139"></a><a name="b185300378710139"></a>MANUAL</strong>.</p>
<a name="en-us_topic_0057972661_ul38262699102658"></a><a name="en-us_topic_0057972661_ul38262699102658"></a><ul id="en-us_topic_0057972661_ul38262699102658"><li><strong id="en-us_topic_0057972661_b1845617405112742"><a name="en-us_topic_0057972661_b1845617405112742"></a><a name="en-us_topic_0057972661_b1845617405112742"></a>MANUAL</strong>: indicates that the image space of the system disk cannot be expanded.</li><li><strong id="en-us_topic_0057972661_b527243814112758"><a name="en-us_topic_0057972661_b527243814112758"></a><a name="en-us_topic_0057972661_b527243814112758"></a>AUTO</strong>: indicates that the image space of the system disk can be automatically expanded to a value same as that specified in flavor.</li></ul>
<p id="en-us_topic_0057972661_p43329035102658"><a name="en-us_topic_0057972661_p43329035102658"></a><a name="en-us_topic_0057972661_p43329035102658"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row15681131174915"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1650191194918"><a name="p1650191194918"></a><a name="p1650191194918"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p19757133619100"><a name="p19757133619100"></a><a name="p19757133619100"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p14650131154914"><a name="p14650131154914"></a><a name="p14650131154914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.2.5.1.4 "><p id="p364511262207"><a name="p364511262207"></a><a name="p364511262207"></a>Specifies the description of an ECS, which is a null string by default. This is an extended attribute.</p>
<a name="ul176291026182010"></a><a name="ul176291026182010"></a><ul id="ul176291026182010"><li>Can contain a maximum of 85 characters.</li><li>Cannot contain special characters, such as &lt; and &gt;.</li></ul>
<div class="note" id="note318983732010"><a name="note318983732010"></a><a name="note318983732010"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1919342653912"></a><a name="ul1919342653912"></a><ul id="ul1919342653912"><li>The V2 API does not support this parameter.</li><li>The V2.1 API supports this parameter. In such a case, add a key-value pair to the request header. The key is consistently <strong id="b842352706145924"><a name="b842352706145924"></a><a name="b842352706145924"></a>X-OpenStack-Nova-API-Version</strong>, and the value is the microversion. When the value is <strong id="b842352706145957"><a name="b842352706145957"></a><a name="b842352706145957"></a>2.19</strong>, this parameter is valid.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  4** **metadata**  field description

<a name="en-us_topic_0057972661_table2373623012315"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row4787810512315"><th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972661_p5292128812315"><a name="en-us_topic_0057972661_p5292128812315"></a><a name="en-us_topic_0057972661_p5292128812315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666668%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057972661_p5876596012315"><a name="en-us_topic_0057972661_p5876596012315"></a><a name="en-us_topic_0057972661_p5876596012315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.705882352941178%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972661_p6242233712315"><a name="en-us_topic_0057972661_p6242233712315"></a><a name="en-us_topic_0057972661_p6242233712315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01960784313725%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972661_p2304450612315"><a name="en-us_topic_0057972661_p2304450612315"></a><a name="en-us_topic_0057972661_p2304450612315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row1717815342412"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p91796345418"><a name="en-us_topic_0057972661_p91796345418"></a><a name="en-us_topic_0057972661_p91796345418"></a>admin_pass</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p131791234844"><a name="en-us_topic_0057972661_p131791234844"></a><a name="en-us_topic_0057972661_p131791234844"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.705882352941178%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p51791934647"><a name="en-us_topic_0057972661_p51791934647"></a><a name="en-us_topic_0057972661_p51791934647"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.01960784313725%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p11179163419418"><a name="en-us_topic_0057972661_p11179163419418"></a><a name="en-us_topic_0057972661_p11179163419418"></a>Specifies the password of user <strong id="b1442086604213330"><a name="b1442086604213330"></a><a name="b1442086604213330"></a>Administrator</strong> for logging in to a Windows ECS.</p>
<p id="en-us_topic_0057972661_p1882625312510"><a name="en-us_topic_0057972661_p1882625312510"></a><a name="en-us_topic_0057972661_p1882625312510"></a>Example: <strong id="en-us_topic_0057972661_b84235270620046"><a name="en-us_topic_0057972661_b84235270620046"></a><a name="en-us_topic_0057972661_b84235270620046"></a>cloud.1234</strong></p>
<div class="note" id="en-us_topic_0057972661_note1931159867"><a name="en-us_topic_0057972661_note1931159867"></a><a name="en-us_topic_0057972661_note1931159867"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p15312694619"><a name="en-us_topic_0057972661_p15312694619"></a><a name="en-us_topic_0057972661_p15312694619"></a>This parameter is mandatory when a Windows ECS using password authentication is created.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  5** **block\_device\_mapping\_v2**  parameters

<a name="en-us_topic_0057972661_table15044407105358"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row46099088105358"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p13422222102415"><a name="p13422222102415"></a><a name="p13422222102415"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p4437192213248"><a name="p4437192213248"></a><a name="p4437192213248"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p1743713226241"><a name="p1743713226241"></a><a name="p1743713226241"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p114371922172411"><a name="p114371922172411"></a><a name="p114371922172411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row61925742105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p3486240110546"><a name="en-us_topic_0057972661_p3486240110546"></a><a name="en-us_topic_0057972661_p3486240110546"></a>source_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p528222710546"><a name="en-us_topic_0057972661_p528222710546"></a><a name="en-us_topic_0057972661_p528222710546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p2520722910546"><a name="en-us_topic_0057972661_p2520722910546"></a><a name="en-us_topic_0057972661_p2520722910546"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p2851968810546"><a name="en-us_topic_0057972661_p2851968810546"></a><a name="en-us_topic_0057972661_p2851968810546"></a>Specifies the source type of the volume device. Its value can be <strong id="b842352706154558"><a name="b842352706154558"></a><a name="b842352706154558"></a>volume</strong>, <strong id="b84235270615461"><a name="b84235270615461"></a><a name="b84235270615461"></a>image</strong>, <strong id="b84235270615465"><a name="b84235270615465"></a><a name="b84235270615465"></a>snapshot</strong>, or <strong id="b842352706161056"><a name="b842352706161056"></a><a name="b842352706161056"></a>blank</strong>.</p>
<p id="en-us_topic_0057972661_p547651293810"><a name="en-us_topic_0057972661_p547651293810"></a><a name="en-us_topic_0057972661_p547651293810"></a>If you use a volume to create an ECS, set <strong id="b57877864153727"><a name="b57877864153727"></a><a name="b57877864153727"></a>source_type</strong> to <strong id="b37827002153758"><a name="b37827002153758"></a><a name="b37827002153758"></a>volume</strong>. If you use an image to create an ECS, set <strong id="b22495374153731"><a name="b22495374153731"></a><a name="b22495374153731"></a>source_type</strong> to <strong id="b37236555153811"><a name="b37236555153811"></a><a name="b37236555153811"></a>image</strong>. If you use a snapshot to create an ECS, set <strong id="b175234490615293"><a name="b175234490615293"></a><a name="b175234490615293"></a>source_type</strong> to <strong id="b38468833153821"><a name="b38468833153821"></a><a name="b38468833153821"></a>snapshot</strong>. If you create an empty data volume, set <strong id="b426112774111"><a name="b426112774111"></a><a name="b426112774111"></a>source_type</strong> to <strong id="b11262167204112"><a name="b11262167204112"></a><a name="b11262167204112"></a>blank</strong>.</p>
<div class="note" id="en-us_topic_0057972661_note25817266173940"><a name="en-us_topic_0057972661_note25817266173940"></a><a name="en-us_topic_0057972661_note25817266173940"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p31028803173940"><a name="en-us_topic_0057972661_p31028803173940"></a><a name="en-us_topic_0057972661_p31028803173940"></a>If <strong id="en-us_topic_0057972661_b842352706174725"><a name="en-us_topic_0057972661_b842352706174725"></a><a name="en-us_topic_0057972661_b842352706174725"></a>source_type</strong> is <strong id="en-us_topic_0057972661_b842352706174651"><a name="en-us_topic_0057972661_b842352706174651"></a><a name="en-us_topic_0057972661_b842352706174651"></a>snapshot</strong> and <strong id="en-us_topic_0057972661_b842352706174743"><a name="en-us_topic_0057972661_b842352706174743"></a><a name="en-us_topic_0057972661_b842352706174743"></a>boot_index</strong> is 0, the EVS disk of this snapshot must be the system disk.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row9923110105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p5421404410546"><a name="en-us_topic_0057972661_p5421404410546"></a><a name="en-us_topic_0057972661_p5421404410546"></a>destination_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p2926143910546"><a name="en-us_topic_0057972661_p2926143910546"></a><a name="en-us_topic_0057972661_p2926143910546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p2136636710546"><a name="en-us_topic_0057972661_p2136636710546"></a><a name="en-us_topic_0057972661_p2136636710546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1970412531749"><a name="p1970412531749"></a><a name="p1970412531749"></a>Specifies the target type of the disk device. Its value can only be <strong id="b1706426110153149"><a name="b1706426110153149"></a><a name="b1706426110153149"></a>volume</strong>.</p>
<p id="en-us_topic_0057972661_p5295414710546"><a name="en-us_topic_0057972661_p5295414710546"></a><a name="en-us_topic_0057972661_p5295414710546"></a><strong id="b1516419404326"><a name="b1516419404326"></a><a name="b1516419404326"></a>volume</strong>: indicates the volume type.</p>
<p id="p1780613817404"><a name="p1780613817404"></a><a name="p1780613817404"></a><strong id="b17805319338"><a name="b17805319338"></a><a name="b17805319338"></a>local</strong>: indicates the local file, which has not been supported.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row9269169105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p1597666010546"><a name="en-us_topic_0057972661_p1597666010546"></a><a name="en-us_topic_0057972661_p1597666010546"></a>guest_format</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p1904109010546"><a name="en-us_topic_0057972661_p1904109010546"></a><a name="en-us_topic_0057972661_p1904109010546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p6593336110546"><a name="en-us_topic_0057972661_p6593336110546"></a><a name="en-us_topic_0057972661_p6593336110546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p3900205710546"><a name="en-us_topic_0057972661_p3900205710546"></a><a name="en-us_topic_0057972661_p3900205710546"></a>Specifies the local file system format. Its value can be <strong id="b1873743962112936"><a name="b1873743962112936"></a><a name="b1873743962112936"></a>swap</strong> or <strong id="b363440314112936"><a name="b363440314112936"></a><a name="b363440314112936"></a>ext4</strong>.</p>
<p id="en-us_topic_0057972661_p1547419510546"><a name="en-us_topic_0057972661_p1547419510546"></a><a name="en-us_topic_0057972661_p1547419510546"></a>This function is not supported.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row32258375105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p639950510546"><a name="en-us_topic_0057972661_p639950510546"></a><a name="en-us_topic_0057972661_p639950510546"></a>device_name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p4859790610546"><a name="en-us_topic_0057972661_p4859790610546"></a><a name="en-us_topic_0057972661_p4859790610546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p4411631510546"><a name="en-us_topic_0057972661_p4411631510546"></a><a name="en-us_topic_0057972661_p4411631510546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p204864456459"><a name="p204864456459"></a><a name="p204864456459"></a>Specifies the disk device name.</p>
<div class="note" id="note0422219468"><a name="note0422219468"></a><a name="note0422219468"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12532675472"><a name="p12532675472"></a><a name="p12532675472"></a>This field has been discarded.</p>
<p id="en-us_topic_0057972661_p1665179710546"><a name="en-us_topic_0057972661_p1665179710546"></a><a name="en-us_topic_0057972661_p1665179710546"></a>The specified <strong id="b1779043114019"><a name="b1779043114019"></a><a name="b1779043114019"></a>device_name</strong> does not take effect. The system generates a device name by default.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row34936617105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p5956509810546"><a name="en-us_topic_0057972661_p5956509810546"></a><a name="en-us_topic_0057972661_p5956509810546"></a>delete_on_termination</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p6004360410546"><a name="en-us_topic_0057972661_p6004360410546"></a><a name="en-us_topic_0057972661_p6004360410546"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p3169373810546"><a name="en-us_topic_0057972661_p3169373810546"></a><a name="en-us_topic_0057972661_p3169373810546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p1705602210546"><a name="en-us_topic_0057972661_p1705602210546"></a><a name="en-us_topic_0057972661_p1705602210546"></a>Specifies whether disks are deleted when an ECS is deleted. Its default value is <strong id="b842352706152455"><a name="b842352706152455"></a><a name="b842352706152455"></a>false</strong>.</p>
<p id="p1749452617197"><a name="p1749452617197"></a><a name="p1749452617197"></a><strong id="b351217913413"><a name="b351217913413"></a><a name="b351217913413"></a>true</strong>: Delete a disk when deleting an ECS.</p>
<p id="p1149519268197"><a name="p1149519268197"></a><a name="p1149519268197"></a><strong id="b67314482411"><a name="b67314482411"></a><a name="b67314482411"></a>false</strong>: When an ECS is deleted, its disk is not deleted.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row18070752105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p1870026710546"><a name="en-us_topic_0057972661_p1870026710546"></a><a name="en-us_topic_0057972661_p1870026710546"></a>boot_index</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p3832668110546"><a name="en-us_topic_0057972661_p3832668110546"></a><a name="en-us_topic_0057972661_p3832668110546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p1745343110546"><a name="en-us_topic_0057972661_p1745343110546"></a><a name="en-us_topic_0057972661_p1745343110546"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p444177310546"><a name="en-us_topic_0057972661_p444177310546"></a><a name="en-us_topic_0057972661_p444177310546"></a>Specifies whether it is a boot disk. <strong id="en-us_topic_0057972661_b84235270621371"><a name="en-us_topic_0057972661_b84235270621371"></a><a name="en-us_topic_0057972661_b84235270621371"></a>0</strong> specifies a boot disk, and <strong id="en-us_topic_0057972661_b842352706213645"><a name="en-us_topic_0057972661_b842352706213645"></a><a name="en-us_topic_0057972661_b842352706213645"></a>-1</strong> specifies a non-boot disk.</p>
<div class="note" id="en-us_topic_0057972661_note1430479894258"><a name="en-us_topic_0057972661_note1430479894258"></a><a name="en-us_topic_0057972661_note1430479894258"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p6163432094258"><a name="en-us_topic_0057972661_p6163432094258"></a><a name="en-us_topic_0057972661_p6163432094258"></a>If <strong id="en-us_topic_0057972661_b842352706162734"><a name="en-us_topic_0057972661_b842352706162734"></a><a name="en-us_topic_0057972661_b842352706162734"></a>source_type</strong> of the volume device is <strong id="en-us_topic_0057972661_b842352706162729"><a name="en-us_topic_0057972661_b842352706162729"></a><a name="en-us_topic_0057972661_b842352706162729"></a>volume</strong>, there must be one <strong id="en-us_topic_0057972661_b842352706161627"><a name="en-us_topic_0057972661_b842352706161627"></a><a name="en-us_topic_0057972661_b842352706161627"></a>boot_index</strong> whose value is <strong id="en-us_topic_0057972661_b842352706161631"><a name="en-us_topic_0057972661_b842352706161631"></a><a name="en-us_topic_0057972661_b842352706161631"></a>0</strong>.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0057972661_row54392189105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p1682739910546"><a name="en-us_topic_0057972661_p1682739910546"></a><a name="en-us_topic_0057972661_p1682739910546"></a>uuid</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p2084208210546"><a name="en-us_topic_0057972661_p2084208210546"></a><a name="en-us_topic_0057972661_p2084208210546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p1048705710546"><a name="en-us_topic_0057972661_p1048705710546"></a><a name="en-us_topic_0057972661_p1048705710546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p4414527710546"><a name="en-us_topic_0057972661_p4414527710546"></a><a name="en-us_topic_0057972661_p4414527710546"></a>If <strong id="b10449135719713"><a name="b10449135719713"></a><a name="b10449135719713"></a>source_type</strong> is <strong id="b14648210812"><a name="b14648210812"></a><a name="b14648210812"></a>volume</strong>, the value of this parameter is the volume UUID.</p>
<p id="p4942173262019"><a name="p4942173262019"></a><a name="p4942173262019"></a>If <strong id="b3404142614813"><a name="b3404142614813"></a><a name="b3404142614813"></a>source_type</strong> is <strong id="b0597629289"><a name="b0597629289"></a><a name="b0597629289"></a>snapshot</strong>, the value of this parameter is the snapshot UUID.</p>
<p id="p15942163242015"><a name="p15942163242015"></a><a name="p15942163242015"></a>If <strong id="b1177853081"><a name="b1177853081"></a><a name="b1177853081"></a>source_type</strong> is <strong id="b59411531488"><a name="b59411531488"></a><a name="b59411531488"></a>image</strong>, the value of this parameter is the image UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row43403738105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p3676107810546"><a name="en-us_topic_0057972661_p3676107810546"></a><a name="en-us_topic_0057972661_p3676107810546"></a>volume_size</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p2485733610546"><a name="en-us_topic_0057972661_p2485733610546"></a><a name="en-us_topic_0057972661_p2485733610546"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p17832210546"><a name="en-us_topic_0057972661_p17832210546"></a><a name="en-us_topic_0057972661_p17832210546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p1444414110546"><a name="en-us_topic_0057972661_p1444414110546"></a><a name="en-us_topic_0057972661_p1444414110546"></a>Specifies the volume size. The value is an integer. This parameter is mandatory when <strong id="b254888028113121"><a name="b254888028113121"></a><a name="b254888028113121"></a>source_type</strong> is set to <strong id="b1240294377113121"><a name="b1240294377113121"></a><a name="b1240294377113121"></a>image</strong> or <strong id="b13565393455"><a name="b13565393455"></a><a name="b13565393455"></a>blank</strong>, and <strong id="b872300708113121"><a name="b872300708113121"></a><a name="b872300708113121"></a>destination_type</strong> is set to <strong id="b131730660113121"><a name="b131730660113121"></a><a name="b131730660113121"></a>volume</strong>.</p>
<p id="en-us_topic_0057972661_p1645936993326"><a name="en-us_topic_0057972661_p1645936993326"></a><a name="en-us_topic_0057972661_p1645936993326"></a>Unit: GB</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row64465110105358"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p6079647310546"><a name="en-us_topic_0057972661_p6079647310546"></a><a name="en-us_topic_0057972661_p6079647310546"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p2556727610546"><a name="en-us_topic_0057972661_p2556727610546"></a><a name="en-us_topic_0057972661_p2556727610546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p5768348410546"><a name="en-us_topic_0057972661_p5768348410546"></a><a name="en-us_topic_0057972661_p5768348410546"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p4185060810546"><a name="en-us_topic_0057972661_p4185060810546"></a><a name="en-us_topic_0057972661_p4185060810546"></a>Specifies the volume type. This parameter is recommended when <strong id="b25526012205"><a name="b25526012205"></a><a name="b25526012205"></a>source_type</strong> is set to <strong id="b8553709207"><a name="b8553709207"></a><a name="b8553709207"></a>image</strong> and <strong id="b055313014207"><a name="b055313014207"></a><a name="b055313014207"></a>destination_type</strong> is set to <strong id="b12553190102014"><a name="b12553190102014"></a><a name="b12553190102014"></a>volume</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **security\_groups**  parameters

<a name="en-us_topic_0057972661_table16920677105453"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row60708739105453"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p14804142712417"><a name="p14804142712417"></a><a name="p14804142712417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.2"><p id="p9555122215124"><a name="p9555122215124"></a><a name="p9555122215124"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p1280402712240"><a name="p1280402712240"></a><a name="p1280402712240"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p208181427132416"><a name="p208181427132416"></a><a name="p208181427132416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row6853617105453"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p3952465110557"><a name="en-us_topic_0057972661_p3952465110557"></a><a name="en-us_topic_0057972661_p3952465110557"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p1755572271210"><a name="p1755572271210"></a><a name="p1755572271210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p4738015610557"><a name="en-us_topic_0057972661_p4738015610557"></a><a name="en-us_topic_0057972661_p4738015610557"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p1294589010557"><a name="en-us_topic_0057972661_p1294589010557"></a><a name="en-us_topic_0057972661_p1294589010557"></a>Specifies the security group name or UUID.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **networks**  parameters

<a name="en-us_topic_0057972661_table9995892105551"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row37997114105551"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p184551730132417"><a name="p184551730132417"></a><a name="p184551730132417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.2"><p id="p146295264122"><a name="p146295264122"></a><a name="p146295264122"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p15471830142410"><a name="p15471830142410"></a><a name="p15471830142410"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.5.1.4"><p id="p44711430132418"><a name="p44711430132418"></a><a name="p44711430132418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row27440950105551"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p1501087310563"><a name="en-us_topic_0057972661_p1501087310563"></a><a name="en-us_topic_0057972661_p1501087310563"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p762942681213"><a name="p762942681213"></a><a name="p762942681213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p792119010563"><a name="en-us_topic_0057972661_p792119010563"></a><a name="en-us_topic_0057972661_p792119010563"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p2866860910563"><a name="en-us_topic_0057972661_p2866860910563"></a><a name="en-us_topic_0057972661_p2866860910563"></a>Specifies the network port UUID.</p>
<p id="en-us_topic_0057972661_p5669089410563"><a name="en-us_topic_0057972661_p5669089410563"></a><a name="en-us_topic_0057972661_p5669089410563"></a>This parameter must be set when the network UUID is not specified.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row53194686105551"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p5571052610563"><a name="en-us_topic_0057972661_p5571052610563"></a><a name="en-us_topic_0057972661_p5571052610563"></a>uuid</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p11629142618127"><a name="p11629142618127"></a><a name="p11629142618127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p1625879010563"><a name="en-us_topic_0057972661_p1625879010563"></a><a name="en-us_topic_0057972661_p1625879010563"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p3793825410563"><a name="en-us_topic_0057972661_p3793825410563"></a><a name="en-us_topic_0057972661_p3793825410563"></a>Specifies the network UUID.</p>
<p id="en-us_topic_0057972661_p589997110563"><a name="en-us_topic_0057972661_p589997110563"></a><a name="en-us_topic_0057972661_p589997110563"></a>This parameter must be set when the network port is not specified.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row58124020105551"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p611192810563"><a name="en-us_topic_0057972661_p611192810563"></a><a name="en-us_topic_0057972661_p611192810563"></a>fixed_ip</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p6629326201219"><a name="p6629326201219"></a><a name="p6629326201219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p2530419410563"><a name="en-us_topic_0057972661_p2530419410563"></a><a name="en-us_topic_0057972661_p2530419410563"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p6060160810563"><a name="en-us_topic_0057972661_p6060160810563"></a><a name="en-us_topic_0057972661_p6060160810563"></a>Specifies the fixed IP address. Parameter <strong id="b1851113086"><a name="b1851113086"></a><a name="b1851113086"></a>port</strong> in the three network parameters (<strong id="b517196128"><a name="b517196128"></a><a name="b517196128"></a>port</strong>, <strong id="b1782053069"><a name="b1782053069"></a><a name="b1782053069"></a>uuid</strong>, and <strong id="b1873372205"><a name="b1873372205"></a><a name="b1873372205"></a>fixed_ip</strong>) has the highest priority. If parameter <strong id="b540286206"><a name="b540286206"></a><a name="b540286206"></a>fixed_ip</strong> is set, you must specify the UUID.</p>
</td>
</tr>
</tbody>
</table>

**Table  8** **os:scheduler\_hints**  parameters

<a name="en-us_topic_0057972661_table12534817105641"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row26068168105641"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p1858783513243"><a name="p1858783513243"></a><a name="p1858783513243"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.5.1.2"><p id="p165381328142"><a name="p165381328142"></a><a name="p165381328142"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p360443592415"><a name="p360443592415"></a><a name="p360443592415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.5.1.4"><p id="p160413532410"><a name="p160413532410"></a><a name="p160413532410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row62928048105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p15046690105656"><a name="en-us_topic_0057972661_p15046690105656"></a><a name="en-us_topic_0057972661_p15046690105656"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p15539528147"><a name="p15539528147"></a><a name="p15539528147"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p322913253235"><a name="p322913253235"></a><a name="p322913253235"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p1711236145217"><a name="p1711236145217"></a><a name="p1711236145217"></a>Specifies the anti-affinity group.</p>
<p id="en-us_topic_0057972661_p4240670105656"><a name="en-us_topic_0057972661_p4240670105656"></a><a name="en-us_topic_0057972661_p4240670105656"></a>The value is in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row64921661105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p39968339105656"><a name="en-us_topic_0057972661_p39968339105656"></a><a name="en-us_topic_0057972661_p39968339105656"></a>different_host</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p75391226145"><a name="p75391226145"></a><a name="p75391226145"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p6465152712239"><a name="p6465152712239"></a><a name="p6465152712239"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p12868562105656"><a name="en-us_topic_0057972661_p12868562105656"></a><a name="en-us_topic_0057972661_p12868562105656"></a>The function has not been supported, and this field is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row30356398105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p53049785105656"><a name="en-us_topic_0057972661_p53049785105656"></a><a name="en-us_topic_0057972661_p53049785105656"></a>same_host</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p17539162191416"><a name="p17539162191416"></a><a name="p17539162191416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p2065343105656"><a name="en-us_topic_0057972661_p2065343105656"></a><a name="en-us_topic_0057972661_p2065343105656"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p19667172105656"><a name="en-us_topic_0057972661_p19667172105656"></a><a name="en-us_topic_0057972661_p19667172105656"></a>The function has not been supported, and this field is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row42773507105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p43180380105656"><a name="en-us_topic_0057972661_p43180380105656"></a><a name="en-us_topic_0057972661_p43180380105656"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p10539172161419"><a name="p10539172161419"></a><a name="p10539172161419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p133891574237"><a name="p133891574237"></a><a name="p133891574237"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p5287950105656"><a name="en-us_topic_0057972661_p5287950105656"></a><a name="en-us_topic_0057972661_p5287950105656"></a>The function has not been supported, and this field is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row12287877105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p29710531105656"><a name="en-us_topic_0057972661_p29710531105656"></a><a name="en-us_topic_0057972661_p29710531105656"></a>build_near_host_ip</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p35394214149"><a name="p35394214149"></a><a name="p35394214149"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p1670754182311"><a name="p1670754182311"></a><a name="p1670754182311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p53961881105656"><a name="en-us_topic_0057972661_p53961881105656"></a><a name="en-us_topic_0057972661_p53961881105656"></a>The function has not been supported, and this field is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row63947270105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p12417014105656"><a name="en-us_topic_0057972661_p12417014105656"></a><a name="en-us_topic_0057972661_p12417014105656"></a>tenancy</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p1854062161414"><a name="p1854062161414"></a><a name="p1854062161414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p66254100105656"><a name="en-us_topic_0057972661_p66254100105656"></a><a name="en-us_topic_0057972661_p66254100105656"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p29039112105656"><a name="en-us_topic_0057972661_p29039112105656"></a><a name="en-us_topic_0057972661_p29039112105656"></a>Specifies whether the ECS is created on a Dedicated Host (DeH) or in a shared pool (default).</p>
<p id="en-us_topic_0057972661_p219220436270"><a name="en-us_topic_0057972661_p219220436270"></a><a name="en-us_topic_0057972661_p219220436270"></a>The value can be <strong id="en-us_topic_0057972661_b177257758703220"><a name="en-us_topic_0057972661_b177257758703220"></a><a name="en-us_topic_0057972661_b177257758703220"></a>shared</strong> or <strong id="en-us_topic_0057972661_b73566161403220"><a name="en-us_topic_0057972661_b73566161403220"></a><a name="en-us_topic_0057972661_b73566161403220"></a>dedicated</strong>.</p>
<a name="en-us_topic_0057972661_ul16179359172716"></a><a name="en-us_topic_0057972661_ul16179359172716"></a><ul id="en-us_topic_0057972661_ul16179359172716"><li><strong id="en-us_topic_0057972661_b84235270603231"><a name="en-us_topic_0057972661_b84235270603231"></a><a name="en-us_topic_0057972661_b84235270603231"></a>shared</strong>: indicates the shared pool.</li><li><strong id="en-us_topic_0057972661_b84235270603241"><a name="en-us_topic_0057972661_b84235270603241"></a><a name="en-us_topic_0057972661_b84235270603241"></a>dedicated</strong>: indicates the DeH.</li></ul>
<p id="en-us_topic_0057972661_p1488816294282"><a name="en-us_topic_0057972661_p1488816294282"></a><a name="en-us_topic_0057972661_p1488816294282"></a>The parameter value also takes effect for ECS query operations.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row31685405105641"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p19286814105656"><a name="en-us_topic_0057972661_p19286814105656"></a><a name="en-us_topic_0057972661_p19286814105656"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p2540112161416"><a name="p2540112161416"></a><a name="p2540112161416"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p18728119105656"><a name="en-us_topic_0057972661_p18728119105656"></a><a name="en-us_topic_0057972661_p18728119105656"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p65968369105656"><a name="en-us_topic_0057972661_p65968369105656"></a><a name="en-us_topic_0057972661_p65968369105656"></a>Specifies the DeH ID.</p>
<p id="en-us_topic_0057972661_p56844412105656"><a name="en-us_topic_0057972661_p56844412105656"></a><a name="en-us_topic_0057972661_p56844412105656"></a>This parameter takes effect only when the value of <strong id="en-us_topic_0057972661_b57098564112329"><a name="en-us_topic_0057972661_b57098564112329"></a><a name="en-us_topic_0057972661_b57098564112329"></a>tenancy</strong> is <strong id="en-us_topic_0057972661_b44125034112329"><a name="en-us_topic_0057972661_b44125034112329"></a><a name="en-us_topic_0057972661_b44125034112329"></a>dedicated</strong>.</p>
<p id="en-us_topic_0057972661_p41837667105656"><a name="en-us_topic_0057972661_p41837667105656"></a><a name="en-us_topic_0057972661_p41837667105656"></a>If you do not specify this parameter, the system will automatically assign a DeH to you to deploy ECSs.</p>
<p id="en-us_topic_0057972661_p40994685105656"><a name="en-us_topic_0057972661_p40994685105656"></a><a name="en-us_topic_0057972661_p40994685105656"></a>The parameter value also takes effect for ECS query operations.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row1451311915810"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p135159935817"><a name="en-us_topic_0057972661_p135159935817"></a><a name="en-us_topic_0057972661_p135159935817"></a>check_resources</p>
</td>
<td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.5.1.2 "><p id="p65408251413"><a name="p65408251413"></a><a name="p65408251413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p10515169125817"><a name="en-us_topic_0057972661_p10515169125817"></a><a name="en-us_topic_0057972661_p10515169125817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.5.1.4 "><p id="p1176174163413"><a name="p1176174163413"></a><a name="p1176174163413"></a>Specifies whether to check resource sufficiency when creating an ECS. If this parameter is not configured, the system does not check resource sufficiency by default.</p>
<p id="en-us_topic_0057972661_p7354558152617"><a name="en-us_topic_0057972661_p7354558152617"></a><a name="en-us_topic_0057972661_p7354558152617"></a>The value can be <strong id="b842352706184734"><a name="b842352706184734"></a><a name="b842352706184734"></a>true</strong> or <strong id="b842352706184738"><a name="b842352706184738"></a><a name="b842352706184738"></a>false</strong>. The default value is <strong id="b842352706184742"><a name="b842352706184742"></a><a name="b842352706184742"></a>false</strong>.</p>
<a name="en-us_topic_0057972661_ul658716261273"></a><a name="en-us_topic_0057972661_ul658716261273"></a><ul id="en-us_topic_0057972661_ul658716261273"><li><strong id="en-us_topic_0057972661_b842352706102527"><a name="en-us_topic_0057972661_b842352706102527"></a><a name="en-us_topic_0057972661_b842352706102527"></a>true</strong>: indicates that the system will check resource sufficiency. If the resources are insufficient, the check result will be returned.</li><li><strong id="en-us_topic_0057972661_b842352706102721"><a name="en-us_topic_0057972661_b842352706102721"></a><a name="en-us_topic_0057972661_b842352706102721"></a>false</strong>: indicates that the system will not check resource sufficiency.</li></ul>
<div class="note" id="en-us_topic_0057972661_note15121261355"><a name="en-us_topic_0057972661_note15121261355"></a><a name="en-us_topic_0057972661_note15121261355"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057972661_p11516136458"><a name="en-us_topic_0057972661_p11516136458"></a><a name="en-us_topic_0057972661_p11516136458"></a>Since the resource usage is dynamic, the resource sufficiency check result is not accurate.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972661_section32057793"></a>

[Table 9](#table44736746)  describes the response parameters.

**Table  9**  Response parameters

<a name="table44736746"></a>
<table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p63657004"><a name="p63657004"></a><a name="p63657004"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p35147813"><a name="p35147813"></a><a name="p35147813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="p28400574"><a name="p28400574"></a><a name="p28400574"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies ECS information. For details, see <a href="#en-us_topic_0057972661_table37882063">Table 10</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  10** **server**  field description

<a name="en-us_topic_0057972661_table37882063"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row35582587"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057972661_p63617293"><a name="en-us_topic_0057972661_p63617293"></a><a name="en-us_topic_0057972661_p63617293"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057972661_p52727095"><a name="en-us_topic_0057972661_p52727095"></a><a name="en-us_topic_0057972661_p52727095"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057972661_p63390070"><a name="en-us_topic_0057972661_p63390070"></a><a name="en-us_topic_0057972661_p63390070"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row1032124"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972661_p16493259"><a name="en-us_topic_0057972661_p16493259"></a><a name="en-us_topic_0057972661_p16493259"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p60885635"><a name="en-us_topic_0057972661_p60885635"></a><a name="en-us_topic_0057972661_p60885635"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972661_p38694667"><a name="en-us_topic_0057972661_p38694667"></a><a name="en-us_topic_0057972661_p38694667"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row12707688"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972661_p22689808"><a name="en-us_topic_0057972661_p22689808"></a><a name="en-us_topic_0057972661_p22689808"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p25935173"><a name="en-us_topic_0057972661_p25935173"></a><a name="en-us_topic_0057972661_p25935173"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972661_p39701876"><a name="en-us_topic_0057972661_p39701876"></a><a name="en-us_topic_0057972661_p39701876"></a>Specifies the URI of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row21772565"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972661_p18747312"><a name="en-us_topic_0057972661_p18747312"></a><a name="en-us_topic_0057972661_p18747312"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p42137308"><a name="en-us_topic_0057972661_p42137308"></a><a name="en-us_topic_0057972661_p42137308"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972661_p41469957"><a name="en-us_topic_0057972661_p41469957"></a><a name="en-us_topic_0057972661_p41469957"></a>Specifies the security group of the ECS.</p>
</td>
</tr>
<tr id="en-us_topic_0057972661_row37685299"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972661_p32610412"><a name="en-us_topic_0057972661_p32610412"></a><a name="en-us_topic_0057972661_p32610412"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p24197721"><a name="en-us_topic_0057972661_p24197721"></a><a name="en-us_topic_0057972661_p24197721"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972661_p48788849"><a name="en-us_topic_0057972661_p48788849"></a><a name="en-us_topic_0057972661_p48788849"></a>Specifies the disk configuration mode.</p>
<a name="en-us_topic_0057972661_ul36446461"></a><a name="en-us_topic_0057972661_ul36446461"></a><ul id="en-us_topic_0057972661_ul36446461"><li><strong id="en-us_topic_0057972661_b63173312"><a name="en-us_topic_0057972661_b63173312"></a><a name="en-us_topic_0057972661_b63173312"></a>MANUAL</strong>: indicates that the image space of the system disk cannot be expanded.</li><li><strong id="en-us_topic_0057972661_b16764629"><a name="en-us_topic_0057972661_b16764629"></a><a name="en-us_topic_0057972661_b16764629"></a>AUTO</strong>: indicates that the image space of the system disk can be automatically expanded to a value same as that specified in flavor.</li></ul>
</td>
</tr>
<tr id="row11302638192316"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p18302113820232"><a name="p18302113820232"></a><a name="p18302113820232"></a>reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p9302138142319"><a name="p9302138142319"></a><a name="p9302138142319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><div class="p" id="p139921927192516"><a name="p139921927192516"></a><a name="p139921927192516"></a>Specifies a filtering criteria to query the created ECSs.<div class="note" id="note11231428132513"><a name="note11231428132513"></a><a name="note11231428132513"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p112322862510"><a name="p112322862510"></a><a name="p112322862510"></a>When you create ECSs in a batch, this parameter is available.</p>
</div></div>
</div>
</td>
</tr>
<tr id="row928515498315"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p22879491036"><a name="p22879491036"></a><a name="p22879491036"></a>adminPass</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p528713493311"><a name="p528713493311"></a><a name="p528713493311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1628710497317"><a name="p1628710497317"></a><a name="p1628710497317"></a>Specifies the password of user <strong id="en-us_topic_0057972661_b842352706195929"><a name="en-us_topic_0057972661_b842352706195929"></a><a name="en-us_topic_0057972661_b842352706195929"></a>Administrator</strong> for logging in to a Windows ECS.</p>
</td>
</tr>
</tbody>
</table>

## Example Request \(Creating an ECS\)<a name="section8540539202712"></a>

Example URL request

```
POST https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers
POST https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers
```

**Example 1: Use an image to create an ECS through the API block\_device\_mapping\_v2.**

```
 { 
    "server": { 
        "flavorRef": "2", 
        "name": "wjvm48", 
        "metadata": { 
            "name": "name_xx1", 
            "id": "id_xxxx1" 
        }, 
        "block_device_mapping_v2": [{ 
            "source_type": "image", 
            "destination_type": "volume", 
            "uuid": "b023fe17-11db-4efb-b800-78882a0e394b", 
            "delete_on_termination": "False", 
            "boot_index": "0",
            "volume_type": "SAS",
            "volume_size": "40"
        }], 
        "security_groups": [{ 
            "name": "name_xx5_sg" 
        }], 
        "networks": [{ 
            "uuid": "fd40e6f8-942d-4b4e-a7ae-465287b02a2c", 
            "port": "e730a11c-1a19-49cc-8797-cee2ad67af6f", 
            "fixed_ip": "10.20.30.137" 
        }], 
        "key_name": "test", 
        "user_data": "ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==", 
        "availability_zone":"az1-dc1"
    } 
}
```

**Example 2: Use a snapshot to create an ECS through the API block\_device\_mapping\_v2.**

>![](/images/icon-note.gif) **NOTE:**   
>When  **source\_type**  is  **snapshot**,  **boot\_index**  is  **0**, and the EVS disk corresponding to the snapshot must be a system disk.  

```
{
    "server":{
        "name":"wjvm48",
        "availability_zone":"az1-dc1",
        "block_device_mapping_v2": [
            {
                "source_type":"snapshot",
                "boot_index":"0",
                "uuid":"df51997d-ee35-4fb3-a372-e2ac933a6565", //Specifies the snapshot ID, which is returned by the API for creating a snapshot.
                "destination_type":"volume"
            }
        ],
        "flavorRef":"s3.xlarge.2",
        "max_count":1,
        "min_count":1,
        "networks": [
            {
                "uuid":"79a68cef-0936-4e21-b1f4-b800ecb70246"
            }
        ] 
    } 
}
```

**Example 3: Use a disk to create an ECS through the API block\_device\_mapping\_v2.**

```
{ 
    "server": { 
        "flavorRef": "2", 
        "name": "wjvm48", 
        "metadata": { 
            "name": "name_xx1", 
            "id": "id_xxxx1" 
        }, 
        "block_device_mapping_v2": [{ 
            "source_type": "volume", 
            "destination_type": "volume", 
            "uuid": "bd7e4f86-b004-4745-bea2-a55b1085f107", 
            "delete_on_termination": "False", 
            "boot_index": "0", 
            "volume_type": "dsware",
            "volume_size": "40"
        }], 
        "security_groups": [{ 
            "name": "name_xx5_sg" 
        }], 
        "networks": [{ 
            "uuid": "fd40e6f8-942d-4b4e-a7ae-465287b02a2c", 
            "port": "e730a11c-1a19-49cc-8797-cee2ad67af6f", 
            "fixed_ip": "10.20.30.137" 
        }], 
        "key_name": "test", 
        "user_data": "ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==", 
        "availability_zone":"az1-dc1"
    } 
}
```

**Example 4: Create an ECS through the API imageRef.**

```
{ 
    "server": { 
        "flavorRef": "2", 
        "name": "wjvm48", 
        "metadata": { 
            "name": "name_xx1", 
            "id": "id_xxxx1" 
        }, 
        "adminPass": "name_xx1", 
        "imageRef": "6b344c54-d606-4e1a-a99e-a7d0250c3d14",
        "security_groups": [{ 
            "name": "name_xx5_sg" 
        }], 
        "networks": [{ 
            "uuid": "fd40e6f8-942d-4b4e-a7ae-465287b02a2c",
            "port": "e730a11c-1a19-49cc-8797-cee2ad67af6f",
            "fixed_ip": "10.20.30.137" 
        }], 
        "key_name": "test", 
        "user_data": "ICAgICAgDQoiQSBjbG91ZCBkb2VzIG5vdCBrbm93IHdoeSBpdCBtb3ZlcyBpbiBqdXN0IHN1Y2ggYSBkaXJlY3Rpb24gYW5kIGF0IHN1Y2ggYSBzcGVlZC4uLkl0IGZlZWxzIGFuIGltcHVsc2lvbi4uLnRoaXMgaXMgdGhlIHBsYWNlIHRvIGdvIG5vdy4gQnV0IHRoZSBza3kga25vd3MgdGhlIHJlYXNvbnMgYW5kIHRoZSBwYXR0ZXJucyBiZWhpbmQgYWxsIGNsb3VkcywgYW5kIHlvdSB3aWxsIGtub3csIHRvbywgd2hlbiB5b3UgbGlmdCB5b3Vyc2VsZiBoaWdoIGVub3VnaCB0byBzZWUgYmV5b25kIGhvcml6b25zLiINCg0KLVJpY2hhcmQgQmFjaA==", 
        "availability_zone":"az1-dc1"
    } 
}
```

## Example Response \(Creating an ECS\)<a name="section5933204164918"></a>

```
{
    "server": {
        "security_groups": [
            {
                "name": "name_xx5_sg"
            }
        ],
        "OS-DCF:diskConfig": " MANUAL",
        "id": "567c1557-0eca-422c-bfce-149d6b8f1bb8",
        "links": [
            {
                "href": "http://192.168.82.230:8774/v2/dc4059e8e7994f2498b514ca04cdaf44/servers/567c1557-0eca-422c-bfce-149d6b8f1bb8",
                "rel": "self"
            },
            {
                "href": "http://192.168.82.230:8774/dc4059e8e7994f2498b514ca04cdaf44/servers/567c1557-0eca-422c-bfce-149d6b8f1bb8",
                "rel": "bookmark"
            }
        ],
        "adminPass": "name_xx1"
    }
}
```

## Example Request \(Creating ECSs in a Batch\)<a name="section9554114338"></a>

```
{
    "server": {
        "availability_zone":"az1.dc1",
        "name": "test",
        "imageRef": "10ff4f01-35b6-4209-8397-359cb4475fa0",
        "flavorRef": "s1.medium",
        "return_reservation_id": "true",
        "networks": [
            {
                "uuid": "51bead38-d1a3-4d08-be20-0970c24b7cab"
            }
        ],
        "min_count": "2",
        "max_count": "3"
    }
}
```

## Example Response \(Creating ECSs in a Batch\)<a name="section4462153875112"></a>

```
{
    "reservation_id": "r-3fhpjulh"
}
```

## Returned Values<a name="en-us_topic_0057972661_section128741313191616"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

