# Adding and Deleting Queue Tags in Batches<a name="EN-US_TOPIC_0128036902"></a>

## Function<a name="section12838154518177"></a>

-   This API is used to add or delete tags in batches for a specified queue.
-   A maximum of 10 tags can be added to a queue.
-   This API is idempotent.
-   When tags are added in batches, if the request body contains duplicated keys, an error message will be reported.
-   When tags are added in batches, if tags with the same key already exist, the existing tags will be overwritten.
-   After tags are deleted in batches, if the tags do not exist, they have been successfully deleted by default.
-   When tags are deleted in batches, their keys cannot be empty or empty strings, and cannot exceed 36 Unicode characters. In addition, their values cannot exceed 43 Unicode characters. Otherwise, status code 400 is returned.

## URI<a name="section178391345151716"></a>

POST /v1.0/\{project\_id\}/queue/\{queue\_id\}/tags/action

**Table  1**  Request header

<a name="table1384214510176"></a>
<table><thead align="left"><tr id="row815554616173"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p1215534615179"><a name="p1215534615179"></a><a name="p1215534615179"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p10155124610174"><a name="p10155124610174"></a><a name="p10155124610174"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p61551466175"><a name="p61551466175"></a><a name="p61551466175"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p1215518467175"><a name="p1215518467175"></a><a name="p1215518467175"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row18155124641710"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p15155124631716"><a name="p15155124631716"></a><a name="p15155124631716"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p4155184615177"><a name="p4155184615177"></a><a name="p4155184615177"></a>Indicates the MIME types of a request body.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p1515594691713"><a name="p1515594691713"></a><a name="p1515594691713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p10155846161714"><a name="p10155846161714"></a><a name="p10155846161714"></a>application/json</p>
</td>
</tr>
<tr id="row111551946181720"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p20155164621719"><a name="p20155164621719"></a><a name="p20155164621719"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p31555464171"><a name="p31555464171"></a><a name="p31555464171"></a>Indicates the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p915584611720"><a name="p915584611720"></a><a name="p915584611720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p7156144661714"><a name="p7156144661714"></a><a name="p7156144661714"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameters

