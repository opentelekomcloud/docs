# Querying Share Access Rules<a name="sfs_02_0031"></a>

## Function<a name="sfc330dd13c3e46789320fcc48f30e764"></a>

This API is used to query a share access rule.

## URI<a name="sbbf3d6c9411c493fa951af509bc99433"></a>

-   POST /v2/\{project\_id\}/shares/\{share\_id\}/action
-   Parameter description

    <a name="en-us_topic_0064390800_table18958859"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390800_row60235282"><th class="cellrowborder" valign="top" width="18.98%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.24%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.75%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390800_row16100147"><td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.1 "><p id="a042a6f3d94c640c99a230c81cbc791fd"><a name="a042a6f3d94c640c99a230c81cbc791fd"></a><a name="a042a6f3d94c640c99a230c81cbc791fd"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.1.5.1.2 "><p id="a6f3a78a671fe4398808ef1370e6854d8"><a name="a6f3a78a671fe4398808ef1370e6854d8"></a><a name="a6f3a78a671fe4398808ef1370e6854d8"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.3 "><p id="a0fa81ab718b948808e7b08264c247d25"><a name="a0fa81ab718b948808e7b08264c247d25"></a><a name="a0fa81ab718b948808e7b08264c247d25"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.75%" headers="mcps1.1.5.1.4 "><p id="a34d13c1d9fb041778c6697c69959172a"><a name="a34d13c1d9fb041778c6697c69959172a"></a><a name="a34d13c1d9fb041778c6697c69959172a"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row24726637"><td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390800_p484083916120"><a name="en-us_topic_0064390800_p484083916120"></a><a name="en-us_topic_0064390800_p484083916120"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.24%" headers="mcps1.1.5.1.2 "><p id="ab9e49f180cb74c04a4e7f7eaada0161b"><a name="ab9e49f180cb74c04a4e7f7eaada0161b"></a><a name="ab9e49f180cb74c04a4e7f7eaada0161b"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.1.5.1.3 "><p id="a98fb9af656a541fb849dfae43da42811"><a name="a98fb9af656a541fb849dfae43da42811"></a><a name="a98fb9af656a541fb849dfae43da42811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.75%" headers="mcps1.1.5.1.4 "><p id="ac650082eebc04454bd7512859110c8d0"><a name="ac650082eebc04454bd7512859110c8d0"></a><a name="ac650082eebc04454bd7512859110c8d0"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s4516ddff66984b8bb66d458539fe3cb7"></a>

