# Restoring a Cluster<a name="dws_02_0032"></a>

## Function<a name="s4bb187ea1af94154b7c794fc9f01b061"></a>

This API is used to restore clusters using the snapshot.

## URI<a name="s6a55719cec1c4188a8156444c922d0d5"></a>

-   URI format

    POST /v1.0/\{project\_id\}/snapshots/\{snapshot\_id\}/actions

-   Parameter description

    **Table  1**  URI parameter description

    <a name="en-us_topic_0084768514_table64754634"></a>
    <table><thead align="left"><tr id="en-us_topic_0084768514_row57662920"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0084768514_p40184969"><a name="en-us_topic_0084768514_p40184969"></a><a name="en-us_topic_0084768514_p40184969"></a><strong id="b84235270617228"><a name="b84235270617228"></a><a name="b84235270617228"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0084768514_p33757095"><a name="en-us_topic_0084768514_p33757095"></a><a name="en-us_topic_0084768514_p33757095"></a><strong id="b6167984116271"><a name="b6167984116271"></a><a name="b6167984116271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="en-us_topic_0084768514_p49970185"><a name="en-us_topic_0084768514_p49970185"></a><a name="en-us_topic_0084768514_p49970185"></a><strong id="b84235270617235"><a name="b84235270617235"></a><a name="b84235270617235"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.5.1.4"><p id="en-us_topic_0084768514_p21053208"><a name="en-us_topic_0084768514_p21053208"></a><a name="en-us_topic_0084768514_p21053208"></a><strong id="b842352706172443"><a name="b842352706172443"></a><a name="b842352706172443"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0084768514_row27588283"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p20058459"><a name="en-us_topic_0084768514_p20058459"></a><a name="en-us_topic_0084768514_p20058459"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p14122463"><a name="en-us_topic_0084768514_p14122463"></a><a name="en-us_topic_0084768514_p14122463"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p3068848"><a name="en-us_topic_0084768514_p3068848"></a><a name="en-us_topic_0084768514_p3068848"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="p2031732215610"><a name="p2031732215610"></a><a name="p2031732215610"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="radbf3bb5426943b68cb03a24c2cf64b2"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="a03c8eca6755c43a48a273c9bf1365e53"><a name="a03c8eca6755c43a48a273c9bf1365e53"></a><a name="a03c8eca6755c43a48a273c9bf1365e53"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="a3bba5ae3c1bc4bcda5c516b68eb651ef"><a name="a3bba5ae3c1bc4bcda5c516b68eb651ef"></a><a name="a3bba5ae3c1bc4bcda5c516b68eb651ef"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="a7b0d688b70084f788ae2a5621c89bb0c"><a name="a7b0d688b70084f788ae2a5621c89bb0c"></a><a name="a7b0d688b70084f788ae2a5621c89bb0c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.5.1.4 "><p id="ad85c0540149049c9bbaec6f01f90fa8d"><a name="ad85c0540149049c9bbaec6f01f90fa8d"></a><a name="ad85c0540149049c9bbaec6f01f90fa8d"></a>Snapshot ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="sa8d6a7d82f7142a0b8f412a419261ad6"></a>

-   Sample request

    ```
    POST /v1.0/89cd04f168b84af6be287f71730fdb4b/snapshots/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba90/actions
    {"restore": {
            "name": "dws-1",
            "subnet_id": "374eca02-cfc4-4de7-8ab5-dbebf7d9a720",
            "security_group_id": "dc3ec145-9029-4b39-b5a3-ace5a01f772b",
            "vpc_id": "85b20d7e-9eb7-4b2a-98f3-3c8843ea3574",
            "availability_zone": "eu-de-01",
            "port": 8000,
            "public_ip": {
                "public_bind_type": "auto_assign",
                "eip_id": ""
            }
        }
    }
    ```


