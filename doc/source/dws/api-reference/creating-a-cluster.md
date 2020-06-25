# Creating a Cluster<a name="dws_02_0020"></a>

## Function<a name="scd66d518a80c4ea88a94f13aa57bb1e1"></a>

This API is used to create clusters.

The cluster must run in the VPC. Before creating a cluster, you need to create a VPC and obtain the VPC and subnet IDs.

This API is an asynchronous API. It takes 10 to 15 minutes to create a cluster.

## URI<a name="see3b10011fa94758b8bc201af3e10d11"></a>

-   URI format

    POST /v1.0/\{project\_id\}/clusters

-   Parameter description

    **Table  1**  URI parameter description

    <a name="en-us_topic_0067607268_table64754634"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607268_row57662920"><th class="cellrowborder" valign="top" width="19.27%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607268_p40184969"><a name="en-us_topic_0067607268_p40184969"></a><a name="en-us_topic_0067607268_p40184969"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.61%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607268_p33757095"><a name="en-us_topic_0067607268_p33757095"></a><a name="en-us_topic_0067607268_p33757095"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.03%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607268_p49970185"><a name="en-us_topic_0067607268_p49970185"></a><a name="en-us_topic_0067607268_p49970185"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.089999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607268_p21053208"><a name="en-us_topic_0067607268_p21053208"></a><a name="en-us_topic_0067607268_p21053208"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607268_row27588283"><td class="cellrowborder" valign="top" width="19.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p20058459"><a name="en-us_topic_0067607268_p20058459"></a><a name="en-us_topic_0067607268_p20058459"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.61%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p14122463"><a name="en-us_topic_0067607268_p14122463"></a><a name="en-us_topic_0067607268_p14122463"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.03%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p3068848"><a name="en-us_topic_0067607268_p3068848"></a><a name="en-us_topic_0067607268_p3068848"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.089999999999996%" headers="mcps1.2.5.1.4 "><p id="a01f243f2ffbf41ddb83b1f470909e787"><a name="a01f243f2ffbf41ddb83b1f470909e787"></a><a name="a01f243f2ffbf41ddb83b1f470909e787"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s79d3edcb64b244b1bf0f33da4adab8d6"></a>

