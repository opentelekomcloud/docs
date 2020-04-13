# Modifying Information About a DCS Instance<a name="EN-US_TOPIC_0237964387"></a>

## Function<a name="section20299897"></a>

This API is used to modify the name and description of a DCS instance.

## URI<a name="section48481349"></a>

-   URI format:

    PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}

-   Parameter description:

    [Table 1](#table61660876)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table61660876"></a>
<table><thead align="left"><tr id="row44806237"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5426570"><a name="p5426570"></a><a name="p5426570"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p36899007"><a name="p36899007"></a><a name="p36899007"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p36029605"><a name="p36029605"></a><a name="p36029605"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p32716899"><a name="p32716899"></a><a name="p32716899"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32823202"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p41433738"><a name="p41433738"></a><a name="p41433738"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p689602"><a name="p689602"></a><a name="p689602"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p55857778"><a name="p55857778"></a><a name="p55857778"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p28186179"><a name="p28186179"></a><a name="p28186179"></a>Project ID.</p>
</td>
</tr>
<tr id="row52349023"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12412484"><a name="p12412484"></a><a name="p12412484"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65887133"><a name="p65887133"></a><a name="p65887133"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p35257555"><a name="p35257555"></a><a name="p35257555"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37289677"><a name="p37289677"></a><a name="p37289677"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33678960"></a>

-   Request parameter:

    [Table 2](#table18076976)  describes request parameters.


**Table  2**  Parameter description

<a name="table18076976"></a>
<table><thead align="left"><tr id="row21124930"><th class="cellrowborder" valign="top" width="19.387755102040817%" id="mcps1.2.5.1.1"><p id="p33397760"><a name="p33397760"></a><a name="p33397760"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.285714285714285%" id="mcps1.2.5.1.2"><p id="p20864043"><a name="p20864043"></a><a name="p20864043"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.387755102040817%" id="mcps1.2.5.1.3"><p id="p12265898"><a name="p12265898"></a><a name="p12265898"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="46.93877551020408%" id="mcps1.2.5.1.4"><p id="p54013670"><a name="p54013670"></a><a name="p54013670"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13031110"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p48886962"><a name="p48886962"></a><a name="p48886962"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p421011"><a name="p421011"></a><a name="p421011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p34101969"><a name="p34101969"></a><a name="p34101969"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p10796115"><a name="p10796115"></a><a name="p10796115"></a>DCS instance name.</p>
<p id="p30056178"><a name="p30056178"></a><a name="p30056178"></a>An instance name is a string of 4–64 characters that contain letters, digits, underscores (_), and hyphens (-). An instance name must start with a letter.</p>
</td>
</tr>
<tr id="row2070146"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p33464133"><a name="p33464133"></a><a name="p33464133"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p26240261"><a name="p26240261"></a><a name="p26240261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p45086377"><a name="p45086377"></a><a name="p45086377"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p28117914"><a name="p28117914"></a><a name="p28117914"></a>Brief description of the DCS instance.</p>
<p id="p51734634"><a name="p51734634"></a><a name="p51734634"></a>A brief description supports up to 1024 characters.</p>
<div class="note" id="note62958527"><a name="note62958527"></a><a name="note62958527"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p29755832"><a name="p29755832"></a><a name="p29755832"></a>"\" is defined as an escape character in the queue description. If you need to enter a backward slash (\) or a double quotation mark (") in the queue description, enter <strong id="b66475904"><a name="b66475904"></a><a name="b66475904"></a>\\</strong> or <strong id="b61412231"><a name="b61412231"></a><a name="b61412231"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row15839175"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p7904761"><a name="p7904761"></a><a name="p7904761"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p36305920"><a name="p36305920"></a><a name="p36305920"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p55098436"><a name="p55098436"></a><a name="p55098436"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p33788332"><a name="p33788332"></a><a name="p33788332"></a>Backup policy.</p>
<p id="p35659537"><a name="p35659537"></a><a name="p35659537"></a>This parameter is available for master/standby DCS instances.</p>
<p id="p52500385"><a name="p52500385"></a><a name="p52500385"></a>For details, see <a href="creating-a-dcs-instance.md#table17319656205111">Table 3</a> and <a href="creating-a-dcs-instance.md#table1322175615513">Table 4</a>.</p>
</td>
</tr>
<tr id="row20728414"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p1279953"><a name="p1279953"></a><a name="p1279953"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p36567340"><a name="p36567340"></a><a name="p36567340"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p9164568"><a name="p9164568"></a><a name="p9164568"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p4132540"><a name="p4132540"></a><a name="p4132540"></a>Time at which the maintenance time window starts.</p>
<p id="p37192867"><a name="p37192867"></a><a name="p37192867"></a>Format: HH:mm:ss.</p>
<a name="ul66300353"></a><a name="ul66300353"></a><ul id="ul66300353"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see section <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The start time must be set to 22:00:00, 02:00:00, 06:00:00, 10:00:00, 14:00:00, or 18:00: 00.</li><li>Parameters <strong id="b39790453"><a name="b39790453"></a><a name="b39790453"></a>maintain_begin</strong> and <strong id="b22569763"><a name="b22569763"></a><a name="b22569763"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b1801279"><a name="b1801279"></a><a name="b1801279"></a>maintain_begin</strong> is left blank, parameter <strong id="b16211514"><a name="b16211514"></a><a name="b16211514"></a>maintain_end</strong> is also blank.</li></ul>
</td>
</tr>
<tr id="row11685901"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p7033928"><a name="p7033928"></a><a name="p7033928"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p32877271"><a name="p32877271"></a><a name="p32877271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p45813283"><a name="p45813283"></a><a name="p45813283"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p19888403"><a name="p19888403"></a><a name="p19888403"></a>Time at which the maintenance time window ends.</p>
<p id="p44777900"><a name="p44777900"></a><a name="p44777900"></a>Format: HH:mm:ss.</p>
<a name="ul347919"></a><a name="ul347919"></a><ul id="ul347919"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see section <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The end time is four hours later than the start time. For example, if the start time is 22:00:00, the end time is 02:00:00.</li><li>Parameters <strong id="b9004739"><a name="b9004739"></a><a name="b9004739"></a>maintain_begin</strong> and <strong id="b13933792"><a name="b13933792"></a><a name="b13933792"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b58295271"><a name="b58295271"></a><a name="b58295271"></a>maintain_end</strong> is left blank, parameter <strong id="b54895391"><a name="b54895391"></a><a name="b54895391"></a>maintain_start</strong> is also blank.</li></ul>
</td>
</tr>
<tr id="row24296474"><td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.1 "><p id="p21857415"><a name="p21857415"></a><a name="p21857415"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.2 "><p id="p25620180"><a name="p25620180"></a><a name="p25620180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.387755102040817%" headers="mcps1.2.5.1.3 "><p id="p61968681"><a name="p61968681"></a><a name="p61968681"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46.93877551020408%" headers="mcps1.2.5.1.4 "><p id="p53407279"><a name="p53407279"></a><a name="p53407279"></a>Security group ID.</p>
</td>
</tr>
</tbody>
</table>

-   Example request:

    ```
    //Example 1 
    { 
     "description": "instance description" 
    } 
    //Example 2  
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


## Response<a name="section34675187"></a>

-   Status code:

    If status code "204 No content" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    None.

-   Example response:

    None.


