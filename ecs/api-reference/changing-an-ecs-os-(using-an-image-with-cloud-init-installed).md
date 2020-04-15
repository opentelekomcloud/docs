# Changing an ECS OS \(Using an Image with Cloud-Init Installed\)<a name="EN-US_TOPIC_0067876971"></a>

## Function<a name="section61372619"></a>

This API is used to change an ECS OS. During the system disk reinstallation using a new image, the data disks of the ECS remain unchanged.

After this API is called, the system uninstalls the system disk, uses the new image to create a system disk, and attaches it to the ECS. In this way, the OS is changed.

## Constraints<a name="section2842257210401"></a>

-   You can only use an image with Cloud-Init or Cloudbase-Init installed. .
-   Only a stopped ECS or an ECS on which reinstalling or changing the OS failed supports changing OS.
-   Only an ECS with a system disk supports changing OS.
-   You are not allowed to perform other operations when changing the OS. Otherwise, changing the OS will fail.

## URI<a name="section15482662"></a>

POST /v2/\{project\_id\}/cloudservers/\{server\_id\}/changeos

[Table 1](#table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table55945983"></a>
<table><thead align="left"><tr id="row11302482"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p294000"><a name="p294000"></a><a name="p294000"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.84%" id="mcps1.2.4.1.3"><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49888896"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.84%" headers="mcps1.2.4.1.3 "><p id="p14668137174919"><a name="p14668137174919"></a><a name="p14668137174919"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row613736410235"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p2736446410235"><a name="p2736446410235"></a><a name="p2736446410235"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p192907210235"><a name="p192907210235"></a><a name="p192907210235"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.84%" headers="mcps1.2.4.1.3 "><p id="p2203711610235"><a name="p2203711610235"></a><a name="p2203711610235"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5126234"></a>

[Table 2](#table2840889)  describes the request parameters.

**Table  2**  Request parameters

<a name="table2840889"></a>
<table><thead align="left"><tr id="row19854472"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p5212090120624"><a name="p5212090120624"></a><a name="p5212090120624"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.68%" id="mcps1.2.5.1.2"><p id="p5568008920626"><a name="p5568008920626"></a><a name="p5568008920626"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.3"><p id="p4189246820628"><a name="p4189246820628"></a><a name="p4189246820628"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.8%" id="mcps1.2.5.1.4"><p id="p2137802720629"><a name="p2137802720629"></a><a name="p2137802720629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6277626"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p38725660"><a name="p38725660"></a><a name="p38725660"></a>os-change</p>
</td>
<td class="cellrowborder" valign="top" width="17.68%" headers="mcps1.2.5.1.2 "><p id="p49770771"><a name="p49770771"></a><a name="p49770771"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.3 "><p id="p4900679"><a name="p4900679"></a><a name="p4900679"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.8%" headers="mcps1.2.5.1.4 "><p id="p61410719"><a name="p61410719"></a><a name="p61410719"></a>Changes an ECS OS. For details, see <a href="#table32200631">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **os-change**  field description

<a name="table32200631"></a>
<table><thead align="left"><tr id="row47660253"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p121269618348"><a name="p121269618348"></a><a name="p121269618348"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p1312613618346"><a name="p1312613618346"></a><a name="p1312613618346"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p51418673415"><a name="p51418673415"></a><a name="p51418673415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p7141166143418"><a name="p7141166143418"></a><a name="p7141166143418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45934497"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p29706771"><a name="p29706771"></a><a name="p29706771"></a>keyname</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p57438237"><a name="p57438237"></a><a name="p57438237"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p21985640"><a name="p21985640"></a><a name="p21985640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p36006428"><a name="p36006428"></a><a name="p36006428"></a>Specifies the key pair name.</p>
</td>
</tr>
<tr id="row2345411710289"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p2073531110289"><a name="p2073531110289"></a><a name="p2073531110289"></a>userid</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p183865010289"><a name="p183865010289"></a><a name="p183865010289"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1471297410289"><a name="p1471297410289"></a><a name="p1471297410289"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p5090020910289"><a name="p5090020910289"></a><a name="p5090020910289"></a>Specifies the user ID. This parameter is mandatory when <strong id="b154176101293"><a name="b154176101293"></a><a name="b154176101293"></a>keyname</strong> is used.</p>
</td>
</tr>
<tr id="row13463057104537"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p16765867104537"><a name="p16765867104537"></a><a name="p16765867104537"></a>imageid</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p15858014104537"><a name="p15858014104537"></a><a name="p15858014104537"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p9430737104537"><a name="p9430737104537"></a><a name="p9430737104537"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p25692204104537"><a name="p25692204104537"></a><a name="p25692204104537"></a>Specifies the ID of the new image in UUID format.</p>
<p id="p280873817134"><a name="p280873817134"></a><a name="p280873817134"></a>You can obtain the image ID from the console or by following the instructions provided in "Querying Images" in <em id="i168512108319"><a name="i168512108319"></a><a name="i168512108319"></a>Image Management Service API Reference</em>.</p>
</td>
</tr>
<tr id="row6144862102847"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p27971812102847"><a name="p27971812102847"></a><a name="p27971812102847"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p51124270102847"><a name="p51124270102847"></a><a name="p51124270102847"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p47425188102847"><a name="p47425188102847"></a><a name="p47425188102847"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p16235056102847"><a name="p16235056102847"></a><a name="p16235056102847"></a>Specifies the metadata of the ECS for which the OS is to be changed.</p>
<p id="p45467933113554"><a name="p45467933113554"></a><a name="p45467933113554"></a>For more information, see <a href="#table9120223">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **metadata**  field description

<a name="table9120223"></a>
<table><thead align="left"><tr id="row45607220"><th class="cellrowborder" valign="top" width="16.5016501650165%" id="mcps1.2.5.1.1"><p id="p5260151013341"><a name="p5260151013341"></a><a name="p5260151013341"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.75177517751775%" id="mcps1.2.5.1.2"><p id="p1226017106348"><a name="p1226017106348"></a><a name="p1226017106348"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.881588158815882%" id="mcps1.2.5.1.3"><p id="p226013107341"><a name="p226013107341"></a><a name="p226013107341"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.86498649864986%" id="mcps1.2.5.1.4"><p id="p526021019349"><a name="p526021019349"></a><a name="p526021019349"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56761457"><td class="cellrowborder" valign="top" width="16.5016501650165%" headers="mcps1.2.5.1.1 "><p id="p36421405103024"><a name="p36421405103024"></a><a name="p36421405103024"></a>BYOL</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.2.5.1.2 "><p id="p24837051"><a name="p24837051"></a><a name="p24837051"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.881588158815882%" headers="mcps1.2.5.1.3 "><p id="p65644149"><a name="p65644149"></a><a name="p65644149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.86498649864986%" headers="mcps1.2.5.1.4 "><p id="p15575880"><a name="p15575880"></a><a name="p15575880"></a>Specifies whether a user has the license of an image.</p>
<a name="ul7453134512326"></a><a name="ul7453134512326"></a><ul id="ul7453134512326"><li>If this parameter is set to <strong id="b842352706215655"><a name="b842352706215655"></a><a name="b842352706215655"></a>true</strong>, the license file delivered with the image is used, indicating that BYOL is used.</li><li>If this parameter is set to a value other than <strong id="b1593034899215814"><a name="b1593034899215814"></a><a name="b1593034899215814"></a>true</strong>, BYOL is not used, and the license file provided by the public cloud platform must be used.</li></ul>
<p id="p1213811423217"><a name="p1213811423217"></a><a name="p1213811423217"></a>The default value is not <strong id="b184625899215847"><a name="b184625899215847"></a><a name="b184625899215847"></a>true</strong>, indicating that BYOL is not used.</p>
</td>
</tr>
<tr id="row11285618104313"><td class="cellrowborder" valign="top" width="16.5016501650165%" headers="mcps1.2.5.1.1 "><p id="p1737951110318"><a name="p1737951110318"></a><a name="p1737951110318"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.2.5.1.2 "><p id="p39934810104313"><a name="p39934810104313"></a><a name="p39934810104313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.881588158815882%" headers="mcps1.2.5.1.3 "><p id="p13494158104313"><a name="p13494158104313"></a><a name="p13494158104313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.86498649864986%" headers="mcps1.2.5.1.4 "><p id="p509712594125"><a name="p509712594125"></a><a name="p509712594125"></a>Specifies the user data to be injected during the ECS OS change process.</p>
<p id="p4587413094125"><a name="p4587413094125"></a><a name="p4587413094125"></a>Text and text files can be injected. The content to be injected cannot be greater than 32 KB in size. The content to be injected must be encoded with base64.</p>
<p id="p1911316217100"><a name="p1911316217100"></a><a name="p1911316217100"></a>For more details, see "User Data Injection" in <em id="en-us_topic_0067876349_i16685141017211"><a name="en-us_topic_0067876349_i16685141017211"></a><a name="en-us_topic_0067876349_i16685141017211"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section46136113"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section6230163813416"></a>

-   Example URL request

    ```
    POST https://{endpoint}/v2/{project_id}/cloudservers/{server_id}/changeos
    ```


-   Example request 1 \(using a password to remotely log in to an ECS with OS changed\)

    ```
    {
        "os-change": {
            "adminpass": "1qazXSW@", 
            "userid": "7e25b1da389f4697a79df3a0e5bd494e", 
            "imageid": "e215580f-73ad-429d-b6f2-5433947433b0",
            "mode": "withStopServer"
        }
    }
    ```


-   Example request 2 \(using a key to remotely log in to an ECS with OS changed\)

    ```
    {
        "os-change": {
            "keyname": "KeyPair-350b", 
            "userid": "7e25b1da389f4697a79df3a0e5bd494e", 
            "imageid": "e215580f-73ad-429d-b6f2-5433947433b0"
        }
    }
    ```


## Example Response<a name="section449243013451"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

