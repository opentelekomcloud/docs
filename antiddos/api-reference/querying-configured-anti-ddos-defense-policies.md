# Querying Configured Anti-DDoS Defense Policies<a name="antiddos_02_0020"></a>

## Function<a name="section44180924"></a>

This API enables you to query configured Anti-DDoS defense policies. You can query the policy of a specified EIP.

## URI<a name="section62083996"></a>

-   URI format

    GET /v1/\{project\_id\}/antiddos/\{floating\_ip\_id\}

-   Parameter description

    <a name="table65178831"></a>
    <table><thead align="left"><tr id="row7351822"><th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.1"><p id="p58626732"><a name="p58626732"></a><a name="p58626732"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52824717528247%" id="mcps1.1.5.1.2"><p id="p51144826"><a name="p51144826"></a><a name="p51144826"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.617938206179375%" id="mcps1.1.5.1.3"><p id="p49090208"><a name="p49090208"></a><a name="p49090208"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.4"><p id="p16883911"><a name="p16883911"></a><a name="p16883911"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25419542"><td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.1 "><p id="p45717046"><a name="p45717046"></a><a name="p45717046"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52824717528247%" headers="mcps1.1.5.1.2 "><p id="p12093263"><a name="p12093263"></a><a name="p12093263"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p40030216"><a name="p40030216"></a><a name="p40030216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p21222025"><a name="p21222025"></a><a name="p21222025"></a>A user's ID</p>
    </td>
    </tr>
    <tr id="row56780500"><td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.1 "><p id="p35817813"><a name="p35817813"></a><a name="p35817813"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52824717528247%" headers="mcps1.1.5.1.2 "><p id="p15561779"><a name="p15561779"></a><a name="p15561779"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p52544597"><a name="p52544597"></a><a name="p52544597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p28253988"><a name="p28253988"></a><a name="p28253988"></a>ID corresponding to the EIP of a user</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section21885054"></a>

-   Request example

    ```
    GET /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/1df977c2-fdc6-4483-bc1c-ba46829f57b8
    ```


## Response<a name="section62747764"></a>

-   Element description

    <a name="table32841884"></a>
    <table><thead align="left"><tr id="row64992155"><th class="cellrowborder" valign="top" width="30.44%" id="mcps1.1.5.1.1"><p id="p29873218"><a name="p29873218"></a><a name="p29873218"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.2"><p id="p3811622"><a name="p3811622"></a><a name="p3811622"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.54%" id="mcps1.1.5.1.3"><p id="p40305966"><a name="p40305966"></a><a name="p40305966"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.54%" id="mcps1.1.5.1.4"><p id="p43557827"><a name="p43557827"></a><a name="p43557827"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38523084"><td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.1.5.1.1 "><p id="p33362098"><a name="p33362098"></a><a name="p33362098"></a>enable_L7</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p17975388"><a name="p17975388"></a><a name="p17975388"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p46720306"><a name="p46720306"></a><a name="p46720306"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.1.5.1.4 "><p id="p26248478"><a name="p26248478"></a><a name="p26248478"></a>Whether L7 defense has been enabled</p>
    </td>
    </tr>
    <tr id="row34909710"><td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.1.5.1.1 "><p id="p9114291"><a name="p9114291"></a><a name="p9114291"></a>traffic_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p60129"><a name="p60129"></a><a name="p60129"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p3079683015913"><a name="p3079683015913"></a><a name="p3079683015913"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.1.5.1.4 "><p id="p58963189"><a name="p58963189"></a><a name="p58963189"></a>Position ID of traffic. The value ranges from 1 to 9 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row60906657"><td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.1.5.1.1 "><p id="p34492175"><a name="p34492175"></a><a name="p34492175"></a>http_request_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p42402794"><a name="p42402794"></a><a name="p42402794"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p6409858615917"><a name="p6409858615917"></a><a name="p6409858615917"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.1.5.1.4 "><p id="p38491397"><a name="p38491397"></a><a name="p38491397"></a>Position ID of number of HTTP requests. The value ranges from 1 to 15 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row10878253"><td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.1.5.1.1 "><p id="p8723262"><a name="p8723262"></a><a name="p8723262"></a>cleaning_access_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p35495616"><a name="p35495616"></a><a name="p35495616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p1175927815921"><a name="p1175927815921"></a><a name="p1175927815921"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.1.5.1.4 "><p id="p18980661"><a name="p18980661"></a><a name="p18980661"></a>Position ID of access limit during cleaning. The value ranges from 1 to 8 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row36608226"><td class="cellrowborder" valign="top" width="30.44%" headers="mcps1.1.5.1.1 "><p id="p12476353"><a name="p12476353"></a><a name="p12476353"></a>app_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.2 "><p id="p3951668"><a name="p3951668"></a><a name="p3951668"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p4577985515925"><a name="p4577985515925"></a><a name="p4577985515925"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.54%" headers="mcps1.1.5.1.4 "><div class="p" id="p5423486315930"><a name="p5423486315930"></a><a name="p5423486315930"></a>Application type ID. Possible values:<a name="ul3859304915932"></a><a name="ul3859304915932"></a><ul id="ul3859304915932"><li>0</li><li>1</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "enable_L7": true,
       "traffic_pos_id": 1,
       "http_request_pos_id": 1,
       "cleaning_access_pos_id": 1,
       "app_type_id": 1
    }
    ```


## Returned Value<a name="section27858965"></a>

See  [Status Code](status-code.md).

