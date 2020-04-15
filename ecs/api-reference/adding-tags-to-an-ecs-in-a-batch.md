# Adding Tags to an ECS in a Batch<a name="EN-US_TOPIC_0167811963"></a>

## Function<a name="en-us_topic_0096282701_section35847011245"></a>

-   This API is used to add tags to a specified ECS in a batch.
-   The Tag Management Service \(TMS\) uses this API to batch manage the tags of an ECS.

## Constraints<a name="en-us_topic_0096282701_section2179161873415"></a>

-   An ECS allows a maximum of 10 tags.
-   This API is idempotent.

    During tag creation, if a tag exists \(both the key and value are the same as those of an existing tag\), the tag is successfully processed by default.

-   A new tag will overwrite the original one if their keys are the same and values are different.

## URI<a name="en-us_topic_0096282701_section16695164917340"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/tags/action

[Table 1](#en-us_topic_0096282701_table19484740133714)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0096282701_table19484740133714"></a>
<table><thead align="left"><tr id="en-us_topic_0096282701_row1351554013716"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282701_p7707213"><a name="en-us_topic_0096282701_p7707213"></a><a name="en-us_topic_0096282701_p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282701_p20304554"><a name="en-us_topic_0096282701_p20304554"></a><a name="en-us_topic_0096282701_p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="69.3069306930693%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282701_p34056167"><a name="en-us_topic_0096282701_p34056167"></a><a name="en-us_topic_0096282701_p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282701_row251512409371"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282701_p8515164093713"><a name="en-us_topic_0096282701_p8515164093713"></a><a name="en-us_topic_0096282701_p8515164093713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282701_p18515240143717"><a name="en-us_topic_0096282701_p18515240143717"></a><a name="en-us_topic_0096282701_p18515240143717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="69.3069306930693%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282701_p37593705"><a name="en-us_topic_0096282701_p37593705"></a><a name="en-us_topic_0096282701_p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096282701_row14515124013712"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282701_p13531204014371"><a name="en-us_topic_0096282701_p13531204014371"></a><a name="en-us_topic_0096282701_p13531204014371"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282701_p3531540183718"><a name="en-us_topic_0096282701_p3531540183718"></a><a name="en-us_topic_0096282701_p3531540183718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="69.3069306930693%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282701_p17531340143714"><a name="en-us_topic_0096282701_p17531340143714"></a><a name="en-us_topic_0096282701_p17531340143714"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096282701_section36878128386"></a>

[Table 2](#en-us_topic_0096282701_table1349994618388)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0096282701_table1349994618388"></a>
<table><thead align="left"><tr id="en-us_topic_0096282701_row1563944663818"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096282701_p17639246103812"><a name="en-us_topic_0096282701_p17639246103812"></a><a name="en-us_topic_0096282701_p17639246103812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096282701_p363934610388"><a name="en-us_topic_0096282701_p363934610388"></a><a name="en-us_topic_0096282701_p363934610388"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096282701_p1763913462389"><a name="en-us_topic_0096282701_p1763913462389"></a><a name="en-us_topic_0096282701_p1763913462389"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.46534653465347%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096282701_p176391446163812"><a name="en-us_topic_0096282701_p176391446163812"></a><a name="en-us_topic_0096282701_p176391446163812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282701_row8639846173815"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282701_p4639144663820"><a name="en-us_topic_0096282701_p4639144663820"></a><a name="en-us_topic_0096282701_p4639144663820"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282701_p4639154616385"><a name="en-us_topic_0096282701_p4639154616385"></a><a name="en-us_topic_0096282701_p4639154616385"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282701_p6639144619381"><a name="en-us_topic_0096282701_p6639144619381"></a><a name="en-us_topic_0096282701_p6639144619381"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="53.46534653465347%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282701_p8639114673812"><a name="en-us_topic_0096282701_p8639114673812"></a><a name="en-us_topic_0096282701_p8639114673812"></a>Specifies tags.</p>
</td>
</tr>
<tr id="en-us_topic_0096282701_row18639194633819"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282701_p963954619387"><a name="en-us_topic_0096282701_p963954619387"></a><a name="en-us_topic_0096282701_p963954619387"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282701_p1963912460389"><a name="en-us_topic_0096282701_p1963912460389"></a><a name="en-us_topic_0096282701_p1963912460389"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282701_p1663974615386"><a name="en-us_topic_0096282701_p1663974615386"></a><a name="en-us_topic_0096282701_p1663974615386"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.46534653465347%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282701_p196391465384"><a name="en-us_topic_0096282701_p196391465384"></a><a name="en-us_topic_0096282701_p196391465384"></a>Specifies the operation. (Only lowercase letters are supported.) For example, <strong id="b842352706152944"><a name="b842352706152944"></a><a name="b842352706152944"></a>create</strong> indicates the creation operation.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="en-us_topic_0096282701_table1751454617383"></a>
<table><thead align="left"><tr id="en-us_topic_0096282701_row363954653815"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096282701_p29592023184516"><a name="en-us_topic_0096282701_p29592023184516"></a><a name="en-us_topic_0096282701_p29592023184516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096282701_p15959182310455"><a name="en-us_topic_0096282701_p15959182310455"></a><a name="en-us_topic_0096282701_p15959182310455"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096282701_p895912318450"><a name="en-us_topic_0096282701_p895912318450"></a><a name="en-us_topic_0096282701_p895912318450"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096282701_p995918231454"><a name="en-us_topic_0096282701_p995918231454"></a><a name="en-us_topic_0096282701_p995918231454"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282701_row15639164653810"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282701_p163934643813"><a name="en-us_topic_0096282701_p163934643813"></a><a name="en-us_topic_0096282701_p163934643813"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282701_p11639104643815"><a name="en-us_topic_0096282701_p11639104643815"></a><a name="en-us_topic_0096282701_p11639104643815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282701_p1863919468382"><a name="en-us_topic_0096282701_p1863919468382"></a><a name="en-us_topic_0096282701_p1863919468382"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282701_p191321456154119"><a name="en-us_topic_0096282701_p191321456154119"></a><a name="en-us_topic_0096282701_p191321456154119"></a>Specifies the tag key.</p>
<a name="en-us_topic_0096282701_ul14506057219"></a><a name="en-us_topic_0096282701_ul14506057219"></a><ul id="en-us_topic_0096282701_ul14506057219"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Contains a maximum of 36 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li><li>Must be unique and cannot be left blank.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096282701_row963964620389"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282701_p66391146173815"><a name="en-us_topic_0096282701_p66391146173815"></a><a name="en-us_topic_0096282701_p66391146173815"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282701_p1863917461382"><a name="en-us_topic_0096282701_p1863917461382"></a><a name="en-us_topic_0096282701_p1863917461382"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282701_p106396466385"><a name="en-us_topic_0096282701_p106396466385"></a><a name="en-us_topic_0096282701_p106396466385"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282701_p822413895013"><a name="en-us_topic_0096282701_p822413895013"></a><a name="en-us_topic_0096282701_p822413895013"></a>Specifies the tag value.</p>
<a name="en-us_topic_0096282701_ul91211113214"></a><a name="en-us_topic_0096282701_ul91211113214"></a><ul id="en-us_topic_0096282701_ul91211113214"><li>Contains a maximum of 43 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0096282701_section08601336145413"></a>

None

## Example Request<a name="en-us_topic_0096282701_section105681635543"></a>

```
POST  https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/tags/action
```

```
{
    "action": "create",
    "tags": [
        {
            "key": "key1",
            "value": "value1"
        },
        {
            "key": "key2",
            "value": "value3"
        }
    ]
}
```

## Example Response<a name="section739350112116"></a>

None

## Returned Values<a name="en-us_topic_0096282701_en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0096282701_en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

