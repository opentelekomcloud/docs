# Querying Project Tags \(Discarded\)<a name="EN-US_TOPIC_0102606094"></a>

## Function<a name="section192222559445"></a>

Projects are used to group and isolate OpenStack resources, which include computing, storage, and network resources. A project can be a department or a team. Multiple projects can be created under one account.

This API is used to query all tags used by a user in a specified project.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are suggested to use the API described in  [Querying Project Tags](querying-project-tags.md).  

## URI<a name="section222245513448"></a>

GET /v1/\{project\_id\}/servers/tags

[Table 1](#table144382516421)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table144382516421"></a>
<table><thead align="left"><tr id="row134312517423"><th class="cellrowborder" valign="top" width="16.66%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row259142515428"><td class="cellrowborder" valign="top" width="16.66%" headers="mcps1.2.4.1.1 "><p id="p1859102519426"><a name="p1859102519426"></a><a name="p1859102519426"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.4.1.2 "><p id="p135962520420"><a name="p135962520420"></a><a name="p135962520420"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section625475584419"></a>

None

## Response<a name="section1825415515447"></a>

[Table 2](#table725495518449)  describes the response parameters.

**Table  2**  Response parameters

<a name="table725495518449"></a>
<table><thead align="left"><tr id="row3363185511442"><th class="cellrowborder" valign="top" width="16.74%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.380000000000003%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.88000000000001%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4363105574411"><td class="cellrowborder" valign="top" width="16.74%" headers="mcps1.2.4.1.1 "><p id="p73639556446"><a name="p73639556446"></a><a name="p73639556446"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p103634552442"><a name="p103634552442"></a><a name="p103634552442"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.88000000000001%" headers="mcps1.2.4.1.3 "><p id="p53631955194415"><a name="p53631955194415"></a><a name="p53631955194415"></a>Specifies tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="table207611141174713"></a>
<table><thead align="left"><tr id="row157616415478"><th class="cellrowborder" valign="top" width="16.66%" id="mcps1.2.4.1.1"><p id="p1990563433715"><a name="p1990563433715"></a><a name="p1990563433715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p11905734183715"><a name="p11905734183715"></a><a name="p11905734183715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.99000000000001%" id="mcps1.2.4.1.3"><p id="p169051234153715"><a name="p169051234153715"></a><a name="p169051234153715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1476124114474"><td class="cellrowborder" valign="top" width="16.66%" headers="mcps1.2.4.1.1 "><p id="p1048131744810"><a name="p1048131744810"></a><a name="p1048131744810"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p5481171719487"><a name="p5481171719487"></a><a name="p5481171719487"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.99000000000001%" headers="mcps1.2.4.1.3 "><p id="p6894311152216"><a name="p6894311152216"></a><a name="p6894311152216"></a>Specifies the tag key.</p>
<a name="ul16669204222215"></a><a name="ul16669204222215"></a><ul id="ul16669204222215"><li>It contains a maximum of 36 Unicode characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
<tr id="row4761184174717"><td class="cellrowborder" valign="top" width="16.66%" headers="mcps1.2.4.1.1 "><p id="p048151716488"><a name="p048151716488"></a><a name="p048151716488"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p1156632102520"><a name="p1156632102520"></a><a name="p1156632102520"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="65.99000000000001%" headers="mcps1.2.4.1.3 "><p id="p1662531514220"><a name="p1662531514220"></a><a name="p1662531514220"></a>Specifies the tag value.</p>
<a name="ul18894121619234"></a><a name="ul18894121619234"></a><ul id="ul18894121619234"><li>Each value contains a maximum of 43 Unicode characters.</li><li>This field can be left blank.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section73711311115217"></a>

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/servers/tags
    ```


-   Example response

    ```
    {
          "tags": [
            {
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            },
            {
                "key": "key2",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ]
    }
    ```


## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