-   Parameter description

    **Table  2**  Request parameter description

    <a name="en-us_topic_0084768514_table20206181"></a>
    <table><thead align="left"><tr id="en-us_topic_0084768514_row50448354"><th class="cellrowborder" valign="top" width="18.91%" id="mcps1.2.5.1.1"><p id="en-us_topic_0084768514_p59784887"><a name="en-us_topic_0084768514_p59784887"></a><a name="en-us_topic_0084768514_p59784887"></a><strong id="b832955609"><a name="b832955609"></a><a name="b832955609"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.73%" id="mcps1.2.5.1.2"><p id="en-us_topic_0084768514_p10737664"><a name="en-us_topic_0084768514_p10737664"></a><a name="en-us_topic_0084768514_p10737664"></a><strong id="b2049186969"><a name="b2049186969"></a><a name="b2049186969"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0084768514_p64444454"><a name="en-us_topic_0084768514_p64444454"></a><a name="en-us_topic_0084768514_p64444454"></a><strong id="b1433795771"><a name="b1433795771"></a><a name="b1433795771"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.21000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0084768514_p52618256"><a name="en-us_topic_0084768514_p52618256"></a><a name="en-us_topic_0084768514_p52618256"></a><strong id="b1117622825"><a name="b1117622825"></a><a name="b1117622825"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0084768514_row34220326"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p20383058"><a name="en-us_topic_0084768514_p20383058"></a><a name="en-us_topic_0084768514_p20383058"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p40414969"><a name="en-us_topic_0084768514_p40414969"></a><a name="en-us_topic_0084768514_p40414969"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p52387077"><a name="en-us_topic_0084768514_p52387077"></a><a name="en-us_topic_0084768514_p52387077"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p15494878"><a name="en-us_topic_0084768514_p15494878"></a><a name="en-us_topic_0084768514_p15494878"></a>Object to be restored</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row5236179"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p21477321"><a name="en-us_topic_0084768514_p21477321"></a><a name="en-us_topic_0084768514_p21477321"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p61941440"><a name="en-us_topic_0084768514_p61941440"></a><a name="en-us_topic_0084768514_p61941440"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p51200735"><a name="en-us_topic_0084768514_p51200735"></a><a name="en-us_topic_0084768514_p51200735"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p53618895"><a name="en-us_topic_0084768514_p53618895"></a><a name="en-us_topic_0084768514_p53618895"></a>Cluster name, which must be unique. The cluster name must contain 4 to 64 characters, which consist of letters, digits, hyphens (-), or underscores (_) only and must start with a letter.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row11272110"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p40625737"><a name="en-us_topic_0084768514_p40625737"></a><a name="en-us_topic_0084768514_p40625737"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p2350413"><a name="en-us_topic_0084768514_p2350413"></a><a name="en-us_topic_0084768514_p2350413"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p56165728"><a name="en-us_topic_0084768514_p56165728"></a><a name="en-us_topic_0084768514_p56165728"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p53130157"><a name="en-us_topic_0084768514_p53130157"></a><a name="en-us_topic_0084768514_p53130157"></a>Subnet ID, which is used for configuring cluster network. The default value is the same as that of the original cluster.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row8409368"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p10070188"><a name="en-us_topic_0084768514_p10070188"></a><a name="en-us_topic_0084768514_p10070188"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p10378893"><a name="en-us_topic_0084768514_p10378893"></a><a name="en-us_topic_0084768514_p10378893"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p35383970"><a name="en-us_topic_0084768514_p35383970"></a><a name="en-us_topic_0084768514_p35383970"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p47529299"><a name="en-us_topic_0084768514_p47529299"></a><a name="en-us_topic_0084768514_p47529299"></a>VPC ID, which is used for configuring cluster network. The default value is the same as that of the original cluster.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row25110514"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p20685786"><a name="en-us_topic_0084768514_p20685786"></a><a name="en-us_topic_0084768514_p20685786"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p64935954"><a name="en-us_topic_0084768514_p64935954"></a><a name="en-us_topic_0084768514_p64935954"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p25320898"><a name="en-us_topic_0084768514_p25320898"></a><a name="en-us_topic_0084768514_p25320898"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p37726867"><a name="en-us_topic_0084768514_p37726867"></a><a name="en-us_topic_0084768514_p37726867"></a>ID of a security group. The ID is used for configuring cluster network. The default value is the same as that of the original cluster.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row3997487"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p55361044"><a name="en-us_topic_0084768514_p55361044"></a><a name="en-us_topic_0084768514_p55361044"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p55059565"><a name="en-us_topic_0084768514_p55059565"></a><a name="en-us_topic_0084768514_p55059565"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p30639779"><a name="en-us_topic_0084768514_p30639779"></a><a name="en-us_topic_0084768514_p30639779"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p65903005"><a name="en-us_topic_0084768514_p65903005"></a><a name="en-us_topic_0084768514_p65903005"></a>AZ of a cluster. The default value is the same as that of the original cluster.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row36319496"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p56198103"><a name="en-us_topic_0084768514_p56198103"></a><a name="en-us_topic_0084768514_p56198103"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p55752527"><a name="en-us_topic_0084768514_p55752527"></a><a name="en-us_topic_0084768514_p55752527"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p19660823"><a name="en-us_topic_0084768514_p19660823"></a><a name="en-us_topic_0084768514_p19660823"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p49022807"><a name="en-us_topic_0084768514_p49022807"></a><a name="en-us_topic_0084768514_p49022807"></a>Service port of a cluster (8000 to 10000). The default value is <strong id="b84235270694758"><a name="b84235270694758"></a><a name="b84235270694758"></a>8000</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row38552084"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p35711100"><a name="en-us_topic_0084768514_p35711100"></a><a name="en-us_topic_0084768514_p35711100"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p6918001"><a name="en-us_topic_0084768514_p6918001"></a><a name="en-us_topic_0084768514_p6918001"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p23487194"><a name="en-us_topic_0084768514_p23487194"></a><a name="en-us_topic_0084768514_p23487194"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p23414560"><a name="en-us_topic_0084768514_p23414560"></a><a name="en-us_topic_0084768514_p23414560"></a>Public IP address. If the value is not specified, public connection is not used by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row9404449"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p23562876"><a name="en-us_topic_0084768514_p23562876"></a><a name="en-us_topic_0084768514_p23562876"></a>public_bind_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p29544808"><a name="en-us_topic_0084768514_p29544808"></a><a name="en-us_topic_0084768514_p29544808"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p44319244"><a name="en-us_topic_0084768514_p44319244"></a><a name="en-us_topic_0084768514_p44319244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p33089041"><a name="en-us_topic_0084768514_p33089041"></a><a name="en-us_topic_0084768514_p33089041"></a>Binding type of an EIP. The value can be either of the following:</p>
    <a name="en-us_topic_0084768514_ul29365919"></a><a name="en-us_topic_0084768514_ul29365919"></a><ul id="en-us_topic_0084768514_ul29365919"><li><strong id="b842352706174142"><a name="b842352706174142"></a><a name="b842352706174142"></a>auto_assign</strong></li><li><strong id="b842352706174712"><a name="b842352706174712"></a><a name="b842352706174712"></a>not_use</strong></li><li><strong id="b842352706162651"><a name="b842352706162651"></a><a name="b842352706162651"></a>bind_existing</strong></li></ul>
    <p id="en-us_topic_0084768514_p27997"><a name="en-us_topic_0084768514_p27997"></a><a name="en-us_topic_0084768514_p27997"></a>The default value is <strong id="b842352706141151"><a name="b842352706141151"></a><a name="b842352706141151"></a>not_use</strong>. </p>
    </td>
    </tr>
    <tr id="r964166d21017459f9912ea5ad7bf6d3c"><td class="cellrowborder" valign="top" width="18.91%" headers="mcps1.2.5.1.1 "><p id="a91e89514786b46448b22d3f157ee648d"><a name="a91e89514786b46448b22d3f157ee648d"></a><a name="a91e89514786b46448b22d3f157ee648d"></a>eip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.73%" headers="mcps1.2.5.1.2 "><p id="aaff17b9d410141f1aaa51efa920eb5bf"><a name="aaff17b9d410141f1aaa51efa920eb5bf"></a><a name="aaff17b9d410141f1aaa51efa920eb5bf"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.5.1.3 "><p id="af5adcb82da99406d9519e1d1b58d80ec"><a name="af5adcb82da99406d9519e1d1b58d80ec"></a><a name="af5adcb82da99406d9519e1d1b58d80ec"></a>UUID</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.21000000000001%" headers="mcps1.2.5.1.4 "><p id="a7b7e148071784e248e63a862fd240a02"><a name="a7b7e148071784e248e63a862fd240a02"></a><a name="a7b7e148071784e248e63a862fd240a02"></a>EIP ID The default value is the same as that of the original cluster.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="sb3ef013c33a348739e46163a3251532e"></a>

