# Updating Anti-DDoS Defense Policies<a name="antiddos_02_0021"></a>

## Function<a name="section40911390"></a>

This API enables you to update the Anti-DDoS defense policy of a specified EIP. Successfully invoking this API only means that the service node has received the update request. You need to use the task querying API to check the task execution status. For details about the task querying API, see  [Querying Anti-DDoS Tasks](querying-anti-ddos-tasks.md).

## URI<a name="section32658192"></a>

-   URI format

    PUT /v1/\{project\_id\}/antiddos/\{floating\_ip\_id\}

-   Parameter description

    <a name="table52089545"></a>
    <table><thead align="left"><tr id="row17201705"><th class="cellrowborder" valign="top" width="27.167283271672826%" id="mcps1.1.5.1.1"><p id="p51160835"><a name="p51160835"></a><a name="p51160835"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.28787121287871%" id="mcps1.1.5.1.2"><p id="p50386953"><a name="p50386953"></a><a name="p50386953"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.617938206179375%" id="mcps1.1.5.1.3"><p id="p54811429"><a name="p54811429"></a><a name="p54811429"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.92690730926907%" id="mcps1.1.5.1.4"><p id="p10540732"><a name="p10540732"></a><a name="p10540732"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48492984"><td class="cellrowborder" valign="top" width="27.167283271672826%" headers="mcps1.1.5.1.1 "><p id="p35617665"><a name="p35617665"></a><a name="p35617665"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.28787121287871%" headers="mcps1.1.5.1.2 "><p id="p66458622"><a name="p66458622"></a><a name="p66458622"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p14439320"><a name="p14439320"></a><a name="p14439320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p28734262"><a name="p28734262"></a><a name="p28734262"></a>A user's ID</p>
    </td>
    </tr>
    <tr id="row57281770"><td class="cellrowborder" valign="top" width="27.167283271672826%" headers="mcps1.1.5.1.1 "><p id="p9311818"><a name="p9311818"></a><a name="p9311818"></a>floating_ip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.28787121287871%" headers="mcps1.1.5.1.2 "><p id="p16059811"><a name="p16059811"></a><a name="p16059811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.617938206179375%" headers="mcps1.1.5.1.3 "><p id="p25776284"><a name="p25776284"></a><a name="p25776284"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.92690730926907%" headers="mcps1.1.5.1.4 "><p id="p7504221"><a name="p7504221"></a><a name="p7504221"></a>ID corresponding to the EIP of a user</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25488274"></a>

