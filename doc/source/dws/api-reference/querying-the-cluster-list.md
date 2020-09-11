# Querying the Cluster List<a name="dws_02_0018"></a>

## Function<a name="s7824f9daa8b546c086192e45721e6e61"></a>

This API is used to query and display the cluster list.

## URI<a name="s18625cd3bdc8450a85dc8bff5ee9c3ab"></a>

-   URI format

    GET /v1.0/\{project\_id\}/clusters

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t575c11e12d424496a5ee5f1e21aed0eb"></a>
    <table><thead align="left"><tr id="r1ae71c4bc7904106878ea7fc6f67ceac"><th class="cellrowborder" valign="top" width="21.059405940594058%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607266_p233791391059"><a name="en-us_topic_0067607266_p233791391059"></a><a name="en-us_topic_0067607266_p233791391059"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.99009900990099%" id="mcps1.2.5.1.2"><p id="a0cfb8bbe0a624f0585b5905a7a8f6600"><a name="a0cfb8bbe0a624f0585b5905a7a8f6600"></a><a name="a0cfb8bbe0a624f0585b5905a7a8f6600"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.405940594059405%" id="mcps1.2.5.1.3"><p id="a7d75ef22fef942ed8e6357de65c2879c"><a name="a7d75ef22fef942ed8e6357de65c2879c"></a><a name="a7d75ef22fef942ed8e6357de65c2879c"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.54455445544554%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607266_p950656191059"><a name="en-us_topic_0067607266_p950656191059"></a><a name="en-us_topic_0067607266_p950656191059"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r88e41a45586c4939ae2395e9731deb6a"><td class="cellrowborder" valign="top" width="21.059405940594058%" headers="mcps1.2.5.1.1 "><p id="ac6422b195ec240799d22e1a6fcf10499"><a name="ac6422b195ec240799d22e1a6fcf10499"></a><a name="ac6422b195ec240799d22e1a6fcf10499"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.99009900990099%" headers="mcps1.2.5.1.2 "><p id="abf13274928fc48beb46904e9db935097"><a name="abf13274928fc48beb46904e9db935097"></a><a name="abf13274928fc48beb46904e9db935097"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.405940594059405%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p810473491059"><a name="en-us_topic_0067607266_p810473491059"></a><a name="en-us_topic_0067607266_p810473491059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54455445544554%" headers="mcps1.2.5.1.4 "><p id="p7395111105411"><a name="p7395111105411"></a><a name="p7395111105411"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sf43e64a4061d416caee22c19f8bb1c47"></a>

Sample request

```
GET /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters
```

## Response<a name="s4a3e14e14b2e46c08af2238496ee149d"></a>

-   Sample response

    ```
    {
            "clusters": [
            {
            "id": "7d85f602-a948-4a30-afd4-e84f47471c15",
            "status": "AVAILABLE",
            "sub_status": "READONLY",            
            "task_status": "SNAPSHOTTING",
            "action_progress": {"SNAPSHOTTING": "20%"},
            "node_type": "dws.m1.xlarge.ultrahigh",
            "subnet_id": "374eca02-cfc4-4de7-8ab5-dbebf7d9a720",
            "security_group_id": "dc3ec145-9029-4b39-b5a3-ace5a01f772b",
            "number_of_node": 3,
            "availability_zone": "eu-de-01",
            "port": 8000,
            "name": "dws-1",
            "version": "1.2.0",
            "vpc_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574",
            "user_name": "dbadmin",
            "public_ip": {
                "public_bind_type": "auto_assign",
                "eip_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574"
             },
            "public_endpoints": [
                {
                    "public_connect_info": "10.0.0.8:8000",
                    "jdbc_url": "jdbc:postgresql://10.0.0.8:8000/<YOUR_DATABASE_NAME>"
                }
             ],
            "endpoints": [
                {
                    "connect_info": "192.168.0.12:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.12:8000/<YOUR_DATABASE_NAME>"
                },
                {
                    "connect_info": "192.168.0.12:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.12:8000/<YOUR_DATABASE_NAME>"
                }
             ] , 
            "updated": "2016-02-10T14:28:14Z",
            "created": "2016-02-10T14:26:14Z"
            }
        ]
    }
    ```


