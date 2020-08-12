# Changing the Password of a DCS Instance<a name="dcs-api-0312019"></a>

## Function<a name="section624561415814"></a>

This API is used to change the password of a DCS instance.

## URI<a name="section10627123311133"></a>

PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}/password

[Table 1](#table1899262913382)  describes the parameters.

**Table  1**  Parameter description

<a name="table1899262913382"></a>
<table><thead align="left"><tr id="row1599115293389"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p15991152913819"><a name="p15991152913819"></a><a name="p15991152913819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p129916298387"><a name="p129916298387"></a><a name="p129916298387"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p13991142913384"><a name="p13991142913384"></a><a name="p13991142913384"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1991329193814"><a name="p1991329193814"></a><a name="p1991329193814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11992929163813"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p159911329153817"><a name="p159911329153817"></a><a name="p159911329153817"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18992192943819"><a name="p18992192943819"></a><a name="p18992192943819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p9992172933814"><a name="p9992172933814"></a><a name="p9992172933814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p20992829103811"><a name="p20992829103811"></a><a name="p20992829103811"></a>Project ID.</p>
</td>
</tr>
<tr id="row17992929193810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1899282919384"><a name="p1899282919384"></a><a name="p1899282919384"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p15992229153810"><a name="p15992229153810"></a><a name="p15992229153810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p199921129133818"><a name="p199921129133818"></a><a name="p199921129133818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p199212910384"><a name="p199212910384"></a><a name="p199212910384"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17412144620133"></a>

**Request parameters**

[Table 2](#table153111335113816)  describes the request parameters.

**Table  2**  Parameter description

<a name="table153111335113816"></a>
<table><thead align="left"><tr id="row73117359383"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p1031043517387"><a name="p1031043517387"></a><a name="p1031043517387"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.2"><p id="p19310113593814"><a name="p19310113593814"></a><a name="p19310113593814"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p93101035183813"><a name="p93101035183813"></a><a name="p93101035183813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="p173101235153817"><a name="p173101235153817"></a><a name="p173101235153817"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1631133513386"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p15311153513819"><a name="p15311153513819"></a><a name="p15311153513819"></a>old_password</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p83117356388"><a name="p83117356388"></a><a name="p83117356388"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p14311153513817"><a name="p14311153513817"></a><a name="p14311153513817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p93111435193817"><a name="p93111435193817"></a><a name="p93111435193817"></a>Old password. </p>
</td>
</tr>
<tr id="row1231173523817"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p163111355384"><a name="p163111355384"></a><a name="p163111355384"></a>new_password</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.2 "><p id="p11311153518384"><a name="p11311153518384"></a><a name="p11311153518384"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p53111335163815"><a name="p53111335163815"></a><a name="p53111335163815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p1151217611544"><a name="p1151217611544"></a><a name="p1151217611544"></a>New password.</p>
<p id="p166770201896"><a name="p166770201896"></a><a name="p166770201896"></a>Password complexity requirements:</p>
<a name="ul17145137175920"></a><a name="ul17145137175920"></a><ul id="ul17145137175920"><li>Must be a string consisting of 8 to 32 characters.</li><li>Must be different from the old password.</li><li>Contains at least three of the following character types:<a name="ul81451373599"></a><a name="ul81451373599"></a><ul id="ul81451373599"><li>Lowercase letters</li><li>Uppercase letters</li><li>Digits</li><li>Special characters (`~!@#$%^&amp;*()-_=+\|[{}]:'",&lt;.&gt;/?)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

**Example request**

```
PUT https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/password
```

```
{
    "old_password": "XXXXXX",
    "new_password": "XXXXXX"
}
```

## Response<a name="section1417213312142"></a>

**Response parameters**

[Table 3](#table1861319576383)  describes the response parameters.

**Table  3**  Parameter description

<a name="table1861319576383"></a>
<table><thead align="left"><tr id="row1961225712388"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p136126577389"><a name="p136126577389"></a><a name="p136126577389"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p76121757113816"><a name="p76121757113816"></a><a name="p76121757113816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p26121157123820"><a name="p26121157123820"></a><a name="p26121157123820"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row166121557203812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p661215713816"><a name="p661215713816"></a><a name="p661215713816"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1361217571386"><a name="p1361217571386"></a><a name="p1361217571386"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p161215718387"><a name="p161215718387"></a><a name="p161215718387"></a>An indicator of whether the password is successfully changed: Options:</p>
<a name="ul961213577385"></a><a name="ul961213577385"></a><ul id="ul961213577385"><li><strong id="b93281455124114"><a name="b93281455124114"></a><a name="b93281455124114"></a>Success</strong>: Password changed successfully.</li><li><strong id="b1620084214"><a name="b1620084214"></a><a name="b1620084214"></a>passwordFailed</strong>: The old password is incorrect.</li><li><strong id="b571619834211"><a name="b571619834211"></a><a name="b571619834211"></a>Locked</strong>: This account has been locked.</li><li><strong id="b9782141304213"><a name="b9782141304213"></a><a name="b9782141304213"></a>Failed</strong>: Failed to change the password.</li></ul>
</td>
</tr>
<tr id="row11613175783810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1661215710381"><a name="p1661215710381"></a><a name="p1661215710381"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p20613957153810"><a name="p20613957153810"></a><a name="p20613957153810"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p13613165713818"><a name="p13613165713818"></a><a name="p13613165713818"></a>Result of password change.</p>
</td>
</tr>
<tr id="row1861345773818"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p146132571380"><a name="p146132571380"></a><a name="p146132571380"></a>retry_times_left</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1693410516476"><a name="p1693410516476"></a><a name="p1693410516476"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p36131657153819"><a name="p36131657153819"></a><a name="p36131657153819"></a>Number of remaining password attempts. If the old password is incorrect, the value of this parameter is not <strong id="b1744113279352"><a name="b1744113279352"></a><a name="b1744113279352"></a>null</strong>.</p>
</td>
</tr>
<tr id="row156131057123818"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p156132057163817"><a name="p156132057163817"></a><a name="p156132057163817"></a>lock_time</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p1393235114720"><a name="p1393235114720"></a><a name="p1393235114720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p261395712388"><a name="p261395712388"></a><a name="p261395712388"></a>Account lockout duration. If the old password is incorrect or the account is locked, the value of this parameter is not <strong id="b298819137386"><a name="b298819137386"></a><a name="b298819137386"></a>null</strong>.</p>
</td>
</tr>
<tr id="row1961385710387"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1961345733810"><a name="p1961345733810"></a><a name="p1961345733810"></a>lock_time_left</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p8927551114720"><a name="p8927551114720"></a><a name="p8927551114720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p13613105783815"><a name="p13613105783815"></a><a name="p13613105783815"></a>Remaining time before the account is unlocked. If the account is locked, the value of this parameter is not <strong id="b1483134414398"><a name="b1483134414398"></a><a name="b1483134414398"></a>null</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
//Change password sucessful.
{
    "result" : "success",
    "message" : "Modify DCSInstance password success.",
    "retry_times_left" : "5",
    "lock_time" : "0",
    "lock_time_left" : "0"
}
//Change password failed.
{
    "result" : "passwordFailed",
    "message" : "verify password failed.",
    "retry_times_left" : "4",
    "lock_time" : "5",
    "lock_time_left" : "5"
}
```

## Status Code<a name="section4860101417132"></a>

[Table 4](#table486141410130)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  4**  Status code

<a name="table486141410130"></a>
<table><thead align="left"><tr id="row18616141139"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1986191418133"><a name="p1986191418133"></a><a name="p1986191418133"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p18861111415138"><a name="p18861111415138"></a><a name="p18861111415138"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row786131451312"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p6861114181311"><a name="p6861114181311"></a><a name="p6861114181311"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p48619143136"><a name="p48619143136"></a><a name="p48619143136"></a>Password changed successfully.</p>
</td>
</tr>
</tbody>
</table>

