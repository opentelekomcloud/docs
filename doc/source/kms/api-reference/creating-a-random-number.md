# Creating a Random Number<a name="kms_02_0019"></a>

## Function<a name="en-us_topic_0112992308_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API generates a 512-bit random number.

## URI<a name="en-us_topic_0112992308_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/gen-random

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992308_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992308_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74227422742274%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992308_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992308_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992308_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.062406240624064%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992308_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992308_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992308_ad98d2f62bd064b4e96ea922645197c24"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.862086208620862%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992308_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992308_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992308_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.33323332333234%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992308_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992308_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992308_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992308_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74227422742274%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992308_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992308_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992308_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992308_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992308_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992308_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992308_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992308_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992308_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.33323332333234%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992308_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992308_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992308_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992308_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992308_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992308_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992308_p16364058101230"><a name="en-us_topic_0112992308_p16364058101230"></a><a name="en-us_topic_0112992308_p16364058101230"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992308_p57514295101230"><a name="en-us_topic_0112992308_p57514295101230"></a><a name="en-us_topic_0112992308_p57514295101230"></a><strong id="en-us_topic_0112992308_b842352706174353"><a name="en-us_topic_0112992308_b842352706174353"></a><a name="en-us_topic_0112992308_b842352706174353"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992308_p50420322101230"><a name="en-us_topic_0112992308_p50420322101230"></a><a name="en-us_topic_0112992308_p50420322101230"></a><strong id="en-us_topic_0112992308_b842352706174350"><a name="en-us_topic_0112992308_b842352706174350"></a><a name="en-us_topic_0112992308_b842352706174350"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992308_p28146304101230"><a name="en-us_topic_0112992308_p28146304101230"></a><a name="en-us_topic_0112992308_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992308_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992308_p4481944111821"><a name="en-us_topic_0112992308_p4481944111821"></a><a name="en-us_topic_0112992308_p4481944111821"></a>random_data_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992308_p12354932111821"><a name="en-us_topic_0112992308_p12354932111821"></a><a name="en-us_topic_0112992308_p12354932111821"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992308_p27493178111821"><a name="en-us_topic_0112992308_p27493178111821"></a><a name="en-us_topic_0112992308_p27493178111821"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992308_p181143345379"><a name="en-us_topic_0112992308_p181143345379"></a><a name="en-us_topic_0112992308_p181143345379"></a>Number of bits of a random number. The value is <strong id="en-us_topic_0112992308_b548313469244"><a name="en-us_topic_0112992308_b548313469244"></a><a name="en-us_topic_0112992308_b548313469244"></a>512</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992308_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992308_p269135101746"><a name="en-us_topic_0112992308_p269135101746"></a><a name="en-us_topic_0112992308_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992308_p20967256101746"><a name="en-us_topic_0112992308_p20967256101746"></a><a name="en-us_topic_0112992308_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992308_p21799971101746"><a name="en-us_topic_0112992308_p21799971101746"></a><a name="en-us_topic_0112992308_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992308_p32671918171823"><a name="en-us_topic_0112992308_p32671918171823"></a><a name="en-us_topic_0112992308_p32671918171823"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992308_p20626198101746"><a name="en-us_topic_0112992308_p20626198101746"></a><a name="en-us_topic_0112992308_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992308_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992308_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992308_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992308_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992308_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992308_a9156e0b03f054d4e8547e0787f88a51b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992308_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992308_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992308_a1851157c81e14d7f82db752a5737195a"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992308_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992308_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992308_a39360acf5daf4c01a1ebddeff5d68a1c"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992308_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992308_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992308_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992308_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992308_p66286535111935"><a name="en-us_topic_0112992308_p66286535111935"></a><a name="en-us_topic_0112992308_p66286535111935"></a>random_data</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992308_p40522553111935"><a name="en-us_topic_0112992308_p40522553111935"></a><a name="en-us_topic_0112992308_p40522553111935"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992308_p500278111935"><a name="en-us_topic_0112992308_p500278111935"></a><a name="en-us_topic_0112992308_p500278111935"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992308_p61101369111935"><a name="en-us_topic_0112992308_p61101369111935"></a><a name="en-us_topic_0112992308_p61101369111935"></a>Random numbers are expressed in hexadecimal format. Two characters indicate one byte. Length of a random number must be consistent with the <span class="parmname" id="en-us_topic_0112992308_parmname671747902144312"><a name="en-us_topic_0112992308_parmname671747902144312"></a><a name="en-us_topic_0112992308_parmname671747902144312"></a><b>random_data_length</b></span> value entered by a user.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992308_section1683920202720"></a>

The following example describes how to create a random number with the length of  **512**  bits.

-   Example request

    ```
    {
        "random_data_length": "512"
    }
    ```

-   Example response

    ```
    {
        "random_data": "5791C223E87124AB9FC29B5A8AC60BE4B98D168F47A58BB2A88833E40D6ED32D57E2AAB5410492EB25096873F9CE3D45E0D22F820A5AB4EEADC33A1A6AE780F1"
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


## Status Codes<a name="en-us_topic_0112992308_section12126152083712"></a>

[Table 4](#en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992308_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992308_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992308_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992308_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992308_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992308_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992308_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992308_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992308_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992308_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992308_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

