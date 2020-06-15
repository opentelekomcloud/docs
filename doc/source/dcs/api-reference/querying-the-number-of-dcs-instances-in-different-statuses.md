# Querying the Number of DCS Instances in Different Statuses<a name="EN-US_TOPIC_0237964363"></a>

## Function<a name="section4729870"></a>

This API is used to query the number of DCS instances in different statuses.

## URI<a name="section42568836"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/status?includeFailure=\{includeFailure\}

-   Parameter description:

    [Table 1](#table50706425)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table50706425"></a>
<table><thead align="left"><tr id="row38006470"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p58625234"><a name="p58625234"></a><a name="p58625234"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p51023510"><a name="p51023510"></a><a name="p51023510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p39263675"><a name="p39263675"></a><a name="p39263675"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.5.1.4"><p id="p26241129"><a name="p26241129"></a><a name="p26241129"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45156679"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p33812349"><a name="p33812349"></a><a name="p33812349"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p54445748"><a name="p54445748"></a><a name="p54445748"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p48029459"><a name="p48029459"></a><a name="p48029459"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p65180995"><a name="p65180995"></a><a name="p65180995"></a>Project ID.</p>
</td>
</tr>
<tr id="row49758049"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3870157"><a name="p3870157"></a><a name="p3870157"></a>includeFailure</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p45047261"><a name="p45047261"></a><a name="p45047261"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p24949497"><a name="p24949497"></a><a name="p24949497"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p7643402"><a name="p7643402"></a><a name="p7643402"></a>An indicator of whether the number of DCS instances that failed to be created will be returned to the API caller.</p>
<p id="p1681762"><a name="p1681762"></a><a name="p1681762"></a>Options:</p>
<a name="ul15135864"></a><a name="ul15135864"></a><ul id="ul15135864"><li><strong id="b18045482"><a name="b18045482"></a><a name="b18045482"></a>true</strong>: The number of DCS instances that failed to be created will be returned to the API caller.</li><li><strong id="b52397961"><a name="b52397961"></a><a name="b52397961"></a>false</strong> or others: The number of DCS instances that failed to be created will not be returned to the API caller.</li></ul>
</td>
</tr>
</tbody>
</table>

-   Example URI:

    ```
    GET /v1.0/{project_id}/instances/status?includeFailure=true
    ```


## Request<a name="section47575204"></a>

None.

## Response<a name="section25523657"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#table89001053202017)  describes response parameters.


**Table  2**  Parameter description

<a name="table89001053202017"></a>
<table><thead align="left"><tr id="row67065735"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p63615456"><a name="p63615456"></a><a name="p63615456"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.4.1.2"><p id="p52578346"><a name="p52578346"></a><a name="p52578346"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.52525252525253%" id="mcps1.2.4.1.3"><p id="p30987661"><a name="p30987661"></a><a name="p30987661"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26972592"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37296315"><a name="p37296315"></a><a name="p37296315"></a>closed_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p1102679"><a name="p1102679"></a><a name="p1102679"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p22208171"><a name="p22208171"></a><a name="p22208171"></a>Number of instances that have been stopped.</p>
</td>
</tr>
<tr id="row65655818"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16521062"><a name="p16521062"></a><a name="p16521062"></a>creating_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p63137679"><a name="p63137679"></a><a name="p63137679"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p13878380"><a name="p13878380"></a><a name="p13878380"></a>Number of instances that are being created.</p>
</td>
</tr>
<tr id="row57796562"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51009945"><a name="p51009945"></a><a name="p51009945"></a>starting_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p38164872"><a name="p38164872"></a><a name="p38164872"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p4346952"><a name="p4346952"></a><a name="p4346952"></a>Number of instances that are being started.</p>
</td>
</tr>
<tr id="row39122574"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14811914"><a name="p14811914"></a><a name="p14811914"></a>deleting_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p58914346"><a name="p58914346"></a><a name="p58914346"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p7332694"><a name="p7332694"></a><a name="p7332694"></a>Number of instances that are being deleted.</p>
</td>
</tr>
<tr id="row65994253"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43934263"><a name="p43934263"></a><a name="p43934263"></a>closing_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p1905570"><a name="p1905570"></a><a name="p1905570"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p20133494"><a name="p20133494"></a><a name="p20133494"></a>Number of instances that are being stopped.</p>
</td>
</tr>
<tr id="row46983718"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p47584809"><a name="p47584809"></a><a name="p47584809"></a>running_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p29164329"><a name="p29164329"></a><a name="p29164329"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p13500429"><a name="p13500429"></a><a name="p13500429"></a>Number of running instances.</p>
</td>
</tr>
<tr id="row54395000"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43918894"><a name="p43918894"></a><a name="p43918894"></a>error_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p660668"><a name="p660668"></a><a name="p660668"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p53514187"><a name="p53514187"></a><a name="p53514187"></a>Number of abnormal instances.</p>
</td>
</tr>
<tr id="row11865643"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21592989"><a name="p21592989"></a><a name="p21592989"></a>restarting_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p4201700"><a name="p4201700"></a><a name="p4201700"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p4793448"><a name="p4793448"></a><a name="p4793448"></a>Number of instances that are being restarted.</p>
</td>
</tr>
<tr id="row43141036"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4763029"><a name="p4763029"></a><a name="p4763029"></a>createfailed_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p50261103"><a name="p50261103"></a><a name="p50261103"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p44617570"><a name="p44617570"></a><a name="p44617570"></a>Number of instances that fail to be created.</p>
</td>
</tr>
<tr id="row66013812"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45518526"><a name="p45518526"></a><a name="p45518526"></a>extending_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.4.1.2 "><p id="p63121972"><a name="p63121972"></a><a name="p63121972"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.52525252525253%" headers="mcps1.2.4.1.3 "><p id="p12606144"><a name="p12606144"></a><a name="p12606144"></a>Number of instances that are being scaled up.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    {  
     "closed_count": 0,  
     "extending_count": 0,  
     "creating_count": 0,  
     "starting_count": 0,  
     "deleting_count": 0,  
     "closing_count": 0,  
     "running_count": 16,  
     "error_count": 0,  
     "restarting_count": 0,  
     "createfailed_count": 44  
    }
    ```


