# Creating a DEK<a name="kms_02_0020"></a>

## Function<a name="en-us_topic_0112992330_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API allows you to create a DEK. A returned result includes the plaintext and the ciphertext of a DEK.

## URI<a name="en-us_topic_0112992330_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/create-datakey

-   Parameter description

    **Table  1**  Parameters

    <a name="en-us_topic_0112992330_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992330_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.737726227377262%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992330_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992330_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992330_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11798820117988%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992330_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992330_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992330_ad98d2f62bd064b4e96ea922645197c24"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.91830816918308%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992330_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992330_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992330_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.22597740225977%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992330_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992330_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992330_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992330_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.737726227377262%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992330_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992330_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11798820117988%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992330_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992330_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91830816918308%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992330_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992330_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.22597740225977%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992330_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992330_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992330_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992330_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992330_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992330_p16364058101230"><a name="en-us_topic_0112992330_p16364058101230"></a><a name="en-us_topic_0112992330_p16364058101230"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992330_p57514295101230"><a name="en-us_topic_0112992330_p57514295101230"></a><a name="en-us_topic_0112992330_p57514295101230"></a><strong id="en-us_topic_0112992330_b842352706183936"><a name="en-us_topic_0112992330_b842352706183936"></a><a name="en-us_topic_0112992330_b842352706183936"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992330_p50420322101230"><a name="en-us_topic_0112992330_p50420322101230"></a><a name="en-us_topic_0112992330_p50420322101230"></a><strong id="en-us_topic_0112992330_b842352706183933"><a name="en-us_topic_0112992330_b842352706183933"></a><a name="en-us_topic_0112992330_b842352706183933"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992330_p28146304101230"><a name="en-us_topic_0112992330_p28146304101230"></a><a name="en-us_topic_0112992330_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992330_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p16662451112314"><a name="en-us_topic_0112992330_p16662451112314"></a><a name="en-us_topic_0112992330_p16662451112314"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p2004950112314"><a name="en-us_topic_0112992330_p2004950112314"></a><a name="en-us_topic_0112992330_p2004950112314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p7481292112314"><a name="en-us_topic_0112992330_p7481292112314"></a><a name="en-us_topic_0112992330_p7481292112314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p44672098172128"><a name="en-us_topic_0112992330_p44672098172128"></a><a name="en-us_topic_0112992330_p44672098172128"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992330_parmvalue80435593163333"><a name="en-us_topic_0112992330_parmvalue80435593163333"></a><a name="en-us_topic_0112992330_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992330_p28183289112314"><a name="en-us_topic_0112992330_p28183289112314"></a><a name="en-us_topic_0112992330_p28183289112314"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992330_row5309884015325"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p529241015328"><a name="en-us_topic_0112992330_p529241015328"></a><a name="en-us_topic_0112992330_p529241015328"></a>encryption_context</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p2822056515328"><a name="en-us_topic_0112992330_p2822056515328"></a><a name="en-us_topic_0112992330_p2822056515328"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p2603204115328"><a name="en-us_topic_0112992330_p2603204115328"></a><a name="en-us_topic_0112992330_p2603204115328"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p1658175312419"><a name="en-us_topic_0112992330_p1658175312419"></a><a name="en-us_topic_0112992330_p1658175312419"></a>Key-value pairs with a maximum length of 8192 characters. This parameter is used to record resource context information, excluding sensitive information, to ensure data integrity.</p>
