# Creating a Plaintext-Free DEK<a name="kms_02_0021"></a>

## Function<a name="en-us_topic_0112992350_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API allows you to create a plaintext-free DEK, that is, the returned result of this API includes only the plaintext of the DEK.

## URI<a name="en-us_topic_0112992350_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/create-datakey-without-plaintext

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992350_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992350_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992350_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992350_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992350_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992350_b842352706184314"><a name="en-us_topic_0112992350_b842352706184314"></a><a name="en-us_topic_0112992350_b842352706184314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.62%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992350_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992350_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992350_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992350_b842352706184318"><a name="en-us_topic_0112992350_b842352706184318"></a><a name="en-us_topic_0112992350_b842352706184318"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992350_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992350_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992350_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.35%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992350_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992350_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992350_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992350_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992350_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992350_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.62%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992350_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992350_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992350_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992350_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.35%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992350_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992350_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992350_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992350_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992350_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992350_p16364058101230"><a name="en-us_topic_0112992350_p16364058101230"></a><a name="en-us_topic_0112992350_p16364058101230"></a><strong id="en-us_topic_0112992350_b459387392"><a name="en-us_topic_0112992350_b459387392"></a><a name="en-us_topic_0112992350_b459387392"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992350_p57514295101230"><a name="en-us_topic_0112992350_p57514295101230"></a><a name="en-us_topic_0112992350_p57514295101230"></a><strong id="en-us_topic_0112992350_b842352706184358"><a name="en-us_topic_0112992350_b842352706184358"></a><a name="en-us_topic_0112992350_b842352706184358"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992350_p50420322101230"><a name="en-us_topic_0112992350_p50420322101230"></a><a name="en-us_topic_0112992350_p50420322101230"></a><strong id="en-us_topic_0112992350_b842352706184352"><a name="en-us_topic_0112992350_b842352706184352"></a><a name="en-us_topic_0112992350_b842352706184352"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992350_p28146304101230"><a name="en-us_topic_0112992350_p28146304101230"></a><a name="en-us_topic_0112992350_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992350_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p55471763113244"><a name="en-us_topic_0112992350_p55471763113244"></a><a name="en-us_topic_0112992350_p55471763113244"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p18869429113244"><a name="en-us_topic_0112992350_p18869429113244"></a><a name="en-us_topic_0112992350_p18869429113244"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p64027801113244"><a name="en-us_topic_0112992350_p64027801113244"></a><a name="en-us_topic_0112992350_p64027801113244"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p6776450172517"><a name="en-us_topic_0112992350_p6776450172517"></a><a name="en-us_topic_0112992350_p6776450172517"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992350_parmvalue80435593163333"><a name="en-us_topic_0112992350_parmvalue80435593163333"></a><a name="en-us_topic_0112992350_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992350_p52028748113244"><a name="en-us_topic_0112992350_p52028748113244"></a><a name="en-us_topic_0112992350_p52028748113244"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992350_row53999113153132"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p9591275153136"><a name="en-us_topic_0112992350_p9591275153136"></a><a name="en-us_topic_0112992350_p9591275153136"></a>encryption_context</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p47351257153136"><a name="en-us_topic_0112992350_p47351257153136"></a><a name="en-us_topic_0112992350_p47351257153136"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p38695790153136"><a name="en-us_topic_0112992350_p38695790153136"></a><a name="en-us_topic_0112992350_p38695790153136"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p299262517255"><a name="en-us_topic_0112992350_p299262517255"></a><a name="en-us_topic_0112992350_p299262517255"></a>Key-value pairs with a maximum length of 8192 characters. This parameter is used to record resource context information, excluding sensitive information, to ensure data integrity.</p>
<p id="en-us_topic_0112992350_p87033116108"><a name="en-us_topic_0112992350_p87033116108"></a><a name="en-us_topic_0112992350_p87033116108"></a>If this parameter is specified during encryption, it is also required for decryption.</p>
<p id="en-us_topic_0112992350_p10246613153136"><a name="en-us_topic_0112992350_p10246613153136"></a><a name="en-us_topic_0112992350_p10246613153136"></a>Example: {"Key1":"Value1","Key2":"Value2"}</p>
</td>
</tr>
<tr id="en-us_topic_0112992350_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p42501708113254"><a name="en-us_topic_0112992350_p42501708113254"></a><a name="en-us_topic_0112992350_p42501708113254"></a>datakey_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p69681116403"><a name="en-us_topic_0112992350_p69681116403"></a><a name="en-us_topic_0112992350_p69681116403"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p20086330113254"><a name="en-us_topic_0112992350_p20086330113254"></a><a name="en-us_topic_0112992350_p20086330113254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p2049671819407"><a name="en-us_topic_0112992350_p2049671819407"></a><a name="en-us_topic_0112992350_p2049671819407"></a>Number of bits of a key. The value is <strong id="en-us_topic_0112992350_b1162913122017"><a name="en-us_topic_0112992350_b1162913122017"></a><a name="en-us_topic_0112992350_b1162913122017"></a>512</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992350_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p269135101746"><a name="en-us_topic_0112992350_p269135101746"></a><a name="en-us_topic_0112992350_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p20967256101746"><a name="en-us_topic_0112992350_p20967256101746"></a><a name="en-us_topic_0112992350_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p21799971101746"><a name="en-us_topic_0112992350_p21799971101746"></a><a name="en-us_topic_0112992350_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p2925745172531"><a name="en-us_topic_0112992350_p2925745172531"></a><a name="en-us_topic_0112992350_p2925745172531"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992350_p20626198101746"><a name="en-us_topic_0112992350_p20626198101746"></a><a name="en-us_topic_0112992350_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992350_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992350_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992350_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992350_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992350_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992350_a9156e0b03f054d4e8547e0787f88a51b"></a><strong id="en-us_topic_0112992350_b1191377398"><a name="en-us_topic_0112992350_b1191377398"></a><a name="en-us_topic_0112992350_b1191377398"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992350_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992350_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992350_a1851157c81e14d7f82db752a5737195a"></a><strong id="en-us_topic_0112992350_b842352706184445"><a name="en-us_topic_0112992350_b842352706184445"></a><a name="en-us_topic_0112992350_b842352706184445"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992350_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992350_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992350_a39360acf5daf4c01a1ebddeff5d68a1c"></a><strong id="en-us_topic_0112992350_b842352706184441"><a name="en-us_topic_0112992350_b842352706184441"></a><a name="en-us_topic_0112992350_b842352706184441"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992350_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992350_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992350_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992350_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p43705601102713"><a name="en-us_topic_0112992350_p43705601102713"></a><a name="en-us_topic_0112992350_p43705601102713"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p63384753102713"><a name="en-us_topic_0112992350_p63384753102713"></a><a name="en-us_topic_0112992350_p63384753102713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p50492797102713"><a name="en-us_topic_0112992350_p50492797102713"></a><a name="en-us_topic_0112992350_p50492797102713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p33891398102713"><a name="en-us_topic_0112992350_p33891398102713"></a><a name="en-us_topic_0112992350_p33891398102713"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992350_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992350_p19123943113423"><a name="en-us_topic_0112992350_p19123943113423"></a><a name="en-us_topic_0112992350_p19123943113423"></a>cipher_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992350_p45726807113423"><a name="en-us_topic_0112992350_p45726807113423"></a><a name="en-us_topic_0112992350_p45726807113423"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992350_p5535555113423"><a name="en-us_topic_0112992350_p5535555113423"></a><a name="en-us_topic_0112992350_p5535555113423"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992350_p12883916113423"><a name="en-us_topic_0112992350_p12883916113423"></a><a name="en-us_topic_0112992350_p12883916113423"></a>The ciphertext of a DEK is expressed in hexadecimal format, and two characters indicate one byte.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992350_section6461153813349"></a>

The following example describes how to create a plaintext free DEK whose ID is  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**.

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "datakey_length": "512"
    }
    ```

-   Example response

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "cipher_text": "020098005CDC28E29EC3230AA42E8985FBABA095037D6474C64519C9B564AB28B15739C88E7E887500D1094973C2DC16353DB7ED3946C73339517AB1E983D521F9E9D700DC5D9C42F557EBF3F608E3CBBEE0BC68136EE7D2A49117E00332BAC4AE4ED805EB6068FA900C5A8019BFE2C2651BE3E130643034363662302D653732372D346439632D623335642D66383462623437346133376600000000F160727EBDB83400C21D80D713B49D3A2C37F24AE160E7BB3DAC025ADC0C45E3"
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


## Status Codes<a name="en-us_topic_0112992350_section3454223421"></a>

[Table 4](#en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992350_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992350_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992350_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992350_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992350_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992350_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992350_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992350_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992350_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992350_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992350_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