-   Sample request

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters
    
    {
    "cluster": {
            "node_type": "dws.m1.xlarge.ultrahigh",
            "number_of_node": 3,
            "subnet_id": "374eca02-cfc4-4de7-8ab5-dbebf7d9a720",
            "security_group_id": "dc3ec145-9029-4b39-b5a3-ace5a01f772b",
            "vpc_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574",
            "availability_zone": "eu-de-01",
            "port": 8000,
            "name": "dws-1",
            "user_name": "dbadmin",
            "user_pwd": "Passw0rd!",
            "public_ip": {
                "public_bind_type": "auto_assign",
                "eip_id": ""
            }
        }
    }
    ```


-   Parameter description

    **Table  2**  Request parameter description

    <a name="table55481021436"></a>
    <table><thead align="left"><tr id="row1856312212312"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="p356682238"><a name="p356682238"></a><a name="p356682238"></a><strong id="b84235270617228_1"><a name="b84235270617228_1"></a><a name="b84235270617228_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p75691625316"><a name="p75691625316"></a><a name="p75691625316"></a><strong id="b6167984116271_1"><a name="b6167984116271_1"></a><a name="b6167984116271_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.282828282828287%" id="mcps1.2.5.1.3"><p id="p13572121033"><a name="p13572121033"></a><a name="p13572121033"></a><strong id="b84235270617235_1"><a name="b84235270617235_1"></a><a name="b84235270617235_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.41414141414141%" id="mcps1.2.5.1.4"><p id="p185771721139"><a name="p185771721139"></a><a name="p185771721139"></a><strong id="b842352706172443_1"><a name="b842352706172443_1"></a><a name="b842352706172443_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1758192536"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="p158411211318"><a name="p158411211318"></a><a name="p158411211318"></a>cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p125867218311"><a name="p125867218311"></a><a name="p125867218311"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.2.5.1.3 "><p id="p358810219313"><a name="p358810219313"></a><a name="p358810219313"></a>Object. For details, see <a href="#en-us_topic_0067607268_table20206181">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.41414141414141%" headers="mcps1.2.5.1.4 "><p id="p6591524314"><a name="p6591524314"></a><a name="p6591524314"></a>Cluster object</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Cluster data structure description

    <a name="en-us_topic_0067607268_table20206181"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607268_row50448354"><th class="cellrowborder" valign="top" width="18.911891189118908%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607268_p59784887"><a name="en-us_topic_0067607268_p59784887"></a><a name="en-us_topic_0067607268_p59784887"></a><strong id="b84235270617228_2"><a name="b84235270617228_2"></a><a name="b84235270617228_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.001200120012001%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607268_p10737664"><a name="en-us_topic_0067607268_p10737664"></a><a name="en-us_topic_0067607268_p10737664"></a><strong id="b6167984116271_2"><a name="b6167984116271_2"></a><a name="b6167984116271_2"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.881188118811883%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607268_p64444454"><a name="en-us_topic_0067607268_p64444454"></a><a name="en-us_topic_0067607268_p64444454"></a><strong id="b84235270617235_2"><a name="b84235270617235_2"></a><a name="b84235270617235_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.205720572057196%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607268_p52618256"><a name="en-us_topic_0067607268_p52618256"></a><a name="en-us_topic_0067607268_p52618256"></a><strong id="b842352706172443_2"><a name="b842352706172443_2"></a><a name="b842352706172443_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607268_row5236179"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p21477321"><a name="en-us_topic_0067607268_p21477321"></a><a name="en-us_topic_0067607268_p21477321"></a>node_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p61941440"><a name="en-us_topic_0067607268_p61941440"></a><a name="en-us_topic_0067607268_p61941440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p51200735"><a name="en-us_topic_0067607268_p51200735"></a><a name="en-us_topic_0067607268_p51200735"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p53618895"><a name="en-us_topic_0067607268_p53618895"></a><a name="en-us_topic_0067607268_p53618895"></a>Node type. You can call the <a href="querying-the-supported-node-types.md">Querying the Supported Node Types</a> API to query the node types supported by DWS.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row12808013"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p30816121"><a name="en-us_topic_0067607268_p30816121"></a><a name="en-us_topic_0067607268_p30816121"></a>number_of_node</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p13077833"><a name="en-us_topic_0067607268_p13077833"></a><a name="en-us_topic_0067607268_p13077833"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p52671525"><a name="en-us_topic_0067607268_p52671525"></a><a name="en-us_topic_0067607268_p52671525"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p38535158"><a name="en-us_topic_0067607268_p38535158"></a><a name="en-us_topic_0067607268_p38535158"></a>Number of nodes in a cluster. The value ranges from 3 to 32.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row11272110"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p40625737"><a name="en-us_topic_0067607268_p40625737"></a><a name="en-us_topic_0067607268_p40625737"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p2350413"><a name="en-us_topic_0067607268_p2350413"></a><a name="en-us_topic_0067607268_p2350413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p56165728"><a name="en-us_topic_0067607268_p56165728"></a><a name="en-us_topic_0067607268_p56165728"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p53130157"><a name="en-us_topic_0067607268_p53130157"></a><a name="en-us_topic_0067607268_p53130157"></a>Subnet ID, which is used for configuring cluster network.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row8409368"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p10070188"><a name="en-us_topic_0067607268_p10070188"></a><a name="en-us_topic_0067607268_p10070188"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p10378893"><a name="en-us_topic_0067607268_p10378893"></a><a name="en-us_topic_0067607268_p10378893"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p35383970"><a name="en-us_topic_0067607268_p35383970"></a><a name="en-us_topic_0067607268_p35383970"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p47529299"><a name="en-us_topic_0067607268_p47529299"></a><a name="en-us_topic_0067607268_p47529299"></a>VPC ID, which is used for configuring cluster network.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row25110514"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p20685786"><a name="en-us_topic_0067607268_p20685786"></a><a name="en-us_topic_0067607268_p20685786"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p64935954"><a name="en-us_topic_0067607268_p64935954"></a><a name="en-us_topic_0067607268_p64935954"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p25320898"><a name="en-us_topic_0067607268_p25320898"></a><a name="en-us_topic_0067607268_p25320898"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p37726867"><a name="en-us_topic_0067607268_p37726867"></a><a name="en-us_topic_0067607268_p37726867"></a>ID of a security group. The ID is used for configuring cluster network.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row3997487"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p55361044"><a name="en-us_topic_0067607268_p55361044"></a><a name="en-us_topic_0067607268_p55361044"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="a8fa5700680494e6391d8522ebd60e8cf"><a name="a8fa5700680494e6391d8522ebd60e8cf"></a><a name="a8fa5700680494e6391d8522ebd60e8cf"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p30639779"><a name="en-us_topic_0067607268_p30639779"></a><a name="en-us_topic_0067607268_p30639779"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p65903005"><a name="en-us_topic_0067607268_p65903005"></a><a name="en-us_topic_0067607268_p65903005"></a>AZ of a cluster</p>
    <p id="p172251819145914"><a name="p172251819145914"></a><a name="p172251819145914"></a>For more information about AZs, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
    <a name="u9ab75d376bf1416fbf51f88aff7e454f"></a><a name="u9ab75d376bf1416fbf51f88aff7e454f"></a>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row56256135"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p60453091"><a name="en-us_topic_0067607268_p60453091"></a><a name="en-us_topic_0067607268_p60453091"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p64862199"><a name="en-us_topic_0067607268_p64862199"></a><a name="en-us_topic_0067607268_p64862199"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p19346796"><a name="en-us_topic_0067607268_p19346796"></a><a name="en-us_topic_0067607268_p19346796"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p23586666"><a name="en-us_topic_0067607268_p23586666"></a><a name="en-us_topic_0067607268_p23586666"></a>Cluster name, which must be unique. The cluster name must contain 4 to 64 characters, which consist of letters, digits, hyphens (-), or underscores (_) only and must start with a letter.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row10953403"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p14810456"><a name="en-us_topic_0067607268_p14810456"></a><a name="en-us_topic_0067607268_p14810456"></a>user_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p58796306"><a name="en-us_topic_0067607268_p58796306"></a><a name="en-us_topic_0067607268_p58796306"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p64880336"><a name="en-us_topic_0067607268_p64880336"></a><a name="en-us_topic_0067607268_p64880336"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p20815867"><a name="en-us_topic_0067607268_p20815867"></a><a name="en-us_topic_0067607268_p20815867"></a>Administrator username for logging in to a data warehouse cluster. The administrator username must:</p>
    <a name="en-us_topic_0067607268_ul9129412825"></a><a name="en-us_topic_0067607268_ul9129412825"></a><ul id="en-us_topic_0067607268_ul9129412825"><li>Consist of lowercase letters, digits, or underscores.</li><li>Start with a lowercase letter or an underscore.</li><li>Contain 1 to 63 characters.</li><li>Cannot be a keyword of the DWS database. For details about the keywords of the DWS database, see <a href="https://docs.otc.t-systems.com/en-us/devg/dws/keyword.html" target="_blank" rel="noopener noreferrer">Keyword</a> in the <em id="i9755622115416"><a name="i9755622115416"></a><a name="i9755622115416"></a>Data Warehouse Service Database Developer Guide</em>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row52215961"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p1634435"><a name="en-us_topic_0067607268_p1634435"></a><a name="en-us_topic_0067607268_p1634435"></a>user_pwd</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p65280430"><a name="en-us_topic_0067607268_p65280430"></a><a name="en-us_topic_0067607268_p65280430"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p53223490"><a name="en-us_topic_0067607268_p53223490"></a><a name="en-us_topic_0067607268_p53223490"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p16135397"><a name="en-us_topic_0067607268_p16135397"></a><a name="en-us_topic_0067607268_p16135397"></a>Administrator password for logging in to a data warehouse cluster</p>
    <p id="en-us_topic_0067607268_p11000853"><a name="en-us_topic_0067607268_p11000853"></a><a name="en-us_topic_0067607268_p11000853"></a>A password must conform to the following rules:</p>
    <a name="en-us_topic_0067607268_ul31898818"></a><a name="en-us_topic_0067607268_ul31898818"></a><ul id="en-us_topic_0067607268_ul31898818"><li>Contains 8 to 32 characters. </li><li>Cannot be the same as the username or the username written in reverse order.</li><li>Contains at least three types of the following:<a name="en-us_topic_0067607268_ul34571641"></a><a name="en-us_topic_0067607268_ul34571641"></a><ul id="en-us_topic_0067607268_ul34571641"><li>Lowercase letters</li><li>Uppercase letters</li><li>Digits</li><li>Special characters ~!@#%^&amp;*()-_=+|[{}];:,&lt;.&gt;/?</li></ul>
    </li><li>Cannot be a weak password (for example, <strong id="b02655576258"><a name="b02655576258"></a><a name="b02655576258"></a>Admin123!</strong>).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row36319496"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p56198103"><a name="en-us_topic_0067607268_p56198103"></a><a name="en-us_topic_0067607268_p56198103"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p55752527"><a name="en-us_topic_0067607268_p55752527"></a><a name="en-us_topic_0067607268_p55752527"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p19660823"><a name="en-us_topic_0067607268_p19660823"></a><a name="en-us_topic_0067607268_p19660823"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p49022807"><a name="en-us_topic_0067607268_p49022807"></a><a name="en-us_topic_0067607268_p49022807"></a>Service port of a cluster. The value ranges from 8000 to 10000. The default value is <strong id="b84235270694758"><a name="b84235270694758"></a><a name="b84235270694758"></a>8000</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row38552084"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p35711100"><a name="en-us_topic_0067607268_p35711100"></a><a name="en-us_topic_0067607268_p35711100"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p6918001"><a name="en-us_topic_0067607268_p6918001"></a><a name="en-us_topic_0067607268_p6918001"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p23487194"><a name="en-us_topic_0067607268_p23487194"></a><a name="en-us_topic_0067607268_p23487194"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p23414560"><a name="en-us_topic_0067607268_p23414560"></a><a name="en-us_topic_0067607268_p23414560"></a>Public IP address. If the value is not specified, public connection is not used by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row9404449"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p23562876"><a name="en-us_topic_0067607268_p23562876"></a><a name="en-us_topic_0067607268_p23562876"></a>public_bind_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p29544808"><a name="en-us_topic_0067607268_p29544808"></a><a name="en-us_topic_0067607268_p29544808"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p44319244"><a name="en-us_topic_0067607268_p44319244"></a><a name="en-us_topic_0067607268_p44319244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p33089041"><a name="en-us_topic_0067607268_p33089041"></a><a name="en-us_topic_0067607268_p33089041"></a>Binding type of an elastic IP address (EIP). The value can be either of the following:</p>
    <a name="en-us_topic_0067607268_ul29365919"></a><a name="en-us_topic_0067607268_ul29365919"></a><ul id="en-us_topic_0067607268_ul29365919"><li><strong id="b842352706174142"><a name="b842352706174142"></a><a name="b842352706174142"></a>auto_assign</strong></li><li><strong id="b842352706174712"><a name="b842352706174712"></a><a name="b842352706174712"></a>not_use</strong></li><li><strong id="b842352706162651"><a name="b842352706162651"></a><a name="b842352706162651"></a>bind_existing</strong></li></ul>
    <p id="en-us_topic_0067607268_p27997"><a name="en-us_topic_0067607268_p27997"></a><a name="en-us_topic_0067607268_p27997"></a>The default value is <strong id="b842352706141151"><a name="b842352706141151"></a><a name="b842352706141151"></a>not_use</strong>. </p>
    </td>
    </tr>
    <tr id="r4ef91cfde5804ca9a3117fdd7e0957f0"><td class="cellrowborder" valign="top" width="18.911891189118908%" headers="mcps1.2.5.1.1 "><p id="acd674841af7e47f182689ec4526dc28a"><a name="acd674841af7e47f182689ec4526dc28a"></a><a name="acd674841af7e47f182689ec4526dc28a"></a>eip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.001200120012001%" headers="mcps1.2.5.1.2 "><p id="ac14f2f32e0504a2b9c938e4ed1dd8d55"><a name="ac14f2f32e0504a2b9c938e4ed1dd8d55"></a><a name="ac14f2f32e0504a2b9c938e4ed1dd8d55"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811883%" headers="mcps1.2.5.1.3 "><p id="af270c9c3a0284ba6b87ad04b1b61de3e"><a name="af270c9c3a0284ba6b87ad04b1b61de3e"></a><a name="af270c9c3a0284ba6b87ad04b1b61de3e"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.205720572057196%" headers="mcps1.2.5.1.4 "><p id="a6abf2e07b9f2476ca2c87f4bfcc35e02"><a name="a6abf2e07b9f2476ca2c87f4bfcc35e02"></a><a name="a6abf2e07b9f2476ca2c87f4bfcc35e02"></a>EIP ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="s14151e40166b47bd9bc6be63c13728d2"></a>

-   Sample response

    ```
    {
        "cluster": {
            "id": "7d85f602-a948-4a30-afd4-e84f47471c15"
         }
    }
    ```


-   Parameter description

    **Table  4**  Response parameter description

    <a name="en-us_topic_0067607268_table66373591"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607268_row53780604"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607268_p61261645"><a name="en-us_topic_0067607268_p61261645"></a><a name="en-us_topic_0067607268_p61261645"></a><strong id="b84235270617228_3"><a name="b84235270617228_3"></a><a name="b84235270617228_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.08869113088691%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607268_p63246244"><a name="en-us_topic_0067607268_p63246244"></a><a name="en-us_topic_0067607268_p63246244"></a><strong id="b6167984116271_3"><a name="b6167984116271_3"></a><a name="b6167984116271_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.358764123587642%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607268_p22672102"><a name="en-us_topic_0067607268_p22672102"></a><a name="en-us_topic_0067607268_p22672102"></a><strong id="b84235270617235_3"><a name="b84235270617235_3"></a><a name="b84235270617235_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.164483551644835%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607268_p24500989"><a name="en-us_topic_0067607268_p24500989"></a><a name="en-us_topic_0067607268_p24500989"></a><strong id="b842352706172443_3"><a name="b842352706172443_3"></a><a name="b842352706172443_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607268_row38423121"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p25265097"><a name="en-us_topic_0067607268_p25265097"></a><a name="en-us_topic_0067607268_p25265097"></a>cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.08869113088691%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p33206990"><a name="en-us_topic_0067607268_p33206990"></a><a name="en-us_topic_0067607268_p33206990"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.358764123587642%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p5411655"><a name="en-us_topic_0067607268_p5411655"></a><a name="en-us_topic_0067607268_p5411655"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.164483551644835%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p35690909"><a name="en-us_topic_0067607268_p35690909"></a><a name="en-us_topic_0067607268_p35690909"></a>Cluster object</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row52782726"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607268_p47542385"><a name="en-us_topic_0067607268_p47542385"></a><a name="en-us_topic_0067607268_p47542385"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.08869113088691%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607268_p25727981"><a name="en-us_topic_0067607268_p25727981"></a><a name="en-us_topic_0067607268_p25727981"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.358764123587642%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607268_p3591713"><a name="en-us_topic_0067607268_p3591713"></a><a name="en-us_topic_0067607268_p3591713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.164483551644835%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607268_p22493366"><a name="en-us_topic_0067607268_p22493366"></a><a name="en-us_topic_0067607268_p22493366"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="sfffefcf1591c452c87cf83b0cf1ac573"></a>

-   Normal

    200

-   Abnormal 

    **Table  5**  Returned value description

    <a name="en-us_topic_0067607268_table27978103"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607268_row60105532"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0067607268_p36709949"><a name="en-us_topic_0067607268_p36709949"></a><a name="en-us_topic_0067607268_p36709949"></a><strong id="b84235270695033"><a name="b84235270695033"></a><a name="b84235270695033"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0067607268_p20715931"><a name="en-us_topic_0067607268_p20715931"></a><a name="en-us_topic_0067607268_p20715931"></a><strong id="b842352706172443_4"><a name="b842352706172443_4"></a><a name="b842352706172443_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607268_row268861"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p21777804"><a name="en-us_topic_0067607268_p21777804"></a><a name="en-us_topic_0067607268_p21777804"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p19171695"><a name="en-us_topic_0067607268_p19171695"></a><a name="en-us_topic_0067607268_p19171695"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row38327532"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p17522377"><a name="en-us_topic_0067607268_p17522377"></a><a name="en-us_topic_0067607268_p17522377"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p10026414"><a name="en-us_topic_0067607268_p10026414"></a><a name="en-us_topic_0067607268_p10026414"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row23128868"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p61498985"><a name="en-us_topic_0067607268_p61498985"></a><a name="en-us_topic_0067607268_p61498985"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p15361866"><a name="en-us_topic_0067607268_p15361866"></a><a name="en-us_topic_0067607268_p15361866"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row4039073"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p58729529"><a name="en-us_topic_0067607268_p58729529"></a><a name="en-us_topic_0067607268_p58729529"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p59471393"><a name="en-us_topic_0067607268_p59471393"></a><a name="en-us_topic_0067607268_p59471393"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row65480490"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p2319502"><a name="en-us_topic_0067607268_p2319502"></a><a name="en-us_topic_0067607268_p2319502"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p53661974"><a name="en-us_topic_0067607268_p53661974"></a><a name="en-us_topic_0067607268_p53661974"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607268_row13195723"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607268_p62220677"><a name="en-us_topic_0067607268_p62220677"></a><a name="en-us_topic_0067607268_p62220677"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607268_p6710104"><a name="en-us_topic_0067607268_p6710104"></a><a name="en-us_topic_0067607268_p6710104"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


