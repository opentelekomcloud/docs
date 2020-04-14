# Decrypting a DEK<a name="kms_02_0023"></a>

## Function<a name="en-us_topic_0112992306_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API enables you to decrypt a DEK using a specified CMK.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Decrypted data is the result in the encrypted data.  

## URI<a name="en-us_topic_0112992306_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/decrypt-datakey

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992306_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992306_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992306_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992306_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992306_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992306_b842352706185055"><a name="en-us_topic_0112992306_b842352706185055"></a><a name="en-us_topic_0112992306_b842352706185055"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992306_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992306_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992306_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992306_b842352706185059"><a name="en-us_topic_0112992306_b842352706185059"></a><a name="en-us_topic_0112992306_b842352706185059"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992306_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992306_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992306_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992306_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992306_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992306_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992306_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992306_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992306_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992306_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992306_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992306_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992306_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992306_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992306_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992306_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992306_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992306_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992306_p16364058101230"><a name="en-us_topic_0112992306_p16364058101230"></a><a name="en-us_topic_0112992306_p16364058101230"></a><strong id="en-us_topic_0112992306_b1581751364"><a name="en-us_topic_0112992306_b1581751364"></a><a name="en-us_topic_0112992306_b1581751364"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992306_p57514295101230"><a name="en-us_topic_0112992306_p57514295101230"></a><a name="en-us_topic_0112992306_p57514295101230"></a><strong id="en-us_topic_0112992306_b842352706185139"><a name="en-us_topic_0112992306_b842352706185139"></a><a name="en-us_topic_0112992306_b842352706185139"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992306_p50420322101230"><a name="en-us_topic_0112992306_p50420322101230"></a><a name="en-us_topic_0112992306_p50420322101230"></a><strong id="en-us_topic_0112992306_b842352706185135"><a name="en-us_topic_0112992306_b842352706185135"></a><a name="en-us_topic_0112992306_b842352706185135"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992306_p28146304101230"><a name="en-us_topic_0112992306_p28146304101230"></a><a name="en-us_topic_0112992306_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992306_row44009584101643"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p25230249114629"><a name="en-us_topic_0112992306_p25230249114629"></a><a name="en-us_topic_0112992306_p25230249114629"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p45211023114629"><a name="en-us_topic_0112992306_p45211023114629"></a><a name="en-us_topic_0112992306_p45211023114629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p30384322114629"><a name="en-us_topic_0112992306_p30384322114629"></a><a name="en-us_topic_0112992306_p30384322114629"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p54539681174026"><a name="en-us_topic_0112992306_p54539681174026"></a><a name="en-us_topic_0112992306_p54539681174026"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992306_parmvalue80435593163333"><a name="en-us_topic_0112992306_parmvalue80435593163333"></a><a name="en-us_topic_0112992306_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992306_p38214265114629"><a name="en-us_topic_0112992306_p38214265114629"></a><a name="en-us_topic_0112992306_p38214265114629"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_row30347711135526"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p5287641135529"><a name="en-us_topic_0112992306_p5287641135529"></a><a name="en-us_topic_0112992306_p5287641135529"></a>encryption_context</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p64039712135529"><a name="en-us_topic_0112992306_p64039712135529"></a><a name="en-us_topic_0112992306_p64039712135529"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p25645748135529"><a name="en-us_topic_0112992306_p25645748135529"></a><a name="en-us_topic_0112992306_p25645748135529"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p299262517255"><a name="en-us_topic_0112992306_p299262517255"></a><a name="en-us_topic_0112992306_p299262517255"></a>Key-value pairs with a maximum length of 8192 characters. This parameter is used to record resource context information, excluding sensitive information, to ensure data integrity.</p>
<p id="en-us_topic_0112992306_p87033116108"><a name="en-us_topic_0112992306_p87033116108"></a><a name="en-us_topic_0112992306_p87033116108"></a>If this parameter is specified during encryption, it is also required for decryption.</p>
<p id="en-us_topic_0112992306_p23626609135526"><a name="en-us_topic_0112992306_p23626609135526"></a><a name="en-us_topic_0112992306_p23626609135526"></a>Example: {"Key1":"Value1","Key2":"Value2"}</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_row57603225101653"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p33956697114642"><a name="en-us_topic_0112992306_p33956697114642"></a><a name="en-us_topic_0112992306_p33956697114642"></a>cipher_text</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p55574642114642"><a name="en-us_topic_0112992306_p55574642114642"></a><a name="en-us_topic_0112992306_p55574642114642"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p66137961114642"><a name="en-us_topic_0112992306_p66137961114642"></a><a name="en-us_topic_0112992306_p66137961114642"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p5252123114642"><a name="en-us_topic_0112992306_p5252123114642"></a><a name="en-us_topic_0112992306_p5252123114642"></a>This parameter indicates the hexadecimal character string of the DEK ciphertext and the metadata. The value is the <span class="parmname" id="en-us_topic_0112992306_parmname769647905171927"><a name="en-us_topic_0112992306_parmname769647905171927"></a><a name="en-us_topic_0112992306_parmname769647905171927"></a><b>cipher_text</b></span> value in the encryption result of a DEK.</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_row2638193101722"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p3383517611471"><a name="en-us_topic_0112992306_p3383517611471"></a><a name="en-us_topic_0112992306_p3383517611471"></a>datakey_cipher_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p6358152411471"><a name="en-us_topic_0112992306_p6358152411471"></a><a name="en-us_topic_0112992306_p6358152411471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p5629475811471"><a name="en-us_topic_0112992306_p5629475811471"></a><a name="en-us_topic_0112992306_p5629475811471"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p512116290426"><a name="en-us_topic_0112992306_p512116290426"></a><a name="en-us_topic_0112992306_p512116290426"></a>Number of bytes of a key. The value is <strong id="en-us_topic_0112992306_b373245813371"><a name="en-us_topic_0112992306_b373245813371"></a><a name="en-us_topic_0112992306_b373245813371"></a>64</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p269135101746"><a name="en-us_topic_0112992306_p269135101746"></a><a name="en-us_topic_0112992306_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p20967256101746"><a name="en-us_topic_0112992306_p20967256101746"></a><a name="en-us_topic_0112992306_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p21799971101746"><a name="en-us_topic_0112992306_p21799971101746"></a><a name="en-us_topic_0112992306_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p3081640174038"><a name="en-us_topic_0112992306_p3081640174038"></a><a name="en-us_topic_0112992306_p3081640174038"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992306_p20626198101746"><a name="en-us_topic_0112992306_p20626198101746"></a><a name="en-us_topic_0112992306_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992306_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992306_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992306_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992306_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992306_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992306_a9156e0b03f054d4e8547e0787f88a51b"></a><strong id="en-us_topic_0112992306_b2084849838"><a name="en-us_topic_0112992306_b2084849838"></a><a name="en-us_topic_0112992306_b2084849838"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992306_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992306_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992306_a1851157c81e14d7f82db752a5737195a"></a><strong id="en-us_topic_0112992306_b842352706185231"><a name="en-us_topic_0112992306_b842352706185231"></a><a name="en-us_topic_0112992306_b842352706185231"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992306_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992306_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992306_a39360acf5daf4c01a1ebddeff5d68a1c"></a><strong id="en-us_topic_0112992306_b842352706185227"><a name="en-us_topic_0112992306_b842352706185227"></a><a name="en-us_topic_0112992306_b842352706185227"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992306_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992306_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992306_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992306_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p59584906114917"><a name="en-us_topic_0112992306_p59584906114917"></a><a name="en-us_topic_0112992306_p59584906114917"></a>data_key</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p27437119114917"><a name="en-us_topic_0112992306_p27437119114917"></a><a name="en-us_topic_0112992306_p27437119114917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p61648062114917"><a name="en-us_topic_0112992306_p61648062114917"></a><a name="en-us_topic_0112992306_p61648062114917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p7814132114917"><a name="en-us_topic_0112992306_p7814132114917"></a><a name="en-us_topic_0112992306_p7814132114917"></a>Hexadecimal character string of the plaintext of a DEK</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p54607285114928"><a name="en-us_topic_0112992306_p54607285114928"></a><a name="en-us_topic_0112992306_p54607285114928"></a>datakey_length</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p51283633114928"><a name="en-us_topic_0112992306_p51283633114928"></a><a name="en-us_topic_0112992306_p51283633114928"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p61113959114928"><a name="en-us_topic_0112992306_p61113959114928"></a><a name="en-us_topic_0112992306_p61113959114928"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p60333628114928"><a name="en-us_topic_0112992306_p60333628114928"></a><a name="en-us_topic_0112992306_p60333628114928"></a>Number of bytes in the length of the plaintext of a DEK</p>
</td>
</tr>
<tr id="en-us_topic_0112992306_row55201929114939"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992306_p59861561114947"><a name="en-us_topic_0112992306_p59861561114947"></a><a name="en-us_topic_0112992306_p59861561114947"></a>datakey_dgst</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992306_p30631348114947"><a name="en-us_topic_0112992306_p30631348114947"></a><a name="en-us_topic_0112992306_p30631348114947"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992306_p16948254114947"><a name="en-us_topic_0112992306_p16948254114947"></a><a name="en-us_topic_0112992306_p16948254114947"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992306_p65220130114947"><a name="en-us_topic_0112992306_p65220130114947"></a><a name="en-us_topic_0112992306_p65220130114947"></a>Hexadecimal character string corresponding to the SHA-256 hash value of the plaintext of a DEK</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992306_section67751049194716"></a>

