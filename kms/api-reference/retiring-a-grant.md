# Retiring a Grant<a name="kms_02_0030"></a>

## Function<a name="en-us_topic_0112992299_section37533920154934"></a>

This API enables users to retire a grant.

For example, user A grants operation permissions on CMK  **A/key**  to user B and authorizes user C to retire the grant. By doing this, users A, B, and C all can cancel the permissions. After the canceling, user B does not have permissions on CMK  **A/key**  any more.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The following are allowed to call this API:  
>-   The user who granted the permissions  
>-   The user indicated by parameter  **retiring\_principal**  
>-   The user indicated by parameter  **grantee\_principal**  when  **retire-grant**  has been selected  

## URI<a name="en-us_topic_0112992299_section37627629154934"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/retire-grant

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992299_table38759358154934"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992299_row60644171154934"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992299_p13230838154934"><a name="en-us_topic_0112992299_p13230838154934"></a><a name="en-us_topic_0112992299_p13230838154934"></a><strong id="en-us_topic_0112992299_b842352706193134"><a name="en-us_topic_0112992299_b842352706193134"></a><a name="en-us_topic_0112992299_b842352706193134"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992299_p65064970154934"><a name="en-us_topic_0112992299_p65064970154934"></a><a name="en-us_topic_0112992299_p65064970154934"></a><strong id="en-us_topic_0112992299_b842352706193137"><a name="en-us_topic_0112992299_b842352706193137"></a><a name="en-us_topic_0112992299_b842352706193137"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992299_p35771181154934"><a name="en-us_topic_0112992299_p35771181154934"></a><a name="en-us_topic_0112992299_p35771181154934"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992299_p11784586154934"><a name="en-us_topic_0112992299_p11784586154934"></a><a name="en-us_topic_0112992299_p11784586154934"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992299_row15027399154934"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992299_p9259788154934"><a name="en-us_topic_0112992299_p9259788154934"></a><a name="en-us_topic_0112992299_p9259788154934"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992299_p11845378154934"><a name="en-us_topic_0112992299_p11845378154934"></a><a name="en-us_topic_0112992299_p11845378154934"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992299_p4386100291125"><a name="en-us_topic_0112992299_p4386100291125"></a><a name="en-us_topic_0112992299_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992299_p5464351154934"><a name="en-us_topic_0112992299_p5464351154934"></a><a name="en-us_topic_0112992299_p5464351154934"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992299_section49179167154934"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992299_table5096792154934"></a>
<table><thead align="left"><tr id="en-us_topic_0112992299_row37570371154934"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992299_p139128461453"><a name="en-us_topic_0112992299_p139128461453"></a><a name="en-us_topic_0112992299_p139128461453"></a><strong id="en-us_topic_0112992299_b851235169"><a name="en-us_topic_0112992299_b851235169"></a><a name="en-us_topic_0112992299_b851235169"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992299_p159121546174511"><a name="en-us_topic_0112992299_p159121546174511"></a><a name="en-us_topic_0112992299_p159121546174511"></a><strong id="en-us_topic_0112992299_b613549592"><a name="en-us_topic_0112992299_b613549592"></a><a name="en-us_topic_0112992299_b613549592"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992299_p29121446134511"><a name="en-us_topic_0112992299_p29121446134511"></a><a name="en-us_topic_0112992299_p29121446134511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992299_p1291211466454"><a name="en-us_topic_0112992299_p1291211466454"></a><a name="en-us_topic_0112992299_p1291211466454"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992299_row3735252154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992299_p5492758715522"><a name="en-us_topic_0112992299_p5492758715522"></a><a name="en-us_topic_0112992299_p5492758715522"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992299_p530110015522"><a name="en-us_topic_0112992299_p530110015522"></a><a name="en-us_topic_0112992299_p530110015522"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992299_p448182811411"><a name="en-us_topic_0112992299_p448182811411"></a><a name="en-us_topic_0112992299_p448182811411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992299_p2673593115522"><a name="en-us_topic_0112992299_p2673593115522"></a><a name="en-us_topic_0112992299_p2673593115522"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992299_parmvalue80435593163333"><a name="en-us_topic_0112992299_parmvalue80435593163333"></a><a name="en-us_topic_0112992299_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992299_p5898392715522"><a name="en-us_topic_0112992299_p5898392715522"></a><a name="en-us_topic_0112992299_p5898392715522"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992299_row2233745154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992299_p3969076161826"><a name="en-us_topic_0112992299_p3969076161826"></a><a name="en-us_topic_0112992299_p3969076161826"></a>grant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992299_p2870774161826"><a name="en-us_topic_0112992299_p2870774161826"></a><a name="en-us_topic_0112992299_p2870774161826"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992299_p737103020418"><a name="en-us_topic_0112992299_p737103020418"></a><a name="en-us_topic_0112992299_p737103020418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992299_p31206156161826"><a name="en-us_topic_0112992299_p31206156161826"></a><a name="en-us_topic_0112992299_p31206156161826"></a>64-byte ID of a grant that meets the regular expression <strong id="en-us_topic_0112992299_b842352706105044"><a name="en-us_topic_0112992299_b842352706105044"></a><a name="en-us_topic_0112992299_b842352706105044"></a>^[A-Fa-f0-9]{64}$</strong></p>
<p id="en-us_topic_0112992299_p7940591162038"><a name="en-us_topic_0112992299_p7940591162038"></a><a name="en-us_topic_0112992299_p7940591162038"></a>Example: 7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d</p>
</td>
</tr>
<tr id="en-us_topic_0112992299_row29452288162122"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992299_p45167875162120"><a name="en-us_topic_0112992299_p45167875162120"></a><a name="en-us_topic_0112992299_p45167875162120"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992299_p60798351162120"><a name="en-us_topic_0112992299_p60798351162120"></a><a name="en-us_topic_0112992299_p60798351162120"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992299_p82968323410"><a name="en-us_topic_0112992299_p82968323410"></a><a name="en-us_topic_0112992299_p82968323410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992299_p25719365162120"><a name="en-us_topic_0112992299_p25719365162120"></a><a name="en-us_topic_0112992299_p25719365162120"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992299_p30147697162120"><a name="en-us_topic_0112992299_p30147697162120"></a><a name="en-us_topic_0112992299_p30147697162120"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992299_section35819930154934"></a>

None

## Examples<a name="en-us_topic_0112992299_section552734918116"></a>

The following example describes how to retire a grant whose grant ID is  **7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d**  and the CMK ID is  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**.

-   Example request

    ```
    {      
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
        "grant_id":"7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d"
    }
    ```

-   Example response

    ```
    {
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0112992299_section3454223421"></a>

[Table 3](#en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992299_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992299_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992299_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992299_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992299_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992299_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992299_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992299_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992299_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992299_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992299_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

