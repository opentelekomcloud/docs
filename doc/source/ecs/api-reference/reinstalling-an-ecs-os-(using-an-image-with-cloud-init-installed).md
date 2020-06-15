# Reinstalling an ECS OS \(Using an Image with Cloud-Init Installed\)<a name="EN-US_TOPIC_0067876349"></a>

## Function<a name="section61372619"></a>

This API is used to reinstall an ECS OS. During the system disk reinstallation using the original image, the data disks of the ECS remain unchanged.

After this API is called, the system uninstalls the system disk, uses the original image to create a system disk, and attaches it to the ECS. In this way, the OS is reinstalled.

## Constraints<a name="section2842257210401"></a>

-   You can only use an image with Cloud-Init or Cloudbase-Init installed. 
-   You can reinstall OS only on an ECS that is stopped or for which OS reinstallation has failed.
-   You are not allowed to reinstall the OS of an ECS that does not have the system disk.
-   You are not allowed to perform other operations when reinstalling the OS. Otherwise, reinstalling the OS will fail.

## URI<a name="section15482662"></a>

POST /v2/\{project\_id\}/cloudservers/\{server\_id\}/reinstallos

[Table 1](#table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table55945983"></a>
<table><thead align="left"><tr id="row11302482"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p294000"><a name="p294000"></a><a name="p294000"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49888896"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p7411459134810"><a name="p7411459134810"></a><a name="p7411459134810"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row613736410235"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p2736446410235"><a name="p2736446410235"></a><a name="p2736446410235"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p192907210235"><a name="p192907210235"></a><a name="p192907210235"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p2203711610235"><a name="p2203711610235"></a><a name="p2203711610235"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5126234"></a>

[Table 2](#table2840889)  describes the request parameters.

**Table  2**  Request parameters

<a name="table2840889"></a>
<table><thead align="left"><tr id="row19854472"><th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.5.1.1"><p id="p5212090120624"><a name="p5212090120624"></a><a name="p5212090120624"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.2"><p id="p5568008920626"><a name="p5568008920626"></a><a name="p5568008920626"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p4189246820628"><a name="p4189246820628"></a><a name="p4189246820628"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.44%" id="mcps1.2.5.1.4"><p id="p2137802720629"><a name="p2137802720629"></a><a name="p2137802720629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6277626"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p38725660"><a name="p38725660"></a><a name="p38725660"></a>os-reinstall</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p49770771"><a name="p49770771"></a><a name="p49770771"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p4900679"><a name="p4900679"></a><a name="p4900679"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.44%" headers="mcps1.2.5.1.4 "><p id="p61410719"><a name="p61410719"></a><a name="p61410719"></a>Reinstalls an ECS OS. For details, see <a href="#table32200631">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **os-reinstall**  field description

<a name="table32200631"></a>
<table><thead align="left"><tr id="row47660253"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="p17130113293015"><a name="p17130113293015"></a><a name="p17130113293015"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.2"><p id="p101301832193010"><a name="p101301832193010"></a><a name="p101301832193010"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p813003213017"><a name="p813003213017"></a><a name="p813003213017"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.43%" id="mcps1.2.5.1.4"><p id="p19146143273020"><a name="p19146143273020"></a><a name="p19146143273020"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45934497"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p29706771"><a name="p29706771"></a><a name="p29706771"></a>keyname</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p57438237"><a name="p57438237"></a><a name="p57438237"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p21985640"><a name="p21985640"></a><a name="p21985640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.2.5.1.4 "><p id="p36006428"><a name="p36006428"></a><a name="p36006428"></a>Specifies the key pair name.</p>
</td>
</tr>
<tr id="row2345411710289"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p2073531110289"><a name="p2073531110289"></a><a name="p2073531110289"></a>userid</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p183865010289"><a name="p183865010289"></a><a name="p183865010289"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p1471297410289"><a name="p1471297410289"></a><a name="p1471297410289"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.2.5.1.4 "><p id="p5090020910289"><a name="p5090020910289"></a><a name="p5090020910289"></a>Specifies the user ID. This parameter is mandatory when <strong id="b132012396254"><a name="b132012396254"></a><a name="b132012396254"></a>keyname</strong> is used.</p>
</td>
</tr>
<tr id="row6144862102847"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p27971812102847"><a name="p27971812102847"></a><a name="p27971812102847"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.2 "><p id="p51124270102847"><a name="p51124270102847"></a><a name="p51124270102847"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p47425188102847"><a name="p47425188102847"></a><a name="p47425188102847"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.2.5.1.4 "><p id="p16235056102847"><a name="p16235056102847"></a><a name="p16235056102847"></a>Specifies metadata of the reinstalled ECS.</p>
<p id="p3830913711291"><a name="p3830913711291"></a><a name="p3830913711291"></a>For more information, see <a href="#table9120223">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **metadata**  field description

<a name="table9120223"></a>
<table><thead align="left"><tr id="row45607220"><th class="cellrowborder" valign="top" width="16.81%" id="mcps1.2.5.1.1"><p id="p1139016367303"><a name="p1139016367303"></a><a name="p1139016367303"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.64%" id="mcps1.2.5.1.2"><p id="p18390836193011"><a name="p18390836193011"></a><a name="p18390836193011"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.189999999999998%" id="mcps1.2.5.1.3"><p id="p6390153618307"><a name="p6390153618307"></a><a name="p6390153618307"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.36%" id="mcps1.2.5.1.4"><p id="p83901436133015"><a name="p83901436133015"></a><a name="p83901436133015"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56761457"><td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.5.1.1 "><p id="p36421405103024"><a name="p36421405103024"></a><a name="p36421405103024"></a>BYOL</p>
</td>
<td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.5.1.2 "><p id="p24837051"><a name="p24837051"></a><a name="p24837051"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p65644149"><a name="p65644149"></a><a name="p65644149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.36%" headers="mcps1.2.5.1.4 "><p id="p13345152413333"><a name="p13345152413333"></a><a name="p13345152413333"></a>Specifies whether a user has the license of an image.</p>
<a name="ul7453134512326"></a><a name="ul7453134512326"></a><ul id="ul7453134512326"><li>If this parameter is set to <strong id="b842352706215655"><a name="b842352706215655"></a><a name="b842352706215655"></a>true</strong>, the license file delivered with the image is used, indicating that BYOL is used.</li><li>If this parameter is set to a value other than <strong id="b1593034899215814"><a name="b1593034899215814"></a><a name="b1593034899215814"></a>true</strong>, BYOL is not used, and the license file provided by the public cloud platform must be used.</li></ul>
<p id="p1213811423217"><a name="p1213811423217"></a><a name="p1213811423217"></a>The default value is not <strong id="b184625899215847"><a name="b184625899215847"></a><a name="b184625899215847"></a>true</strong>, indicating that BYOL is not used.</p>
</td>
</tr>
<tr id="row11285618104313"><td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.5.1.1 "><p id="p1737951110318"><a name="p1737951110318"></a><a name="p1737951110318"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="17.64%" headers="mcps1.2.5.1.2 "><p id="p39934810104313"><a name="p39934810104313"></a><a name="p39934810104313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.189999999999998%" headers="mcps1.2.5.1.3 "><p id="p13494158104313"><a name="p13494158104313"></a><a name="p13494158104313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.36%" headers="mcps1.2.5.1.4 "><p id="p4078366294136"><a name="p4078366294136"></a><a name="p4078366294136"></a>Specifies the user data to be injected during the ECS reinstallation process.</p>
<p id="p3150863894136"><a name="p3150863894136"></a><a name="p3150863894136"></a>Text and text files can be injected. The content to be injected cannot be greater than 32 KB in size. The content to be injected must be encoded with base64.</p>
<p id="p18485123125818"><a name="p18485123125818"></a><a name="p18485123125818"></a>For more details, see "User Data Injection" in <em id="i16685141017211"><a name="i16685141017211"></a><a name="i16685141017211"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section46136113"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section4722162513312"></a>

-   Example URL request

    ```
    POST https://{endpoint}/v2/{project_id}/cloudservers/{server_id}/reinstallos
    ```

-   Example request 1 \(using a password to remotely log in to an ECS with OS reinstalled\)

    ```
    {
        "os-reinstall": {
            "adminpass": "!QAZxsw2", 
            "userid": "7e25b1da389f4697a79df3a0e5bd494e",
            "mode": "withStopServer"
        }
    }
    ```


-   Example request 2 \(using a key to remotely log in to an ECS with OS reinstalled\)

    ```
    {
        "os-reinstall": {
            "keyname": "KeyPair-350b", 
            "userid": "7e25b1da389f4697a79df3a0e5bd494e"
        }
    }
    ```


## Example Response<a name="section079845214419"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

