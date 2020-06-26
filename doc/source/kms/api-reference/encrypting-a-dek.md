# Encrypting a DEK<a name="kms_02_0022"></a>

## Function<a name="en-us_topic_0112992344_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API enables you to encrypt a DEK using a specified CMK.

## URI<a name="en-us_topic_0112992344_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/encrypt-datakey

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992344_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992344_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992344_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992344_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992344_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992344_b842352706184616"><a name="en-us_topic_0112992344_b842352706184616"></a><a name="en-us_topic_0112992344_b842352706184616"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.119999999999997%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992344_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992344_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992344_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992344_b842352706184620"><a name="en-us_topic_0112992344_b842352706184620"></a><a name="en-us_topic_0112992344_b842352706184620"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.56%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992344_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992344_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992344_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.580000000000002%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992344_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992344_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992344_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992344_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992344_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992344_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992344_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992344_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992344_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992344_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992344_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992344_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992344_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992344_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992344_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992344_p16364058101230"><a name="en-us_topic_0112992344_p16364058101230"></a><a name="en-us_topic_0112992344_p16364058101230"></a><strong id="en-us_topic_0112992344_b264481518"><a name="en-us_topic_0112992344_b264481518"></a><a name="en-us_topic_0112992344_b264481518"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992344_p57514295101230"><a name="en-us_topic_0112992344_p57514295101230"></a><a name="en-us_topic_0112992344_p57514295101230"></a><strong id="en-us_topic_0112992344_b842352706184654"><a name="en-us_topic_0112992344_b842352706184654"></a><a name="en-us_topic_0112992344_b842352706184654"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992344_p50420322101230"><a name="en-us_topic_0112992344_p50420322101230"></a><a name="en-us_topic_0112992344_p50420322101230"></a><strong id="en-us_topic_0112992344_b842352706184650"><a name="en-us_topic_0112992344_b842352706184650"></a><a name="en-us_topic_0112992344_b842352706184650"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992344_p28146304101230"><a name="en-us_topic_0112992344_p28146304101230"></a><a name="en-us_topic_0112992344_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992344_row44009584101643"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p30581115113751"><a name="en-us_topic_0112992344_p30581115113751"></a><a name="en-us_topic_0112992344_p30581115113751"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p54306670113751"><a name="en-us_topic_0112992344_p54306670113751"></a><a name="en-us_topic_0112992344_p54306670113751"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p61151280113751"><a name="en-us_topic_0112992344_p61151280113751"></a><a name="en-us_topic_0112992344_p61151280113751"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p15086246172845"><a name="en-us_topic_0112992344_p15086246172845"></a><a name="en-us_topic_0112992344_p15086246172845"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992344_parmvalue80435593163333"><a name="en-us_topic_0112992344_parmvalue80435593163333"></a><a name="en-us_topic_0112992344_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992344_p36764124113751"><a name="en-us_topic_0112992344_p36764124113751"></a><a name="en-us_topic_0112992344_p36764124113751"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_row6126595713547"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p6359549113547"><a name="en-us_topic_0112992344_p6359549113547"></a><a name="en-us_topic_0112992344_p6359549113547"></a>encryption_context</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p3421543413547"><a name="en-us_topic_0112992344_p3421543413547"></a><a name="en-us_topic_0112992344_p3421543413547"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p5096118613547"><a name="en-us_topic_0112992344_p5096118613547"></a><a name="en-us_topic_0112992344_p5096118613547"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p299262517255"><a name="en-us_topic_0112992344_p299262517255"></a><a name="en-us_topic_0112992344_p299262517255"></a>Key-value pairs with a maximum length of 8192 characters. This parameter is used to record resource context information, excluding sensitive information, to ensure data integrity.</p>
<p id="en-us_topic_0112992344_p87033116108"><a name="en-us_topic_0112992344_p87033116108"></a><a name="en-us_topic_0112992344_p87033116108"></a>If this parameter is specified during encryption, it is also required for decryption.</p>
<p id="en-us_topic_0112992344_p1998675413547"><a name="en-us_topic_0112992344_p1998675413547"></a><a name="en-us_topic_0112992344_p1998675413547"></a>Example: {"Key1":"Value1","Key2":"Value2"}</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p40816810113819"><a name="en-us_topic_0112992344_p40816810113819"></a><a name="en-us_topic_0112992344_p40816810113819"></a>plain_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p34729111113819"><a name="en-us_topic_0112992344_p34729111113819"></a><a name="en-us_topic_0112992344_p34729111113819"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p17827348113819"><a name="en-us_topic_0112992344_p17827348113819"></a><a name="en-us_topic_0112992344_p17827348113819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p965135964018"><a name="en-us_topic_0112992344_p965135964018"></a><a name="en-us_topic_0112992344_p965135964018"></a>Both the plaintext (64 bytes) of a DEK and the SHA-256 hash value (32 bytes) of the plaintext are expressed as a hexadecimal character string.</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p63747682113930"><a name="en-us_topic_0112992344_p63747682113930"></a><a name="en-us_topic_0112992344_p63747682113930"></a>datakey_plain_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p26101679113930"><a name="en-us_topic_0112992344_p26101679113930"></a><a name="en-us_topic_0112992344_p26101679113930"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p63288584113930"><a name="en-us_topic_0112992344_p63288584113930"></a><a name="en-us_topic_0112992344_p63288584113930"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p7134121514415"><a name="en-us_topic_0112992344_p7134121514415"></a><a name="en-us_topic_0112992344_p7134121514415"></a>Number of bytes of a DEK in plaintext. The value is <strong id="en-us_topic_0112992344_b14844103283612"><a name="en-us_topic_0112992344_b14844103283612"></a><a name="en-us_topic_0112992344_b14844103283612"></a>64</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p269135101746"><a name="en-us_topic_0112992344_p269135101746"></a><a name="en-us_topic_0112992344_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p20967256101746"><a name="en-us_topic_0112992344_p20967256101746"></a><a name="en-us_topic_0112992344_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p21799971101746"><a name="en-us_topic_0112992344_p21799971101746"></a><a name="en-us_topic_0112992344_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p1376019217293"><a name="en-us_topic_0112992344_p1376019217293"></a><a name="en-us_topic_0112992344_p1376019217293"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992344_p20626198101746"><a name="en-us_topic_0112992344_p20626198101746"></a><a name="en-us_topic_0112992344_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992344_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992344_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992344_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992344_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992344_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992344_a9156e0b03f054d4e8547e0787f88a51b"></a><strong id="en-us_topic_0112992344_b63432748"><a name="en-us_topic_0112992344_b63432748"></a><a name="en-us_topic_0112992344_b63432748"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992344_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992344_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992344_a1851157c81e14d7f82db752a5737195a"></a><strong id="en-us_topic_0112992344_b842352706184736"><a name="en-us_topic_0112992344_b842352706184736"></a><a name="en-us_topic_0112992344_b842352706184736"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992344_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992344_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992344_a39360acf5daf4c01a1ebddeff5d68a1c"></a><strong id="en-us_topic_0112992344_b842352706184730"><a name="en-us_topic_0112992344_b842352706184730"></a><a name="en-us_topic_0112992344_b842352706184730"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992344_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992344_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992344_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992344_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p43705601102713"><a name="en-us_topic_0112992344_p43705601102713"></a><a name="en-us_topic_0112992344_p43705601102713"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p63384753102713"><a name="en-us_topic_0112992344_p63384753102713"></a><a name="en-us_topic_0112992344_p63384753102713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p50492797102713"><a name="en-us_topic_0112992344_p50492797102713"></a><a name="en-us_topic_0112992344_p50492797102713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p33891398102713"><a name="en-us_topic_0112992344_p33891398102713"></a><a name="en-us_topic_0112992344_p33891398102713"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p39084276114251"><a name="en-us_topic_0112992344_p39084276114251"></a><a name="en-us_topic_0112992344_p39084276114251"></a>cipher_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p8966119114251"><a name="en-us_topic_0112992344_p8966119114251"></a><a name="en-us_topic_0112992344_p8966119114251"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p11709755114251"><a name="en-us_topic_0112992344_p11709755114251"></a><a name="en-us_topic_0112992344_p11709755114251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p55167072114251"><a name="en-us_topic_0112992344_p55167072114251"></a><a name="en-us_topic_0112992344_p55167072114251"></a>The ciphertext of a DEK is expressed in hexadecimal format, and two characters indicate one byte.</p>
</td>
</tr>
<tr id="en-us_topic_0112992344_row2815702411432"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992344_p52145403114310"><a name="en-us_topic_0112992344_p52145403114310"></a><a name="en-us_topic_0112992344_p52145403114310"></a>datakey_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992344_p5005242114310"><a name="en-us_topic_0112992344_p5005242114310"></a><a name="en-us_topic_0112992344_p5005242114310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992344_p63028134114310"><a name="en-us_topic_0112992344_p63028134114310"></a><a name="en-us_topic_0112992344_p63028134114310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992344_p2771421114310"><a name="en-us_topic_0112992344_p2771421114310"></a><a name="en-us_topic_0112992344_p2771421114310"></a>Number of bytes in the length of a DEK</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992344_section144011443913"></a>