<a name="table5855145141718"></a>
<table><thead align="left"><tr id="row11566469178"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p615694621717"><a name="p615694621717"></a><a name="p615694621717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p171561946121712"><a name="p171561946121712"></a><a name="p171561946121712"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p6156114617179"><a name="p6156114617179"></a><a name="p6156114617179"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14156134618171"><a name="p14156134618171"></a><a name="p14156134618171"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2156124610174"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p91561746171719"><a name="p91561746171719"></a><a name="p91561746171719"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p01581046121718"><a name="p01581046121718"></a><a name="p01581046121718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p515810469171"><a name="p515810469171"></a><a name="p515810469171"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p73321357353"><a name="p73321357353"></a><a name="p73321357353"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row1715814621718"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12158246111718"><a name="p12158246111718"></a><a name="p12158246111718"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p715814465174"><a name="p715814465174"></a><a name="p715814465174"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p5158194661711"><a name="p5158194661711"></a><a name="p5158194661711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p19332115717511"><a name="p19332115717511"></a><a name="p19332115717511"></a>Indicates the queue ID.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
/v1.0/67c01b92944144a19d2da968ef34a912/queue/dd713484-e0b6-4e70-9942-4250e773d17c/tags/action
```

## Request<a name="section83272448218"></a>

[Table 3](#table3333134418220)  and  [Table 4](#table19345844328)  describe the parameters.

**Table  3**  Parameter

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
<tbody><tr id="row16022444211"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1916514911395"><a name="p1916514911395"></a><a name="p1916514911395"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p316784913392"><a name="p316784913392"></a><a name="p316784913392"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p121681849203915"><a name="p121681849203915"></a><a name="p121681849203915"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p9170549143915"><a name="p9170549143915"></a><a name="p9170549143915"></a>Indicates a list of tags.</p>
</td>
</tr>
<tr id="row57631747163911"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1317614903910"><a name="p1317614903910"></a><a name="p1317614903910"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p817710491394"><a name="p817710491394"></a><a name="p817710491394"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p11179194943911"><a name="p11179194943911"></a><a name="p11179194943911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p181801149143916"><a name="p181801149143916"></a><a name="p181801149143916"></a>Indicates an operation, which can be <strong id="b2082614410204"><a name="b2082614410204"></a><a name="b2082614410204"></a>create</strong> or <strong id="b19748134132020"><a name="b19748134132020"></a><a name="b19748134132020"></a>delete</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  tags parameter description

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
<tbody><tr id="row17603154411219"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p3681142918416"><a name="p3681142918416"></a><a name="p3681142918416"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p12684129124118"><a name="p12684129124118"></a><a name="p12684129124118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p668616297419"><a name="p668616297419"></a><a name="p668616297419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p7687102994116"><a name="p7687102994116"></a><a name="p7687102994116"></a>Indicates a tag key, which can contain a maximum of 36 Unicode characters. It cannot be empty and cannot contain nonprintable ASCII (0–31) characters and the following special characters: =*&lt;&gt;\,|/</p>
</td>
</tr>
<tr id="row1360318441520"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p1969012944119"><a name="p1969012944119"></a><a name="p1969012944119"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p186911929164114"><a name="p186911929164114"></a><a name="p186911929164114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p136931229154119"><a name="p136931229154119"></a><a name="p136931229154119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p1759178202310"><a name="p1759178202310"></a><a name="p1759178202310"></a>Indicates a tag value. A tag value can contain a maximum of 43 Unicode characters. It can be an empty string and cannot contain nonprintable ASCII (0–31) characters and the following special characters: =*&lt;&gt;\,|/</p>
<p id="p183561510152312"><a name="p183561510152312"></a><a name="p183561510152312"></a>When tags are deleted in batches, if both keys and values are specified, tags containing the specified keys and values are deleted; if keys are specified but values are not specified, tags containing the specified keys are deleted.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
    "action": "create",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key",
            "value": "value3"
        }
    ]
}
```

Or

```
{
    "action": "delete",
    "tags": [
        {
            "key": "key1"
         },
        {
            "key": "key2",
            "value": "value3"
        }
    ]
}
```

## Response<a name="section49332166"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section13930134510173"></a>

<a name="table593914581719"></a>
<table><thead align="left"><tr id="row4167746181710"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p3167174661712"><a name="p3167174661712"></a><a name="p3167174661712"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p10167114619178"><a name="p10167114619178"></a><a name="p10167114619178"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1659514510359"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p145561050103511"><a name="p145561050103511"></a><a name="p145561050103511"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6556165083518"><a name="p6556165083518"></a><a name="p6556165083518"></a>No content</p>
</td>
</tr>
<tr id="row41671463171"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12167146171711"><a name="p12167146171711"></a><a name="p12167146171711"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p31671246191714"><a name="p31671246191714"></a><a name="p31671246191714"></a>Invalid parameters, such as <strong id="b555124216507"><a name="b555124216507"></a><a name="b555124216507"></a>tag</strong>.</p>
</td>
</tr>
<tr id="row16167046171712"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7167184620176"><a name="p7167184620176"></a><a name="p7167184620176"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p616719469175"><a name="p616719469175"></a><a name="p616719469175"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row4167114616178"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12168846181720"><a name="p12168846181720"></a><a name="p12168846181720"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1516884619179"><a name="p1516884619179"></a><a name="p1516884619179"></a>Insufficient permission.</p>
</td>
</tr>
<tr id="row12168184681719"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1170114681714"><a name="p1170114681714"></a><a name="p1170114681714"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p3170546161718"><a name="p3170546161718"></a><a name="p3170546161718"></a>No queue found.</p>
</td>
</tr>
<tr id="row317074691718"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3170204611718"><a name="p3170204611718"></a><a name="p3170204611718"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61709465171"><a name="p61709465171"></a><a name="p61709465171"></a>System error.</p>
</td>
</tr>
</tbody>
</table>