-   Sample response

    ```
    {
        "cluster": {
            "id": "7d85f602-a948-4a30-afd4-e84f47471c15"
         }
    }
    ```


-   Parameter description

    **Table  3**  Response parameter description

    <a name="en-us_topic_0084768514_table66373591"></a>
    <table><thead align="left"><tr id="en-us_topic_0084768514_row53780604"><th class="cellrowborder" valign="top" width="16.96830316968303%" id="mcps1.2.5.1.1"><p id="en-us_topic_0084768514_p61261645"><a name="en-us_topic_0084768514_p61261645"></a><a name="en-us_topic_0084768514_p61261645"></a><strong id="b1012800411"><a name="b1012800411"></a><a name="b1012800411"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.47875212478752%" id="mcps1.2.5.1.2"><p id="en-us_topic_0084768514_p63246244"><a name="en-us_topic_0084768514_p63246244"></a><a name="en-us_topic_0084768514_p63246244"></a><strong id="b251843264"><a name="b251843264"></a><a name="b251843264"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10.05899410058994%" id="mcps1.2.5.1.3"><p id="en-us_topic_0084768514_p22672102"><a name="en-us_topic_0084768514_p22672102"></a><a name="en-us_topic_0084768514_p22672102"></a><strong id="b553260650"><a name="b553260650"></a><a name="b553260650"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60.493950604939506%" id="mcps1.2.5.1.4"><p id="en-us_topic_0084768514_p24500989"><a name="en-us_topic_0084768514_p24500989"></a><a name="en-us_topic_0084768514_p24500989"></a><strong id="b237411410"><a name="b237411410"></a><a name="b237411410"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0084768514_row38423121"><td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p25265097"><a name="en-us_topic_0084768514_p25265097"></a><a name="en-us_topic_0084768514_p25265097"></a>cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.47875212478752%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p33206990"><a name="en-us_topic_0084768514_p33206990"></a><a name="en-us_topic_0084768514_p33206990"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.05899410058994%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p5411655"><a name="en-us_topic_0084768514_p5411655"></a><a name="en-us_topic_0084768514_p5411655"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.493950604939506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p35690909"><a name="en-us_topic_0084768514_p35690909"></a><a name="en-us_topic_0084768514_p35690909"></a>Cluster object</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row52782726"><td class="cellrowborder" valign="top" width="16.96830316968303%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0084768514_p47542385"><a name="en-us_topic_0084768514_p47542385"></a><a name="en-us_topic_0084768514_p47542385"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.47875212478752%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0084768514_p25727981"><a name="en-us_topic_0084768514_p25727981"></a><a name="en-us_topic_0084768514_p25727981"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.05899410058994%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0084768514_p3591713"><a name="en-us_topic_0084768514_p3591713"></a><a name="en-us_topic_0084768514_p3591713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.493950604939506%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0084768514_p22493366"><a name="en-us_topic_0084768514_p22493366"></a><a name="en-us_topic_0084768514_p22493366"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Returned Value<a name="s47782db7ac574d0596c1a51df09a94cc"></a>

