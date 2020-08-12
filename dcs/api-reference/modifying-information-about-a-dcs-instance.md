# Modifying Information About a DCS Instance<a name="dcs-api-0312007"></a>

## Function<a name="section1160237530"></a>

This API is used to modify the information about a DCS instance, including the instance name, description, backup policy, start and end time of the maintenance window, and security group.

## **URI**<a name="section1280994914394"></a>

PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}

[Table 1](#table938420556341)  describes the parameters.

**Table  1**  Parameter description

<a name="table938420556341"></a>
<table><thead align="left"><tr id="row173849558349"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p33841155103412"><a name="p33841155103412"></a><a name="p33841155103412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p193842555348"><a name="p193842555348"></a><a name="p193842555348"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63841255173414"><a name="p63841255173414"></a><a name="p63841255173414"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p63841255193412"><a name="p63841255193412"></a><a name="p63841255193412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1038418553349"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p93841755143410"><a name="p93841755143410"></a><a name="p93841755143410"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p93841855183415"><a name="p93841855183415"></a><a name="p93841855183415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p3384155518344"><a name="p3384155518344"></a><a name="p3384155518344"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p173841855123420"><a name="p173841855123420"></a><a name="p173841855123420"></a>Project ID.</p>
</td>
</tr>
<tr id="row163841755113413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53841255193410"><a name="p53841255193410"></a><a name="p53841255193410"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p538414550343"><a name="p538414550343"></a><a name="p538414550343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1384165517346"><a name="p1384165517346"></a><a name="p1384165517346"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p0384455123420"><a name="p0384455123420"></a><a name="p0384455123420"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section143751710194016"></a>

**Request parameters**

[Table 2](#table785213273513)  describes the request parameters.

**Table  2**  Parameter description

<a name="table785213273513"></a>
<table><thead align="left"><tr id="row1585116223517"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p88511827356"><a name="p88511827356"></a><a name="p88511827356"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p58515253512"><a name="p58515253512"></a><a name="p58515253512"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="9%" id="mcps1.2.5.1.3"><p id="p1485112193510"><a name="p1485112193510"></a><a name="p1485112193510"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p10851925356"><a name="p10851925356"></a><a name="p10851925356"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1085112273514"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p1885119243518"><a name="p1885119243518"></a><a name="p1885119243518"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p10851112143519"><a name="p10851112143519"></a><a name="p10851112143519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p385117263516"><a name="p385117263516"></a><a name="p385117263516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p15851172133513"><a name="p15851172133513"></a><a name="p15851172133513"></a>DCS instance name.</p>
<p id="p5676152019920"><a name="p5676152019920"></a><a name="p5676152019920"></a>An instance name is a string of 4 to 64 characters that contain letters, digits, underscores (_), and hyphens (-) and must start with a letter.</p>
</td>
</tr>
<tr id="row198523215355"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p1685115211359"><a name="p1685115211359"></a><a name="p1685115211359"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1585216293512"><a name="p1585216293512"></a><a name="p1585216293512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p148521528356"><a name="p148521528356"></a><a name="p148521528356"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p1852124352"><a name="p1852124352"></a><a name="p1852124352"></a>Brief description of the DCS instance.</p>
<p id="p1782063116014"><a name="p1782063116014"></a><a name="p1782063116014"></a>A brief description supports up to 1024 characters.</p>
<div class="note" id="note450874595312"><a name="note450874595312"></a><a name="note450874595312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p155091445135316"><a name="p155091445135316"></a><a name="p155091445135316"></a>"\" is defined as an escape character in the queue description. If you need to enter a backward slash (\) or a double quotation mark (") in the queue description, enter <strong id="b12224005144110"><a name="b12224005144110"></a><a name="b12224005144110"></a>\\</strong> or <strong id="b5675418144110"><a name="b5675418144110"></a><a name="b5675418144110"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row27821175915"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p14303144614"><a name="p14303144614"></a><a name="p14303144614"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p183031446120"><a name="p183031446120"></a><a name="p183031446120"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p93031141411"><a name="p93031141411"></a><a name="p93031141411"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p10047281144121"><a name="p10047281144121"></a><a name="p10047281144121"></a>Backup policy.</p>
<p id="p355912469149"><a name="p355912469149"></a><a name="p355912469149"></a>This parameter is available for master/standby and cluster DCS instances. For details, see <a href="creating-a-dcs-instance.md#table12803218151513">Table 3</a> and <a href="creating-a-dcs-instance.md#table187492037201518">Table 4</a>.</p>
</td>
</tr>
<tr id="row10563194525819"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p1339311593585"><a name="p1339311593585"></a><a name="p1339311593585"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1839355913585"><a name="p1839355913585"></a><a name="p1839355913585"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p13393115916580"><a name="p13393115916580"></a><a name="p13393115916580"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p1058769144129"><a name="p1058769144129"></a><a name="p1058769144129"></a>Time at which the maintenance time window starts.</p>
<p id="p19394125913588"><a name="p19394125913588"></a><a name="p19394125913588"></a>Format: HH:mm:ss.</p>
<a name="ul1039485925815"></a><a name="ul1039485925815"></a><ul id="ul1039485925815"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-window.md">Querying Maintenance Time Window</a>.</li><li>The start time must be set to 22:00:00, 02:00:00, 06:00:00, 10:00:00, 14:00:00, or 18:00: 00.</li><li>Parameters <strong id="b56748219194258"><a name="b56748219194258"></a><a name="b56748219194258"></a>maintain_begin</strong> and <strong id="b40971925194258"><a name="b40971925194258"></a><a name="b40971925194258"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b587561699143218"><a name="b587561699143218"></a><a name="b587561699143218"></a>maintain_begin</strong> is left blank, parameter <strong id="b786701452143218"><a name="b786701452143218"></a><a name="b786701452143218"></a>maintain_end</strong> is also blank.</li></ul>
</td>
</tr>
<tr id="row311274695815"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p139425905813"><a name="p139425905813"></a><a name="p139425905813"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p12394195917585"><a name="p12394195917585"></a><a name="p12394195917585"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p123941059105813"><a name="p123941059105813"></a><a name="p123941059105813"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p58934172144144"><a name="p58934172144144"></a><a name="p58934172144144"></a>Time at which the maintenance time window ends.</p>
<p id="p10394205975819"><a name="p10394205975819"></a><a name="p10394205975819"></a>Format: HH:mm:ss.</p>
<a name="ul93951259155810"></a><a name="ul93951259155810"></a><ul id="ul93951259155810"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-window.md">Querying Maintenance Time Window</a>.</li></ul>
<a name="ul183951559135818"></a><a name="ul183951559135818"></a><ul id="ul183951559135818"><li>The end time is four hours later than the start time. For example, if the start time is 22:00:00, the end time is 02:00:00.</li><li>Parameters <strong id="b52982079194536"><a name="b52982079194536"></a><a name="b52982079194536"></a>maintain_begin</strong> and <strong id="b24090421194540"><a name="b24090421194540"></a><a name="b24090421194540"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b1274439765143241"><a name="b1274439765143241"></a><a name="b1274439765143241"></a>maintain_end</strong> is left blank, parameter <strong id="b2016295787143241"><a name="b2016295787143241"></a><a name="b2016295787143241"></a>maintain_start</strong> is also blank.</li></ul>
</td>
</tr>
<tr id="row1281151472916"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p5971325112912"><a name="p5971325112912"></a><a name="p5971325112912"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p49711125112910"><a name="p49711125112910"></a><a name="p49711125112910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p19710250295"><a name="p19710250295"></a><a name="p19710250295"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p797132511297"><a name="p797132511297"></a><a name="p797132511297"></a>Security group ID.</p>
<p id="p7952614184115"><a name="p7952614184115"></a><a name="p7952614184115"></a>The value can be obtained from the VPC console or the API.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

Request URL:

```
PUT https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}
```

-   Example 1

    ```
    {
        "description": "instance description"
    }
    ```

-   Example 2

    ```
    {
        "name": "dcs002",
        "description": "instance description",
        "instance_backup_policy": {
            "backup_type": "auto",
            "save_days": 1,
            "periodical_backup_plan": {
                "begin_at": "00:00-01:00",
                "period_type": "weekly",
                "backup_at": [
                    "1",
                    "2",
                    "3",
                    "4",
                    "6",
                    "7"
                ]
            }
        },
        "security_group_id": "18e9309f-f81a-4749-bb21-f74576292162",
        "maintain_begin": "02:00:00",
        "maintain_end": "06:00:00"
    }
    ```


## Response<a name="section1971312572428"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section1375913561211"></a>

[Table 3](#table1475915181216)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  3**  Status code

<a name="table1475915181216"></a>
<table><thead align="left"><tr id="row97607581218"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1676020511123"><a name="p1676020511123"></a><a name="p1676020511123"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p18760351121"><a name="p18760351121"></a><a name="p18760351121"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row177611155124"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p37612517124"><a name="p37612517124"></a><a name="p37612517124"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p776112513121"><a name="p776112513121"></a><a name="p776112513121"></a>DCS instance modified successfully.</p>
</td>
</tr>
</tbody>
</table>