<p id="en-us_topic_0112992330_p10713871141"><a name="en-us_topic_0112992330_p10713871141"></a><a name="en-us_topic_0112992330_p10713871141"></a>If this parameter is specified during encryption, it is also required for decryption.</p>
<p id="en-us_topic_0112992330_p416438915328"><a name="en-us_topic_0112992330_p416438915328"></a><a name="en-us_topic_0112992330_p416438915328"></a>Example: {"Key1":"Value1","Key2":"Value2"}</p>
</td>
</tr>
<tr id="en-us_topic_0112992330_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p32137860112326"><a name="en-us_topic_0112992330_p32137860112326"></a><a name="en-us_topic_0112992330_p32137860112326"></a>datakey_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p1517917412382"><a name="en-us_topic_0112992330_p1517917412382"></a><a name="en-us_topic_0112992330_p1517917412382"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p53029852112326"><a name="en-us_topic_0112992330_p53029852112326"></a><a name="en-us_topic_0112992330_p53029852112326"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p19885746392"><a name="en-us_topic_0112992330_p19885746392"></a><a name="en-us_topic_0112992330_p19885746392"></a>Number of bits of a key. The value is <strong id="en-us_topic_0112992330_b10480199183519"><a name="en-us_topic_0112992330_b10480199183519"></a><a name="en-us_topic_0112992330_b10480199183519"></a>512</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992330_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p269135101746"><a name="en-us_topic_0112992330_p269135101746"></a><a name="en-us_topic_0112992330_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p20967256101746"><a name="en-us_topic_0112992330_p20967256101746"></a><a name="en-us_topic_0112992330_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p21799971101746"><a name="en-us_topic_0112992330_p21799971101746"></a><a name="en-us_topic_0112992330_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p12977434172135"><a name="en-us_topic_0112992330_p12977434172135"></a><a name="en-us_topic_0112992330_p12977434172135"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992330_p20626198101746"><a name="en-us_topic_0112992330_p20626198101746"></a><a name="en-us_topic_0112992330_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992330_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992330_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992330_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992330_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992330_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992330_a9156e0b03f054d4e8547e0787f88a51b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992330_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992330_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992330_a1851157c81e14d7f82db752a5737195a"></a><strong id="en-us_topic_0112992330_b842352706184023"><a name="en-us_topic_0112992330_b842352706184023"></a><a name="en-us_topic_0112992330_b842352706184023"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992330_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992330_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992330_a39360acf5daf4c01a1ebddeff5d68a1c"></a><strong id="en-us_topic_0112992330_b842352706184020"><a name="en-us_topic_0112992330_b842352706184020"></a><a name="en-us_topic_0112992330_b842352706184020"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992330_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992330_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992330_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992330_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p43705601102713"><a name="en-us_topic_0112992330_p43705601102713"></a><a name="en-us_topic_0112992330_p43705601102713"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p63384753102713"><a name="en-us_topic_0112992330_p63384753102713"></a><a name="en-us_topic_0112992330_p63384753102713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p50492797102713"><a name="en-us_topic_0112992330_p50492797102713"></a><a name="en-us_topic_0112992330_p50492797102713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p33891398102713"><a name="en-us_topic_0112992330_p33891398102713"></a><a name="en-us_topic_0112992330_p33891398102713"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992330_row49143924112419"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p41535243112430"><a name="en-us_topic_0112992330_p41535243112430"></a><a name="en-us_topic_0112992330_p41535243112430"></a>plain_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p50742623112430"><a name="en-us_topic_0112992330_p50742623112430"></a><a name="en-us_topic_0112992330_p50742623112430"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p8911497112430"><a name="en-us_topic_0112992330_p8911497112430"></a><a name="en-us_topic_0112992330_p8911497112430"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p16511798112430"><a name="en-us_topic_0112992330_p16511798112430"></a><a name="en-us_topic_0112992330_p16511798112430"></a>The plaintext of a DEK is expressed in hexadecimal format, and two characters indicate one byte.</p>
</td>
</tr>
<tr id="en-us_topic_0112992330_row59157744112423"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992330_p54991495112437"><a name="en-us_topic_0112992330_p54991495112437"></a><a name="en-us_topic_0112992330_p54991495112437"></a>cipher_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992330_p21950354112437"><a name="en-us_topic_0112992330_p21950354112437"></a><a name="en-us_topic_0112992330_p21950354112437"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992330_p25126126112437"><a name="en-us_topic_0112992330_p25126126112437"></a><a name="en-us_topic_0112992330_p25126126112437"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992330_p33148250112437"><a name="en-us_topic_0112992330_p33148250112437"></a><a name="en-us_topic_0112992330_p33148250112437"></a>The ciphertext of a DEK is expressed in hexadecimal format, and two characters indicate one byte.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992330_section110811433011"></a>

The following example describes how to create a DEK whose ID is  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**  and length is  **512**  bits.

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
        "plain_text": "8151014275E426C72EE7D44267EF11590DCE0089E19863BA8CC832187B156A72A5A17F17B5EF0D525872C59ECEB72948AF85E18427F8BE0D46545C979306C08D",
        "cipher_text": "020098009EEAFCE122CAA5927D2E020086F9548BA1675FDB022E4ECC01B96F2189CF4B85E78357E73E1CEB518DAF7A4960E7C7DE8885ED3FB2F1471ABF400119CC1B20BD3C4A9B80AF590EFD0AEDABFDBB0E2B689DA7B6C9E7D3C5645FCD9274802586BE63779471F9156F2CDF07CD8412FFBE9230643034363662302D653732372D346439632D623335642D6638346262343734613337660000000045B05321483BD9F9561865EE7DFE9BE267A42EB104E98C16589CE46940B18E52"
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


## Status Codes<a name="en-us_topic_0112992330_section3454223421"></a>

[Table 4](#en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992330_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992330_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992330_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992330_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992330_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992330_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992330_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992330_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992330_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992330_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992330_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

