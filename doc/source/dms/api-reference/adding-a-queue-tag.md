# Adding a Queue Tag<a name="EN-US_TOPIC_0128036882"></a>

## Function<a name="section327013445218"></a>

This API is used to add a queue tag. A maximum of 10 tags can be added to a queue.

This API is idempotent.

If the tag key to be created already exists, the previous tag is overwritten.

## URI<a name="section427515441826"></a>

POST /v1.0/\{project\_id\}/queue/\{queue\_id\}/tags

**Table  1**  Request header

<a name="table142831244224"></a>
<table><thead align="left"><tr id="row115984441224"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p1359824420217"><a name="p1359824420217"></a><a name="p1359824420217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p15600104415220"><a name="p15600104415220"></a><a name="p15600104415220"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p156001448211"><a name="p156001448211"></a><a name="p156001448211"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p1960084410214"><a name="p1960084410214"></a><a name="p1960084410214"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row12600644821"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p206001444626"><a name="p206001444626"></a><a name="p206001444626"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p15600164417211"><a name="p15600164417211"></a><a name="p15600164417211"></a>Indicates the MIME types of a request body.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p18600544528"><a name="p18600544528"></a><a name="p18600544528"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p1360016445211"><a name="p1360016445211"></a><a name="p1360016445211"></a>application/json</p>
</td>
</tr>
<tr id="row19600184419215"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p56004441326"><a name="p56004441326"></a><a name="p56004441326"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p460014442025"><a name="p460014442025"></a><a name="p460014442025"></a>Indicates the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p1160014414211"><a name="p1160014414211"></a><a name="p1160014414211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p66003441218"><a name="p66003441218"></a><a name="p66003441218"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameters

<a name="table133021944127"></a>
<table><thead align="left"><tr id="row46004449215"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5600144921"><a name="p5600144921"></a><a name="p5600144921"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p196006448220"><a name="p196006448220"></a><a name="p196006448220"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p146001744224"><a name="p146001744224"></a><a name="p146001744224"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p16600144414211"><a name="p16600144414211"></a><a name="p16600144414211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36020326116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2060273214111"><a name="p2060273214111"></a><a name="p2060273214111"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p80124841117"><a name="p80124841117"></a><a name="p80124841117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4311481117"><a name="p4311481117"></a><a name="p4311481117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1560303261110"><a name="p1560303261110"></a><a name="p1560303261110"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row14601344027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p156011844127"><a name="p156011844127"></a><a name="p156011844127"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p166015446210"><a name="p166015446210"></a><a name="p166015446210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p126011244426"><a name="p126011244426"></a><a name="p126011244426"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1760114449218"><a name="p1760114449218"></a><a name="p1760114449218"></a>Indicates the queue ID.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
 /v1.0/67c01b92944144a19d2da968ef34a912/queue/dd713484-e0b6-4e70-9942-4250e773d17c/tags
```

## Request<a name="section83272448218"></a>

[Table 3](#table3333134418220)  and  [Table 4](#table19345844328)  describe the parameters.

**Table  3**  Request parameters

<a name="table3333134418220"></a>
<table><thead align="left"><tr id="row260254410215"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1602204412212"><a name="p1602204412212"></a><a name="p1602204412212"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1360218441210"><a name="p1360218441210"></a><a name="p1360218441210"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p176021644427"><a name="p176021644427"></a><a name="p176021644427"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p560213441326"><a name="p560213441326"></a><a name="p560213441326"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16022444211"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p76023443217"><a name="p76023443217"></a><a name="p76023443217"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p5602114410213"><a name="p5602114410213"></a><a name="p5602114410213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p146026441022"><a name="p146026441022"></a><a name="p146026441022"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p11602744029"><a name="p11602744029"></a><a name="p11602744029"></a>Indicates a list of tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  tag parameter description

<a name="table19345844328"></a>
<table><thead align="left"><tr id="row460204413215"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p1160294418211"><a name="p1160294418211"></a><a name="p1160294418211"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1160274413219"><a name="p1160274413219"></a><a name="p1160274413219"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p166021544726"><a name="p166021544726"></a><a name="p166021544726"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p136028441926"><a name="p136028441926"></a><a name="p136028441926"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17603154411219"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p56031244727"><a name="p56031244727"></a><a name="p56031244727"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p56031344727"><a name="p56031344727"></a><a name="p56031344727"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p860314444217"><a name="p860314444217"></a><a name="p860314444217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p3603944528"><a name="p3603944528"></a><a name="p3603944528"></a>Indicates the tag key, which can contain a maximum of 36 Unicode characters. It cannot be left unspecified, and cannot contain nonprintable ASCII (0–31) characters and the following special characters: =*&lt;&gt;\,|/</p>
</td>
</tr>
<tr id="row1360318441520"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p260334410213"><a name="p260334410213"></a><a name="p260334410213"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p660315441522"><a name="p660315441522"></a><a name="p660315441522"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p1160319445216"><a name="p1160319445216"></a><a name="p1160319445216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p18603194410214"><a name="p18603194410214"></a><a name="p18603194410214"></a>Indicates a tag value, which can contain a maximum of 43 Unicode characters. It can be empty, but cannot contain nonprintable ASCII (0–31) characters and the following special characters: =*&lt;&gt;\,|/</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
     "tag":
{
        "key":"DEV",
        "value":"DEV1"
}
}
```

## Response<a name="section49332166"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section1539594410210"></a>

<a name="table134025441323"></a>
<table><thead align="left"><tr id="row116051744522"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p960594414220"><a name="p960594414220"></a><a name="p960594414220"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p56051443216"><a name="p56051443216"></a><a name="p56051443216"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14472121692914"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p5829131016359"><a name="p5829131016359"></a><a name="p5829131016359"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p11829161019356"><a name="p11829161019356"></a><a name="p11829161019356"></a>No content.</p>
</td>
</tr>
<tr id="row4605944125"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1260517445220"><a name="p1260517445220"></a><a name="p1260517445220"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1060513441324"><a name="p1060513441324"></a><a name="p1060513441324"></a>Invalid parameters, such as <strong id="b1243515401387"><a name="b1243515401387"></a><a name="b1243515401387"></a>tag</strong>.</p>
</td>
</tr>
<tr id="row10605194414214"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p26054444217"><a name="p26054444217"></a><a name="p26054444217"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p66055443219"><a name="p66055443219"></a><a name="p66055443219"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row196057441624"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1260574413213"><a name="p1260574413213"></a><a name="p1260574413213"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p126051644629"><a name="p126051644629"></a><a name="p126051644629"></a>Insufficient permission.</p>
</td>
</tr>
<tr id="row176051944624"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p56057441020"><a name="p56057441020"></a><a name="p56057441020"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1060519445219"><a name="p1060519445219"></a><a name="p1060519445219"></a>No queue found.</p>
</td>
</tr>
<tr id="row460544416211"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p126056441427"><a name="p126056441427"></a><a name="p126056441427"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1760514441623"><a name="p1760514441623"></a><a name="p1760514441623"></a>System error.</p>
</td>
</tr>
</tbody>
</table>

