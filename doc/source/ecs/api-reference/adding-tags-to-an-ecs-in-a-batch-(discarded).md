# Adding Tags to an ECS in a Batch \(Discarded\)<a name="EN-US_TOPIC_0096282701"></a>

## Function<a name="section35847011245"></a>

-   This API is used to add tags to a specified ECS in a batch.
-   The Tag Management Service \(TMS\) uses this API to batch manage the tags of an ECS.

>![](/images/icon-note.gif) **NOTE:**   
>You are suggested to use the API described in  [Adding Tags to an ECS in a Batch](adding-tags-to-an-ecs-in-a-batch.md).  

## Constraints<a name="section2179161873415"></a>

-   An ECS allows a maximum of 10 tags.
-   This API is idempotent.

    During tag creation, if a tag exists \(both the key and value are the same as those of an existing tag\), the tag is successfully processed by default.

-   A new tag will overwrite the original one if their keys are the same and values are different.

## URI<a name="section16695164917340"></a>

POST /v1/\{project\_id\}/servers/\{server\_id\}/tags/action

[Table 1](#table19484740133714)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table19484740133714"></a>
<table><thead align="left"><tr id="row1351554013716"><th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.61%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row251512409371"><td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.1 "><p id="p8515164093713"><a name="p8515164093713"></a><a name="p8515164093713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.2 "><p id="p18515240143717"><a name="p18515240143717"></a><a name="p18515240143717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.61%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row14515124013712"><td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.4.1.1 "><p id="p13531204014371"><a name="p13531204014371"></a><a name="p13531204014371"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.4.1.2 "><p id="p3531540183718"><a name="p3531540183718"></a><a name="p3531540183718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.61%" headers="mcps1.2.4.1.3 "><p id="p17531340143714"><a name="p17531340143714"></a><a name="p17531340143714"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36878128386"></a>

[Table 2](#table1349994618388)  describes the request parameters.

**Table  2**  Request parameters

<a name="table1349994618388"></a>
<table><thead align="left"><tr id="row1563944663818"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.5.1.1"><p id="p17639246103812"><a name="p17639246103812"></a><a name="p17639246103812"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.5.1.2"><p id="p363934610388"><a name="p363934610388"></a><a name="p363934610388"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.599999999999998%" id="mcps1.2.5.1.3"><p id="p1763913462389"><a name="p1763913462389"></a><a name="p1763913462389"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.870000000000005%" id="mcps1.2.5.1.4"><p id="p176391446163812"><a name="p176391446163812"></a><a name="p176391446163812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8639846173815"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.5.1.1 "><p id="p4639144663820"><a name="p4639144663820"></a><a name="p4639144663820"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.5.1.2 "><p id="p4639154616385"><a name="p4639154616385"></a><a name="p4639154616385"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p6639144619381"><a name="p6639144619381"></a><a name="p6639144619381"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="47.870000000000005%" headers="mcps1.2.5.1.4 "><p id="p8639114673812"><a name="p8639114673812"></a><a name="p8639114673812"></a>Specifies the tag list.</p>
</td>
</tr>
<tr id="row18639194633819"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.5.1.1 "><p id="p963954619387"><a name="p963954619387"></a><a name="p963954619387"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.5.1.2 "><p id="p1963912460389"><a name="p1963912460389"></a><a name="p1963912460389"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p1663974615386"><a name="p1663974615386"></a><a name="p1663974615386"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.870000000000005%" headers="mcps1.2.5.1.4 "><p id="p196391465384"><a name="p196391465384"></a><a name="p196391465384"></a>Specifies the operation. (Only lowercase letters are supported.) For example, <strong id="b842352706152944"><a name="b842352706152944"></a><a name="b842352706152944"></a>create</strong> indicates the creation operation.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="table1751454617383"></a>
<table><thead align="left"><tr id="row363954653815"><th class="cellrowborder" valign="top" width="16.82%" id="mcps1.2.5.1.1"><p id="p29592023184516"><a name="p29592023184516"></a><a name="p29592023184516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.75%" id="mcps1.2.5.1.2"><p id="p15959182310455"><a name="p15959182310455"></a><a name="p15959182310455"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.17%" id="mcps1.2.5.1.3"><p id="p895912318450"><a name="p895912318450"></a><a name="p895912318450"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.26%" id="mcps1.2.5.1.4"><p id="p995918231454"><a name="p995918231454"></a><a name="p995918231454"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15639164653810"><td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.2.5.1.1 "><p id="p163934643813"><a name="p163934643813"></a><a name="p163934643813"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.75%" headers="mcps1.2.5.1.2 "><p id="p11639104643815"><a name="p11639104643815"></a><a name="p11639104643815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.5.1.3 "><p id="p1863919468382"><a name="p1863919468382"></a><a name="p1863919468382"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.5.1.4 "><p id="p191321456154119"><a name="p191321456154119"></a><a name="p191321456154119"></a>Specifies the tag key.</p>
<a name="ul14506057219"></a><a name="ul14506057219"></a><ul id="ul14506057219"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li><li>The tag key must be unique and cannot be empty.</li></ul>
</td>
</tr>
<tr id="row963964620389"><td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.2.5.1.1 "><p id="p66391146173815"><a name="p66391146173815"></a><a name="p66391146173815"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.75%" headers="mcps1.2.5.1.2 "><p id="p1863917461382"><a name="p1863917461382"></a><a name="p1863917461382"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.17%" headers="mcps1.2.5.1.3 "><p id="p106396466385"><a name="p106396466385"></a><a name="p106396466385"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.26%" headers="mcps1.2.5.1.4 "><p id="p822413895013"><a name="p822413895013"></a><a name="p822413895013"></a>Specifies the tag value.</p>
<a name="ul91211113214"></a><a name="ul91211113214"></a><ul id="ul91211113214"><li>Can contain a maximum of 43 characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section08601336145413"></a>

None

## Example Request<a name="section105681635543"></a>

```
POST https://{endpoint}/v1/{project_id}/servers/{server_id}/tags/action
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

## Example Response<a name="section14437257173813"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

