# Querying DCS Instance Restoration Records<a name="EN-US_TOPIC_0237964372"></a>

## Function<a name="section19609461"></a>

This API is used to query the restoration records of a specified DCS instance.

## URI<a name="section42267424"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/restores?start=\{start\}&limit=\{limit\}&beginTime=\{beginTime\}&endTime=\{endTime\}

-   Parameter description:

    [Table 1](#d0e6725)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e6725"></a>
<table><thead align="left"><tr id="row28032468"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p56037421"><a name="p56037421"></a><a name="p56037421"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p42737251"><a name="p42737251"></a><a name="p42737251"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p39165277"><a name="p39165277"></a><a name="p39165277"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p18270851"><a name="p18270851"></a><a name="p18270851"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3543999"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p18628470"><a name="p18628470"></a><a name="p18628470"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p32511122"><a name="p32511122"></a><a name="p32511122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16155259"><a name="p16155259"></a><a name="p16155259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p33507608"><a name="p33507608"></a><a name="p33507608"></a>Project ID.</p>
</td>
</tr>
<tr id="row33133022"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66529125"><a name="p66529125"></a><a name="p66529125"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p20150036"><a name="p20150036"></a><a name="p20150036"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p21540244"><a name="p21540244"></a><a name="p21540244"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p67038221"><a name="p67038221"></a><a name="p67038221"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row66473078"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15610198"><a name="p15610198"></a><a name="p15610198"></a>start</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p56466498"><a name="p56466498"></a><a name="p56466498"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p10383651"><a name="p10383651"></a><a name="p10383651"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p35769441"><a name="p35769441"></a><a name="p35769441"></a>Start sequence number of the to-be-queried restoration record. By default, this parameter is set to <strong id="b53489518"><a name="b53489518"></a><a name="b53489518"></a>1</strong>.</p>
</td>
</tr>
<tr id="row11643619"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3609106"><a name="p3609106"></a><a name="p3609106"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p23902165"><a name="p23902165"></a><a name="p23902165"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p57027221"><a name="p57027221"></a><a name="p57027221"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p55802169"><a name="p55802169"></a><a name="p55802169"></a>Number of restoration records displayed on each page. The minimum value of this parameter is <strong id="b32457476"><a name="b32457476"></a><a name="b32457476"></a>1</strong>. If this parameter is not specified, 10 restoration records are displayed on each page by default.</p>
</td>
</tr>
<tr id="row23681834"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p39180367"><a name="p39180367"></a><a name="p39180367"></a>beginTime</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p19493136"><a name="p19493136"></a><a name="p19493136"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p35440215"><a name="p35440215"></a><a name="p35440215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p52085129"><a name="p52085129"></a><a name="p52085129"></a>Start time of the period to be queried.</p>
<p id="p66112983"><a name="p66112983"></a><a name="p66112983"></a>Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
<tr id="row58145936"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12200404"><a name="p12200404"></a><a name="p12200404"></a>endTime</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p48708668"><a name="p48708668"></a><a name="p48708668"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p53088049"><a name="p53088049"></a><a name="p53088049"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p5164698"><a name="p5164698"></a><a name="p5164698"></a>End time of the period to be queried.</p>
<p id="p46482286"><a name="p46482286"></a><a name="p46482286"></a>Format: yyyyMMddHHmmss, for example, 20170718235959.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section44862504"></a>

None.

## Response<a name="section1109357"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#d0e6860)  describes the response parameters.


**Table  2**  Parameter description

<a name="d0e6860"></a>
<table><thead align="left"><tr id="row8197194"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p59992969"><a name="p59992969"></a><a name="p59992969"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p27592345"><a name="p27592345"></a><a name="p27592345"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p20387490"><a name="p20387490"></a><a name="p20387490"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40773963"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p14356668"><a name="p14356668"></a><a name="p14356668"></a>restore_record_response</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p22039454"><a name="p22039454"></a><a name="p22039454"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p40365336"><a name="p40365336"></a><a name="p40365336"></a>Array of the restoration records. For details about backup_record_response, see <a href="#table36973149">Table 3</a>.</p>
</td>
</tr>
<tr id="row48366803"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25396983"><a name="p25396983"></a><a name="p25396983"></a>total_num</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p43889706"><a name="p43889706"></a><a name="p43889706"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p65405335"><a name="p65405335"></a><a name="p65405335"></a>Number of obtained restoration records.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the restore\_record\_response array

<a name="table36973149"></a>
<table><thead align="left"><tr id="row10063389"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.1"><p id="p9828220"><a name="p9828220"></a><a name="p9828220"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p57888388"><a name="p57888388"></a><a name="p57888388"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p58447836"><a name="p58447836"></a><a name="p58447836"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36654252"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p16204445"><a name="p16204445"></a><a name="p16204445"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p37491670"><a name="p37491670"></a><a name="p37491670"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p16926464"><a name="p16926464"></a><a name="p16926464"></a>Restoration status.</p>
<a name="ul18120455"></a><a name="ul18120455"></a><ul id="ul18120455"><li><strong id="b58470749"><a name="b58470749"></a><a name="b58470749"></a>waiting</strong>: DCS instance restoration is waiting to begin.</li><li><strong id="b38510199"><a name="b38510199"></a><a name="b38510199"></a>restoring</strong>: DCS instance restoration is in progress.</li><li><strong id="b32318397"><a name="b32318397"></a><a name="b32318397"></a>succeed</strong>: DCS instance restoration succeeded.</li><li><strong id="b544537"><a name="b544537"></a><a name="b544537"></a>failed</strong>: DCS instance restoration failed.</li></ul>
</td>
</tr>
<tr id="row4900833"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p61423222"><a name="p61423222"></a><a name="p61423222"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p9225108"><a name="p9225108"></a><a name="p9225108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p9036258"><a name="p9036258"></a><a name="p9036258"></a>Restoration progress.</p>
</td>
</tr>
<tr id="row14217458"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p10763468"><a name="p10763468"></a><a name="p10763468"></a>restore_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p66534570"><a name="p66534570"></a><a name="p66534570"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p20591093"><a name="p20591093"></a><a name="p20591093"></a>ID of the restoration record.</p>
</td>
</tr>
<tr id="row51102110"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p45630263"><a name="p45630263"></a><a name="p45630263"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p5063792"><a name="p5063792"></a><a name="p5063792"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p7513969"><a name="p7513969"></a><a name="p7513969"></a>ID of the backup record.</p>
</td>
</tr>
<tr id="row516860"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p41865725"><a name="p41865725"></a><a name="p41865725"></a>restore_remark</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p35680603"><a name="p35680603"></a><a name="p35680603"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p4447741"><a name="p4447741"></a><a name="p4447741"></a>Description of DCS instance restoration.</p>
</td>
</tr>
<tr id="row40029676"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p21178287"><a name="p21178287"></a><a name="p21178287"></a>backup_remark</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p37719724"><a name="p37719724"></a><a name="p37719724"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p35398793"><a name="p35398793"></a><a name="p35398793"></a>Description of DCS instance backup.</p>
</td>
</tr>
<tr id="row50153683"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p35916516"><a name="p35916516"></a><a name="p35916516"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p23556649"><a name="p23556649"></a><a name="p23556649"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p29040394"><a name="p29040394"></a><a name="p29040394"></a>Time at which the restoration task is created.</p>
</td>
</tr>
<tr id="row60036961"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p31155705"><a name="p31155705"></a><a name="p31155705"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p40584161"><a name="p40584161"></a><a name="p40584161"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p66091585"><a name="p66091585"></a><a name="p66091585"></a>Time at which DCS instance restoration completes.</p>
</td>
</tr>
<tr id="row57953358"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p63710422"><a name="p63710422"></a><a name="p63710422"></a>restore_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p60270571"><a name="p60270571"></a><a name="p60270571"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p50078068"><a name="p50078068"></a><a name="p50078068"></a>Name of the restoration record.</p>
</td>
</tr>
<tr id="row48049432"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p66798763"><a name="p66798763"></a><a name="p66798763"></a>backup_name</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p41990694"><a name="p41990694"></a><a name="p41990694"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p45803058"><a name="p45803058"></a><a name="p45803058"></a>Name of the backup record.</p>
</td>
</tr>
<tr id="row9574342"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.1 "><p id="p37324205"><a name="p37324205"></a><a name="p37324205"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p3361785"><a name="p3361785"></a><a name="p3361785"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p3869202"><a name="p3869202"></a><a name="p3869202"></a>Error code returned if DCS instance restoration fails.</p>
<p id="p34822823"><a name="p34822823"></a><a name="p34822823"></a>For details about error codes, see <a href="querying-dcs-instance-backup-records.md#table39834343">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "restore_record_response": [ 
            { 
                "status": "succeed", 
                "progress": "100.00", 
                "restore_id": "a6155972-800c-4170-a479-3231e907d2f6", 
                "backup_id": "f4823e9e-fe9b-4ffd-be79-4e5d6de272bb", 
                "restore_remark": "doctest", 
                "backup_remark": null, 
                "created_at": "2017-07-18T21:41:20.721Z", 
                "updated_at": "2017-07-18T21:41:35.182Z", 
                "restore_name": "restore_20170718214120", 
                "backup_name": "backup_20170718000002", 
                "error_code": null 
            } 
     ], 
     "total_num": 1 
    }
    ```


