# Deleting Tags from an ECS in a Batch<a name="EN-US_TOPIC_0167811964"></a>

## Function<a name="en-us_topic_0096282702_section2854124164213"></a>

-   This API is used to delete tags from a specified ECS in a batch.
-   The Tag Management Service \(TMS\) uses this API to batch manage the tags of an ECS.

>![](/images/icon-note.gif) **NOTE:**   
>-   This API is idempotent. When you delete a tag but the tag does not exist, a successful result is returned.  

## Constraints<a name="en-us_topic_0096282702_section118542413427"></a>

An ECS allows a maximum of 10 tags.

## URI<a name="en-us_topic_0096282702_section18541045425"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/tags/action

[Table 1](#en-us_topic_0096282702_en-us_topic_0096282701_table19484740133714)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0096282702_en-us_topic_0096282701_table19484740133714"></a>
<table><thead align="left"><tr id="en-us_topic_0096282702_en-us_topic_0096282701_row1351554013716"><th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282702_en-us_topic_0096282701_p7707213"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p7707213"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.05%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282702_en-us_topic_0096282701_p20304554"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p20304554"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.03999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282702_en-us_topic_0096282701_p34056167"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p34056167"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282702_en-us_topic_0096282701_row251512409371"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p8515164093713"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p8515164093713"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p8515164093713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p18515240143717"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p18515240143717"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p18515240143717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p37593705"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p37593705"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096282702_en-us_topic_0096282701_row14515124013712"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p13531204014371"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p13531204014371"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p13531204014371"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p3531540183718"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p3531540183718"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p3531540183718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282702_en-us_topic_0096282701_p17531340143714"><a name="en-us_topic_0096282702_en-us_topic_0096282701_p17531340143714"></a><a name="en-us_topic_0096282702_en-us_topic_0096282701_p17531340143714"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096282702_section1687010415429"></a>

[Table 2](#en-us_topic_0096282702_table787034194212)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0096282702_table787034194212"></a>
<table><thead align="left"><tr id="en-us_topic_0096282702_row192616564219"><th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096282702_p026354424"><a name="en-us_topic_0096282702_p026354424"></a><a name="en-us_topic_0096282702_p026354424"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.948205179482052%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096282702_p4261754425"><a name="en-us_topic_0096282702_p4261754425"></a><a name="en-us_topic_0096282702_p4261754425"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.618238176182384%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096282702_p16269584213"><a name="en-us_topic_0096282702_p16269584213"></a><a name="en-us_topic_0096282702_p16269584213"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.51524847515249%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096282702_p126125114213"><a name="en-us_topic_0096282702_p126125114213"></a><a name="en-us_topic_0096282702_p126125114213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282702_row182665154220"><td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282702_p4263515426"><a name="en-us_topic_0096282702_p4263515426"></a><a name="en-us_topic_0096282702_p4263515426"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.948205179482052%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282702_p5261253426"><a name="en-us_topic_0096282702_p5261253426"></a><a name="en-us_topic_0096282702_p5261253426"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.618238176182384%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282702_p13261058420"><a name="en-us_topic_0096282702_p13261058420"></a><a name="en-us_topic_0096282702_p13261058420"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="47.51524847515249%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282702_p6269512424"><a name="en-us_topic_0096282702_p6269512424"></a><a name="en-us_topic_0096282702_p6269512424"></a>Specifies tags.</p>
</td>
</tr>
<tr id="en-us_topic_0096282702_row126165114218"><td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282702_p18262517421"><a name="en-us_topic_0096282702_p18262517421"></a><a name="en-us_topic_0096282702_p18262517421"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.948205179482052%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282702_p72665184211"><a name="en-us_topic_0096282702_p72665184211"></a><a name="en-us_topic_0096282702_p72665184211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.618238176182384%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282702_p826252425"><a name="en-us_topic_0096282702_p826252425"></a><a name="en-us_topic_0096282702_p826252425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.51524847515249%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282702_p132625154215"><a name="en-us_topic_0096282702_p132625154215"></a><a name="en-us_topic_0096282702_p132625154215"></a>Specifies the operation. (Only lowercase letters are supported.) For example, <strong id="b842352706152944"><a name="b842352706152944"></a><a name="b842352706152944"></a>delete</strong> indicates the deletion operation.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="en-us_topic_0096282702_table3147055191316"></a>
<table><thead align="left"><tr id="en-us_topic_0096282702_row10147145518131"><th class="cellrowborder" valign="top" width="16.861686168616863%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096282702_p14890161219476"><a name="en-us_topic_0096282702_p14890161219476"></a><a name="en-us_topic_0096282702_p14890161219476"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.87178717871787%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096282702_p1889081213476"><a name="en-us_topic_0096282702_p1889081213476"></a><a name="en-us_topic_0096282702_p1889081213476"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.691769176917692%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096282702_p13890131284718"><a name="en-us_topic_0096282702_p13890131284718"></a><a name="en-us_topic_0096282702_p13890131284718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.574757475747575%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096282702_p16890512124715"><a name="en-us_topic_0096282702_p16890512124715"></a><a name="en-us_topic_0096282702_p16890512124715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282702_row11147125521317"><td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282702_p19147135511139"><a name="en-us_topic_0096282702_p19147135511139"></a><a name="en-us_topic_0096282702_p19147135511139"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.87178717871787%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282702_p19147185516138"><a name="en-us_topic_0096282702_p19147185516138"></a><a name="en-us_topic_0096282702_p19147185516138"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.691769176917692%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282702_p4147145514138"><a name="en-us_topic_0096282702_p4147145514138"></a><a name="en-us_topic_0096282702_p4147145514138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.574757475747575%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282702_p12147195511131"><a name="en-us_topic_0096282702_p12147195511131"></a><a name="en-us_topic_0096282702_p12147195511131"></a>Specifies the tag key.</p>
<p id="en-us_topic_0096282702_p19147165591310"><a name="en-us_topic_0096282702_p19147165591310"></a><a name="en-us_topic_0096282702_p19147165591310"></a>It contains a maximum of 127 Unicode characters and cannot be left blank.</p>
<p id="en-us_topic_0096282702_p5147115515135"><a name="en-us_topic_0096282702_p5147115515135"></a><a name="en-us_topic_0096282702_p5147115515135"></a>The tag key of an ECS must be unique.</p>
</td>
</tr>
<tr id="en-us_topic_0096282702_row11147455151311"><td class="cellrowborder" valign="top" width="16.861686168616863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096282702_p12147055101318"><a name="en-us_topic_0096282702_p12147055101318"></a><a name="en-us_topic_0096282702_p12147055101318"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.87178717871787%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096282702_p91471554134"><a name="en-us_topic_0096282702_p91471554134"></a><a name="en-us_topic_0096282702_p91471554134"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.691769176917692%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096282702_p71472553134"><a name="en-us_topic_0096282702_p71472553134"></a><a name="en-us_topic_0096282702_p71472553134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.574757475747575%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096282702_p1114785515139"><a name="en-us_topic_0096282702_p1114785515139"></a><a name="en-us_topic_0096282702_p1114785515139"></a>Specifies the tag value.</p>
<p id="en-us_topic_0096282702_p18147255141317"><a name="en-us_topic_0096282702_p18147255141317"></a><a name="en-us_topic_0096282702_p18147255141317"></a>It contains a maximum of 255 Unicode characters and can be left blank.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0096282702_section272211306539"></a>

None

## Example Request<a name="en-us_topic_0096282702_section69241026145215"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/tags/action
```

```
{
    "action": "delete",
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

## Example Response<a name="section14223193362118"></a>

None

## Returned Values<a name="en-us_topic_0096282702_en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0096282702_en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

