# Querying Cluster Details<a name="dws_02_0019"></a>

## Function<a name="s6c3ce4d938454b62bfcd3d18bfca642a"></a>

This API is used to query cluster details.

## URI<a name="s296f59f86fdf42119ec97e38f235ef7e"></a>

-   URI format

    GET /v1.0/\{project\_id\}/clusters/\{cluster\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="en-us_topic_0067607267_table11041789"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607267_row9230088"><th class="cellrowborder" valign="top" width="20.07%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607267_p9439626"><a name="en-us_topic_0067607267_p9439626"></a><a name="en-us_topic_0067607267_p9439626"></a><strong id="b84235270617228_1"><a name="b84235270617228_1"></a><a name="b84235270617228_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607267_p26412257"><a name="en-us_topic_0067607267_p26412257"></a><a name="en-us_topic_0067607267_p26412257"></a><strong id="b6167984116271_1"><a name="b6167984116271_1"></a><a name="b6167984116271_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.76%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607267_p59018101"><a name="en-us_topic_0067607267_p59018101"></a><a name="en-us_topic_0067607267_p59018101"></a><strong id="b84235270617235_1"><a name="b84235270617235_1"></a><a name="b84235270617235_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.93%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607267_p15736877"><a name="en-us_topic_0067607267_p15736877"></a><a name="en-us_topic_0067607267_p15736877"></a><strong id="b842352706172443_1"><a name="b842352706172443_1"></a><a name="b842352706172443_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607267_row66727538"><td class="cellrowborder" valign="top" width="20.07%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p36221483"><a name="en-us_topic_0067607267_p36221483"></a><a name="en-us_topic_0067607267_p36221483"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p48259009"><a name="en-us_topic_0067607267_p48259009"></a><a name="en-us_topic_0067607267_p48259009"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.76%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p16665627"><a name="en-us_topic_0067607267_p16665627"></a><a name="en-us_topic_0067607267_p16665627"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.93%" headers="mcps1.2.5.1.4 "><p id="p17699440125419"><a name="p17699440125419"></a><a name="p17699440125419"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row2537905"><td class="cellrowborder" valign="top" width="20.07%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p4243749"><a name="en-us_topic_0067607267_p4243749"></a><a name="en-us_topic_0067607267_p4243749"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p8199418"><a name="en-us_topic_0067607267_p8199418"></a><a name="en-us_topic_0067607267_p8199418"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.76%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p60173144"><a name="en-us_topic_0067607267_p60173144"></a><a name="en-us_topic_0067607267_p60173144"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.93%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p42186470"><a name="en-us_topic_0067607267_p42186470"></a><a name="en-us_topic_0067607267_p42186470"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s685ffa4144484cb4b84536852a4ac4e0"></a>

Sample request

```
GET /v1.0/89cd04f168b84af6be287f71730fdb4b/clusters/b5c45780-1006-49e3-b2d5-b3229975bbc7
```

## Response<a name="s0d10a4327b3e4533b977c49b08c87be0"></a>

-   Sample response

    ```
    {
        "cluster": {
            "id": "7d85f602-a948-4a30-afd4-e84f47471c15",
            "status": "AVAILABLE",
            "name": "dws-1",
            "updated": "2018-02-10T14:28:14Z",
            "created": "2018-02-10T14:28:14Z",
            "user_name": "dbadmin",
            "sub_status": "READONLY",
            "task_status": "SNAPSHOTTING",
            "action_progress": {"SNAPSHOTTING": "20%"},
            "node_type": "dws.m1.xlarge.ultrahigh",        
            "node_type_id": "5ddb1071-c5d7-40e0-a874-8a032e81a697",
            "subnet_id": "374eca02-cfc4-4de7-8ab5-dbebf7d9a720",
            "security_group_id": "dc3ec145-9029-4b39-b5a3-ace5a01f772b",
            "number_of_node": 3,
            "availability_zone": "eu-de-01",
            "port": 8000,        
            "vpc_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574",        
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
                    "connect_info": "192.168.0.10:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.10:8000/<YOUR_DATABASE_NAME>"
                },
                {
                    "connect_info": "192.168.0.12:8000",
                    "jdbc_url": "jdbc:postgresql://192.168.0.12:8000/<YOUR_DATABASE_NAME>"
                }
             ],
            "version": "1.2.0",
            "maintain_window": {
                "day": "Wed",
                "start_time": "22:00",
                "end_time": "02:00"
            },
            "resize_info" : {            
                "target_node_num": "6",
                "origin_node_num": "3",
                "status": "GROWING",
                "start_time": "2018-02-14T14:28:14Z"
            }, 
            "tags":[ 
                { 
                    "key": "key1", 
                    "value": "value1" 
                }, 
                { 
                    "key": "key2", 
                    "value": "value2" 
                } 
              ], 
    
             "parameter_group": {
                  "id": "157e9cc4-64a8-11e8-adc0-fa7ae01bbebc",
                  "name": "Default-Parameter-Group-DWS",
                  "status": "In-Sync"
             } 
        }
    }
    ```


-   Parameter description

    **Table  2**  Response parameter description

    <a name="en-us_topic_0067607267_table60896162"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607267_row43299552"><th class="cellrowborder" valign="top" width="21.27%" id="mcps1.2.5.1.1"><p id="en-us_topic_0067607267_p17602849"><a name="en-us_topic_0067607267_p17602849"></a><a name="en-us_topic_0067607267_p17602849"></a><strong id="b84235270617228_3"><a name="b84235270617228_3"></a><a name="b84235270617228_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.479999999999999%" id="mcps1.2.5.1.2"><p id="en-us_topic_0067607267_p16544703"><a name="en-us_topic_0067607267_p16544703"></a><a name="en-us_topic_0067607267_p16544703"></a><strong id="b6167984116271_3"><a name="b6167984116271_3"></a><a name="b6167984116271_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.700000000000001%" id="mcps1.2.5.1.3"><p id="en-us_topic_0067607267_p65052577"><a name="en-us_topic_0067607267_p65052577"></a><a name="en-us_topic_0067607267_p65052577"></a><strong id="b84235270617235_3"><a name="b84235270617235_3"></a><a name="b84235270617235_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.55%" id="mcps1.2.5.1.4"><p id="en-us_topic_0067607267_p34767408"><a name="en-us_topic_0067607267_p34767408"></a><a name="en-us_topic_0067607267_p34767408"></a><strong id="b842352706172443_3"><a name="b842352706172443_3"></a><a name="b842352706172443_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607267_row64696659"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p5938035"><a name="en-us_topic_0067607267_p5938035"></a><a name="en-us_topic_0067607267_p5938035"></a>cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p11218807"><a name="en-us_topic_0067607267_p11218807"></a><a name="en-us_topic_0067607267_p11218807"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p36308168"><a name="en-us_topic_0067607267_p36308168"></a><a name="en-us_topic_0067607267_p36308168"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p55280461"><a name="en-us_topic_0067607267_p55280461"></a><a name="en-us_topic_0067607267_p55280461"></a>Cluster object</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row27762102"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p34137829"><a name="en-us_topic_0067607267_p34137829"></a><a name="en-us_topic_0067607267_p34137829"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p13700797"><a name="en-us_topic_0067607267_p13700797"></a><a name="en-us_topic_0067607267_p13700797"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p36022757"><a name="en-us_topic_0067607267_p36022757"></a><a name="en-us_topic_0067607267_p36022757"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p32162181"><a name="en-us_topic_0067607267_p32162181"></a><a name="en-us_topic_0067607267_p32162181"></a>Cluster ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row21024178"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p25236858"><a name="en-us_topic_0067607267_p25236858"></a><a name="en-us_topic_0067607267_p25236858"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p30919631"><a name="en-us_topic_0067607267_p30919631"></a><a name="en-us_topic_0067607267_p30919631"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p21462168"><a name="en-us_topic_0067607267_p21462168"></a><a name="en-us_topic_0067607267_p21462168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="ae88ce587a99a43f296ca2f71162e8f97"><a name="ae88ce587a99a43f296ca2f71162e8f97"></a><a name="ae88ce587a99a43f296ca2f71162e8f97"></a>Cluster status, which can be one of the following:</p>
    <a name="u32a777ae08e24ec3a93b8679270ab91e"></a><a name="u32a777ae08e24ec3a93b8679270ab91e"></a><ul id="u32a777ae08e24ec3a93b8679270ab91e"><li><strong id="b842352706152546"><a name="b842352706152546"></a><a name="b842352706152546"></a>CREATING</strong></li><li><strong id="b335382630162424"><a name="b335382630162424"></a><a name="b335382630162424"></a>AVAILABLE</strong></li><li><strong id="b842352706162411"><a name="b842352706162411"></a><a name="b842352706162411"></a>UNAVAILABLE</strong></li><li><strong>CREATION FAILED</strong></li></ul>
    </td>
    </tr>
    <tr id="row102950113112"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p9295111414"><a name="p9295111414"></a><a name="p9295111414"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p02959116115"><a name="p02959116115"></a><a name="p02959116115"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p1729611118110"><a name="p1729611118110"></a><a name="p1729611118110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p1129612119113"><a name="p1129612119113"></a><a name="p1129612119113"></a>Cluster name</p>
    </td>
    </tr>
    <tr id="row729431615119"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p112953160119"><a name="p112953160119"></a><a name="p112953160119"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p630117161118"><a name="p630117161118"></a><a name="p630117161118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p03011016919"><a name="p03011016919"></a><a name="p03011016919"></a>Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p13027161813"><a name="p13027161813"></a><a name="p13027161813"></a>Last modification time of a cluster. The format is <strong id="b842352706174936"><a name="b842352706174936"></a><a name="b842352706174936"></a>ISO8601:YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="row165392271310"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p195401627318"><a name="p195401627318"></a><a name="p195401627318"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p05401927513"><a name="p05401927513"></a><a name="p05401927513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p554022711117"><a name="p554022711117"></a><a name="p554022711117"></a>Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p45404271117"><a name="p45404271117"></a><a name="p45404271117"></a>Cluster creation time. The format is <strong id="b842352706174833"><a name="b842352706174833"></a><a name="b842352706174833"></a>ISO8601:YYYY-MM-DDThh:mm:ssZ</strong>.</p>
    </td>
    </tr>
    <tr id="row118981132813"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p089823218117"><a name="p089823218117"></a><a name="p089823218117"></a>user_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p49021332515"><a name="p49021332515"></a><a name="p49021332515"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p190218321112"><a name="p190218321112"></a><a name="p190218321112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p1690213218116"><a name="p1690213218116"></a><a name="p1690213218116"></a>Administrator username</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row55898385"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p31475357"><a name="en-us_topic_0067607267_p31475357"></a><a name="en-us_topic_0067607267_p31475357"></a>sub_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p66476022"><a name="en-us_topic_0067607267_p66476022"></a><a name="en-us_topic_0067607267_p66476022"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p15848707"><a name="en-us_topic_0067607267_p15848707"></a><a name="en-us_topic_0067607267_p15848707"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="acaeb108ee4ad49b7872d4956fb339d49"><a name="acaeb108ee4ad49b7872d4956fb339d49"></a><a name="acaeb108ee4ad49b7872d4956fb339d49"></a>Sub-status of clusters in the <strong id="b1341008343162427"><a name="b1341008343162427"></a><a name="b1341008343162427"></a>AVAILABLE</strong> state. The value can be one of the following:</p>
    <a name="ua3cf7da30a1d47c2ac4c7b654870356c"></a><a name="ua3cf7da30a1d47c2ac4c7b654870356c"></a><ul id="ua3cf7da30a1d47c2ac4c7b654870356c"><li><strong id="b842352706172235"><a name="b842352706172235"></a><a name="b842352706172235"></a>NORMAL</strong></li><li><strong id="b843639795172048"><a name="b843639795172048"></a><a name="b843639795172048"></a>READONLY</strong></li><li><strong id="b842352706172246"><a name="b842352706172246"></a><a name="b842352706172246"></a>REDISTRIBUTING</strong></li><li><strong id="b84235270617239"><a name="b84235270617239"></a><a name="b84235270617239"></a>REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706172339"><a name="b842352706172339"></a><a name="b842352706172339"></a>UNBALANCED</strong></li><li><strong id="b842352706172359"><a name="b842352706172359"></a><a name="b842352706172359"></a>UNBALANCED | READONLY</strong></li><li><strong id="b842352706172436"><a name="b842352706172436"></a><a name="b842352706172436"></a>DEGRADED</strong></li><li><strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>DEGRADED | READONLY</strong></li><li><strong id="b842352706172721_1"><a name="b842352706172721_1"></a><a name="b842352706172721_1"></a>DEGRADED | UNBALANCED</strong></li><li><strong id="b842352706172755"><a name="b842352706172755"></a><a name="b842352706172755"></a>UNBALANCED | REDISTRIBUTING</strong></li><li><strong id="b84235270617297"><a name="b84235270617297"></a><a name="b84235270617297"></a>UNBALANCED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706172941"><a name="b842352706172941"></a><a name="b842352706172941"></a>READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706162513"><a name="b842352706162513"></a><a name="b842352706162513"></a>UNBALANCED | READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706173050"><a name="b842352706173050"></a><a name="b842352706173050"></a>DEGRADED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b84235270615284"><a name="b84235270615284"></a><a name="b84235270615284"></a>DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706173010"><a name="b842352706173010"></a><a name="b842352706173010"></a>DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE</strong></li><li><strong id="b842352706172721_3"><a name="b842352706172721_3"></a><a name="b842352706172721_3"></a>DEGRADED | UNBALANCED | READONLY</strong></li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row49614245"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p59330872"><a name="en-us_topic_0067607267_p59330872"></a><a name="en-us_topic_0067607267_p59330872"></a>task_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p41071365"><a name="en-us_topic_0067607267_p41071365"></a><a name="en-us_topic_0067607267_p41071365"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p38446258"><a name="en-us_topic_0067607267_p38446258"></a><a name="en-us_topic_0067607267_p38446258"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="a65f1116087e5428eb0c122a17bd358f6"><a name="a65f1116087e5428eb0c122a17bd358f6"></a><a name="a65f1116087e5428eb0c122a17bd358f6"></a>Cluster management task. The value can be one of the following:</p>
    <a name="ud3004947d5b248f1965936dc378c5206"></a><a name="ud3004947d5b248f1965936dc378c5206"></a><ul id="ud3004947d5b248f1965936dc378c5206"><li><strong id="b842352706173523_1"><a name="b842352706173523_1"></a><a name="b842352706173523_1"></a>RESTORING</strong></li><li><strong id="b842352706173540_1"><a name="b842352706173540_1"></a><a name="b842352706173540_1"></a>SNAPSHOTTING</strong></li><li><strong id="b84235270617363_1"><a name="b84235270617363_1"></a><a name="b84235270617363_1"></a>GROWING</strong></li><li><strong id="b842352706173642"><a name="b842352706173642"></a><a name="b842352706173642"></a>REBOOTING</strong></li><li><strong id="b842352706164634"><a name="b842352706164634"></a><a name="b842352706164634"></a>SETTING_CONFIGURATION</strong></li><li><strong id="b842352706164641"><a name="b842352706164641"></a><a name="b842352706164641"></a>CONFIGURING_EXT_DATASOURCE</strong></li><li><strong id="b842352706164649"><a name="b842352706164649"></a><a name="b842352706164649"></a>DELETING_EXT_DATASOURCE</strong></li><li><strong id="b842352706173725"><a name="b842352706173725"></a><a name="b842352706173725"></a>REBOOT_FAILURE</strong></li><li><strong id="b842352706162543_1"><a name="b842352706162543_1"></a><a name="b842352706162543_1"></a>RESIZE_FAILURE</strong></li></ul>
    </td>
    </tr>
    <tr id="row43165144512"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p93181514185111"><a name="p93181514185111"></a><a name="p93181514185111"></a>action_progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p1931816144513"><a name="p1931816144513"></a><a name="p1931816144513"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p631871417519"><a name="p631871417519"></a><a name="p631871417519"></a>Map</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p20780434172512"><a name="p20780434172512"></a><a name="p20780434172512"></a>The key indicates an ongoing task. The value can be one of the following:</p>
    <a name="ul1958205713298"></a><a name="ul1958205713298"></a><ul id="ul1958205713298"><li><strong id="b84235270617363_3"><a name="b84235270617363_3"></a><a name="b84235270617363_3"></a>GROWING</strong></li><li><strong id="b842352706173523_3"><a name="b842352706173523_3"></a><a name="b842352706173523_3"></a>RESTORING</strong></li><li><strong id="b842352706173540_3"><a name="b842352706173540_3"></a><a name="b842352706173540_3"></a>SNAPSHOTTING</strong></li><li><strong id="b84235270611057"><a name="b84235270611057"></a><a name="b84235270611057"></a>REPAIRING</strong></li><li><strong id="b8423527061114"><a name="b8423527061114"></a><a name="b8423527061114"></a>GREATING</strong><p id="p4575190184120"><a name="p4575190184120"></a><a name="p4575190184120"></a>The key value indicates the progress of the ongoing task.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row15816986"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p6107499"><a name="en-us_topic_0067607267_p6107499"></a><a name="en-us_topic_0067607267_p6107499"></a>node_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p24945412"><a name="en-us_topic_0067607267_p24945412"></a><a name="en-us_topic_0067607267_p24945412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p7312526"><a name="en-us_topic_0067607267_p7312526"></a><a name="en-us_topic_0067607267_p7312526"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p55443761"><a name="en-us_topic_0067607267_p55443761"></a><a name="en-us_topic_0067607267_p55443761"></a>Node type</p>
    </td>
    </tr>
    <tr id="row499894618910"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p19998146397"><a name="p19998146397"></a><a name="p19998146397"></a>node_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p1299810462916"><a name="p1299810462916"></a><a name="p1299810462916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p11998184612912"><a name="p11998184612912"></a><a name="p11998184612912"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p159981461298"><a name="p159981461298"></a><a name="p159981461298"></a>ID of a node type</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row29231803"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p18965813"><a name="en-us_topic_0067607267_p18965813"></a><a name="en-us_topic_0067607267_p18965813"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p59835867"><a name="en-us_topic_0067607267_p59835867"></a><a name="en-us_topic_0067607267_p59835867"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p14867095"><a name="en-us_topic_0067607267_p14867095"></a><a name="en-us_topic_0067607267_p14867095"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p63384014"><a name="en-us_topic_0067607267_p63384014"></a><a name="en-us_topic_0067607267_p63384014"></a>Subnet ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row33585220"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p36048322"><a name="en-us_topic_0067607267_p36048322"></a><a name="en-us_topic_0067607267_p36048322"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p34232944"><a name="en-us_topic_0067607267_p34232944"></a><a name="en-us_topic_0067607267_p34232944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p21405046"><a name="en-us_topic_0067607267_p21405046"></a><a name="en-us_topic_0067607267_p21405046"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p56087165"><a name="en-us_topic_0067607267_p56087165"></a><a name="en-us_topic_0067607267_p56087165"></a>ID of a security group</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row35022440"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p18245395"><a name="en-us_topic_0067607267_p18245395"></a><a name="en-us_topic_0067607267_p18245395"></a>number_of_node</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p1482002"><a name="en-us_topic_0067607267_p1482002"></a><a name="en-us_topic_0067607267_p1482002"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p52933326"><a name="en-us_topic_0067607267_p52933326"></a><a name="en-us_topic_0067607267_p52933326"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p59740974"><a name="en-us_topic_0067607267_p59740974"></a><a name="en-us_topic_0067607267_p59740974"></a>Number of nodes</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row797855"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p64626289"><a name="en-us_topic_0067607267_p64626289"></a><a name="en-us_topic_0067607267_p64626289"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p238043"><a name="en-us_topic_0067607267_p238043"></a><a name="en-us_topic_0067607267_p238043"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p19281542"><a name="en-us_topic_0067607267_p19281542"></a><a name="en-us_topic_0067607267_p19281542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p18301082"><a name="en-us_topic_0067607267_p18301082"></a><a name="en-us_topic_0067607267_p18301082"></a>AZ</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row30492010"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p53933741"><a name="en-us_topic_0067607267_p53933741"></a><a name="en-us_topic_0067607267_p53933741"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p6556909"><a name="en-us_topic_0067607267_p6556909"></a><a name="en-us_topic_0067607267_p6556909"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p61347601"><a name="en-us_topic_0067607267_p61347601"></a><a name="en-us_topic_0067607267_p61347601"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p3099778"><a name="en-us_topic_0067607267_p3099778"></a><a name="en-us_topic_0067607267_p3099778"></a>Service port of a cluster (8000 to 10000). The default value is <strong id="b84235270694758"><a name="b84235270694758"></a><a name="b84235270694758"></a>8000</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row46277382"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p57480441"><a name="en-us_topic_0067607267_p57480441"></a><a name="en-us_topic_0067607267_p57480441"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p25404116"><a name="en-us_topic_0067607267_p25404116"></a><a name="en-us_topic_0067607267_p25404116"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p44467520"><a name="en-us_topic_0067607267_p44467520"></a><a name="en-us_topic_0067607267_p44467520"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p45099364"><a name="en-us_topic_0067607267_p45099364"></a><a name="en-us_topic_0067607267_p45099364"></a>VPC ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row66531170"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p20315681"><a name="en-us_topic_0067607267_p20315681"></a><a name="en-us_topic_0067607267_p20315681"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p34957489"><a name="en-us_topic_0067607267_p34957489"></a><a name="en-us_topic_0067607267_p34957489"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p12984378"><a name="en-us_topic_0067607267_p12984378"></a><a name="en-us_topic_0067607267_p12984378"></a>Object. For details, see <a href="#table11574153020156">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p45101667"><a name="en-us_topic_0067607267_p45101667"></a><a name="en-us_topic_0067607267_p45101667"></a>Public IP address. If the value is not specified, public connection is not used by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row26818564"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p24820109"><a name="en-us_topic_0067607267_p24820109"></a><a name="en-us_topic_0067607267_p24820109"></a>public_endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p64271818"><a name="en-us_topic_0067607267_p64271818"></a><a name="en-us_topic_0067607267_p64271818"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p38634788"><a name="en-us_topic_0067607267_p38634788"></a><a name="en-us_topic_0067607267_p38634788"></a>Array. For details, see <a href="#table17892711171916">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p42410114"><a name="en-us_topic_0067607267_p42410114"></a><a name="en-us_topic_0067607267_p42410114"></a>Public network connection information about the cluster. If the value is not specified, the public network connection information is not used by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row25986055"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0067607267_p24495719"><a name="en-us_topic_0067607267_p24495719"></a><a name="en-us_topic_0067607267_p24495719"></a>endpoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0067607267_p37996203"><a name="en-us_topic_0067607267_p37996203"></a><a name="en-us_topic_0067607267_p37996203"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0067607267_p57793596"><a name="en-us_topic_0067607267_p57793596"></a><a name="en-us_topic_0067607267_p57793596"></a>Array. For details, see <a href="#table338520331214">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0067607267_p50769665"><a name="en-us_topic_0067607267_p50769665"></a><a name="en-us_topic_0067607267_p50769665"></a>View the private network connection information about the cluster.</p>
    </td>
    </tr>
    <tr id="row168011625115910"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p168021725145915"><a name="p168021725145915"></a><a name="p168021725145915"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p13803525205911"><a name="p13803525205911"></a><a name="p13803525205911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p88031925155911"><a name="p88031925155911"></a><a name="p88031925155911"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p1580342585914"><a name="p1580342585914"></a><a name="p1580342585914"></a>Data warehouse version</p>
    </td>
    </tr>
    <tr id="row21211172547"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p112161720541"><a name="p112161720541"></a><a name="p112161720541"></a>maintain_window</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p1412271717545"><a name="p1412271717545"></a><a name="p1412271717545"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p15123161775414"><a name="p15123161775414"></a><a name="p15123161775414"></a>Object. For details, see <a href="#table1280114239235">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p2123161735414"><a name="p2123161735414"></a><a name="p2123161735414"></a>Cluster maintenance time window</p>
    </td>
    </tr>
    <tr id="row1380332815416"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p6803102814548"><a name="p6803102814548"></a><a name="p6803102814548"></a>resize_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p38034285543"><a name="p38034285543"></a><a name="p38034285543"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p198047285549"><a name="p198047285549"></a><a name="p198047285549"></a>Object. For details, see <a href="#table11415448252">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p5804428195417"><a name="p5804428195417"></a><a name="p5804428195417"></a>Cluster scale-out status details</p>
    </td>
    </tr>
    <tr id="r4ca887d31cd5461c8513227917981f45"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="aafe19211ae134558a96889f1e72b711d"><a name="aafe19211ae134558a96889f1e72b711d"></a><a name="aafe19211ae134558a96889f1e72b711d"></a>failed_reasons</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="a7920ea40446647e4b87da7adab614744"><a name="a7920ea40446647e4b87da7adab614744"></a><a name="a7920ea40446647e4b87da7adab614744"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="a944d74a220cd423dba912cfc4946c929"><a name="a944d74a220cd423dba912cfc4946c929"></a><a name="a944d74a220cd423dba912cfc4946c929"></a>Object. For details, see <a href="#table1501965285">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="a2c1b07d2c6924db2bdb9fb5140b3eb10"><a name="a2c1b07d2c6924db2bdb9fb5140b3eb10"></a><a name="a2c1b07d2c6924db2bdb9fb5140b3eb10"></a>Cause of failure. If the value is empty, the cluster is in the normal state.</p>
    </td>
    </tr>
    <tr id="row147651252114115"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p97655527418"><a name="p97655527418"></a><a name="p97655527418"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p1176517525414"><a name="p1176517525414"></a><a name="p1176517525414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p107650529418"><a name="p107650529418"></a><a name="p107650529418"></a>Array. For details, see <a href="#table16661175514414">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p14765252154118"><a name="p14765252154118"></a><a name="p14765252154118"></a>Tags in a cluster</p>
    </td>
    </tr>
    <tr id="row12452761816"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.5.1.1 "><p id="p8794151911481"><a name="p8794151911481"></a><a name="p8794151911481"></a>parameter_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.479999999999999%" headers="mcps1.2.5.1.2 "><p id="p15245678181"><a name="p15245678181"></a><a name="p15245678181"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.3 "><p id="p152453717187"><a name="p152453717187"></a><a name="p152453717187"></a>Object. For details, see <a href="#table989317913224">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.55%" headers="mcps1.2.5.1.4 "><p id="p42451476185"><a name="p42451476185"></a><a name="p42451476185"></a>Information about the parameter group associated with the cluster</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **public\_ip**  field data structure description

    <a name="table11574153020156"></a>
    <table><thead align="left"><tr id="row14574330171513"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p55741030121513"><a name="p55741030121513"></a><a name="p55741030121513"></a><strong id="b84235270611710_3"><a name="b84235270611710_3"></a><a name="b84235270611710_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p25742302152"><a name="p25742302152"></a><a name="p25742302152"></a><strong id="b6167984116271_7"><a name="b6167984116271_7"></a><a name="b6167984116271_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p9574630101516"><a name="p9574630101516"></a><a name="p9574630101516"></a><strong id="b84235270617235_7"><a name="b84235270617235_7"></a><a name="b84235270617235_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p25741630171512"><a name="p25741630171512"></a><a name="p25741630171512"></a><strong id="b842352706134712_3"><a name="b842352706134712_3"></a><a name="b842352706134712_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35742030121512"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p10574113071518"><a name="p10574113071518"></a><a name="p10574113071518"></a>public_bind_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1257473051519"><a name="p1257473051519"></a><a name="p1257473051519"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p95741306159"><a name="p95741306159"></a><a name="p95741306159"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p7403174331718"><a name="p7403174331718"></a><a name="p7403174331718"></a>Binding type of an EIP. The value can be either of the following:</p>
    <a name="ul1341984331717"></a><a name="ul1341984331717"></a><ul id="ul1341984331717"><li><strong id="b842352706174142"><a name="b842352706174142"></a><a name="b842352706174142"></a>auto_assign</strong></li><li><strong id="b842352706174712"><a name="b842352706174712"></a><a name="b842352706174712"></a>not_use</strong></li><li><strong id="b842352706162651"><a name="b842352706162651"></a><a name="b842352706162651"></a>bind_existing</strong></li></ul>
    </td>
    </tr>
    <tr id="row14574203012156"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p7574153021513"><a name="p7574153021513"></a><a name="p7574153021513"></a>eip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p657418305157"><a name="p657418305157"></a><a name="p657418305157"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p757416304150"><a name="p757416304150"></a><a name="p757416304150"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p7574530161516"><a name="p7574530161516"></a><a name="p7574530161516"></a>EIP ID</p>
    </td>
    </tr>
    <tr id="row195747308159"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p19574103015151"><a name="p19574103015151"></a><a name="p19574103015151"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p05743308154"><a name="p05743308154"></a><a name="p05743308154"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p75745305152"><a name="p75745305152"></a><a name="p75745305152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p4106115861713"><a name="p4106115861713"></a><a name="p4106115861713"></a>Binding status of an EIP. The parameter value is as follows:</p>
    <a name="ul141065581173"></a><a name="ul141065581173"></a><ul id="ul141065581173"><li><strong id="b84235270611259"><a name="b84235270611259"></a><a name="b84235270611259"></a>FAIL</strong></li></ul>
    </td>
    </tr>
    <tr id="row457473015155"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p1857473011154"><a name="p1857473011154"></a><a name="p1857473011154"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p13574630171513"><a name="p13574630171513"></a><a name="p13574630171513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p1457463018154"><a name="p1457463018154"></a><a name="p1457463018154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p4574183041518"><a name="p4574183041518"></a><a name="p4574183041518"></a>Cause of an EIP binding failure</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **public\_endpoints**  field data structure description

    <a name="table17892711171916"></a>
    <table><thead align="left"><tr id="row1189251111917"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p178921111161916"><a name="p178921111161916"></a><a name="p178921111161916"></a><strong id="b84235270611710_5"><a name="b84235270611710_5"></a><a name="b84235270611710_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p1789220111194"><a name="p1789220111194"></a><a name="p1789220111194"></a><strong id="b6167984116271_9"><a name="b6167984116271_9"></a><a name="b6167984116271_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p18892011201920"><a name="p18892011201920"></a><a name="p18892011201920"></a><strong id="b84235270617235_9"><a name="b84235270617235_9"></a><a name="b84235270617235_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p14892151110190"><a name="p14892151110190"></a><a name="p14892151110190"></a><strong id="b842352706134712_5"><a name="b842352706134712_5"></a><a name="b842352706134712_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row389291111195"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p78921411161915"><a name="p78921411161915"></a><a name="p78921411161915"></a>public_connect_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p12892181181918"><a name="p12892181181918"></a><a name="p12892181181918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p88926119196"><a name="p88926119196"></a><a name="p88926119196"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p3892201114196"><a name="p3892201114196"></a><a name="p3892201114196"></a>Public network connection information</p>
    </td>
    </tr>
    <tr id="row189251161920"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p1989215111196"><a name="p1989215111196"></a><a name="p1989215111196"></a>jdbc_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1389211115196"><a name="p1389211115196"></a><a name="p1389211115196"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p1989291120196"><a name="p1989291120196"></a><a name="p1989291120196"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p13496182313212"><a name="p13496182313212"></a><a name="p13496182313212"></a>JDBC URL on the public network. The following is the default format:</p>
    <p id="p349672392112"><a name="p349672392112"></a><a name="p349672392112"></a>jdbc:postgresql://&lt; public_connect_info&gt;/&lt;YOUR_DATABASE_NAME&gt;</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **endpoints**  field data structure description

    <a name="table338520331214"></a>
    <table><thead align="left"><tr id="row1138543320219"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p15385103362110"><a name="p15385103362110"></a><a name="p15385103362110"></a><strong id="b84235270611710_7"><a name="b84235270611710_7"></a><a name="b84235270611710_7"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p5385163316219"><a name="p5385163316219"></a><a name="p5385163316219"></a><strong id="b6167984116271_11"><a name="b6167984116271_11"></a><a name="b6167984116271_11"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p11385833152117"><a name="p11385833152117"></a><a name="p11385833152117"></a><strong id="b84235270617235_11"><a name="b84235270617235_11"></a><a name="b84235270617235_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="p938593320212"><a name="p938593320212"></a><a name="p938593320212"></a><strong id="b842352706134712_7"><a name="b842352706134712_7"></a><a name="b842352706134712_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1138583372116"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p17385133312211"><a name="p17385133312211"></a><a name="p17385133312211"></a>connect_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p53851333172119"><a name="p53851333172119"></a><a name="p53851333172119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1638593310217"><a name="p1638593310217"></a><a name="p1638593310217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p13385183352118"><a name="p13385183352118"></a><a name="p13385183352118"></a>Private network connection information</p>
    </td>
    </tr>
    <tr id="row938510339216"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p193851233172119"><a name="p193851233172119"></a><a name="p193851233172119"></a>jdbc_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p338583310217"><a name="p338583310217"></a><a name="p338583310217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p5385163342115"><a name="p5385163342115"></a><a name="p5385163342115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p1833195372218"><a name="p1833195372218"></a><a name="p1833195372218"></a>JDBC URL on the private network. The following is the default format:</p>
    <p id="p633175362213"><a name="p633175362213"></a><a name="p633175362213"></a>jdbc:postgresql://&lt; connect_info&gt;/&lt;YOUR_DATABASE_NAME&gt;</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **maintain\_window**  field data structure description

    <a name="table1280114239235"></a>
    <table><thead align="left"><tr id="row168011523152313"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p8801182322315"><a name="p8801182322315"></a><a name="p8801182322315"></a><strong id="b84235270611710_9"><a name="b84235270611710_9"></a><a name="b84235270611710_9"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p78011231235"><a name="p78011231235"></a><a name="p78011231235"></a><strong id="b6167984116271_13"><a name="b6167984116271_13"></a><a name="b6167984116271_13"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p188010239232"><a name="p188010239232"></a><a name="p188010239232"></a><strong id="b84235270617235_13"><a name="b84235270617235_13"></a><a name="b84235270617235_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.2.5.1.4"><p id="p13801142315236"><a name="p13801142315236"></a><a name="p13801142315236"></a><strong id="b842352706134712_9"><a name="b842352706134712_9"></a><a name="b842352706134712_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row178017235237"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p78011923122316"><a name="p78011923122316"></a><a name="p78011923122316"></a>day</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p2080113231233"><a name="p2080113231233"></a><a name="p2080113231233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p480119235234"><a name="p480119235234"></a><a name="p480119235234"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p119771882412"><a name="p119771882412"></a><a name="p119771882412"></a>Maintenance time in each week in the unit of day. The value can be one of the following:</p>
    <a name="ul797318182413"></a><a name="ul797318182413"></a><ul id="ul797318182413"><li><strong id="b842352706144024"><a name="b842352706144024"></a><a name="b842352706144024"></a>Mon</strong></li><li><strong id="b842352706144031"><a name="b842352706144031"></a><a name="b842352706144031"></a>Tue</strong></li><li><strong id="b842352706144043"><a name="b842352706144043"></a><a name="b842352706144043"></a>Wed</strong></li><li><strong id="b842352706144048"><a name="b842352706144048"></a><a name="b842352706144048"></a>Thu</strong></li><li><strong id="b842352706144055"><a name="b842352706144055"></a><a name="b842352706144055"></a>Fri</strong></li><li><strong id="b84235270614412"><a name="b84235270614412"></a><a name="b84235270614412"></a>Sat</strong></li><li><strong id="b84235270614419"><a name="b84235270614419"></a><a name="b84235270614419"></a>Sun</strong></li></ul>
    </td>
    </tr>
    <tr id="row480152317232"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p7801152342312"><a name="p7801152342312"></a><a name="p7801152342312"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p580119237239"><a name="p580119237239"></a><a name="p580119237239"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p17801122372316"><a name="p17801122372316"></a><a name="p17801122372316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p14801102313237"><a name="p14801102313237"></a><a name="p14801102313237"></a>Maintenance start time. The format is <strong id="b842352706174833_1_1"><a name="b842352706174833_1_1"></a><a name="b842352706174833_1_1"></a>HH:mm</strong>. The time zone is GMT+0.</p>
    </td>
    </tr>
    <tr id="row17801192372311"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p5801112319232"><a name="p5801112319232"></a><a name="p5801112319232"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p480119232231"><a name="p480119232231"></a><a name="p480119232231"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p88011233233"><a name="p88011233233"></a><a name="p88011233233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p1580132313233"><a name="p1580132313233"></a><a name="p1580132313233"></a>Maintenance end time. The format is <strong id="b842352706174833_1_3"><a name="b842352706174833_1_3"></a><a name="b842352706174833_1_3"></a>HH:mm</strong>. The time zone is GMT+0.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **resize\_info**  field data structure description

    <a name="table11415448252"></a>
    <table><thead align="left"><tr id="row4454414253"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p1880250142519"><a name="p1880250142519"></a><a name="p1880250142519"></a><strong id="b84235270611710_11"><a name="b84235270611710_11"></a><a name="b84235270611710_11"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p04114492515"><a name="p04114492515"></a><a name="p04114492515"></a><strong id="b6167984116271_15"><a name="b6167984116271_15"></a><a name="b6167984116271_15"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p041244152511"><a name="p041244152511"></a><a name="p041244152511"></a><strong id="b84235270617235_15"><a name="b84235270617235_15"></a><a name="b84235270617235_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.2.5.1.4"><p id="p16413445257"><a name="p16413445257"></a><a name="p16413445257"></a><strong id="b842352706134712_11"><a name="b842352706134712_11"></a><a name="b842352706134712_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13454415254"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p114194412254"><a name="p114194412254"></a><a name="p114194412254"></a>target_node_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p17415446259"><a name="p17415446259"></a><a name="p17415446259"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p4474492512"><a name="p4474492512"></a><a name="p4474492512"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p1241644202519"><a name="p1241644202519"></a><a name="p1241644202519"></a>Number of nodes after the scale-out</p>
    </td>
    </tr>
    <tr id="row11414482511"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p9420444253"><a name="p9420444253"></a><a name="p9420444253"></a>origin_node_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p2454413255"><a name="p2454413255"></a><a name="p2454413255"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p144174422510"><a name="p144174422510"></a><a name="p144174422510"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p941844152510"><a name="p941844152510"></a><a name="p941844152510"></a>Number of nodes before the scale-out</p>
    </td>
    </tr>
    <tr id="row1641044122515"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p539215431962"><a name="p539215431962"></a><a name="p539215431962"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p841444192517"><a name="p841444192517"></a><a name="p841444192517"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p741444172512"><a name="p741444172512"></a><a name="p741444172512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p78051416277"><a name="p78051416277"></a><a name="p78051416277"></a>Scale-out status. The value can be either of the following:</p>
    <a name="ul280414152720"></a><a name="ul280414152720"></a><ul id="ul280414152720"><li><strong id="b84235270617363_5"><a name="b84235270617363_5"></a><a name="b84235270617363_5"></a>GROWING</strong></li><li><strong id="b842352706162543_3"><a name="b842352706162543_3"></a><a name="b842352706162543_3"></a>RESIZE_FAILURE</strong></li></ul>
    </td>
    </tr>
    <tr id="row114844142519"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p143212011917"><a name="p143212011917"></a><a name="p143212011917"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p1441744102510"><a name="p1441744102510"></a><a name="p1441744102510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p1148441254"><a name="p1148441254"></a><a name="p1148441254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.5.1.4 "><p id="p145444252"><a name="p145444252"></a><a name="p145444252"></a>Scale-out start time. The format is <strong id="b842352706174833_1_5"><a name="b842352706174833_1_5"></a><a name="b842352706174833_1_5"></a>ISO8601:YYYY-MM-DDThh:mm:ss</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **failed\_reasons**  field data structure description

    <a name="table1501965285"></a>
    <table><thead align="left"><tr id="row75013611284"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p4501568284"><a name="p4501568284"></a><a name="p4501568284"></a><strong id="b84235270611710_13"><a name="b84235270611710_13"></a><a name="b84235270611710_13"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p1950166142814"><a name="p1950166142814"></a><a name="p1950166142814"></a><strong id="b6167984116271_17"><a name="b6167984116271_17"></a><a name="b6167984116271_17"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p2050126182815"><a name="p2050126182815"></a><a name="p2050126182815"></a><strong id="b84235270617235_17"><a name="b84235270617235_17"></a><a name="b84235270617235_17"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="p2050262284"><a name="p2050262284"></a><a name="p2050262284"></a><strong id="b842352706134712_13"><a name="b842352706134712_13"></a><a name="b842352706134712_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6505622812"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p20509613284"><a name="p20509613284"></a><a name="p20509613284"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p4501369288"><a name="p4501369288"></a><a name="p4501369288"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p145015619284"><a name="p145015619284"></a><a name="p145015619284"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p63112523397"><a name="p63112523397"></a><a name="p63112523397"></a>Error code. Possible values can be:</p>
    <a name="ul2311452143914"></a><a name="ul2311452143914"></a><ul id="ul2311452143914"><li><strong id="b842352706154429"><a name="b842352706154429"></a><a name="b842352706154429"></a>DWS.6000</strong>: indicates that cluster creation fails.</li><li><strong id="b842352706154441"><a name="b842352706154441"></a><a name="b842352706154441"></a>DWS.6001</strong>: indicates that cluster scale-out fails.</li><li><strong id="b842352706154556"><a name="b842352706154556"></a><a name="b842352706154556"></a>DWS.6002</strong>: indicates that cluster restart fails.</li><li><strong id="b1711244489154721"><a name="b1711244489154721"></a><a name="b1711244489154721"></a>DWS.6003</strong>: indicates that cluster restoration fails.</li></ul>
    </td>
    </tr>
    <tr id="row55036172817"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p13505612282"><a name="p13505612282"></a><a name="p13505612282"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1050567289"><a name="p1050567289"></a><a name="p1050567289"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1050867281"><a name="p1050867281"></a><a name="p1050867281"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p5501968282"><a name="p5501968282"></a><a name="p5501968282"></a>Error message</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **tags**  field data structure description

    <a name="table16661175514414"></a>
    <table><thead align="left"><tr id="row176611555144412"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p176610550446"><a name="p176610550446"></a><a name="p176610550446"></a><strong id="b84235270611710_15"><a name="b84235270611710_15"></a><a name="b84235270611710_15"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p66611755104414"><a name="p66611755104414"></a><a name="p66611755104414"></a><strong id="b6167984116271_19"><a name="b6167984116271_19"></a><a name="b6167984116271_19"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p566125584411"><a name="p566125584411"></a><a name="p566125584411"></a><strong id="b84235270617235_19"><a name="b84235270617235_19"></a><a name="b84235270617235_19"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="p1866135594419"><a name="p1866135594419"></a><a name="p1866135594419"></a><strong id="b842352706134712_15"><a name="b842352706134712_15"></a><a name="b842352706134712_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row566125514443"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p166112553443"><a name="p166112553443"></a><a name="p166112553443"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p1366165544412"><a name="p1366165544412"></a><a name="p1366165544412"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p2066195518448"><a name="p2066195518448"></a><a name="p2066195518448"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p7661145516449"><a name="p7661145516449"></a><a name="p7661145516449"></a>Tag key</p>
    </td>
    </tr>
    <tr id="row56611355164417"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p136610553444"><a name="p136610553444"></a><a name="p136610553444"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p1566175512443"><a name="p1566175512443"></a><a name="p1566175512443"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p9661135517446"><a name="p9661135517446"></a><a name="p9661135517446"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p1266145518449"><a name="p1266145518449"></a><a name="p1266145518449"></a>Tag value</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **parameter\_group**  field data structure description

    <a name="table989317913224"></a>
    <table><thead align="left"><tr id="row13924199182213"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.1"><p id="p159402992219"><a name="p159402992219"></a><a name="p159402992219"></a><strong id="b84235270611710_17"><a name="b84235270611710_17"></a><a name="b84235270611710_17"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p209401596223"><a name="p209401596223"></a><a name="p209401596223"></a><strong id="b6167984116271_21"><a name="b6167984116271_21"></a><a name="b6167984116271_21"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p7940189162218"><a name="p7940189162218"></a><a name="p7940189162218"></a><strong id="b84235270617235_21"><a name="b84235270617235_21"></a><a name="b84235270617235_21"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="p169560919220"><a name="p169560919220"></a><a name="p169560919220"></a><strong id="b842352706134712_17"><a name="b842352706134712_17"></a><a name="b842352706134712_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39561997221"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p297116982218"><a name="p297116982218"></a><a name="p297116982218"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p1397111962218"><a name="p1397111962218"></a><a name="p1397111962218"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p3971109102216"><a name="p3971109102216"></a><a name="p3971109102216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p6987193229"><a name="p6987193229"></a><a name="p6987193229"></a>Parameter group ID</p>
    </td>
    </tr>
    <tr id="row1398711910223"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p198712972220"><a name="p198712972220"></a><a name="p198712972220"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p10341014228"><a name="p10341014228"></a><a name="p10341014228"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p4318104228"><a name="p4318104228"></a><a name="p4318104228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p121851017228"><a name="p121851017228"></a><a name="p121851017228"></a>Parameter group name</p>
    </td>
    </tr>
    <tr id="row83331325192310"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.1 "><p id="p153331225142319"><a name="p153331225142319"></a><a name="p153331225142319"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p6333162542319"><a name="p6333162542319"></a><a name="p6333162542319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p17333225122317"><a name="p17333225122317"></a><a name="p17333225122317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="p1333142552316"><a name="p1333142552316"></a><a name="p1333142552316"></a>Cluster parameter status. Possible values are:</p>
    <a name="ul1919585218247"></a><a name="ul1919585218247"></a><ul id="ul1919585218247"><li>In-Sync: synchronized</li><li>Applying: in application</li><li>Pending-Reboot: restart for the modification to take effect</li><li>Sync-Failure: application failure</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="s69cd3211bfc9442c99a71f8aa13fe2d8"></a>

-   Normal

    200

-   Abnormal 

    **Table  11**  Returned value description

    <a name="en-us_topic_0067607267_table33937134"></a>
    <table><thead align="left"><tr id="en-us_topic_0067607267_row16050694"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0067607267_p25037822"><a name="en-us_topic_0067607267_p25037822"></a><a name="en-us_topic_0067607267_p25037822"></a><strong id="b84235270693458"><a name="b84235270693458"></a><a name="b84235270693458"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0067607267_p14797678"><a name="en-us_topic_0067607267_p14797678"></a><a name="en-us_topic_0067607267_p14797678"></a><strong id="b842352706172443_5"><a name="b842352706172443_5"></a><a name="b842352706172443_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0067607267_row57761279"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p48152024"><a name="en-us_topic_0067607267_p48152024"></a><a name="en-us_topic_0067607267_p48152024"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p7999906"><a name="en-us_topic_0067607267_p7999906"></a><a name="en-us_topic_0067607267_p7999906"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row4890297"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p60569775"><a name="en-us_topic_0067607267_p60569775"></a><a name="en-us_topic_0067607267_p60569775"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p7204713"><a name="en-us_topic_0067607267_p7204713"></a><a name="en-us_topic_0067607267_p7204713"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row64842419"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p17744591"><a name="en-us_topic_0067607267_p17744591"></a><a name="en-us_topic_0067607267_p17744591"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p28025763"><a name="en-us_topic_0067607267_p28025763"></a><a name="en-us_topic_0067607267_p28025763"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row50905282"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p29687198"><a name="en-us_topic_0067607267_p29687198"></a><a name="en-us_topic_0067607267_p29687198"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p55852871"><a name="en-us_topic_0067607267_p55852871"></a><a name="en-us_topic_0067607267_p55852871"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row32913796"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p48771786"><a name="en-us_topic_0067607267_p48771786"></a><a name="en-us_topic_0067607267_p48771786"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p58200593"><a name="en-us_topic_0067607267_p58200593"></a><a name="en-us_topic_0067607267_p58200593"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0067607267_row54043292"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0067607267_p15430535"><a name="en-us_topic_0067607267_p15430535"></a><a name="en-us_topic_0067607267_p15430535"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0067607267_p41913798"><a name="en-us_topic_0067607267_p41913798"></a><a name="en-us_topic_0067607267_p41913798"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