The following example describes how to use a CMK \(ID:  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**\) to encrypt a plaintext DEK \(plaintext:  **00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000F5A5FD42D16A20302798EF6ED309979B43003D2320D9F0E8EA9831A92759FB4B**; length: 64 bits\).

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "plain_text": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000F5A5FD42D16A20302798EF6ED309979B43003D2320D9F0E8EA9831A92759FB4B",
        "datakey_plain_length": "64"
    }
    ```

-   Example response

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "cipher_text": "020098005273E14E6E8E95F5463BECDC27E80AF820B9FC086CB47861899149F67CF07DAFF2810B7D27BDF19AB7632488E0926A48DB2FC85BEA905119411B46244C5E6B8036C60A0B0B4842FFE6994518E89C19B1C1D688D9043BCD6053EA7BA0652642CE59F2543C80669139F4F71ABB9BD9A24330643034363662302D653732372D346439632D623335642D66383462623437346133376600000000D34457984F9730D57F228C210FD22CA6017913964B21D4ECE45D81092BB9112E",
        "datakey_length": "64"
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


## Status Codes<a name="en-us_topic_0112992344_section3454223421"></a>

[Table 4](#en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992344_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992344_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992344_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992344_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992344_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992344_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992344_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992344_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992344_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992344_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992344_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