-   Parameter description

    **Table  2**  Response parameter description

    <a name="en-us_topic_0067607266_table14008765"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607266_row53729511"><th class="cellrowborder" valign="top" width="21.39%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607266_p57123120"><a name="en-us_topic_0067607266_p57123120"></a><a name="en-us_topic_0067607266_p57123120"></a><strong id="b1093308636"><a name="b1093308636"></a><a name="b1093308636"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.299999999999999%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607266_p63570006"><a name="en-us_topic_0067607266_p63570006"></a><a name="en-us_topic_0067607266_p63570006"></a><strong id="b288721438"><a name="b288721438"></a><a name="b288721438"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607266_p48896832"><a name="en-us_topic_0067607266_p48896832"></a><a name="en-us_topic_0067607266_p48896832"></a><strong id="b1348250329"><a name="b1348250329"></a><a name="b1348250329"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.440000000000005%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607266_p1220438"><a name="en-us_topic_0067607266_p1220438"></a><a name="en-us_topic_0067607266_p1220438"></a><strong id="b561961905"><a name="b561961905"></a><a name="b561961905"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607266_row31746690"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p21345065"><a name="en-us_topic_0067607266_p21345065"></a><a name="en-us_topic_0067607266_p21345065"></a>clusters</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p51228725"><a name="en-us_topic_0067607266_p51228725"></a><a name="en-us_topic_0067607266_p51228725"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p55886094"><a name="en-us_topic_0067607266_p55886094"></a><a name="en-us_topic_0067607266_p55886094"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p30479771"><a name="en-us_topic_0067607266_p30479771"></a><a name="en-us_topic_0067607266_p30479771"></a>List of cluster objects</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row5882489"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p6719600"><a name="en-us_topic_0067607266_p6719600"></a><a name="en-us_topic_0067607266_p6719600"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p7416719"><a name="en-us_topic_0067607266_p7416719"></a><a name="en-us_topic_0067607266_p7416719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p63883391"><a name="en-us_topic_0067607266_p63883391"></a><a name="en-us_topic_0067607266_p63883391"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p7172200"><a name="en-us_topic_0067607266_p7172200"></a><a name="en-us_topic_0067607266_p7172200"></a>Cluster ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row64549801"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p61151353"><a name="en-us_topic_0067607266_p61151353"></a><a name="en-us_topic_0067607266_p61151353"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p54312533"><a name="en-us_topic_0067607266_p54312533"></a><a name="en-us_topic_0067607266_p54312533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p37239078"><a name="en-us_topic_0067607266_p37239078"></a><a name="en-us_topic_0067607266_p37239078"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p63575380"><a name="en-us_topic_0067607266_p63575380"></a><a name="en-us_topic_0067607266_p63575380"></a>Cluster status, which can be one of the following:</p>
    <a name="en-us_topic_0067607266_ul35307513"></a><a name="en-us_topic_0067607266_ul35307513"></a><ul id="en-us_topic_0067607266_ul35307513"><li><strong id="b842352706152546"><a name="b842352706152546"></a><a name="b842352706152546"></a>CREATING</strong></li><li><strong id="b335382630162424"><a name="b335382630162424"></a><a name="b335382630162424"></a>AVAILABLE</strong></li><li><strong id="b842352706162411"><a name="b842352706162411"></a><a name="b842352706162411"></a>UNAVAILABLE</strong></li><li><strong>CREATION FAILED</strong></li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row51692872"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p26373084"><a name="en-us_topic_0067607266_p26373084"></a><a name="en-us_topic_0067607266_p26373084"></a>sub_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p55845053"><a name="en-us_topic_0067607266_p55845053"></a><a name="en-us_topic_0067607266_p55845053"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p27155410"><a name="en-us_topic_0067607266_p27155410"></a><a name="en-us_topic_0067607266_p27155410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p52104579"><a name="en-us_topic_0067607266_p52104579"></a><a name="en-us_topic_0067607266_p52104579"></a>Sub-status of clusters in the <strong id="b1341008343162427"><a name="b1341008343162427"></a><a name="b1341008343162427"></a>AVAILABLE</strong> state. The value can be one of the following:</p>
    <a name="en-us_topic_0067607266_ul66288034"></a><a name="en-us_topic_0067607266_ul66288034"></a><ul id="en-us_topic_0067607266_ul66288034"><li><strong id="b842352706172235"><a name="b842352706172235"></a><a name="b842352706172235"></a>NORMAL</strong></li><li><strong id="b843639795172048"><a name="b843639795172048"></a><a name="b843639795172048"></a>READONLY</strong></li><li><strong id="b842352706172246"><a name="b842352706172246"></a><a name="b842352706172246"></a>REDISTRIBUTING</strong></li><li><strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706172339"><a name="b842352706172339"></a><a name="b842352706172339"></a>UNBALANCED</strong></li><li><strong id="b842352706172359"><a name="b842352706172359"></a><a name="b842352706172359"></a>UNBALANCED | READONLY</strong></li><li><strong id="b842352706172436"><a name="b842352706172436"></a><a name="b842352706172436"></a>DEGRADED</strong></li><li><strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>DEGRADED | READONLY</strong></li><li><strong id="b842352706172721"><a name="b842352706172721"></a><a name="b842352706172721"></a>DEGRADED | UNBALANCED</strong></li><li><strong id="b842352706172755"><a name="b842352706172755"></a><a name="b842352706172755"></a>UNBALANCED | REDISTRIBUTING</strong></li><li><strong id="b84235270617297"><a name="b84235270617297"></a><a name="b84235270617297"></a>UNBALANCED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706172941"><a name="b842352706172941"></a><a name="b842352706172941"></a>READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706162513"><a name="b842352706162513"></a><a name="b842352706162513"></a>UNBALANCED | READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706173050"><a name="b842352706173050"></a><a name="b842352706173050"></a>DEGRADED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b84235270615284"><a name="b84235270615284"></a><a name="b84235270615284"></a>DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706173010"><a name="b842352706173010"></a><a name="b842352706173010"></a>DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b1015743183"><a name="b1015743183"></a><a name="b1015743183"></a>DEGRADED | UNBALANCED | READONLY</strong></li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row3094327"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p49313939"><a name="en-us_topic_0067607266_p49313939"></a><a name="en-us_topic_0067607266_p49313939"></a>task_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p35006119"><a name="en-us_topic_0067607266_p35006119"></a><a name="en-us_topic_0067607266_p35006119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p16923420"><a name="en-us_topic_0067607266_p16923420"></a><a name="en-us_topic_0067607266_p16923420"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p28619802"><a name="en-us_topic_0067607266_p28619802"></a><a name="en-us_topic_0067607266_p28619802"></a>Cluster management task. The value can be one of the following:</p>
    <a name="en-us_topic_0067607266_ul56251627"></a><a name="en-us_topic_0067607266_ul56251627"></a><ul id="en-us_topic_0067607266_ul56251627"><li><strong id="b842352706173523"><a name="b842352706173523"></a><a name="b842352706173523"></a>RESTORING</strong></li><li><strong id="b842352706173540"><a name="b842352706173540"></a><a name="b842352706173540"></a>SNAPSHOTTING</strong></li><li><strong id="b84235270617363"><a name="b84235270617363"></a><a name="b84235270617363"></a>GROWING</strong></li><li><strong id="b842352706173642"><a name="b842352706173642"></a><a name="b842352706173642"></a>REBOOTING</strong></li><li><strong id="b842352706164634"><a name="b842352706164634"></a><a name="b842352706164634"></a>SETTING_CONFIGURATION</strong></li><li><strong id="b842352706164641"><a name="b842352706164641"></a><a name="b842352706164641"></a>CONFIGURING_EXT_DATASOURCE</strong></li><li><strong id="b842352706164649"><a name="b842352706164649"></a><a name="b842352706164649"></a>DELETING_EXT_DATASOURCE</strong></li><li><strong id="b842352706173725"><a name="b842352706173725"></a><a name="b842352706173725"></a>REBOOT_FAILURE</strong></li><li><strong id="b842352706162543"><a name="b842352706162543"></a><a name="b842352706162543"></a>RESIZE_FAILURE</strong></li></ul>
    </td>
    </tr>
    <tr id="row5778134152514"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="p13779163419259"><a name="p13779163419259"></a><a name="p13779163419259"></a>action_progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="p8780103422513"><a name="p8780103422513"></a><a name="p8780103422513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p878003482510"><a name="p878003482510"></a><a name="p878003482510"></a>Map</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p114351910121614"><a name="p114351910121614"></a><a name="p114351910121614"></a>The key indicates the ongoing task, and the value indicates the progress of the ongoing task.</p>
    <p id="p20780434172512"><a name="p20780434172512"></a><a name="p20780434172512"></a>Valid key values include:</p>
    <a name="ul1958205713298"></a><a name="ul1958205713298"></a><ul id="ul1958205713298"><li><strong id="b713600949"><a name="b713600949"></a><a name="b713600949"></a>GROWING</strong></li><li><strong id="b2121341199"><a name="b2121341199"></a><a name="b2121341199"></a>RESTORING</strong></li><li><strong id="b334992627"><a name="b334992627"></a><a name="b334992627"></a>SNAPSHOTTING</strong></li><li><strong id="b84235270611057"><a name="b84235270611057"></a><a name="b84235270611057"></a>REPAIRING</strong></li><li><strong id="b8423527061114"><a name="b8423527061114"></a><a name="b8423527061114"></a>GREATING</strong></li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row39516413"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p46712854"><a name="en-us_topic_0067607266_p46712854"></a><a name="en-us_topic_0067607266_p46712854"></a>node_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p25644791"><a name="en-us_topic_0067607266_p25644791"></a><a name="en-us_topic_0067607266_p25644791"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p63962185"><a name="en-us_topic_0067607266_p63962185"></a><a name="en-us_topic_0067607266_p63962185"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p13554483"><a name="en-us_topic_0067607266_p13554483"></a><a name="en-us_topic_0067607266_p13554483"></a>Node type</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row54881489"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p16215635"><a name="en-us_topic_0067607266_p16215635"></a><a name="en-us_topic_0067607266_p16215635"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p38398082"><a name="en-us_topic_0067607266_p38398082"></a><a name="en-us_topic_0067607266_p38398082"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p23236933"><a name="en-us_topic_0067607266_p23236933"></a><a name="en-us_topic_0067607266_p23236933"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p3143429"><a name="en-us_topic_0067607266_p3143429"></a><a name="en-us_topic_0067607266_p3143429"></a>Subnet ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row28290863"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p9858548"><a name="en-us_topic_0067607266_p9858548"></a><a name="en-us_topic_0067607266_p9858548"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p60344938"><a name="en-us_topic_0067607266_p60344938"></a><a name="en-us_topic_0067607266_p60344938"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p56101816"><a name="en-us_topic_0067607266_p56101816"></a><a name="en-us_topic_0067607266_p56101816"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p47953287"><a name="en-us_topic_0067607266_p47953287"></a><a name="en-us_topic_0067607266_p47953287"></a>ID of a security group</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row28926407"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p61337593"><a name="en-us_topic_0067607266_p61337593"></a><a name="en-us_topic_0067607266_p61337593"></a>number_of_node</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p2289152"><a name="en-us_topic_0067607266_p2289152"></a><a name="en-us_topic_0067607266_p2289152"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p51203652"><a name="en-us_topic_0067607266_p51203652"></a><a name="en-us_topic_0067607266_p51203652"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p53855148"><a name="en-us_topic_0067607266_p53855148"></a><a name="en-us_topic_0067607266_p53855148"></a>Number of nodes</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row14934289"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p1717931"><a name="en-us_topic_0067607266_p1717931"></a><a name="en-us_topic_0067607266_p1717931"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p4934750"><a name="en-us_topic_0067607266_p4934750"></a><a name="en-us_topic_0067607266_p4934750"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p64170449"><a name="en-us_topic_0067607266_p64170449"></a><a name="en-us_topic_0067607266_p64170449"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p30423852"><a name="en-us_topic_0067607266_p30423852"></a><a name="en-us_topic_0067607266_p30423852"></a>AZ</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row5379216"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p33063388"><a name="en-us_topic_0067607266_p33063388"></a><a name="en-us_topic_0067607266_p33063388"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p60888739"><a name="en-us_topic_0067607266_p60888739"></a><a name="en-us_topic_0067607266_p60888739"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p33040847"><a name="en-us_topic_0067607266_p33040847"></a><a name="en-us_topic_0067607266_p33040847"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p59062984"><a name="en-us_topic_0067607266_p59062984"></a><a name="en-us_topic_0067607266_p59062984"></a>Service port of a cluster (8000 to 10000). The default value is <strong id="b84235270694758"><a name="b84235270694758"></a><a name="b84235270694758"></a>8000</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row61804813"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p40133923"><a name="en-us_topic_0067607266_p40133923"></a><a name="en-us_topic_0067607266_p40133923"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p29622330"><a name="en-us_topic_0067607266_p29622330"></a><a name="en-us_topic_0067607266_p29622330"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p50598521"><a name="en-us_topic_0067607266_p50598521"></a><a name="en-us_topic_0067607266_p50598521"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p4839561"><a name="en-us_topic_0067607266_p4839561"></a><a name="en-us_topic_0067607266_p4839561"></a>Cluster name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row43556055"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p38379555"><a name="en-us_topic_0067607266_p38379555"></a><a name="en-us_topic_0067607266_p38379555"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p21736211"><a name="en-us_topic_0067607266_p21736211"></a><a name="en-us_topic_0067607266_p21736211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p15802639"><a name="en-us_topic_0067607266_p15802639"></a><a name="en-us_topic_0067607266_p15802639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p4945408"><a name="en-us_topic_0067607266_p4945408"></a><a name="en-us_topic_0067607266_p4945408"></a>Data warehouse version</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row44508680"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p48433347"><a name="en-us_topic_0067607266_p48433347"></a><a name="en-us_topic_0067607266_p48433347"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p30787047"><a name="en-us_topic_0067607266_p30787047"></a><a name="en-us_topic_0067607266_p30787047"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p10722842"><a name="en-us_topic_0067607266_p10722842"></a><a name="en-us_topic_0067607266_p10722842"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p63243911"><a name="en-us_topic_0067607266_p63243911"></a><a name="en-us_topic_0067607266_p63243911"></a>VPC ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row32324290"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p1021814"><a name="en-us_topic_0067607266_p1021814"></a><a name="en-us_topic_0067607266_p1021814"></a>user_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p15658103"><a name="en-us_topic_0067607266_p15658103"></a><a name="en-us_topic_0067607266_p15658103"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p60346796"><a name="en-us_topic_0067607266_p60346796"></a><a name="en-us_topic_0067607266_p60346796"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p56252285"><a name="en-us_topic_0067607266_p56252285"></a><a name="en-us_topic_0067607266_p56252285"></a>Username of the administrator</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row36508524"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p4400500"><a name="en-us_topic_0067607266_p4400500"></a><a name="en-us_topic_0067607266_p4400500"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p20896204"><a name="en-us_topic_0067607266_p20896204"></a><a name="en-us_topic_0067607266_p20896204"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p14870940"><a name="en-us_topic_0067607266_p14870940"></a><a name="en-us_topic_0067607266_p14870940"></a>Object. For details, see <a href="#table15507042124119">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p63695501"><a name="en-us_topic_0067607266_p63695501"></a><a name="en-us_topic_0067607266_p63695501"></a>Public IP address. If the value is not specified, public connection is not used by default.</p>
    </td>
    </tr>
    <tr id="row183742016163819"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="p203755169388"><a name="p203755169388"></a><a name="p203755169388"></a>public_endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="p1337617161389"><a name="p1337617161389"></a><a name="p1337617161389"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p143765163383"><a name="p143765163383"></a><a name="p143765163383"></a>Array. For details, see <a href="#table5772171165019">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p1376191610387"><a name="p1376191610387"></a><a name="p1376191610387"></a>Public network connection information about the cluster. If the value is not specified, the public network connection information is not used by default.</p>
    </td>
    </tr>
    <tr id="row17306172684414"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="p163072026124416"><a name="p163072026124416"></a><a name="p163072026124416"></a>endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="p1430812263445"><a name="p1430812263445"></a><a name="p1430812263445"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p630912614445"><a name="p630912614445"></a><a name="p630912614445"></a>Array. For details, see <a href="#table467420155524">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p13331226114418"><a name="p13331226114418"></a><a name="p13331226114418"></a>Private network connection information about the cluster</p>
    </td>
    </tr>
    <tr id="row793319516303"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="p1993325110305"><a name="p1993325110305"></a><a name="p1993325110305"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="p39342517306"><a name="p39342517306"></a><a name="p39342517306"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p7935551123010"><a name="p7935551123010"></a><a name="p7935551123010"></a>Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p10935205119307"><a name="p10935205119307"></a><a name="p10935205119307"></a>Last modification time of a cluster. The format is <strong id="b842352706174936"><a name="b842352706174936"></a><a name="b842352706174936"></a>ISO8601:YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row13072760"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607266_p52260639"><a name="en-us_topic_0067607266_p52260639"></a><a name="en-us_topic_0067607266_p52260639"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607266_p5253358"><a name="en-us_topic_0067607266_p5253358"></a><a name="en-us_topic_0067607266_p5253358"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607266_p22868878"><a name="en-us_topic_0067607266_p22868878"></a><a name="en-us_topic_0067607266_p22868878"></a>Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607266_p40439847"><a name="en-us_topic_0067607266_p40439847"></a><a name="en-us_topic_0067607266_p40439847"></a>Cluster creation time. The format is <strong id="b842352706174833"><a name="b842352706174833"></a><a name="b842352706174833"></a>ISO8601:YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="r61e6d9fd9e9541e8819d56432ee0b3d4"><td class="cellrowborder" valign="top" width="21.39%" headers="mcps1.2.5.1.1 "><p id="a18ac79d883914ae4b7d6c90075a40d3d"><a name="a18ac79d883914ae4b7d6c90075a40d3d"></a><a name="a18ac79d883914ae4b7d6c90075a40d3d"></a>failed_reasons</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.299999999999999%" headers="mcps1.2.5.1.2 "><p id="a840f7eae8f4c41589b9064965dc83229"><a name="a840f7eae8f4c41589b9064965dc83229"></a><a name="a840f7eae8f4c41589b9064965dc83229"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="a0e16b35c825941d3b76f226088695983"><a name="a0e16b35c825941d3b76f226088695983"></a><a name="a0e16b35c825941d3b76f226088695983"></a>Object. For details, see <a href="#table34501136155716">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="ab381a4f749554738b6eba09c464edc7e"><a name="ab381a4f749554738b6eba09c464edc7e"></a><a name="ab381a4f749554738b6eba09c464edc7e"></a>Cause of failure. If the value is empty, the cluster is in the normal state.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **public\_ip**  field data structure description

    <a name="table15507042124119"></a>
    <table><thead align="left"><tr id="row150744214110"><th class="cellrowborder" valign="top" width="21.484848484848484%" id="mcps1.2.5.1.1"><p id="p145079427411"><a name="p145079427411"></a><a name="p145079427411"></a><strong id="b84235270611710"><a name="b84235270611710"></a><a name="b84235270611710"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.444444444444443%" id="mcps1.2.5.1.2"><p id="p950718422411"><a name="p950718422411"></a><a name="p950718422411"></a><strong id="b348294490"><a name="b348294490"></a><a name="b348294490"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.939393939393938%" id="mcps1.2.5.1.3"><p id="p14507542124112"><a name="p14507542124112"></a><a name="p14507542124112"></a><strong id="b1689447909"><a name="b1689447909"></a><a name="b1689447909"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.13131313131313%" id="mcps1.2.5.1.4"><p id="p75071742174116"><a name="p75071742174116"></a><a name="p75071742174116"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1750774215416"><td class="cellrowborder" valign="top" width="21.484848484848484%" headers="mcps1.2.5.1.1 "><p id="p16507144274111"><a name="p16507144274111"></a><a name="p16507144274111"></a>public_bind_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.444444444444443%" headers="mcps1.2.5.1.2 "><p id="p550744210417"><a name="p550744210417"></a><a name="p550744210417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.939393939393938%" headers="mcps1.2.5.1.3 "><p id="p1507134216412"><a name="p1507134216412"></a><a name="p1507134216412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.13131313131313%" headers="mcps1.2.5.1.4 "><p id="p247316414714"><a name="p247316414714"></a><a name="p247316414714"></a>Binding type of an EIP. The value can be either of the following:</p>
    <a name="ul1247384124715"></a><a name="ul1247384124715"></a><ul id="ul1247384124715"><li><strong id="b842352706174142"><a name="b842352706174142"></a><a name="b842352706174142"></a>auto_assign</strong></li><li><strong id="b842352706174712"><a name="b842352706174712"></a><a name="b842352706174712"></a>not_use</strong></li><li><strong id="b842352706162651"><a name="b842352706162651"></a><a name="b842352706162651"></a>bind_existing</strong></li></ul>
    </td>
    </tr>
    <tr id="row850712429411"><td class="cellrowborder" valign="top" width="21.484848484848484%" headers="mcps1.2.5.1.1 "><p id="p18507134264119"><a name="p18507134264119"></a><a name="p18507134264119"></a>eip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.444444444444443%" headers="mcps1.2.5.1.2 "><p id="p10507204204120"><a name="p10507204204120"></a><a name="p10507204204120"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.939393939393938%" headers="mcps1.2.5.1.3 "><p id="p14507242154118"><a name="p14507242154118"></a><a name="p14507242154118"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.13131313131313%" headers="mcps1.2.5.1.4 "><p id="p750724234115"><a name="p750724234115"></a><a name="p750724234115"></a>EIP ID</p>
    </td>
    </tr>
    <tr id="row14840164924515"><td class="cellrowborder" valign="top" width="21.484848484848484%" headers="mcps1.2.5.1.1 "><p id="p128409498454"><a name="p128409498454"></a><a name="p128409498454"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.444444444444443%" headers="mcps1.2.5.1.2 "><p id="p084004924518"><a name="p084004924518"></a><a name="p084004924518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.939393939393938%" headers="mcps1.2.5.1.3 "><p id="p14840134924514"><a name="p14840134924514"></a><a name="p14840134924514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.13131313131313%" headers="mcps1.2.5.1.4 "><p id="p1687915486474"><a name="p1687915486474"></a><a name="p1687915486474"></a>EIP binding status. An optional value is <strong id="b84235270614758"><a name="b84235270614758"></a><a name="b84235270614758"></a>FAIL</strong> (binding fails).</p>
    </td>
    </tr>
    <tr id="row39815538457"><td class="cellrowborder" valign="top" width="21.484848484848484%" headers="mcps1.2.5.1.1 "><p id="p1498119534452"><a name="p1498119534452"></a><a name="p1498119534452"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.444444444444443%" headers="mcps1.2.5.1.2 "><p id="p1298135324510"><a name="p1298135324510"></a><a name="p1298135324510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.939393939393938%" headers="mcps1.2.5.1.3 "><p id="p098113533450"><a name="p098113533450"></a><a name="p098113533450"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.13131313131313%" headers="mcps1.2.5.1.4 "><p id="p11981165315456"><a name="p11981165315456"></a><a name="p11981165315456"></a>Cause of an EIP binding failure</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **public\_endpoints**  field data structure description

    <a name="table5772171165019"></a>
    <table><thead align="left"><tr id="row5772171135012"><th class="cellrowborder" valign="top" width="21.059405940594058%" id="mcps1.2.5.1.1"><p id="p4772516508"><a name="p4772516508"></a><a name="p4772516508"></a><strong id="b2110334185"><a name="b2110334185"></a><a name="b2110334185"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.87128712871287%" id="mcps1.2.5.1.2"><p id="p147726105013"><a name="p147726105013"></a><a name="p147726105013"></a><strong id="b757664086"><a name="b757664086"></a><a name="b757664086"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.03960396039604%" id="mcps1.2.5.1.3"><p id="p1077231115011"><a name="p1077231115011"></a><a name="p1077231115011"></a><strong id="b2142242984"><a name="b2142242984"></a><a name="b2142242984"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.02970297029702%" id="mcps1.2.5.1.4"><p id="p1577210111500"><a name="p1577210111500"></a><a name="p1577210111500"></a><strong id="b480357003"><a name="b480357003"></a><a name="b480357003"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27729116505"><td class="cellrowborder" valign="top" width="21.059405940594058%" headers="mcps1.2.5.1.1 "><p id="p107727116509"><a name="p107727116509"></a><a name="p107727116509"></a>public_connect_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87128712871287%" headers="mcps1.2.5.1.2 "><p id="p1277220135015"><a name="p1277220135015"></a><a name="p1277220135015"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.03960396039604%" headers="mcps1.2.5.1.3 "><p id="p377216185014"><a name="p377216185014"></a><a name="p377216185014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.02970297029702%" headers="mcps1.2.5.1.4 "><p id="p57721812505"><a name="p57721812505"></a><a name="p57721812505"></a>Public network connection information</p>
    </td>
    </tr>
    <tr id="row1763153318509"><td class="cellrowborder" valign="top" width="21.059405940594058%" headers="mcps1.2.5.1.1 "><p id="p186313337506"><a name="p186313337506"></a><a name="p186313337506"></a>jdbc_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87128712871287%" headers="mcps1.2.5.1.2 "><p id="p166311833175011"><a name="p166311833175011"></a><a name="p166311833175011"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.03960396039604%" headers="mcps1.2.5.1.3 "><p id="p17631633195017"><a name="p17631633195017"></a><a name="p17631633195017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.02970297029702%" headers="mcps1.2.5.1.4 "><p id="p6611185916515"><a name="p6611185916515"></a><a name="p6611185916515"></a>JDBC URL on the public network. The following is the default format:</p>
    <p id="p661118599513"><a name="p661118599513"></a><a name="p661118599513"></a>jdbc:postgresql://&lt; public_connect_info&gt;/&lt;YOUR_DATABASE_NAME&gt;</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **endpoints**  field data structure description

    <a name="table467420155524"></a>
    <table><thead align="left"><tr id="row106741154520"><th class="cellrowborder" valign="top" width="21.029999999999998%" id="mcps1.2.5.1.1"><p id="p18674415105217"><a name="p18674415105217"></a><a name="p18674415105217"></a><strong id="b1880227153"><a name="b1880227153"></a><a name="b1880227153"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.899999999999999%" id="mcps1.2.5.1.2"><p id="p26741815155211"><a name="p26741815155211"></a><a name="p26741815155211"></a><strong id="b1652491817"><a name="b1652491817"></a><a name="b1652491817"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.87%" id="mcps1.2.5.1.3"><p id="p167431514528"><a name="p167431514528"></a><a name="p167431514528"></a><strong id="b1867173503"><a name="b1867173503"></a><a name="b1867173503"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.2%" id="mcps1.2.5.1.4"><p id="p867420154529"><a name="p867420154529"></a><a name="p867420154529"></a><strong id="b1019880643"><a name="b1019880643"></a><a name="b1019880643"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16674111535218"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.2.5.1.1 "><p id="p367414159521"><a name="p367414159521"></a><a name="p367414159521"></a>connect_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.2.5.1.2 "><p id="p2674171517521"><a name="p2674171517521"></a><a name="p2674171517521"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p267418159520"><a name="p267418159520"></a><a name="p267418159520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.2%" headers="mcps1.2.5.1.4 "><p id="p176741315125211"><a name="p176741315125211"></a><a name="p176741315125211"></a>Private network connection information</p>
    </td>
    </tr>
    <tr id="row1067421505217"><td class="cellrowborder" valign="top" width="21.029999999999998%" headers="mcps1.2.5.1.1 "><p id="p11674181535211"><a name="p11674181535211"></a><a name="p11674181535211"></a>jdbc_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.2.5.1.2 "><p id="p14674181519521"><a name="p14674181519521"></a><a name="p14674181519521"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.87%" headers="mcps1.2.5.1.3 "><p id="p8674315125212"><a name="p8674315125212"></a><a name="p8674315125212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.2%" headers="mcps1.2.5.1.4 "><p id="p8719716145314"><a name="p8719716145314"></a><a name="p8719716145314"></a>JDBC URL on the private network. The following is the default format:</p>
    <p id="p207191167538"><a name="p207191167538"></a><a name="p207191167538"></a>jdbc:postgresql://&lt; connect_info&gt;/&lt;YOUR_DATABASE_NAME&gt;</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **failed\_reasons**  field data structure description

    <a name="table34501136155716"></a>
    <table><thead align="left"><tr id="row1445093610574"><th class="cellrowborder" valign="top" width="21.2970297029703%" id="mcps1.2.5.1.1"><p id="p94501536105716"><a name="p94501536105716"></a><a name="p94501536105716"></a><strong id="b1725738815"><a name="b1725738815"></a><a name="b1725738815"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.227722772277227%" id="mcps1.2.5.1.2"><p id="p134501936145710"><a name="p134501936145710"></a><a name="p134501936145710"></a><strong id="b354693525"><a name="b354693525"></a><a name="b354693525"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.801980198019802%" id="mcps1.2.5.1.3"><p id="p54506363575"><a name="p54506363575"></a><a name="p54506363575"></a><strong id="b72248346"><a name="b72248346"></a><a name="b72248346"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.67326732673268%" id="mcps1.2.5.1.4"><p id="p5450113615573"><a name="p5450113615573"></a><a name="p5450113615573"></a><strong id="b910857357"><a name="b910857357"></a><a name="b910857357"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row645053618574"><td class="cellrowborder" valign="top" width="21.2970297029703%" headers="mcps1.2.5.1.1 "><p id="p1445073625714"><a name="p1445073625714"></a><a name="p1445073625714"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.227722772277227%" headers="mcps1.2.5.1.2 "><p id="p14501636115716"><a name="p14501636115716"></a><a name="p14501636115716"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.801980198019802%" headers="mcps1.2.5.1.3 "><p id="p74505363571"><a name="p74505363571"></a><a name="p74505363571"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.67326732673268%" headers="mcps1.2.5.1.4 "><p id="p3697103419316"><a name="p3697103419316"></a><a name="p3697103419316"></a>Error code. Possible values can be:</p>
    <a name="ul1169711341132"></a><a name="ul1169711341132"></a><ul id="ul1169711341132"><li><strong id="b842352706154429"><a name="b842352706154429"></a><a name="b842352706154429"></a>DWS.6000</strong>: indicates that cluster creation fails.</li><li><strong id="b842352706154441"><a name="b842352706154441"></a><a name="b842352706154441"></a>DWS.6001</strong>: indicates that cluster scale-out fails.</li><li><strong id="b842352706154556"><a name="b842352706154556"></a><a name="b842352706154556"></a>DWS.6002</strong>: indicates that cluster restart fails.</li><li><strong id="b1711244489154721"><a name="b1711244489154721"></a><a name="b1711244489154721"></a>DWS.6003</strong>: indicates that cluster restoration fails.</li></ul>
    </td>
    </tr>
    <tr id="row2045053635715"><td class="cellrowborder" valign="top" width="21.2970297029703%" headers="mcps1.2.5.1.1 "><p id="p15450123625711"><a name="p15450123625711"></a><a name="p15450123625711"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.227722772277227%" headers="mcps1.2.5.1.2 "><p id="p34507367579"><a name="p34507367579"></a><a name="p34507367579"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.801980198019802%" headers="mcps1.2.5.1.3 "><p id="p5450136115713"><a name="p5450136115713"></a><a name="p5450136115713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.67326732673268%" headers="mcps1.2.5.1.4 "><p id="p14450183611573"><a name="p14450183611573"></a><a name="p14450183611573"></a>Error message</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="s48e877f46afe4aed93303b04041be848"></a>