-   Normal

    200

-   Abnormal 

    **Table  4**  Returned value description

    <a name="en-us_topic_0084768514_table27978103"></a>
    <table><thead align="left"><tr id="en-us_topic_0084768514_row60105532"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.2.3.1.1"><p id="en-us_topic_0084768514_p36709949"><a name="en-us_topic_0084768514_p36709949"></a><a name="en-us_topic_0084768514_p36709949"></a><strong id="b842352706141543"><a name="b842352706141543"></a><a name="b842352706141543"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.3.1.2"><p id="en-us_topic_0084768514_p20715931"><a name="en-us_topic_0084768514_p20715931"></a><a name="en-us_topic_0084768514_p20715931"></a><strong id="b1206124419"><a name="b1206124419"></a><a name="b1206124419"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0084768514_row268861"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p21777804"><a name="en-us_topic_0084768514_p21777804"></a><a name="en-us_topic_0084768514_p21777804"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p19171695"><a name="en-us_topic_0084768514_p19171695"></a><a name="en-us_topic_0084768514_p19171695"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row38327532"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p17522377"><a name="en-us_topic_0084768514_p17522377"></a><a name="en-us_topic_0084768514_p17522377"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p10026414"><a name="en-us_topic_0084768514_p10026414"></a><a name="en-us_topic_0084768514_p10026414"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row23128868"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p61498985"><a name="en-us_topic_0084768514_p61498985"></a><a name="en-us_topic_0084768514_p61498985"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p15361866"><a name="en-us_topic_0084768514_p15361866"></a><a name="en-us_topic_0084768514_p15361866"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row4039073"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p58729529"><a name="en-us_topic_0084768514_p58729529"></a><a name="en-us_topic_0084768514_p58729529"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p59471393"><a name="en-us_topic_0084768514_p59471393"></a><a name="en-us_topic_0084768514_p59471393"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row65480490"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p2319502"><a name="en-us_topic_0084768514_p2319502"></a><a name="en-us_topic_0084768514_p2319502"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p53661974"><a name="en-us_topic_0084768514_p53661974"></a><a name="en-us_topic_0084768514_p53661974"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0084768514_row13195723"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0084768514_p62220677"><a name="en-us_topic_0084768514_p62220677"></a><a name="en-us_topic_0084768514_p62220677"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0084768514_p6710104"><a name="en-us_topic_0084768514_p6710104"></a><a name="en-us_topic_0084768514_p6710104"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