The following is an example about how to use a CMK \(ID:  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**\) to decrypt a DEK \(ciphertext:  **020098005273E14E6E8E95F5463BECDC27E80AF820B9FC086CB47861899149F67CF07DAFF2810B7D27BDF19AB7632488E0926A48DB2FC85BEA905119411B46244C5E6B8036C60A0B0B4842FFE6994518E89C19B1C1D688D9043BCD6053EA7BA0652642CE59F2543C80669139F4F71ABB9BD9A24330643034363662302D653732372D346439632D623335642D66383462623437346133376600000000D34457984F9730D57F228C210FD22CA6017913964B21D4ECE45D81092BB9112E**; length:  **64**  bits\).

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
        "datakey_cipher_length": "64",
        "cipher_text": "020098005273E14E6E8E95F5463BECDC27E80AF820B9FC086CB47861899149F67CF07DAFF2810B7D27BDF19AB7632488E0926A48DB2FC85BEA905119411B46244C5E6B8036C60A0B0B4842FFE6994518E89C19B1C1D688D9043BCD6053EA7BA0652642CE59F2543C80669139F4F71ABB9BD9A24330643034363662302D653732372D346439632D623335642D66383462623437346133376600000000D34457984F9730D57F228C210FD22CA6017913964B21D4ECE45D81092BB9112E"
    }
    ```


-   Example response

    ```
    {
        "data_key": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "datakey_length": "64",
        "datakey_dgst": "F5A5FD42D16A20302798EF6ED309979B43003D2320D9F0E8EA9831A92759FB4B"
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


## Status Codes<a name="en-us_topic_0112992306_section3454223421"></a>

[Table 4](#en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992306_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992306_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992306_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992306_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992306_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992306_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992306_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992306_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992306_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992306_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992306_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

