# Creating a CMK<a name="kms_02_0012"></a>

## Function<a name="en-us_topic_0112992294_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API is used to create customer master keys \(CMKs\) used to encrypt data encryption keys \(DEKs\).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Default Master Keys are created by services integrated with KMS. Names of Default Master Keys end with  **/default**. Therefore, in naming your CMKs, do not choose those ending with  **/default**.  

## URI<a name="en-us_topic_0112992294_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/create-key

-   Parameter description

    **Table  1**  Parameters

    <a name="en-us_topic_0112992294_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992294_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992294_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992294_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992294_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992294_b842352706165836"><a name="en-us_topic_0112992294_b842352706165836"></a><a name="en-us_topic_0112992294_b842352706165836"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.31%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992294_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992294_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992294_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992294_b842352706165839"><a name="en-us_topic_0112992294_b842352706165839"></a><a name="en-us_topic_0112992294_b842352706165839"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.86%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992294_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992294_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992294_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.09%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992294_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992294_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992294_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992294_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992294_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992294_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.31%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992294_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992294_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992294_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992294_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.09%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992294_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992294_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992294_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992294_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992294_row9315574101230"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992294_p16364058101230"><a name="en-us_topic_0112992294_p16364058101230"></a><a name="en-us_topic_0112992294_p16364058101230"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992294_p57514295101230"><a name="en-us_topic_0112992294_p57514295101230"></a><a name="en-us_topic_0112992294_p57514295101230"></a><strong id="en-us_topic_0112992294_b842352706165630"><a name="en-us_topic_0112992294_b842352706165630"></a><a name="en-us_topic_0112992294_b842352706165630"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992294_p50420322101230"><a name="en-us_topic_0112992294_p50420322101230"></a><a name="en-us_topic_0112992294_p50420322101230"></a><strong id="en-us_topic_0112992294_b842352706165626"><a name="en-us_topic_0112992294_b842352706165626"></a><a name="en-us_topic_0112992294_b842352706165626"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992294_p28146304101230"><a name="en-us_topic_0112992294_p28146304101230"></a><a name="en-us_topic_0112992294_p28146304101230"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992294_row65258150101230"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p1543290910164"><a name="en-us_topic_0112992294_p1543290910164"></a><a name="en-us_topic_0112992294_p1543290910164"></a>key_alias</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p5515069010164"><a name="en-us_topic_0112992294_p5515069010164"></a><a name="en-us_topic_0112992294_p5515069010164"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p4210609710164"><a name="en-us_topic_0112992294_p4210609710164"></a><a name="en-us_topic_0112992294_p4210609710164"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_p3802087110164"><a name="en-us_topic_0112992294_p3802087110164"></a><a name="en-us_topic_0112992294_p3802087110164"></a>Alias of a non-default master key (The alias's length ranges from 1 to 255 characters and matches the regular expression <span class="parmvalue" id="en-us_topic_0112992294_parmvalue698033652174049"><a name="en-us_topic_0112992294_parmvalue698033652174049"></a><a name="en-us_topic_0112992294_parmvalue698033652174049"></a><b>^[a-zA-Z0-9:/_-]{1,255}$</b></span>. In addition, it must be different from the alias of a Default Master Key created by the system.)</p>
