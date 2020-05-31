# Querying the Brief Information on an Image Repository<a name="EN-US_TOPIC_0198655136"></a>

## Function<a name="section14905762191056"></a>

Query the brief information on an image repository in an organization.

## URI<a name="section10482810165331"></a>

GET /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}

For details about parameters, see  [Table 1](#table184146147323).

**Table  1**  Parameter description

<a name="table184146147323"></a>
<table><thead align="left"><tr id="row1415114163212"><th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.5.1.1"><p id="p9415114193219"><a name="p9415114193219"></a><a name="p9415114193219"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.63%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="26.169999999999998%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.42%" id="mcps1.2.5.1.4"><p id="p841591415328"><a name="p841591415328"></a><a name="p841591415328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row941641411326"><td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.1 "><p id="p8416314113213"><a name="p8416314113213"></a><a name="p8416314113213"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.5.1.2 "><p id="p105058419438"><a name="p105058419438"></a><a name="p105058419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.5.1.4 "><p id="p125744537118"><a name="p125744537118"></a><a name="p125744537118"></a>Organization name.</p>
</td>
</tr>
<tr id="row7417171415327"><td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.1 "><p id="p84177144326"><a name="p84177144326"></a><a name="p84177144326"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.5.1.2 "><p id="p148332434416"><a name="p148332434416"></a><a name="p148332434416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p18841424144414"><a name="p18841424144414"></a><a name="p18841424144414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.42%" headers="mcps1.2.5.1.4 "><p id="p181285313257"><a name="p181285313257"></a><a name="p181285313257"></a>Image repository name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

N/A

## Response<a name="section46271297104114"></a>

**Response parameters**

**Table  2**  Response body parameter description

<a name="table45446245174724"></a>
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="27.322732273227324%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.64226422642264%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.03500350035003%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18183212111616"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p7183111214169"><a name="p7183111214169"></a><a name="p7183111214169"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p579804420915"><a name="p579804420915"></a><a name="p579804420915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p618314125166"><a name="p618314125166"></a><a name="p618314125166"></a>Repository ID.</p>
</td>
</tr>
<tr id="row83724064918"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p175531977553"><a name="p175531977553"></a><a name="p175531977553"></a>ns_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p682894411915"><a name="p682894411915"></a><a name="p682894411915"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p478874916559"><a name="p478874916559"></a><a name="p478874916559"></a>Organization ID.</p>
</td>
</tr>
<tr id="row27392900174724"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p136471412613"><a name="p136471412613"></a><a name="p136471412613"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p121496311896"><a name="p121496311896"></a><a name="p121496311896"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p16410141865"><a name="p16410141865"></a><a name="p16410141865"></a>Repository name.</p>
</td>
</tr>
<tr id="row13262719202519"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p17262422112519"><a name="p17262422112519"></a><a name="p17262422112519"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p915418311394"><a name="p915418311394"></a><a name="p915418311394"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p72659228257"><a name="p72659228257"></a><a name="p72659228257"></a>Repository category.</p>
</td>
</tr>
<tr id="row54857361101036"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p164314066"><a name="p164314066"></a><a name="p164314066"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p51581931293"><a name="p51581931293"></a><a name="p51581931293"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p76481417619"><a name="p76481417619"></a><a name="p76481417619"></a>Repository description.</p>
</td>
</tr>
<tr id="row1333214382546"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p76414148613"><a name="p76414148613"></a><a name="p76414148613"></a>creator_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p13162193119915"><a name="p13162193119915"></a><a name="p13162193119915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p6645142613"><a name="p6645142613"></a><a name="p6645142613"></a>ID of the repository creator.</p>
</td>
</tr>
<tr id="row1627910320538"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p327917322532"><a name="p327917322532"></a><a name="p327917322532"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p91679311793"><a name="p91679311793"></a><a name="p91679311793"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p227953216531"><a name="p227953216531"></a><a name="p227953216531"></a>Repository creator.</p>
</td>
</tr>
<tr id="row252105335414"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p5652145619"><a name="p5652145619"></a><a name="p5652145619"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p197902115100"><a name="p197902115100"></a><a name="p197902115100"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p16651514769"><a name="p16651514769"></a><a name="p16651514769"></a>Repository size.</p>
</td>
</tr>
<tr id="row0112162345416"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p16605123617541"><a name="p16605123617541"></a><a name="p16605123617541"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p17790611191017"><a name="p17790611191017"></a><a name="p17790611191017"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p160713635413"><a name="p160713635413"></a><a name="p160713635413"></a>Whether the repository is public. When the value is <strong id="b1456932310313"><a name="b1456932310313"></a><a name="b1456932310313"></a>true</strong>, it indicates the repository is public. When the value is <strong id="b15439641135010"><a name="b15439641135010"></a><a name="b15439641135010"></a>false</strong>, it indicates the repository is private.</p>
</td>
</tr>
<tr id="row1298756155518"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p4652141067"><a name="p4652141067"></a><a name="p4652141067"></a>num_images</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p2790191131017"><a name="p2790191131017"></a><a name="p2790191131017"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p1065111415618"><a name="p1065111415618"></a><a name="p1065111415618"></a>Number of image tags in a repository.</p>
</td>
</tr>
<tr id="row18552048185417"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p85515483548"><a name="p85515483548"></a><a name="p85515483548"></a>num_download</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p117919113100"><a name="p117919113100"></a><a name="p117919113100"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p1955174817545"><a name="p1955174817545"></a><a name="p1955174817545"></a>Download times.</p>
</td>
</tr>
<tr id="row18027352101030"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p186581412611"><a name="p186581412611"></a><a name="p186581412611"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p52523331299"><a name="p52523331299"></a><a name="p52523331299"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p196551411613"><a name="p196551411613"></a><a name="p196551411613"></a>URL of the repository logo image. This field has been discarded and is left empty by default.</p>
</td>
</tr>
<tr id="row40294727101415"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p16512141666"><a name="p16512141666"></a><a name="p16512141666"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p12258433592"><a name="p12258433592"></a><a name="p12258433592"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p8659141362"><a name="p8659141362"></a><a name="p8659141362"></a>Image address for docker pull.</p>
</td>
</tr>
<tr id="row1532805417015"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p18329554201"><a name="p18329554201"></a><a name="p18329554201"></a>internal_path</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p1226410338916"><a name="p1226410338916"></a><a name="p1226410338916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p93304541909"><a name="p93304541909"></a><a name="p93304541909"></a>Intra-cluster image address for docker pull.</p>
</td>
</tr>
<tr id="row30282713101412"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p665161411614"><a name="p665161411614"></a><a name="p665161411614"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p027093310910"><a name="p027093310910"></a><a name="p027093310910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p16659141867"><a name="p16659141867"></a><a name="p16659141867"></a>Time when a repository is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row4788970510172"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p12652141616"><a name="p12652141616"></a><a name="p12652141616"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p065414567"><a name="p065414567"></a><a name="p065414567"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p16521413613"><a name="p16521413613"></a><a name="p16521413613"></a>Time when a repository is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row15113233114"><td class="cellrowborder" valign="top" width="27.322732273227324%" headers="mcps1.2.4.1.1 "><p id="p14115193016"><a name="p14115193016"></a><a name="p14115193016"></a>domain_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.64226422642264%" headers="mcps1.2.4.1.2 "><p id="p7115163219"><a name="p7115163219"></a><a name="p7115163219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.03500350035003%" headers="mcps1.2.4.1.3 "><p id="p17115231514"><a name="p17115231514"></a><a name="p17115231514"></a>Domain ID.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "id": 0,
    "ns_id": 0,
    "name": "busybox",
    "category": "other",
    "description": "containerops",
    "creator_id": "1",
    "creator_name": "admin",
    "size": 2099575,
    "is_public": false,
    "num_images": 0,
    "num_download": 0,
    "url": "",
    "path": "192.158.24.86/namespace/repository",
    "internal_path": "10.125.0.198:20202/namespace/repository",
    "created": "2017-08-17T12:00:03.915153267Z",
    "updated": "2017-08-17T12:00:03.915153267Z",
    "domain_id": "035744******dd5d2"
}
```

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 3](#table106791511367).

**Table  3**  Status code

<a name="table106791511367"></a>
<table><thead align="left"><tr id="row268045123616"><th class="cellrowborder" valign="top" width="24.279999999999998%" id="mcps1.2.3.1.1"><p id="p16680857367"><a name="p16680857367"></a><a name="p16680857367"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="75.72%" id="mcps1.2.3.1.2"><p id="p76801953368"><a name="p76801953368"></a><a name="p76801953368"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2680165133612"><td class="cellrowborder" valign="top" width="24.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p1768014593614"><a name="p1768014593614"></a><a name="p1768014593614"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="75.72%" headers="mcps1.2.3.1.2 "><p id="p176802583613"><a name="p176802583613"></a><a name="p176802583613"></a>Request sent successfully.</p>
</td>
</tr>
<tr id="row2680185123618"><td class="cellrowborder" valign="top" width="24.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p26809517369"><a name="p26809517369"></a><a name="p26809517369"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="75.72%" headers="mcps1.2.3.1.2 "><p id="p1168035153618"><a name="p1168035153618"></a><a name="p1168035153618"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row1681105193615"><td class="cellrowborder" valign="top" width="24.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p668115514364"><a name="p668115514364"></a><a name="p668115514364"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="75.72%" headers="mcps1.2.3.1.2 "><p id="p568111515366"><a name="p568111515366"></a><a name="p568111515366"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row126811153366"><td class="cellrowborder" valign="top" width="24.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p4681155123617"><a name="p4681155123617"></a><a name="p4681155123617"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="75.72%" headers="mcps1.2.3.1.2 "><p id="p126811459364"><a name="p126811459364"></a><a name="p126811459364"></a>The repository does not exist.</p>
</td>
</tr>
<tr id="row668175153613"><td class="cellrowborder" valign="top" width="24.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p18681155173614"><a name="p18681155173614"></a><a name="p18681155173614"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="75.72%" headers="mcps1.2.3.1.2 "><p id="p126818511363"><a name="p126818511363"></a><a name="p126818511363"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

