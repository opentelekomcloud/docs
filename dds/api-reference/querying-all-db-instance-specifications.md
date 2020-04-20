# Querying All DB Instance Specifications<a name="dds_instance_specification"></a>

## Function<a name="section36902586"></a>

This API is used to query all DB instance specifications in a specified region.

## URI<a name="section63687823"></a>

-   URI format

    GET /v3/\{project\_id\}/flavors?region=\{region\}&engine\_name=\{engine\_name\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table6918001"></a>
    <table><thead align="left"><tr id="row17531178"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p10739296"><a name="p10739296"></a><a name="p10739296"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.2"><p id="p64576684"><a name="p64576684"></a><a name="p64576684"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.24999999999999%" id="mcps1.2.4.1.3"><p id="p63328883"><a name="p63328883"></a><a name="p63328883"></a><strong id="b34664267318"><a name="b34664267318"></a><a name="b34664267318"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29365919"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p29829272"><a name="p29829272"></a><a name="p29829272"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p251973"><a name="p251973"></a><a name="p251973"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p20409871"><a name="p20409871"></a><a name="p20409871"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row41144153615"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p192021597362"><a name="p192021597362"></a><a name="p192021597362"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p4209591362"><a name="p4209591362"></a><a name="p4209591362"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p122138933613"><a name="p122138933613"></a><a name="p122138933613"></a>Specifies the region where the DB instance exists.</p>
    <p id="p721579193612"><a name="p721579193612"></a><a name="p721579193612"></a>Valid value:</p>
    <p id="p1021569163610"><a name="p1021569163610"></a><a name="p1021569163610"></a>The value cannot be empty. For details about how to obtain this parameter value, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    </td>
    </tr>
    <tr id="row13206254366"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p18235698361"><a name="p18235698361"></a><a name="p18235698361"></a>engine_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p172387953613"><a name="p172387953613"></a><a name="p172387953613"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p72411394361"><a name="p72411394361"></a><a name="p72411394361"></a>Specifies the database type. The value is <strong id="b138937353234"><a name="b138937353234"></a><a name="b138937353234"></a>DDS-Community</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="section3074340117316"></a>

-   Request header

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The value of  **region**  in the following is used as an example.  

    ```
    GET https://DDS endpoint/v3/375d8d8fad1f43039e23d3b6c0f60a19/flavors?region=aaa&engine_name=DDS-Community
    ```

-   Request body

    N/A


## Responses<a name="section58440016"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table30427456"></a>
    <table><thead align="left"><tr id="row47542385"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.1"><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.689999999999998%" id="mcps1.2.4.1.2"><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a><strong id="b3231103353117"><a name="b3231103353117"></a><a name="b3231103353117"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10023380"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p6587426"><a name="p6587426"></a><a name="p6587426"></a>flavors</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.689999999999998%" headers="mcps1.2.4.1.2 "><p id="p16243522134212"><a name="p16243522134212"></a><a name="p16243522134212"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p17946858"><a name="p17946858"></a><a name="p17946858"></a>Indicates the DB instance specifications information list. For more information, see <a href="#table64140254">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  flavors field data structure description

    <a name="table64140254"></a>
    <table><thead align="left"><tr id="row21591473"><th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.1"><p id="p4078883"><a name="p4078883"></a><a name="p4078883"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.700000000000003%" id="mcps1.2.4.1.2"><p id="p61954093"><a name="p61954093"></a><a name="p61954093"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.43%" id="mcps1.2.4.1.3"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b16503133419315"><a name="b16503133419315"></a><a name="b16503133419315"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row144161918155712"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p1841691815718"><a name="p1841691815718"></a><a name="p1841691815718"></a>engine_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p3416518155719"><a name="p3416518155719"></a><a name="p3416518155719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p736191365818"><a name="p736191365818"></a><a name="p736191365818"></a>Indicates the engine name.</p>
    </td>
    </tr>
    <tr id="row15504321112612"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p1517492872610"><a name="p1517492872610"></a><a name="p1517492872610"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p617452810260"><a name="p617452810260"></a><a name="p617452810260"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p1717472872612"><a name="p1717472872612"></a><a name="p1717472872612"></a>Indicates the node type. DDS contains the following types of nodes:</p>
    <a name="ul7598411874"></a><a name="ul7598411874"></a><ul id="ul7598411874"><li>mongos</li><li>shard</li><li>config</li><li>replica</li></ul>
    </td>
    </tr>
    <tr id="row23483667"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p141542054152620"><a name="p141542054152620"></a><a name="p141542054152620"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p0154115418263"><a name="p0154115418263"></a><a name="p0154115418263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p1415417549268"><a name="p1415417549268"></a><a name="p1415417549268"></a>Number of vCPUs.</p>
    </td>
    </tr>
    <tr id="row4039073"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p11541554132615"><a name="p11541554132615"></a><a name="p11541554132615"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p18154125472620"><a name="p18154125472620"></a><a name="p18154125472620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p2015414545264"><a name="p2015414545264"></a><a name="p2015414545264"></a>Indicates the memory size in megabytes (MB).</p>
    </td>
    </tr>
    <tr id="row51398059195617"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p131548547269"><a name="p131548547269"></a><a name="p131548547269"></a>spec_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p615410548268"><a name="p615410548268"></a><a name="p615410548268"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p81541954102614"><a name="p81541954102614"></a><a name="p81541954102614"></a>Indicates the resource specifications code.</p>
    <p id="p182201831133114"><a name="p182201831133114"></a><a name="p182201831133114"></a>Example: dds.mongodb.s2.xlarge.4.shard</p>
    <div class="note" id="note91791257947"><a name="note91791257947"></a><a name="note91791257947"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul152321261558"></a><a name="ul152321261558"></a><ul id="ul152321261558"><li><strong id="b2744870"><a name="b2744870"></a><a name="b2744870"></a>dds.mongodb</strong>: indicates the DDS service.</li><li><strong id="b1647793121"><a name="b1647793121"></a><a name="b1647793121"></a>s2.xlarge.4</strong>: indicates the performance specification, which is high memory.</li><li><strong id="b17574134273013"><a name="b17574134273013"></a><a name="b17574134273013"></a>shard</strong>: indicates the node type.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row1648065712261"><td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.1 "><p id="p83951322710"><a name="p83951322710"></a><a name="p83951322710"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.700000000000003%" headers="mcps1.2.4.1.2 "><p id="p964875794315"><a name="p964875794315"></a><a name="p964875794315"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p1639517318272"><a name="p1639517318272"></a><a name="p1639517318272"></a>Indicates the ID of the AZ that supports this specification.</p>
    </td>
    </tr>
    </tbody>
    </table>


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The value of  **availability\_zone**  is used as an example.  

-   Response example

    ```
    {
        "flavors": [
            {
                "engine_name": "DDS-Community",
                "type": "mongos",
                "vcpus": "1",
                "ram": "4",
                "spec_code": "dds.mongodb.s2.medium.4.mongos",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "mongos",
                "vcpus": "2",
                "ram": "8",
                "spec_code": "dds.mongodb.s2.large.4.mongos",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "mongos",
                "vcpus": "4",
                "ram": "16",
                "spec_code": "dds.mongodb.s2.xlarge.4.mongos",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "mongos",
                "vcpus": "8",
                "ram": "32",
                "spec_code": "dds.mongodb.s2.2xlarge.4.mongos",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "mongos",
                "vcpus": "16",
                "ram": "64",
                "spec_code": "dds.mongodb.s2.4xlarge.4.mongos",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "shard",
                "vcpus": "1",
                "ram": "4",
                "spec_code": "dds.mongodb.s2.medium.4.shard",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "shard",
                "vcpus": "2",
                "ram": "8",
                "spec_code": "dds.mongodb.s2.large.4.shard",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "shard",
                "vcpus": "4",
                "ram": "16",
                "spec_code": "dds.mongodb.s2.xlarge.4.shard",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "shard",
                "vcpus": "8",
                "ram": "32",
                "spec_code": "dds.mongodb.s2.2xlarge.4.shard",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "shard",
                "vcpus": "16",
                "ram": "64",
                "spec_code": "dds.mongodb.s2.4xlarge.4.shard",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "config",
                "vcpus": "2",
                "ram": "4",
                "spec_code": "dds.mongodb.s2.large.2.config",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "replica",
                "vcpus": "1",
                "ram": "4",
                "spec_code": "dds.mongodb.s2.medium.4.repset",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "replica",
                "vcpus": "2",
                "ram": "8",
                "spec_code": "dds.mongodb.s2.large.4.repset",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "replica",
                "vcpus": "4",
                "ram": "16",
                "spec_code": "dds.mongodb.s2.xlarge.4.repset",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "replica",
                "vcpus": "8",
                "ram": "32",
                "spec_code": "dds.mongodb.s2.2xlarge.4.repset",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            },
            {
                "engine_name": "DDS-Community",
                "type": "replica",
                "vcpus": "16",
                "ram": "64",
                "spec_code": "dds.mongodb.s2.4xlarge.4.repset",
                "availability_zone": [
                    "eu-de-01",
                    "eu-de-02"
                ]
            }
        ]
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