-   Parameter description

    <a name="table1660410"></a>
    <table><thead align="left"><tr id="row30785969"><th class="cellrowborder" valign="top" width="30.3%" id="mcps1.1.5.1.1"><p id="p10635570"><a name="p10635570"></a><a name="p10635570"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.98%" id="mcps1.1.5.1.2"><p id="p56174843"><a name="p56174843"></a><a name="p56174843"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.94%" id="mcps1.1.5.1.3"><p id="p53868469"><a name="p53868469"></a><a name="p53868469"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.78%" id="mcps1.1.5.1.4"><p id="p1269896"><a name="p1269896"></a><a name="p1269896"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35752731"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p10290070"><a name="p10290070"></a><a name="p10290070"></a>enable_L7</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p28189346"><a name="p28189346"></a><a name="p28189346"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p1635686"><a name="p1635686"></a><a name="p1635686"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p65381771"><a name="p65381771"></a><a name="p65381771"></a>Whether to enable L7 defense</p>
    </td>
    </tr>
    <tr id="row51565033"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p16018178"><a name="p16018178"></a><a name="p16018178"></a>traffic_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p22404047"><a name="p22404047"></a><a name="p22404047"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p367798481566"><a name="p367798481566"></a><a name="p367798481566"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p24544935"><a name="p24544935"></a><a name="p24544935"></a>Position ID of traffic. The value ranges from 1 to 9 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row19577827"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p42300179"><a name="p42300179"></a><a name="p42300179"></a>http_request_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p3762492"><a name="p3762492"></a><a name="p3762492"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p2257395515612"><a name="p2257395515612"></a><a name="p2257395515612"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p56757654"><a name="p56757654"></a><a name="p56757654"></a>Position ID of number of HTTP requests. The value ranges from 1 to 15 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row41056841"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p37269850"><a name="p37269850"></a><a name="p37269850"></a>cleaning_access_pos_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p66067912"><a name="p66067912"></a><a name="p66067912"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p1659686615617"><a name="p1659686615617"></a><a name="p1659686615617"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><p id="p15422169"><a name="p15422169"></a><a name="p15422169"></a>Position ID of access limit during cleaning. The value ranges from 1 to 8 and 33 to 36.</p>
    </td>
    </tr>
    <tr id="row4581796"><td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.1.5.1.1 "><p id="p35581233"><a name="p35581233"></a><a name="p35581233"></a>app_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.1.5.1.2 "><p id="p63507614"><a name="p63507614"></a><a name="p63507614"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.94%" headers="mcps1.1.5.1.3 "><p id="p4066881915621"><a name="p4066881915621"></a><a name="p4066881915621"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.78%" headers="mcps1.1.5.1.4 "><div class="p" id="p2630238915650"><a name="p2630238915650"></a><a name="p2630238915650"></a>Application type ID. Possible values:<a name="ul2584619815657"></a><a name="ul2584619815657"></a><ul id="ul2584619815657"><li>0</li><li>1</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >If values of  **traffic\_pos\_id**,  **http\_request\_pos\_id**,  **cleaning\_access\_pos\_id**  are set between  **33 to 36**, their values must be the same.


-   Example request

    ```
    PUT /v1/67641fe6886f43fcb78edbbf0ad0b99f/antiddos/ee0c854e-082f-499e-b7d8-1b42c22781af
    ```

    ```
    {
        "enable_L7":false,
        "traffic_pos_id":2,
        "http_request_pos_id":1,
        "cleaning_access_pos_id":1,
        "app_type_id":1
    }
    ```


## Response<a name="section28067877"></a>

-   Element description

    <a name="table12060815"></a>
    <table><thead align="left"><tr id="row44341874"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.1.4.1.1"><p id="p34922074"><a name="p34922074"></a><a name="p34922074"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14%" id="mcps1.1.4.1.2"><p id="p10115730"><a name="p10115730"></a><a name="p10115730"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.1.4.1.3"><p id="p14067778"><a name="p14067778"></a><a name="p14067778"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65748243"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.1.4.1.1 "><p id="p24007468"><a name="p24007468"></a><a name="p24007468"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.4.1.2 "><p id="p65556790"><a name="p65556790"></a><a name="p65556790"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.1.4.1.3 "><p id="p8499801"><a name="p8499801"></a><a name="p8499801"></a>Internal error code</p>
    </td>
    </tr>
    <tr id="row9389347"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.1.4.1.1 "><p id="p22339613"><a name="p22339613"></a><a name="p22339613"></a>error_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.4.1.2 "><p id="p64678211"><a name="p64678211"></a><a name="p64678211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.1.4.1.3 "><p id="p4443775"><a name="p4443775"></a><a name="p4443775"></a>Internal error description</p>
    </td>
    </tr>
    <tr id="row39993975"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.1.4.1.1 "><p id="p18286572"><a name="p18286572"></a><a name="p18286572"></a>task_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.1.4.1.2 "><p id="p4817386"><a name="p4817386"></a><a name="p4817386"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.1.4.1.3 "><p id="p3932656116241"><a name="p3932656116241"></a><a name="p3932656116241"></a>ID of a task. This ID can be used to query the status of the task.</p>
    <p id="p54663960"><a name="p54663960"></a><a name="p54663960"></a>This field is reserved for use in task auditing later. It is temporarily unused.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "error_code": "10000000",
       "error_description": "Task has been received and is being processed.",
       "task_id": "4a4fefe7-34a1-40e2-a87c-16932af3ac4a"
    }
    ```


## Returned Value<a name="section51284307"></a>

See  [Status Code](status-code.md).

