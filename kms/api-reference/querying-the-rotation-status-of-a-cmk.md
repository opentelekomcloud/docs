# Querying the Rotation Status of a CMK<a name="kms_02_0041"></a>

## Function<a name="en-us_topic_0112992305_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API enables you to query the rotation status of a CMK.

## URI<a name="en-us_topic_0112992305_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/get-key-rotation-status

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992305_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992305_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="19.170000000000005%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992305_p2739096916511"><a name="en-us_topic_0112992305_p2739096916511"></a><a name="en-us_topic_0112992305_p2739096916511"></a><strong id="en-us_topic_0112992305_b842352706202545"><a name="en-us_topic_0112992305_b842352706202545"></a><a name="en-us_topic_0112992305_b842352706202545"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.180000000000003%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992305_p407603016511"><a name="en-us_topic_0112992305_p407603016511"></a><a name="en-us_topic_0112992305_p407603016511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.610000000000003%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992305_p6172299916511"><a name="en-us_topic_0112992305_p6172299916511"></a><a name="en-us_topic_0112992305_p6172299916511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.040000000000006%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992305_p3350702116511"><a name="en-us_topic_0112992305_p3350702116511"></a><a name="en-us_topic_0112992305_p3350702116511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992305_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="19.170000000000005%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992305_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992305_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.180000000000003%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992305_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992305_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p4386100291125"><a name="en-us_topic_0112992305_p4386100291125"></a><a name="en-us_topic_0112992305_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.040000000000006%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992305_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992305_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992305_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992305_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992305_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992305_p588193020561"><a name="en-us_topic_0112992305_p588193020561"></a><a name="en-us_topic_0112992305_p588193020561"></a><strong id="en-us_topic_0112992305_b1848255014"><a name="en-us_topic_0112992305_b1848255014"></a><a name="en-us_topic_0112992305_b1848255014"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992305_p15880308565"><a name="en-us_topic_0112992305_p15880308565"></a><a name="en-us_topic_0112992305_p15880308565"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992305_p14881230145613"><a name="en-us_topic_0112992305_p14881230145613"></a><a name="en-us_topic_0112992305_p14881230145613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992305_p28811306563"><a name="en-us_topic_0112992305_p28811306563"></a><a name="en-us_topic_0112992305_p28811306563"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992305_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p41908563105428"><a name="en-us_topic_0112992305_p41908563105428"></a><a name="en-us_topic_0112992305_p41908563105428"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p17072096105428"><a name="en-us_topic_0112992305_p17072096105428"></a><a name="en-us_topic_0112992305_p17072096105428"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p1382011218818"><a name="en-us_topic_0112992305_p1382011218818"></a><a name="en-us_topic_0112992305_p1382011218818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p65699359161410"><a name="en-us_topic_0112992305_p65699359161410"></a><a name="en-us_topic_0112992305_p65699359161410"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992305_parmvalue80435593163333"><a name="en-us_topic_0112992305_parmvalue80435593163333"></a><a name="en-us_topic_0112992305_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992305_p40662515105428"><a name="en-us_topic_0112992305_p40662515105428"></a><a name="en-us_topic_0112992305_p40662515105428"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992305_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p269135101746"><a name="en-us_topic_0112992305_p269135101746"></a><a name="en-us_topic_0112992305_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p20967256101746"><a name="en-us_topic_0112992305_p20967256101746"></a><a name="en-us_topic_0112992305_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p3331191510818"><a name="en-us_topic_0112992305_p3331191510818"></a><a name="en-us_topic_0112992305_p3331191510818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p1692914716294"><a name="en-us_topic_0112992305_p1692914716294"></a><a name="en-us_topic_0112992305_p1692914716294"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992305_p20626198101746"><a name="en-us_topic_0112992305_p20626198101746"></a><a name="en-us_topic_0112992305_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992305_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992305_table166431040746"></a>
<table><thead align="left"><tr id="en-us_topic_0112992305_row166441940847"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992305_p1264419406413"><a name="en-us_topic_0112992305_p1264419406413"></a><a name="en-us_topic_0112992305_p1264419406413"></a><strong id="en-us_topic_0112992305_b1790645517"><a name="en-us_topic_0112992305_b1790645517"></a><a name="en-us_topic_0112992305_b1790645517"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992305_p206441240446"><a name="en-us_topic_0112992305_p206441240446"></a><a name="en-us_topic_0112992305_p206441240446"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992305_p564417401849"><a name="en-us_topic_0112992305_p564417401849"></a><a name="en-us_topic_0112992305_p564417401849"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992305_p106441340047"><a name="en-us_topic_0112992305_p106441340047"></a><a name="en-us_topic_0112992305_p106441340047"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992305_row0644124016413"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p06449401044"><a name="en-us_topic_0112992305_p06449401044"></a><a name="en-us_topic_0112992305_p06449401044"></a>key_rotation_enabled</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p4644640543"><a name="en-us_topic_0112992305_p4644640543"></a><a name="en-us_topic_0112992305_p4644640543"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p66447406416"><a name="en-us_topic_0112992305_p66447406416"></a><a name="en-us_topic_0112992305_p66447406416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p969917147612"><a name="en-us_topic_0112992305_p969917147612"></a><a name="en-us_topic_0112992305_p969917147612"></a>Key rotation status. The default value is <strong id="en-us_topic_0112992305_b8423527069926"><a name="en-us_topic_0112992305_b8423527069926"></a><a name="en-us_topic_0112992305_b8423527069926"></a>false</strong>, indicating that key rotation is disabled.</p>
</td>
</tr>
<tr id="en-us_topic_0112992305_row264454013411"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p1364419401419"><a name="en-us_topic_0112992305_p1364419401419"></a><a name="en-us_topic_0112992305_p1364419401419"></a>rotation_interval</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p864415408414"><a name="en-us_topic_0112992305_p864415408414"></a><a name="en-us_topic_0112992305_p864415408414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p164454010419"><a name="en-us_topic_0112992305_p164454010419"></a><a name="en-us_topic_0112992305_p164454010419"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p66921814364"><a name="en-us_topic_0112992305_p66921814364"></a><a name="en-us_topic_0112992305_p66921814364"></a>Rotation interval. The value is an integer ranging from <strong id="en-us_topic_0112992305_b842352706113339"><a name="en-us_topic_0112992305_b842352706113339"></a><a name="en-us_topic_0112992305_b842352706113339"></a>30</strong> to <strong id="en-us_topic_0112992305_b842352706113343"><a name="en-us_topic_0112992305_b842352706113343"></a><a name="en-us_topic_0112992305_b842352706113343"></a>365</strong>.</p>
<p id="en-us_topic_0112992305_p12244341395"><a name="en-us_topic_0112992305_p12244341395"></a><a name="en-us_topic_0112992305_p12244341395"></a>Set the interval based on how often a CMK is used. If it is frequently used, set a short interval; otherwise, set a long one.</p>
</td>
</tr>
<tr id="en-us_topic_0112992305_row52711533956"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p1727163317516"><a name="en-us_topic_0112992305_p1727163317516"></a><a name="en-us_topic_0112992305_p1727163317516"></a>last_rotation_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p192718332517"><a name="en-us_topic_0112992305_p192718332517"></a><a name="en-us_topic_0112992305_p192718332517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p15769181711612"><a name="en-us_topic_0112992305_p15769181711612"></a><a name="en-us_topic_0112992305_p15769181711612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p142711332515"><a name="en-us_topic_0112992305_p142711332515"></a><a name="en-us_topic_0112992305_p142711332515"></a>Last key rotation time. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970.</p>
</td>
</tr>
<tr id="en-us_topic_0112992305_row196153018510"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992305_p179811301653"><a name="en-us_topic_0112992305_p179811301653"></a><a name="en-us_topic_0112992305_p179811301653"></a>number_of_rotations</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992305_p6981030258"><a name="en-us_topic_0112992305_p6981030258"></a><a name="en-us_topic_0112992305_p6981030258"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992305_p1638420181761"><a name="en-us_topic_0112992305_p1638420181761"></a><a name="en-us_topic_0112992305_p1638420181761"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992305_p598173013511"><a name="en-us_topic_0112992305_p598173013511"></a><a name="en-us_topic_0112992305_p598173013511"></a>Number of key rotations</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992305_section1776515304561"></a>

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f"
    }
    ```

-   Example response

    ```
    {
        "key_rotation_enabled": true,
        "rotation_interval": 30,
        "last_rotation_time": "1501578672000",
        "number_of_rotations": 3
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


## Status Codes<a name="en-us_topic_0112992305_section655115613254"></a>

[Table 4](#en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992305_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992305_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992305_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992305_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992305_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992305_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992305_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992305_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992305_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992305_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992305_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

