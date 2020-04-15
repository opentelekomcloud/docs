# Creating an EVS Replication Pair \(Deprecated\)<a name="evs_04_2044"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to create an EVS replication pair using a specified production disk and a disaster recovery \(DR\) disk. The production disk is in the primary AZ, and the DR disk is in the secondary AZ.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API has been deprecated. To use this function, see  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Constraints<a name="en-us_topic_0079693002_section26746391"></a>

-   Two EVS disks used to create the EVS replication pair have been created and belong to different AZs.
-   The types and capacities of the two EVS disks must be consistent.
-   If the DR disk has been attached to a server, the server must be stopped.

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-replications

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="25.3%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693002_p25151854"><a name="en-us_topic_0079693002_p25151854"></a><a name="en-us_topic_0079693002_p25151854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.12%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693002_p1556805116115"><a name="en-us_topic_0079693002_p1556805116115"></a><a name="en-us_topic_0079693002_p1556805116115"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.58%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693002_p2565159161120"><a name="en-us_topic_0079693002_p2565159161120"></a><a name="en-us_topic_0079693002_p2565159161120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="25.3%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p10190321"><a name="en-us_topic_0079693002_p10190321"></a><a name="en-us_topic_0079693002_p10190321"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p60774950161114"><a name="en-us_topic_0079693002_p60774950161114"></a><a name="en-us_topic_0079693002_p60774950161114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p3475817"><a name="en-us_topic_0079693002_p3475817"></a><a name="en-us_topic_0079693002_p3475817"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="table7739348341"></a>
    <table><thead align="left"><tr id="row18755194816419"><th class="cellrowborder" valign="top" width="23.46%" id="mcps1.1.5.1.1"><p id="p5755648740"><a name="p5755648740"></a><a name="p5755648740"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.71%" id="mcps1.1.5.1.2"><p id="p97551848348"><a name="p97551848348"></a><a name="p97551848348"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.5.1.3"><p id="p6755548449"><a name="p6755548449"></a><a name="p6755548449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.540000000000006%" id="mcps1.1.5.1.4"><p id="p1977113481149"><a name="p1977113481149"></a><a name="p1977113481149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1877119480410"><td class="cellrowborder" valign="top" width="23.46%" headers="mcps1.1.5.1.1 "><p id="p142732231153"><a name="p142732231153"></a><a name="p142732231153"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.71%" headers="mcps1.1.5.1.2 "><p id="p117711482418"><a name="p117711482418"></a><a name="p117711482418"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.3 "><p id="p1366719501195"><a name="p1366719501195"></a><a name="p1366719501195"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.540000000000006%" headers="mcps1.1.5.1.4 "><p id="p137712486417"><a name="p137712486417"></a><a name="p137712486417"></a>Specifies the replication pair creation marker. For details, see <a href="#en-us_topic_0079693002_li50842877">Parameters in the replication field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="en-us_topic_0079693002_li50842877"></a>Parameters in the  **replication**  field

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="22.000000000000004%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p8696081161227"><a name="en-us_topic_0079693002_p8696081161227"></a><a name="en-us_topic_0079693002_p8696081161227"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.000000000000007%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p33293980161227"><a name="en-us_topic_0079693002_p33293980161227"></a><a name="en-us_topic_0079693002_p33293980161227"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.000000000000004%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079693002_p12457872161227"><a name="en-us_topic_0079693002_p12457872161227"></a><a name="en-us_topic_0079693002_p12457872161227"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2454675161227"><a name="en-us_topic_0079693002_p2454675161227"></a><a name="en-us_topic_0079693002_p2454675161227"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693002_p52610097"><a name="en-us_topic_0079693002_p52610097"></a><a name="en-us_topic_0079693002_p52610097"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.000000000000007%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p56892285161248"><a name="en-us_topic_0079693002_p56892285161248"></a><a name="en-us_topic_0079693002_p56892285161248"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693002_p33962670"><a name="en-us_topic_0079693002_p33962670"></a><a name="en-us_topic_0079693002_p33962670"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693002_p66621782"><a name="en-us_topic_0079693002_p66621782"></a><a name="en-us_topic_0079693002_p66621782"></a>Specifies the name of the EVS replication pair. The name can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row62725128"><td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693002_p47570623"><a name="en-us_topic_0079693002_p47570623"></a><a name="en-us_topic_0079693002_p47570623"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.000000000000007%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p22690068161253"><a name="en-us_topic_0079693002_p22690068161253"></a><a name="en-us_topic_0079693002_p22690068161253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693002_p54645451"><a name="en-us_topic_0079693002_p54645451"></a><a name="en-us_topic_0079693002_p54645451"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693002_p64205424"><a name="en-us_topic_0079693002_p64205424"></a><a name="en-us_topic_0079693002_p64205424"></a>Specifies the description of the EVS replication pair. The description can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row40977906"><td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693002_p30876117"><a name="en-us_topic_0079693002_p30876117"></a><a name="en-us_topic_0079693002_p30876117"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.000000000000007%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p22906808161259"><a name="en-us_topic_0079693002_p22906808161259"></a><a name="en-us_topic_0079693002_p22906808161259"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693002_p43653635"><a name="en-us_topic_0079693002_p43653635"></a><a name="en-us_topic_0079693002_p43653635"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693002_p46283551"><a name="en-us_topic_0079693002_p46283551"></a><a name="en-us_topic_0079693002_p46283551"></a>Specifies the IDs of the EVS disks used to create the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row13898779"><td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.5.1.1 "><p id="p1876249594649"><a name="p1876249594649"></a><a name="p1876249594649"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.000000000000007%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p1574641916133"><a name="en-us_topic_0079693002_p1574641916133"></a><a name="en-us_topic_0079693002_p1574641916133"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693002_p43945239"><a name="en-us_topic_0079693002_p43945239"></a><a name="en-us_topic_0079693002_p43945239"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693002_p2794612"><a name="en-us_topic_0079693002_p2794612"></a><a name="en-us_topic_0079693002_p2794612"></a>Specifies the primary AZ of the EVS replication pair, that is, the AZ where the production disk belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row25151514"><td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0079693002_p24006753"><a name="en-us_topic_0079693002_p24006753"></a><a name="en-us_topic_0079693002_p24006753"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.000000000000007%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0079693002_p807284516137"><a name="en-us_topic_0079693002_p807284516137"></a><a name="en-us_topic_0079693002_p807284516137"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.000000000000004%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0079693002_p3805200"><a name="en-us_topic_0079693002_p3805200"></a><a name="en-us_topic_0079693002_p3805200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0079693002_p39785801"><a name="en-us_topic_0079693002_p39785801"></a><a name="en-us_topic_0079693002_p39785801"></a>Specifies the type of the EVS replication pair. Currently, only type <strong id="b842352706141934"><a name="b842352706141934"></a><a name="b842352706141934"></a>hypermetro</strong> is supported.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "replication": {
            "name": "my replication", 
            "description": "my replication", 
            "volume_ids": [
                "18aa67ea-c7cb-4826-800d-50e67f0de75b", 
                "375d23be-3658-498f-8b50-d3b950a890ec"
            ], 
            "priority_station": "az2.dc2", 
            "replication_model": "hypermetro"
        }
    }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="en-us_topic_0079693002_table55223077"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row47625437"><th class="cellrowborder" valign="top" width="29.73%" id="mcps1.1.4.1.1"><p id="en-us_topic_0079693002_p42340960161635"><a name="en-us_topic_0079693002_p42340960161635"></a><a name="en-us_topic_0079693002_p42340960161635"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.32%" id="mcps1.1.4.1.2"><p id="en-us_topic_0079693002_p35455910161635"><a name="en-us_topic_0079693002_p35455910161635"></a><a name="en-us_topic_0079693002_p35455910161635"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.95%" id="mcps1.1.4.1.3"><p id="en-us_topic_0079693002_p53356433161635"><a name="en-us_topic_0079693002_p53356433161635"></a><a name="en-us_topic_0079693002_p53356433161635"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1217173215718"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="p121715321073"><a name="p121715321073"></a><a name="p121715321073"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="p1217120321771"><a name="p1217120321771"></a><a name="p1217120321771"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="p81717321073"><a name="p81717321073"></a><a name="p81717321073"></a>Specifies the EVS replication pair information.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row45298596"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p45307656"><a name="en-us_topic_0079693002_p45307656"></a><a name="en-us_topic_0079693002_p45307656"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p38378011"><a name="en-us_topic_0079693002_p38378011"></a><a name="en-us_topic_0079693002_p38378011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p21611161"><a name="en-us_topic_0079693002_p21611161"></a><a name="en-us_topic_0079693002_p21611161"></a>Specifies the ID of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row60282721"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p51062251"><a name="en-us_topic_0079693002_p51062251"></a><a name="en-us_topic_0079693002_p51062251"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p11982196"><a name="en-us_topic_0079693002_p11982196"></a><a name="en-us_topic_0079693002_p11982196"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p31033795"><a name="en-us_topic_0079693002_p31033795"></a><a name="en-us_topic_0079693002_p31033795"></a>Specifies the name of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row10868702"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p7949639"><a name="en-us_topic_0079693002_p7949639"></a><a name="en-us_topic_0079693002_p7949639"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p13994266"><a name="en-us_topic_0079693002_p13994266"></a><a name="en-us_topic_0079693002_p13994266"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p59793748"><a name="en-us_topic_0079693002_p59793748"></a><a name="en-us_topic_0079693002_p59793748"></a>Specifies the description of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row1272826"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p35990092"><a name="en-us_topic_0079693002_p35990092"></a><a name="en-us_topic_0079693002_p35990092"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p42015198"><a name="en-us_topic_0079693002_p42015198"></a><a name="en-us_topic_0079693002_p42015198"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p47787886"><a name="en-us_topic_0079693002_p47787886"></a><a name="en-us_topic_0079693002_p47787886"></a>Specifies the status of the EVS replication pair. For details, see <a href="evs-replication-pair-status-(deprecated).md">EVS Replication Pair Status (Deprecated)</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row27437792"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p29870405194653"><a name="en-us_topic_0079693002_p29870405194653"></a><a name="en-us_topic_0079693002_p29870405194653"></a>replication_consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p21844542194653"><a name="en-us_topic_0079693002_p21844542194653"></a><a name="en-us_topic_0079693002_p21844542194653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p24577506194653"><a name="en-us_topic_0079693002_p24577506194653"></a><a name="en-us_topic_0079693002_p24577506194653"></a>Specifies the ID of the replication consistency group where the EVS replication pair belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row41510976"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p6945858"><a name="en-us_topic_0079693002_p6945858"></a><a name="en-us_topic_0079693002_p6945858"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p4860205"><a name="en-us_topic_0079693002_p4860205"></a><a name="en-us_topic_0079693002_p4860205"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p58132325"><a name="en-us_topic_0079693002_p58132325"></a><a name="en-us_topic_0079693002_p58132325"></a>Specifies the IDs of the EVS disks used to create the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row53428882"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p32772220"><a name="en-us_topic_0079693002_p32772220"></a><a name="en-us_topic_0079693002_p32772220"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p1740610"><a name="en-us_topic_0079693002_p1740610"></a><a name="en-us_topic_0079693002_p1740610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p6771693"><a name="en-us_topic_0079693002_p6771693"></a><a name="en-us_topic_0079693002_p6771693"></a>Specifies the primary site of the EVS replication pair.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row60945241"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p37617525"><a name="en-us_topic_0079693002_p37617525"></a><a name="en-us_topic_0079693002_p37617525"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p49289224"><a name="en-us_topic_0079693002_p49289224"></a><a name="en-us_topic_0079693002_p49289224"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p33004241"><a name="en-us_topic_0079693002_p33004241"></a><a name="en-us_topic_0079693002_p33004241"></a>Specifies the creation time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0079693002_row28602718"><td class="cellrowborder" valign="top" width="29.73%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0079693002_p35118788"><a name="en-us_topic_0079693002_p35118788"></a><a name="en-us_topic_0079693002_p35118788"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.32%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0079693002_p29641146"><a name="en-us_topic_0079693002_p29641146"></a><a name="en-us_topic_0079693002_p29641146"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.95%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0079693002_p52122650"><a name="en-us_topic_0079693002_p52122650"></a><a name="en-us_topic_0079693002_p52122650"></a>Specifies the update time.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "replication": {
            "id": "91085433-9499-4a68-b2c6-35072467ccd2", 
            "name": "my replication", 
            "description": "my replication", 
            "status": "creating", 
            "replication_consistency_group_id": null, 
            "volume_ids": "18aa67ea-c7cb-4826-800d-50e67f0de75b, 375d23be-3658-498f-8b50-d3b950a890ec", 
            "priority_station": "az2.dc2", 
            "created_at": "2017-09-28T05:08:32.839953", 
            "updated_at": null
        }
    }
    ```


## Status Codes<a name="en-us_topic_0079693002_section60507121"></a>

-   Normal

    <a name="table4315991194956"></a>
    <table><thead align="left"><tr id="row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="p1363125894956"><a name="p1363125894956"></a><a name="p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="p3039012494956"><a name="p3039012494956"></a><a name="p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="p847584694956"><a name="p847584694956"></a><a name="p847584694956"></a>202</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="p1545496394956"><a name="p1545496394956"></a><a name="p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table22458872203835"></a>
    <table><thead align="left"><tr id="row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p6387753203835"><a name="p6387753203835"></a><a name="p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p47646009203835"><a name="p47646009203835"></a><a name="p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p12381163203835"><a name="p12381163203835"></a><a name="p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p63350108203835"><a name="p63350108203835"></a><a name="p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p11330608203835"><a name="p11330608203835"></a><a name="p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p45364094203835"><a name="p45364094203835"></a><a name="p45364094203835"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p52863895203835"><a name="p52863895203835"></a><a name="p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p54117066203835"><a name="p54117066203835"></a><a name="p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p58438642203835"><a name="p58438642203835"></a><a name="p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p35909542203835"><a name="p35909542203835"></a><a name="p35909542203835"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5599455203835"><a name="p5599455203835"></a><a name="p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p50902717203835"><a name="p50902717203835"></a><a name="p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p63988484203835"><a name="p63988484203835"></a><a name="p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p15684678203835"><a name="p15684678203835"></a><a name="p15684678203835"></a>The response generated by the server cannot be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25623884203835"><a name="p25623884203835"></a><a name="p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p62268733203835"><a name="p62268733203835"></a><a name="p62268733203835"></a>You must use the proxy server for authentication. Then, the request can be processed.</p>
    </td>
    </tr>
    <tr id="row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28314670203835"><a name="p28314670203835"></a><a name="p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11786919203835"><a name="p11786919203835"></a><a name="p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2729702203835"><a name="p2729702203835"></a><a name="p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p19779281203835"><a name="p19779281203835"></a><a name="p19779281203835"></a>The request cannot be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57799353203835"><a name="p57799353203835"></a><a name="p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p51235984203835"><a name="p51235984203835"></a><a name="p51235984203835"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38504500203835"><a name="p38504500203835"></a><a name="p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31856770203835"><a name="p31856770203835"></a><a name="p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3918444203835"><a name="p3918444203835"></a><a name="p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p48958538203835"><a name="p48958538203835"></a><a name="p48958538203835"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55967806203835"><a name="p55967806203835"></a><a name="p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p37098455203835"><a name="p37098455203835"></a><a name="p37098455203835"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p67010448203835"><a name="p67010448203835"></a><a name="p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59137180203835"><a name="p59137180203835"></a><a name="p59137180203835"></a>A gateway timeout error occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


