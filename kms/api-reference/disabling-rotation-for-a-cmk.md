# Disabling Rotation for a CMK<a name="kms_02_0040"></a>

## Function<a name="en-us_topic_0112992347_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API allows you to disable rotation for a CMK.

## URI<a name="en-us_topic_0112992347_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/disable-key-rotation

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992347_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992347_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="19.170000000000005%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992347_p2739096916511"><a name="en-us_topic_0112992347_p2739096916511"></a><a name="en-us_topic_0112992347_p2739096916511"></a><strong id="en-us_topic_0112992347_b842352706202331"><a name="en-us_topic_0112992347_b842352706202331"></a><a name="en-us_topic_0112992347_b842352706202331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.180000000000003%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992347_p407603016511"><a name="en-us_topic_0112992347_p407603016511"></a><a name="en-us_topic_0112992347_p407603016511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.610000000000003%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992347_p6172299916511"><a name="en-us_topic_0112992347_p6172299916511"></a><a name="en-us_topic_0112992347_p6172299916511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.040000000000006%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992347_p3350702116511"><a name="en-us_topic_0112992347_p3350702116511"></a><a name="en-us_topic_0112992347_p3350702116511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992347_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="19.170000000000005%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992347_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992347_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992347_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.180000000000003%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992347_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992347_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992347_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992347_p4386100291125"><a name="en-us_topic_0112992347_p4386100291125"></a><a name="en-us_topic_0112992347_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.040000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992347_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992347_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992347_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992347_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992347_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992347_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992347_p842479145612"><a name="en-us_topic_0112992347_p842479145612"></a><a name="en-us_topic_0112992347_p842479145612"></a><strong id="en-us_topic_0112992347_b1933286066"><a name="en-us_topic_0112992347_b1933286066"></a><a name="en-us_topic_0112992347_b1933286066"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992347_p1442499105614"><a name="en-us_topic_0112992347_p1442499105614"></a><a name="en-us_topic_0112992347_p1442499105614"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992347_p342459125610"><a name="en-us_topic_0112992347_p342459125610"></a><a name="en-us_topic_0112992347_p342459125610"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992347_p34241396569"><a name="en-us_topic_0112992347_p34241396569"></a><a name="en-us_topic_0112992347_p34241396569"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992347_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992347_p41908563105428"><a name="en-us_topic_0112992347_p41908563105428"></a><a name="en-us_topic_0112992347_p41908563105428"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992347_p17072096105428"><a name="en-us_topic_0112992347_p17072096105428"></a><a name="en-us_topic_0112992347_p17072096105428"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992347_p8728818814"><a name="en-us_topic_0112992347_p8728818814"></a><a name="en-us_topic_0112992347_p8728818814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992347_p65699359161410"><a name="en-us_topic_0112992347_p65699359161410"></a><a name="en-us_topic_0112992347_p65699359161410"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992347_parmvalue80435593163333"><a name="en-us_topic_0112992347_parmvalue80435593163333"></a><a name="en-us_topic_0112992347_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992347_p40662515105428"><a name="en-us_topic_0112992347_p40662515105428"></a><a name="en-us_topic_0112992347_p40662515105428"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992347_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992347_p269135101746"><a name="en-us_topic_0112992347_p269135101746"></a><a name="en-us_topic_0112992347_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992347_p20967256101746"><a name="en-us_topic_0112992347_p20967256101746"></a><a name="en-us_topic_0112992347_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992347_p05452032083"><a name="en-us_topic_0112992347_p05452032083"></a><a name="en-us_topic_0112992347_p05452032083"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992347_p13871143202914"><a name="en-us_topic_0112992347_p13871143202914"></a><a name="en-us_topic_0112992347_p13871143202914"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992347_p20626198101746"><a name="en-us_topic_0112992347_p20626198101746"></a><a name="en-us_topic_0112992347_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992347_sfadd53a5f4714e8f87811818d62d0296"></a>

None

## Examples<a name="en-us_topic_0112992347_section9910129105318"></a>

The following example describes how to disable rotation for a CMK \(ID:  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**\).

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f"
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


## Status Codes<a name="en-us_topic_0112992347_section655115613254"></a>

[Table 3](#en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992347_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992347_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992347_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992347_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992347_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992347_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992347_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992347_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992347_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992347_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992347_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

