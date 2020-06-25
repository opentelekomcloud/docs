# Deleting Tags from an ECS in a Batch \(Discarded\)<a name="EN-US_TOPIC_0096282702"></a>

## Function<a name="section2854124164213"></a>

-   This API is used to delete tags from a specified ECS in a batch.
-   The Tag Management Service \(TMS\) uses this API to batch manage the tags of an ECS.
-   This API is idempotent. When you delete a tag but the tag does not exist, a successful result is returned.

>![](/images/icon-note.gif) **NOTE:**   
>You are suggested to use the API described in  [Deleting Tags from an ECS in a Batch](deleting-tags-from-an-ecs-in-a-batch.md).  

## Constraints<a name="section118542413427"></a>

An ECS allows a maximum of 10 tags.

## URI<a name="section18541045425"></a>

POST /v1/\{project\_id\}/servers/\{server\_id\}/tags/action

[Table 1](#en-us_topic_0096282701_table19484740133714)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0096282701_table19484740133714"></a>
<table><thead align="left"><tr id="en-us_topic_0096282701_row1351554013716"><th class="cellrowborder" valign="top" width="16.72167216721672%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282701_p7707213"><a name="en-us_topic_0096282701_p7707213"></a><a name="en-us_topic_0096282701_p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.291729172917293%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282701_p20304554"><a name="en-us_topic_0096282701_p20304554"></a><a name="en-us_topic_0096282701_p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.98659865986599%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282701_p34056167"><a name="en-us_topic_0096282701_p34056167"></a><a name="en-us_topic_0096282701_p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282701_row251512409371"><td class="cellrowborder" valign="top" width="16.72167216721672%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282701_p8515164093713"><a name="en-us_topic_0096282701_p8515164093713"></a><a name="en-us_topic_0096282701_p8515164093713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.291729172917293%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282701_p18515240143717"><a name="en-us_topic_0096282701_p18515240143717"></a><a name="en-us_topic_0096282701_p18515240143717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.98659865986599%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282701_p37593705"><a name="en-us_topic_0096282701_p37593705"></a><a name="en-us_topic_0096282701_p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096282701_row14515124013712"><td class="cellrowborder" valign="top" width="16.72167216721672%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282701_p13531204014371"><a name="en-us_topic_0096282701_p13531204014371"></a><a name="en-us_topic_0096282701_p13531204014371"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.291729172917293%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282701_p3531540183718"><a name="en-us_topic_0096282701_p3531540183718"></a><a name="en-us_topic_0096282701_p3531540183718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.98659865986599%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282701_p17531340143714"><a name="en-us_topic_0096282701_p17531340143714"></a><a name="en-us_topic_0096282701_p17531340143714"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1687010415429"></a>

[Table 2](#table787034194212)  describes the request parameters.

**Table  2**  Request parameters

<a name="table787034194212"></a>
<table><thead align="left"><tr id="row192616564219"><th class="cellrowborder" valign="top" width="16.728327167283272%" id="mcps1.2.5.1.1"><p id="p026354424"><a name="p026354424"></a><a name="p026354424"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.1982801719828%" id="mcps1.2.5.1.2"><p id="p4261754425"><a name="p4261754425"></a><a name="p4261754425"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.808219178082194%" id="mcps1.2.5.1.3"><p id="p16269584213"><a name="p16269584213"></a><a name="p16269584213"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.26517348265173%" id="mcps1.2.5.1.4"><p id="p126125114213"><a name="p126125114213"></a><a name="p126125114213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row182665154220"><td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.2.5.1.1 "><p id="p4263515426"><a name="p4263515426"></a><a name="p4263515426"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.1982801719828%" headers="mcps1.2.5.1.2 "><p id="p5261253426"><a name="p5261253426"></a><a name="p5261253426"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.808219178082194%" headers="mcps1.2.5.1.3 "><p id="p13261058420"><a name="p13261058420"></a><a name="p13261058420"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="48.26517348265173%" headers="mcps1.2.5.1.4 "><p id="p6269512424"><a name="p6269512424"></a><a name="p6269512424"></a>Specifies the tag list.</p>
</td>
</tr>
<tr id="row126165114218"><td class="cellrowborder" valign="top" width="16.728327167283272%" headers="mcps1.2.5.1.1 "><p id="p18262517421"><a name="p18262517421"></a><a name="p18262517421"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.1982801719828%" headers="mcps1.2.5.1.2 "><p id="p72665184211"><a name="p72665184211"></a><a name="p72665184211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.808219178082194%" headers="mcps1.2.5.1.3 "><p id="p826252425"><a name="p826252425"></a><a name="p826252425"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.26517348265173%" headers="mcps1.2.5.1.4 "><p id="p132625154215"><a name="p132625154215"></a><a name="p132625154215"></a>Specifies the operation. (Only lowercase letters are supported.) For example, <strong id="b842352706152944"><a name="b842352706152944"></a><a name="b842352706152944"></a>delete</strong> indicates the deletion operation.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="table3147055191316"></a>
<table><thead align="left"><tr id="row10147145518131"><th class="cellrowborder" valign="top" width="16.67833216678332%" id="mcps1.2.5.1.1"><p id="p14890161219476"><a name="p14890161219476"></a><a name="p14890161219476"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.11828817118288%" id="mcps1.2.5.1.2"><p id="p1889081213476"><a name="p1889081213476"></a><a name="p1889081213476"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.87821217878212%" id="mcps1.2.5.1.3"><p id="p13890131284718"><a name="p13890131284718"></a><a name="p13890131284718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.325167483251676%" id="mcps1.2.5.1.4"><p id="p16890512124715"><a name="p16890512124715"></a><a name="p16890512124715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11147125521317"><td class="cellrowborder" valign="top" width="16.67833216678332%" headers="mcps1.2.5.1.1 "><p id="p19147135511139"><a name="p19147135511139"></a><a name="p19147135511139"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.11828817118288%" headers="mcps1.2.5.1.2 "><p id="p19147185516138"><a name="p19147185516138"></a><a name="p19147185516138"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.87821217878212%" headers="mcps1.2.5.1.3 "><p id="p4147145514138"><a name="p4147145514138"></a><a name="p4147145514138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.325167483251676%" headers="mcps1.2.5.1.4 "><p id="p12147195511131"><a name="p12147195511131"></a><a name="p12147195511131"></a>Specifies the tag key.</p>
<p id="p19147165591310"><a name="p19147165591310"></a><a name="p19147165591310"></a>It contains a maximum of 127 Unicode characters and cannot be left blank.</p>
<p id="p5147115515135"><a name="p5147115515135"></a><a name="p5147115515135"></a>The tag key of an ECS must be unique.</p>
</td>
</tr>
<tr id="row11147455151311"><td class="cellrowborder" valign="top" width="16.67833216678332%" headers="mcps1.2.5.1.1 "><p id="p12147055101318"><a name="p12147055101318"></a><a name="p12147055101318"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.11828817118288%" headers="mcps1.2.5.1.2 "><p id="p91471554134"><a name="p91471554134"></a><a name="p91471554134"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.87821217878212%" headers="mcps1.2.5.1.3 "><p id="p71472553134"><a name="p71472553134"></a><a name="p71472553134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.325167483251676%" headers="mcps1.2.5.1.4 "><p id="p1114785515139"><a name="p1114785515139"></a><a name="p1114785515139"></a>Specifies the tag value.</p>
<p id="p18147255141317"><a name="p18147255141317"></a><a name="p18147255141317"></a>The value can contain a maximum of 255 Unicode characters and can be left blank.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section272211306539"></a>

None

## Example Request<a name="section69241026145215"></a>

```
POST https://{endpoint}/v1/{project_id}/servers/{server_id}/tags/action
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

## Example Response<a name="section10756132410390"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

