# Adding Tags to a DeH in Batches<a name="EN-US_TOPIC_0134153397"></a>

## Function<a name="section54478915181842"></a>

-   This API is used to add tags to a specified DeH in batches.

-   Tag Management Service \(TMS\) uses this API to batch add tags to a DeH.

## **Constraint**<a name="section141154519480"></a>

-   A DeH allows a maximum of 10 tags.
-   This API is idempotent.

    During tag creation, if a tag exists \(both the key and value are the same as those of an existing tag\), the tag is successfully processed by default.

-   A new tag will overwrite the original one if their keys are the same and values are different.

## URI<a name="en-us_topic_0057972838_section58912114"></a>

POST /v1.0/\{project\_id\}/dedicated-host-tags/\{dedicated\_host\_id\}/tags/action

[Table 1](#table1913014815289)  describes the parameters.

**Table  1**  Parameters description

<a name="table1913014815289"></a>
<table><thead align="left"><tr id="row6132548192819"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1453395718282"><a name="p1453395718282"></a><a name="p1453395718282"></a><strong id="b023082265513"><a name="b023082265513"></a><a name="b023082265513"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p12672121152914"><a name="p12672121152914"></a><a name="p12672121152914"></a><strong id="b5595123145520"><a name="b5595123145520"></a><a name="b5595123145520"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p036416672910"><a name="p036416672910"></a><a name="p036416672910"></a><strong id="b1922112505512"><a name="b1922112505512"></a><a name="b1922112505512"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p13607121012919"><a name="p13607121012919"></a><a name="p13607121012919"></a><strong id="b18468927105520"><a name="b18468927105520"></a><a name="b18468927105520"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1513224882810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7535157152814"><a name="p7535157152814"></a><a name="p7535157152814"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p106746132910"><a name="p106746132910"></a><a name="p106746132910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p5368176122914"><a name="p5368176122914"></a><a name="p5368176122914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p361114109293"><a name="p361114109293"></a><a name="p361114109293"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row18132154822812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p653716573284"><a name="p653716573284"></a><a name="p653716573284"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p116765112916"><a name="p116765112916"></a><a name="p116765112916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p18369106112920"><a name="p18369106112920"></a><a name="p18369106112920"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p3612201014297"><a name="p3612201014297"></a><a name="p3612201014297"></a>Specifies the DeH ID.</p>
<p id="p858154817367"><a name="p858154817367"></a><a name="p858154817367"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972838_section60446980"></a>

-   Request parameters

    <a name="table1500453193615"></a>
    <table><thead align="left"><tr id="row5505125383610"><th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.1.5.1.1"><p id="p18507115316361"><a name="p18507115316361"></a><a name="p18507115316361"></a><strong id="b4442144385513"><a name="b4442144385513"></a><a name="b4442144385513"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.1.5.1.2"><p id="p9510853133612"><a name="p9510853133612"></a><a name="p9510853133612"></a><strong id="b429874620557"><a name="b429874620557"></a><a name="b429874620557"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.61793820617938%" id="mcps1.1.5.1.3"><p id="p11144124133116"><a name="p11144124133116"></a><a name="p11144124133116"></a><strong id="b48172473555"><a name="b48172473555"></a><a name="b48172473555"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.205979402059796%" id="mcps1.1.5.1.4"><p id="p751114534366"><a name="p751114534366"></a><a name="p751114534366"></a><strong id="b18590496552"><a name="b18590496552"></a><a name="b18590496552"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row85141953113615"><td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.1 "><p id="p15150532368"><a name="p15150532368"></a><a name="p15150532368"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.2 "><p id="p14518853113610"><a name="p14518853113610"></a><a name="p14518853113610"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.61793820617938%" headers="mcps1.1.5.1.3 "><p id="p101472045319"><a name="p101472045319"></a><a name="p101472045319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.205979402059796%" headers="mcps1.1.5.1.4 "><p id="p2519553103617"><a name="p2519553103617"></a><a name="p2519553103617"></a>Specifies the tag list.</p>
    </td>
    </tr>
    <tr id="row2521753193610"><td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.1 "><p id="p1352275320369"><a name="p1352275320369"></a><a name="p1352275320369"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.1.5.1.2 "><p id="p252435312366"><a name="p252435312366"></a><a name="p252435312366"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.61793820617938%" headers="mcps1.1.5.1.3 "><p id="p91482463120"><a name="p91482463120"></a><a name="p91482463120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.205979402059796%" headers="mcps1.1.5.1.4 "><p id="p1352625333614"><a name="p1352625333614"></a><a name="p1352625333614"></a>Specifies the operation. (Only lowercase letters are supported.) For example, <strong id="b842352706152944"><a name="b842352706152944"></a><a name="b842352706152944"></a>create</strong> indicates the creation operation.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **resource\_tag**  field description

    <a name="table1291492117268"></a>
    <table><thead align="left"><tr id="en-us_topic_0087389315_row17915421152613"><th class="cellrowborder" valign="top" width="16.731673167316732%" id="mcps1.1.5.1.1"><p id="en-us_topic_0087389315_p88171201349"><a name="en-us_topic_0087389315_p88171201349"></a><a name="en-us_topic_0087389315_p88171201349"></a><strong id="en-us_topic_0087389315_b36711287344"><a name="en-us_topic_0087389315_b36711287344"></a><a name="en-us_topic_0087389315_b36711287344"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.31163116311631%" id="mcps1.1.5.1.2"><p id="en-us_topic_0087389315_p198191902346"><a name="en-us_topic_0087389315_p198191902346"></a><a name="en-us_topic_0087389315_p198191902346"></a><strong id="en-us_topic_0087389315_b87133010341"><a name="en-us_topic_0087389315_b87133010341"></a><a name="en-us_topic_0087389315_b87133010341"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.72177217721772%" id="mcps1.1.5.1.3"><p id="en-us_topic_0087389315_p118191013413"><a name="en-us_topic_0087389315_p118191013413"></a><a name="en-us_topic_0087389315_p118191013413"></a><strong id="en-us_topic_0087389315_b1030273133412"><a name="en-us_topic_0087389315_b1030273133412"></a><a name="en-us_topic_0087389315_b1030273133412"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.23492349234924%" id="mcps1.1.5.1.4"><p id="en-us_topic_0087389315_p1582070173413"><a name="en-us_topic_0087389315_p1582070173413"></a><a name="en-us_topic_0087389315_p1582070173413"></a><strong id="en-us_topic_0087389315_b643313283410"><a name="en-us_topic_0087389315_b643313283410"></a><a name="en-us_topic_0087389315_b643313283410"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0087389315_row20915132182619"><td class="cellrowborder" valign="top" width="16.731673167316732%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0087389315_p1079518715372"><a name="en-us_topic_0087389315_p1079518715372"></a><a name="en-us_topic_0087389315_p1079518715372"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.31163116311631%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0087389315_p1798167163710"><a name="en-us_topic_0087389315_p1798167163710"></a><a name="en-us_topic_0087389315_p1798167163710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.72177217721772%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0087389315_p1143462293118"><a name="en-us_topic_0087389315_p1143462293118"></a><a name="en-us_topic_0087389315_p1143462293118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.23492349234924%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0087389315_p187993733712"><a name="en-us_topic_0087389315_p187993733712"></a><a name="en-us_topic_0087389315_p187993733712"></a>Specifies the tag key.</p>
    <a name="en-us_topic_0087389315_ul85106389279"></a><a name="en-us_topic_0087389315_ul85106389279"></a><ul id="en-us_topic_0087389315_ul85106389279"><li>It contains a maximum of 36 Unicode characters.</li><li>The value cannot be empty.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li><li>It can contain letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0087389315_row13915421202616"><td class="cellrowborder" valign="top" width="16.731673167316732%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0087389315_p180118718372"><a name="en-us_topic_0087389315_p180118718372"></a><a name="en-us_topic_0087389315_p180118718372"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.31163116311631%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0087389315_p280411723712"><a name="en-us_topic_0087389315_p280411723712"></a><a name="en-us_topic_0087389315_p280411723712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.72177217721772%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0087389315_p7435142215318"><a name="en-us_topic_0087389315_p7435142215318"></a><a name="en-us_topic_0087389315_p7435142215318"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.23492349234924%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0087389315_p1480513718375"><a name="en-us_topic_0087389315_p1480513718375"></a><a name="en-us_topic_0087389315_p1480513718375"></a>Specifies the tag value.</p>
    <a name="en-us_topic_0087389315_ul198416113281"></a><a name="en-us_topic_0087389315_ul198416113281"></a><ul id="en-us_topic_0087389315_ul198416113281"><li>It contains a maximum of 43 Unicode characters.</li><li>It cannot contain the following ASCII characters: =*&lt;&gt;\|/,</li><li>It can contain letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-host-tags/74259164-e63a-4ad9-9c77-a1bd2c9aa187/tags/action
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
                "value": "value2"
            }
        ]
    }
    ```


## Response<a name="section40529449"></a>

N/A

## Status Code<a name="section12666143310316"></a>

See  [Status Codes](status-codes.md).