-   Parameter description

    <a name="en-us_topic_0064390800_table42069424"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390800_row20618333"><th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.1.5.1.1"><p id="p33061732167"><a name="p33061732167"></a><a name="p33061732167"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.1.5.1.2"><p id="p73062315163"><a name="p73062315163"></a><a name="p73062315163"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.3%" id="mcps1.1.5.1.3"><p id="p1532112318161"><a name="p1532112318161"></a><a name="p1532112318161"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.19%" id="mcps1.1.5.1.4"><p id="p3321937166"><a name="p3321937166"></a><a name="p3321937166"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390800_row35228531"><td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390800_p34938791"><a name="en-us_topic_0064390800_p34938791"></a><a name="en-us_topic_0064390800_p34938791"></a>os-access_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.5.1.2 "><p id="aa84ea7aa2f4f442c947c57e3b91984ea"><a name="aa84ea7aa2f4f442c947c57e3b91984ea"></a><a name="aa84ea7aa2f4f442c947c57e3b91984ea"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.3 "><p id="a4424785a39014ff4953b2c507752ec06"><a name="a4424785a39014ff4953b2c507752ec06"></a><a name="a4424785a39014ff4953b2c507752ec06"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.19%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390800_p18961705"><a name="en-us_topic_0064390800_p18961705"></a><a name="en-us_topic_0064390800_p18961705"></a>Specifies the <strong id="ae9f1c47f8cfa4f8a80b0e91be0dc173b"><a name="ae9f1c47f8cfa4f8a80b0e91be0dc173b"></a><a name="ae9f1c47f8cfa4f8a80b0e91be0dc173b"></a>os-access_list</strong> object. To view access rules, set this value to <strong id="b115681257105510"><a name="b115681257105510"></a><a name="b115681257105510"></a>null</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "os-access_list": null
    }
    ```


## Response<a name="seab648ffefb54176abde485b2f0516a2"></a>

-   **Description**

    <a name="en-us_topic_0064390800_table42930000"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390800_row2515205"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.1.4.1.1"><p id="p058798111616"><a name="p058798111616"></a><a name="p058798111616"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.26%" id="mcps1.1.4.1.2"><p id="p1658711841614"><a name="p1658711841614"></a><a name="p1658711841614"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.75%" id="mcps1.1.4.1.3"><p id="p158718131612"><a name="p158718131612"></a><a name="p158718131612"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390800_row53959953"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390800_p8680100"><a name="en-us_topic_0064390800_p8680100"></a><a name="en-us_topic_0064390800_p8680100"></a>access_list</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.1.4.1.2 "><p id="a5e45069dda6f495ba9daf090ff968c0d"><a name="a5e45069dda6f495ba9daf090ff968c0d"></a><a name="a5e45069dda6f495ba9daf090ff968c0d"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.75%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390800_p20069106"><a name="en-us_topic_0064390800_p20069106"></a><a name="en-us_topic_0064390800_p20069106"></a>Lists the access rules.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **access\_list**

    <a name="en-us_topic_0064390800_table14984857"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390800_row44671593"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.1.4.1.1"><p id="p1750921011618"><a name="p1750921011618"></a><a name="p1750921011618"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.98%" id="mcps1.1.4.1.2"><p id="p25091610181610"><a name="p25091610181610"></a><a name="p25091610181610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.800000000000004%" id="mcps1.1.4.1.3"><p id="p17509111001611"><a name="p17509111001611"></a><a name="p17509111001611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390800_row20756449"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="a654a016e1834425192abbc0f3731362f"><a name="a654a016e1834425192abbc0f3731362f"></a><a name="a654a016e1834425192abbc0f3731362f"></a>access_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="a5dd1a2c1872c42d098ea74f8947f4074"><a name="a5dd1a2c1872c42d098ea74f8947f4074"></a><a name="a5dd1a2c1872c42d098ea74f8947f4074"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="a585b9cc28b83407e88c3edae8d4fca11"><a name="a585b9cc28b83407e88c3edae8d4fca11"></a><a name="a585b9cc28b83407e88c3edae8d4fca11"></a>Specifies the type of the share access rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row51759670"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="a3dbacfe1728940058e0ab563bc93bff0"><a name="a3dbacfe1728940058e0ab563bc93bff0"></a><a name="a3dbacfe1728940058e0ab563bc93bff0"></a>access_to</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="a460735d2dfab4f30923f723ac46c053c"><a name="a460735d2dfab4f30923f723ac46c053c"></a><a name="a460735d2dfab4f30923f723ac46c053c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="a5dd004105af840eabf92147f564eda2f"><a name="a5dd004105af840eabf92147f564eda2f"></a><a name="a5dd004105af840eabf92147f564eda2f"></a>Specifies the access that the back end grants or denies.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row61813935"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390800_p445371116628"><a name="en-us_topic_0064390800_p445371116628"></a><a name="en-us_topic_0064390800_p445371116628"></a>access_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="a14545a3cdbff475ab7accdd4ea1cc281"><a name="a14545a3cdbff475ab7accdd4ea1cc281"></a><a name="a14545a3cdbff475ab7accdd4ea1cc281"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="a49931291536a4876ba9ffb429571a52c"><a name="a49931291536a4876ba9ffb429571a52c"></a><a name="a49931291536a4876ba9ffb429571a52c"></a>Specifies the level of the access rule.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row34965068"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="a9891284139324ba884969841c517498e"><a name="a9891284139324ba884969841c517498e"></a><a name="a9891284139324ba884969841c517498e"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="ab7df6917949d406fb83dc9373a2ddd05"><a name="ab7df6917949d406fb83dc9373a2ddd05"></a><a name="ab7df6917949d406fb83dc9373a2ddd05"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="p121105177474"><a name="p121105177474"></a><a name="p121105177474"></a>Specifies the status of the share access rule. If the API version is earlier than 2.28, the status of the share access rule is <strong id="b1425455104020"><a name="b1425455104020"></a><a name="b1425455104020"></a>new</strong>, <strong id="b13267553403"><a name="b13267553403"></a><a name="b13267553403"></a>active</strong>, or <strong id="b192965513405"><a name="b192965513405"></a><a name="b192965513405"></a>error</strong>. In versions from 2.28 to 2.42, the status of the share access rule is <strong id="b113085515404"><a name="b113085515404"></a><a name="b113085515404"></a>queued_to_apply</strong>, <strong id="b19311556402"><a name="b19311556402"></a><a name="b19311556402"></a>applying</strong>, <strong id="b153225512400"><a name="b153225512400"></a><a name="b153225512400"></a>active</strong>, <strong id="b33375517409"><a name="b33375517409"></a><a name="b33375517409"></a>error</strong>, <strong id="b14345558408"><a name="b14345558408"></a><a name="b14345558408"></a>queued_to_deny</strong>, or <strong id="b93415520407"><a name="b93415520407"></a><a name="b93415520407"></a>denying</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row28798367"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390800_p211614816628"><a name="en-us_topic_0064390800_p211614816628"></a><a name="en-us_topic_0064390800_p211614816628"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="acdf633b42f4d46ce8cad0ed30b403d25"><a name="acdf633b42f4d46ce8cad0ed30b403d25"></a><a name="acdf633b42f4d46ce8cad0ed30b403d25"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="a00aa32d97765477497f3c72a1cf770b9"><a name="a00aa32d97765477497f3c72a1cf770b9"></a><a name="a00aa32d97765477497f3c72a1cf770b9"></a>Specifies the UUID of the share access rule.</p>
    </td>
    </tr>
    <tr id="row10514105216457"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="p10201155134810"><a name="p10201155134810"></a><a name="p10201155134810"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="p5201165514816"><a name="p5201165514816"></a><a name="p5201165514816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="p72011155134814"><a name="p72011155134814"></a><a name="p72011155134814"></a>Specifies the time when a shared access rule is created. This parameter exists only when the value of <strong id="b24998911917"><a name="b24998911917"></a><a name="b24998911917"></a>X-Openstack-Manila-Api-Version</strong> in the request header is greater than or equal to 2.33.</p>
    </td>
    </tr>
    <tr id="row8182165515455"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="p8201185584818"><a name="p8201185584818"></a><a name="p8201185584818"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.1.4.1.2 "><p id="p1520115553482"><a name="p1520115553482"></a><a name="p1520115553482"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.800000000000004%" headers="mcps1.1.4.1.3 "><p id="p1720135512481"><a name="p1720135512481"></a><a name="p1720135512481"></a>Specifies the time when a shared access rule is updated. This parameter exists only when the value of <strong id="b09075011199"><a name="b09075011199"></a><a name="b09075011199"></a>X-Openstack-Manila-Api-Version</strong> in the request header is greater than or equal to 2.33.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
      "access_list": [
        {
          "access_level": "rw",
          "state": "active",
          "id": "85417bed-5e26-4c99-8c0c-92c95b5c640e",
          "access_type": "cert",
          "access_to": "a91556b7-c7c8-4273-915e-2729e04cdb01",
          "created_at": "2017-07-07T03:15:06.858662",
          "updated_at": "2018-07-07T03:15:06.858662"
        },
        {
          "access_level": "rw",
          "state": "active",
          "id": "2ecbeb0b-b2ba-41f1-ba63-0666548925b9",
          "access_type": "cert",
          "access_to": "0560a527-0e77-40a6-aa3b-110beecad368#0.0.0.0/0#0#all_squash,root_squash",
          "created_at": "2017-07-07T03:15:06.858662",
          "updated_at": "2018-07-07T03:15:06.858662"
        },
        {
          "access_level": "rw",
          "state": "active",
          "id": "24615391-d58d-4a74-ac5a-520233c9c396",
          "access_type": "cert",
          "access_to": "0560a527-0e77-40a6-aa3b-110beecad368#192.168.196.47#1#all_squash,root_squash",
          "created_at": "2017-07-07T03:15:06.858662",
          "updated_at": "2018-07-07T03:15:06.858662"
        }
      ]
    }
    ```