-   Normal

    200

-   Abnormal 

    **Table  7**  Returned value description

    <a name="en-us_topic_0067607266_table32016662"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607266_row28099101"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0067607266_p61434729"><a name="en-us_topic_0067607266_p61434729"></a><a name="en-us_topic_0067607266_p61434729"></a><strong id="b842352706175024"><a name="b842352706175024"></a><a name="b842352706175024"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0067607266_p10157186"><a name="en-us_topic_0067607266_p10157186"></a><a name="en-us_topic_0067607266_p10157186"></a><strong id="b1166006651"><a name="b1166006651"></a><a name="b1166006651"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607266_row17425743"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p2199097"><a name="en-us_topic_0067607266_p2199097"></a><a name="en-us_topic_0067607266_p2199097"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p43909159"><a name="en-us_topic_0067607266_p43909159"></a><a name="en-us_topic_0067607266_p43909159"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row66980994"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p56751409"><a name="en-us_topic_0067607266_p56751409"></a><a name="en-us_topic_0067607266_p56751409"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p33461405"><a name="en-us_topic_0067607266_p33461405"></a><a name="en-us_topic_0067607266_p33461405"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row32717189"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p32846614"><a name="en-us_topic_0067607266_p32846614"></a><a name="en-us_topic_0067607266_p32846614"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p43330072"><a name="en-us_topic_0067607266_p43330072"></a><a name="en-us_topic_0067607266_p43330072"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row54426330"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p46456648"><a name="en-us_topic_0067607266_p46456648"></a><a name="en-us_topic_0067607266_p46456648"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p4892154"><a name="en-us_topic_0067607266_p4892154"></a><a name="en-us_topic_0067607266_p4892154"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row44029393"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p9611044"><a name="en-us_topic_0067607266_p9611044"></a><a name="en-us_topic_0067607266_p9611044"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p40297137"><a name="en-us_topic_0067607266_p40297137"></a><a name="en-us_topic_0067607266_p40297137"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607266_row27129916"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607266_p50039568"><a name="en-us_topic_0067607266_p50039568"></a><a name="en-us_topic_0067607266_p50039568"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607266_p26673201"><a name="en-us_topic_0067607266_p26673201"></a><a name="en-us_topic_0067607266_p26673201"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


