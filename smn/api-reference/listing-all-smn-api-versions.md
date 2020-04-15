# Listing All SMN API Versions<a name="smn_api_510001"></a>

## Description<a name="en-us_topic_0118694332_section46354700"></a>

-   API name

    QueryApiSupportVersions

-   Function

    List all SMN API versions.


## URI<a name="en-us_topic_0118694332_section14539121"></a>

-   URI format

    GET /


## Request<a name="en-us_topic_0118694332_section63743225"></a>

-   Request example

    ```
    GET https://{SMN_Endpoint}/
    ```


## Response<a name="en-us_topic_0118694332_section36818119"></a>

-   Parameter description

    <a name="en-us_topic_0118694332_table26328706"></a>
    <table><thead align="left"><tr id="en-us_topic_0118694332_row6366124"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="en-us_topic_0118694332_p45894015"><a name="en-us_topic_0118694332_p45894015"></a><a name="en-us_topic_0118694332_p45894015"></a><strong>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.2"><p id="en-us_topic_0118694332_p26427706"><a name="en-us_topic_0118694332_p26427706"></a><a name="en-us_topic_0118694332_p26427706"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.1.4.1.3"><p id="en-us_topic_0118694332_p60269446"><a name="en-us_topic_0118694332_p60269446"></a><a name="en-us_topic_0118694332_p60269446"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118694332_row22411503"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0118694332_p3392477"><a name="en-us_topic_0118694332_p3392477"></a><a name="en-us_topic_0118694332_p3392477"></a>versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0118694332_p6355195"><a name="en-us_topic_0118694332_p6355195"></a><a name="en-us_topic_0118694332_p6355195"></a>Versions structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.1.4.1.3 "><p id="p09481736355"><a name="p09481736355"></a><a name="p09481736355"></a>Version object list. For details, see <a href="#table219819244718">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Versions structure

    <a name="table219819244718"></a>
    <table><thead align="left"><tr id="row1526011204718"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p182602274711"><a name="p182602274711"></a><a name="p182602274711"></a><strong id="b12444115720445"><a name="b12444115720445"></a><a name="b12444115720445"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39%" id="mcps1.2.4.1.2"><p id="p19260192154719"><a name="p19260192154719"></a><a name="p19260192154719"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="p126017204718"><a name="p126017204718"></a><a name="p126017204718"></a><strong id="b33231158134412"><a name="b33231158134412"></a><a name="b33231158134412"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15260132164715"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p8907105518498"><a name="p8907105518498"></a><a name="p8907105518498"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p129078554491"><a name="p129078554491"></a><a name="p129078554491"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p88531517575"><a name="p88531517575"></a><a name="p88531517575"></a>Version number, for example, <strong id="b842352706151910"><a name="b842352706151910"></a><a name="b842352706151910"></a>v2</strong></p>
    </td>
    </tr>
    <tr id="row826819249365"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118694332_p9543622"><a name="en-us_topic_0118694332_p9543622"></a><a name="en-us_topic_0118694332_p9543622"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118694332_p34835893"><a name="en-us_topic_0118694332_p34835893"></a><a name="en-us_topic_0118694332_p34835893"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p7948334354"><a name="p7948334354"></a><a name="p7948334354"></a>Minimum micro-version number. If the APIs do not support micro-versions, no information will be returned.</p>
    </td>
    </tr>
    <tr id="row972024243711"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2069817541346"><a name="p2069817541346"></a><a name="p2069817541346"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p1698115415341"><a name="p1698115415341"></a><a name="p1698115415341"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p1098793361817"><a name="p1098793361817"></a><a name="p1098793361817"></a>Version status, which can be the following:</p>
    <a name="ul1496114571817"></a><a name="ul1496114571817"></a><ul id="ul1496114571817"><li><strong id="b842352706115252"><a name="b842352706115252"></a><a name="b842352706115252"></a>CURRENT</strong>: widely used version</li><li><strong id="b19815101718012"><a name="b19815101718012"></a><a name="b19815101718012"></a>SUPPORTED</strong>: earlier version, which is still supported</li><li><strong id="b842352706115458"><a name="b842352706115458"></a><a name="b842352706115458"></a>DEPRECATED</strong>: deprecated version, which may be deleted later</li></ul>
    </td>
    </tr>
    <tr id="row79551828143611"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p14902136113515"><a name="p14902136113515"></a><a name="p14902136113515"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p99021268355"><a name="p99021268355"></a><a name="p99021268355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p590215614356"><a name="p590215614356"></a><a name="p590215614356"></a>Version release time, which must be UTC time. For example, the release time of v2 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="row17393526173617"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p29120166354"><a name="p29120166354"></a><a name="p29120166354"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p691191611356"><a name="p691191611356"></a><a name="p691191611356"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p209171618355"><a name="p209171618355"></a><a name="p209171618355"></a>Maximum micro-version number. If the APIs do not support micro-versions, no information will be returned.</p>
    </td>
    </tr>
    <tr id="row926062154712"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1390725544917"><a name="p1390725544917"></a><a name="p1390725544917"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p13515150155715"><a name="p13515150155715"></a><a name="p13515150155715"></a>Links structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p1785191514575"><a name="p1785191514575"></a><a name="p1785191514575"></a>URL of an API. For details, see <a href="#table1259118084015">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Links structure

    <a name="table1259118084015"></a>
    <table><thead align="left"><tr id="row159118012401"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.4.1.1"><p id="p115911807403"><a name="p115911807403"></a><a name="p115911807403"></a><strong id="b152913357209"><a name="b152913357209"></a><a name="b152913357209"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.4.1.2"><p id="p1459115044014"><a name="p1459115044014"></a><a name="p1459115044014"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.44554455445545%" id="mcps1.2.4.1.3"><p id="p1559111015407"><a name="p1559111015407"></a><a name="p1559111015407"></a><strong id="b19775143712019"><a name="b19775143712019"></a><a name="b19775143712019"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1459113024020"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p175910054015"><a name="p175910054015"></a><a name="p175910054015"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.2 "><p id="p459614402597"><a name="p459614402597"></a><a name="p459614402597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.44554455445545%" headers="mcps1.2.4.1.3 "><p id="p2591150144013"><a name="p2591150144013"></a><a name="p2591150144013"></a>Shortcut link</p>
    </td>
    </tr>
    <tr id="row459130144018"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p185911807401"><a name="p185911807401"></a><a name="p185911807401"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.2 "><p id="p856574025910"><a name="p856574025910"></a><a name="p856574025910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.44554455445545%" headers="mcps1.2.4.1.3 "><p id="p959219013405"><a name="p959219013405"></a><a name="p959219013405"></a>Shortcut link marker name</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "versions": [
            {
                "id": "v2",
                "links": [
                    {
                        "href": "https://127.0.0.1/v2",
                        "rel": "self"
                    }
                ],
                "min_version": "",
                "status": "CURRENT",
                "updated": "2018-09-19T00:00:00Z",
                "version": ""
            }
       ]
    }
    ```


## Returned Value<a name="en-us_topic_0118694332_section62927619"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