## Status Codes<a name="s7fc5f19dc3084299a3bda6a055eeafa6"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0064390800_table41753265"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390800_row43144677"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="en-us_topic_0064390800_p5057967"><a name="en-us_topic_0064390800_p5057967"></a><a name="en-us_topic_0064390800_p5057967"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="en-us_topic_0064390800_p7042173"><a name="en-us_topic_0064390800_p7042173"></a><a name="en-us_topic_0064390800_p7042173"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390800_row33545144"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p32802119"><a name="en-us_topic_0064390800_p32802119"></a><a name="en-us_topic_0064390800_p32802119"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p39725971"><a name="en-us_topic_0064390800_p39725971"></a><a name="en-us_topic_0064390800_p39725971"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row21989419"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p36312476"><a name="en-us_topic_0064390800_p36312476"></a><a name="en-us_topic_0064390800_p36312476"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p55629438"><a name="en-us_topic_0064390800_p55629438"></a><a name="en-us_topic_0064390800_p55629438"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row30902896"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p20106686"><a name="en-us_topic_0064390800_p20106686"></a><a name="en-us_topic_0064390800_p20106686"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p18028880"><a name="en-us_topic_0064390800_p18028880"></a><a name="en-us_topic_0064390800_p18028880"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row28042199"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p56825610"><a name="en-us_topic_0064390800_p56825610"></a><a name="en-us_topic_0064390800_p56825610"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p39471735"><a name="en-us_topic_0064390800_p39471735"></a><a name="en-us_topic_0064390800_p39471735"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row19701298"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p52301286"><a name="en-us_topic_0064390800_p52301286"></a><a name="en-us_topic_0064390800_p52301286"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p8545767"><a name="en-us_topic_0064390800_p8545767"></a><a name="en-us_topic_0064390800_p8545767"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row9803039"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p55848701"><a name="en-us_topic_0064390800_p55848701"></a><a name="en-us_topic_0064390800_p55848701"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p27450972"><a name="en-us_topic_0064390800_p27450972"></a><a name="en-us_topic_0064390800_p27450972"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row45732164"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p13317766"><a name="en-us_topic_0064390800_p13317766"></a><a name="en-us_topic_0064390800_p13317766"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p4997277"><a name="en-us_topic_0064390800_p4997277"></a><a name="en-us_topic_0064390800_p4997277"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row44975500"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p19136893"><a name="en-us_topic_0064390800_p19136893"></a><a name="en-us_topic_0064390800_p19136893"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p6584502"><a name="en-us_topic_0064390800_p6584502"></a><a name="en-us_topic_0064390800_p6584502"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row59260526"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p35373287"><a name="en-us_topic_0064390800_p35373287"></a><a name="en-us_topic_0064390800_p35373287"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p46663997"><a name="en-us_topic_0064390800_p46663997"></a><a name="en-us_topic_0064390800_p46663997"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row17322790"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p60968721"><a name="en-us_topic_0064390800_p60968721"></a><a name="en-us_topic_0064390800_p60968721"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p39519373"><a name="en-us_topic_0064390800_p39519373"></a><a name="en-us_topic_0064390800_p39519373"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row20130041"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p19920592"><a name="en-us_topic_0064390800_p19920592"></a><a name="en-us_topic_0064390800_p19920592"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p2955276"><a name="en-us_topic_0064390800_p2955276"></a><a name="en-us_topic_0064390800_p2955276"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row26597492"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p6913218"><a name="en-us_topic_0064390800_p6913218"></a><a name="en-us_topic_0064390800_p6913218"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p23099752"><a name="en-us_topic_0064390800_p23099752"></a><a name="en-us_topic_0064390800_p23099752"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row6571180"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p62503562"><a name="en-us_topic_0064390800_p62503562"></a><a name="en-us_topic_0064390800_p62503562"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p29623765"><a name="en-us_topic_0064390800_p29623765"></a><a name="en-us_topic_0064390800_p29623765"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390800_row65287294"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390800_p53779479"><a name="en-us_topic_0064390800_p53779479"></a><a name="en-us_topic_0064390800_p53779479"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390800_p61170512"><a name="en-us_topic_0064390800_p61170512"></a><a name="en-us_topic_0064390800_p61170512"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