</td>
</tr>
<tr id="en-us_topic_0112992294_row2245699720624"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p707743220624"><a name="en-us_topic_0112992294_p707743220624"></a><a name="en-us_topic_0112992294_p707743220624"></a>key_description</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p6281259420624"><a name="en-us_topic_0112992294_p6281259420624"></a><a name="en-us_topic_0112992294_p6281259420624"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p3640115720624"><a name="en-us_topic_0112992294_p3640115720624"></a><a name="en-us_topic_0112992294_p3640115720624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_p5465533520624"><a name="en-us_topic_0112992294_p5465533520624"></a><a name="en-us_topic_0112992294_p5465533520624"></a>CMK description (The value ranges from 0 to 255 characters.)</p>
</td>
</tr>
<tr id="en-us_topic_0112992294_row56396726142438"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p4732068142438"><a name="en-us_topic_0112992294_p4732068142438"></a><a name="en-us_topic_0112992294_p4732068142438"></a>origin</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p42803505142438"><a name="en-us_topic_0112992294_p42803505142438"></a><a name="en-us_topic_0112992294_p42803505142438"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p47753194142438"><a name="en-us_topic_0112992294_p47753194142438"></a><a name="en-us_topic_0112992294_p47753194142438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992294_p44531872142438"><a name="en-us_topic_0112992294_p44531872142438"></a><a name="en-us_topic_0112992294_p44531872142438"></a>Origin of a CMK. The default value is <span class="parmvalue" id="en-us_topic_0112992294_parmvalue1849726112141249"><a name="en-us_topic_0112992294_parmvalue1849726112141249"></a><a name="en-us_topic_0112992294_parmvalue1849726112141249"></a><b>kms</b></span>. The following values are enumerated:<a name="en-us_topic_0112992294_ul43826915161742"></a><a name="en-us_topic_0112992294_ul43826915161742"></a><ul id="en-us_topic_0112992294_ul43826915161742"><li><span class="parmvalue" id="en-us_topic_0112992294_parmvalue1011124252141313"><a name="en-us_topic_0112992294_parmvalue1011124252141313"></a><a name="en-us_topic_0112992294_parmvalue1011124252141313"></a><b>kms</b></span> indicates that the CMK material is generated by KMS.</li><li><span class="parmvalue" id="en-us_topic_0112992294_parmvalue501259129141335"><a name="en-us_topic_0112992294_parmvalue501259129141335"></a><a name="en-us_topic_0112992294_parmvalue501259129141335"></a><b>external</b></span> indicates that the CMK material is imported.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992294_row35142504101726"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p269135101746"><a name="en-us_topic_0112992294_p269135101746"></a><a name="en-us_topic_0112992294_p269135101746"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p20967256101746"><a name="en-us_topic_0112992294_p20967256101746"></a><a name="en-us_topic_0112992294_p20967256101746"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p21799971101746"><a name="en-us_topic_0112992294_p21799971101746"></a><a name="en-us_topic_0112992294_p21799971101746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_p89331932112120"><a name="en-us_topic_0112992294_p89331932112120"></a><a name="en-us_topic_0112992294_p89331932112120"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992294_p20626198101746"><a name="en-us_topic_0112992294_p20626198101746"></a><a name="en-us_topic_0112992294_p20626198101746"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992294_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992294_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992294_r144a2c52c5054c6d9243eb2ef3875a21"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992294_a9156e0b03f054d4e8547e0787f88a51b"><a name="en-us_topic_0112992294_a9156e0b03f054d4e8547e0787f88a51b"></a><a name="en-us_topic_0112992294_a9156e0b03f054d4e8547e0787f88a51b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992294_a1851157c81e14d7f82db752a5737195a"><a name="en-us_topic_0112992294_a1851157c81e14d7f82db752a5737195a"></a><a name="en-us_topic_0112992294_a1851157c81e14d7f82db752a5737195a"></a><strong id="en-us_topic_0112992294_b842352706165935"><a name="en-us_topic_0112992294_b842352706165935"></a><a name="en-us_topic_0112992294_b842352706165935"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992294_a39360acf5daf4c01a1ebddeff5d68a1c"><a name="en-us_topic_0112992294_a39360acf5daf4c01a1ebddeff5d68a1c"></a><a name="en-us_topic_0112992294_a39360acf5daf4c01a1ebddeff5d68a1c"></a><strong id="en-us_topic_0112992294_b842352706165929"><a name="en-us_topic_0112992294_b842352706165929"></a><a name="en-us_topic_0112992294_b842352706165929"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992294_a0097000016b14857972b7929bcaaa038"><a name="en-us_topic_0112992294_a0097000016b14857972b7929bcaaa038"></a><a name="en-us_topic_0112992294_a0097000016b14857972b7929bcaaa038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992294_r3c4af7b36e9240d197ab56255e37b83c"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p43705601102713"><a name="en-us_topic_0112992294_p43705601102713"></a><a name="en-us_topic_0112992294_p43705601102713"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p63384753102713"><a name="en-us_topic_0112992294_p63384753102713"></a><a name="en-us_topic_0112992294_p63384753102713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p50492797102713"><a name="en-us_topic_0112992294_p50492797102713"></a><a name="en-us_topic_0112992294_p50492797102713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_p33891398102713"><a name="en-us_topic_0112992294_p33891398102713"></a><a name="en-us_topic_0112992294_p33891398102713"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992294_rf212a916c502452a8e151eba2f118272"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992294_p15241273102723"><a name="en-us_topic_0112992294_p15241273102723"></a><a name="en-us_topic_0112992294_p15241273102723"></a>domain_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992294_p5791264102723"><a name="en-us_topic_0112992294_p5791264102723"></a><a name="en-us_topic_0112992294_p5791264102723"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992294_p26583640102723"><a name="en-us_topic_0112992294_p26583640102723"></a><a name="en-us_topic_0112992294_p26583640102723"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992294_p66439224102723"><a name="en-us_topic_0112992294_p66439224102723"></a><a name="en-us_topic_0112992294_p66439224102723"></a>User domain ID</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992294_section1079019295212"></a>

The following example describes how to create a CMK with an alias of  **test**.

-   Example request

    ```
    {
        "key_alias": "test"
    }
    ```

-   Example response

    ```
    {
        "key_info": {
            "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
            "domain_id": "b168fe00ff56492495a7d22974df2d0b"
        }
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


## Status Codes<a name="en-us_topic_0112992294_s811d1a98cd5242509abd6671a9959d55"></a>

[Table 4](#en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

