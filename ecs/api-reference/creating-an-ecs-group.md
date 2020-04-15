# Creating an ECS Group<a name="EN-US_TOPIC_0161097718"></a>

## Function<a name="en-us_topic_0057973153_section31887518"></a>

This API is used to create an ECS group.

## Constraints<a name="en-us_topic_0057973153_section32752180"></a>

Only anti-affinity groups are supported.

## URI<a name="en-us_topic_0057973153_section18552212"></a>

POST /v1/\{project\_id\}/cloudservers/os-server-groups

[Table 1](#en-us_topic_0057973153_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973153_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.10000000000001%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973153_section35680930"></a>

[Table 2](#en-us_topic_0057973153_table57386915)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973153_table57386915"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row22108653"><th class="cellrowborder" valign="top" width="19.46%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.5.1.2"><p id="p9576185035613"><a name="p9576185035613"></a><a name="p9576185035613"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.740000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.27%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row62192793"><td class="cellrowborder" valign="top" width="19.46%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p4451468"><a name="en-us_topic_0057973153_p4451468"></a><a name="en-us_topic_0057973153_p4451468"></a>server_group</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.5.1.2 "><p id="p11576165045612"><a name="p11576165045612"></a><a name="p11576165045612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.740000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p25024636"><a name="en-us_topic_0057973153_p25024636"></a><a name="en-us_topic_0057973153_p25024636"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47.27%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p38357105"><a name="en-us_topic_0057973153_p38357105"></a><a name="en-us_topic_0057973153_p38357105"></a>Specifies the ECS group information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **server\_group**  parameters

<a name="en-us_topic_0057973153_table19917766"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row59878934"><th class="cellrowborder" valign="top" width="19.518048195180484%" id="mcps1.2.5.1.1"><p id="p115851920182615"><a name="p115851920182615"></a><a name="p115851920182615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.578242175782425%" id="mcps1.2.5.1.2"><p id="p184120288567"><a name="p184120288567"></a><a name="p184120288567"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.178382161783823%" id="mcps1.2.5.1.3"><p id="p1560210202260"><a name="p1560210202260"></a><a name="p1560210202260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.72532746725327%" id="mcps1.2.5.1.4"><p id="p10602192016264"><a name="p10602192016264"></a><a name="p10602192016264"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row28765213"><td class="cellrowborder" valign="top" width="19.518048195180484%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p48280896"><a name="en-us_topic_0057973153_p48280896"></a><a name="en-us_topic_0057973153_p48280896"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.578242175782425%" headers="mcps1.2.5.1.2 "><p id="p13412228125618"><a name="p13412228125618"></a><a name="p13412228125618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.178382161783823%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p18438475"><a name="en-us_topic_0057973153_p18438475"></a><a name="en-us_topic_0057973153_p18438475"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.72532746725327%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p44665147"><a name="en-us_topic_0057973153_p44665147"></a><a name="en-us_topic_0057973153_p44665147"></a>Specifies the ECS group name. The value contains 1 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057973153_row66442010"><td class="cellrowborder" valign="top" width="19.518048195180484%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p13093750"><a name="en-us_topic_0057973153_p13093750"></a><a name="en-us_topic_0057973153_p13093750"></a>policies</p>
</td>
<td class="cellrowborder" valign="top" width="17.578242175782425%" headers="mcps1.2.5.1.2 "><p id="p4412122855620"><a name="p4412122855620"></a><a name="p4412122855620"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.178382161783823%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p53960863"><a name="en-us_topic_0057973153_p53960863"></a><a name="en-us_topic_0057973153_p53960863"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="46.72532746725327%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p173471532155519"><a name="en-us_topic_0057973153_p173471532155519"></a><a name="en-us_topic_0057973153_p173471532155519"></a>Specifies the policies associated with an ECS group. Options:</p>
<a name="en-us_topic_0057973153_ul1237514118527"></a><a name="en-us_topic_0057973153_ul1237514118527"></a><ul id="en-us_topic_0057973153_ul1237514118527"><li><strong id="b76011237203011"><a name="b76011237203011"></a><a name="b76011237203011"></a>anti-affinity</strong>: ECSs in this group must be deployed on different hosts.</li><li><strong id="b25134843012"><a name="b25134843012"></a><a name="b25134843012"></a>affinity</strong>: ECSs in this group must be deployed on the same host.</li><li><strong id="b433245743011"><a name="b433245743011"></a><a name="b433245743011"></a>soft-anti-affinity</strong>: ECSs in this group are deployed on different hosts if possible. If the ECSs cannot be deployed on different hosts, deploy them based on the actual condition for successful ECS creation.</li><li><strong id="b1613110294319"><a name="b1613110294319"></a><a name="b1613110294319"></a>soft-affinity</strong>: ECSs in this group are deployed on the same host if possible. If the ECSs cannot be deployed on the same host, deploy them based on the actual condition for successful ECS creation.<div class="note" id="en-us_topic_0057973153_note172209325315"><a name="en-us_topic_0057973153_note172209325315"></a><a name="en-us_topic_0057973153_note172209325315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057973153_p17221036536"><a name="en-us_topic_0057973153_p17221036536"></a><a name="en-us_topic_0057973153_p17221036536"></a>Only the anti-affinity policy is supported. If other policies are used, creating the ECS group will fail.</p>
</div></div>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973153_section52692922"></a>

[Table 4](#en-us_topic_0057973153_table55529076)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057973153_table55529076"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row53394154"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.4.1.1"><p id="p32821024102610"><a name="p32821024102610"></a><a name="p32821024102610"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.93189318931893%" id="mcps1.2.4.1.2"><p id="p202822024132618"><a name="p202822024132618"></a><a name="p202822024132618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.87618761876188%" id="mcps1.2.4.1.3"><p id="p10298192442612"><a name="p10298192442612"></a><a name="p10298192442612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row43894534"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p65796329"><a name="en-us_topic_0057973153_p65796329"></a><a name="en-us_topic_0057973153_p65796329"></a>server_group</p>
</td>
<td class="cellrowborder" valign="top" width="18.93189318931893%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p27902470"><a name="en-us_topic_0057973153_p27902470"></a><a name="en-us_topic_0057973153_p27902470"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="61.87618761876188%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p62235912"><a name="en-us_topic_0057973153_p62235912"></a><a name="en-us_topic_0057973153_p62235912"></a>Specifies the ECS group information.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **server\_group**  parameters

<a name="en-us_topic_0057973153_table7944126"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row9238701"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p177470268263"><a name="p177470268263"></a><a name="p177470268263"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.13%" id="mcps1.2.4.1.2"><p id="p167471026112613"><a name="p167471026112613"></a><a name="p167471026112613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.870000000000005%" id="mcps1.2.4.1.3"><p id="p67471426112617"><a name="p67471426112617"></a><a name="p67471426112617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row60872190"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p31700356"><a name="en-us_topic_0057973153_p31700356"></a><a name="en-us_topic_0057973153_p31700356"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p17592014"><a name="en-us_topic_0057973153_p17592014"></a><a name="en-us_topic_0057973153_p17592014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.870000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p61068496"><a name="en-us_topic_0057973153_p61068496"></a><a name="en-us_topic_0057973153_p61068496"></a>Specifies the ECS group UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973153_row12745552"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p25756821"><a name="en-us_topic_0057973153_p25756821"></a><a name="en-us_topic_0057973153_p25756821"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p5927779"><a name="en-us_topic_0057973153_p5927779"></a><a name="en-us_topic_0057973153_p5927779"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.870000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p36126903"><a name="en-us_topic_0057973153_p36126903"></a><a name="en-us_topic_0057973153_p36126903"></a>Specifies the ECS group name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973153_row56706675"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p29837953"><a name="en-us_topic_0057973153_p29837953"></a><a name="en-us_topic_0057973153_p29837953"></a>policies</p>
</td>
<td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p955132"><a name="en-us_topic_0057973153_p955132"></a><a name="en-us_topic_0057973153_p955132"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="61.870000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p18801115810585"><a name="en-us_topic_0057973153_p18801115810585"></a><a name="en-us_topic_0057973153_p18801115810585"></a>Specifies the policies associated with an ECS group. Options:</p>
<p id="en-us_topic_0057973153_p1380255810580"><a name="en-us_topic_0057973153_p1380255810580"></a><a name="en-us_topic_0057973153_p1380255810580"></a><strong id="b842352706161537"><a name="b842352706161537"></a><a name="b842352706161537"></a>anti-affinity</strong>: ECSs in this group must be deployed on different hosts.</p>
<p id="en-us_topic_0057973153_p138031158195815"><a name="en-us_topic_0057973153_p138031158195815"></a><a name="en-us_topic_0057973153_p138031158195815"></a><strong id="b842352706161548"><a name="b842352706161548"></a><a name="b842352706161548"></a>affinity</strong>: ECSs in this group must be deployed on the same host.</p>
<p id="en-us_topic_0057973153_p68041058195811"><a name="en-us_topic_0057973153_p68041058195811"></a><a name="en-us_topic_0057973153_p68041058195811"></a><strong id="b842352706161556"><a name="b842352706161556"></a><a name="b842352706161556"></a>soft-anti-affinity</strong>: ECSs in this group are deployed on different hosts if possible. If the ECSs cannot be deployed on different hosts, deploy them based on the actual condition for successful ECS creation.</p>
<p id="en-us_topic_0057973153_p680565816581"><a name="en-us_topic_0057973153_p680565816581"></a><a name="en-us_topic_0057973153_p680565816581"></a><strong id="b842352706161637"><a name="b842352706161637"></a><a name="b842352706161637"></a>soft-affinity</strong>: ECSs in this group are deployed on the same host if possible. If the ECSs cannot be deployed on the same host, deploy them based on the actual condition for successful ECS creation.</p>
</td>
</tr>
<tr id="en-us_topic_0057973153_row28154895"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p65953984"><a name="en-us_topic_0057973153_p65953984"></a><a name="en-us_topic_0057973153_p65953984"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p40672482"><a name="en-us_topic_0057973153_p40672482"></a><a name="en-us_topic_0057973153_p40672482"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="61.870000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p27313303"><a name="en-us_topic_0057973153_p27313303"></a><a name="en-us_topic_0057973153_p27313303"></a>Specifies the IDs of the ECSs in an ECS group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973153_row44493140"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_p47174611"><a name="en-us_topic_0057973153_p47174611"></a><a name="en-us_topic_0057973153_p47174611"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_p63047142"><a name="en-us_topic_0057973153_p63047142"></a><a name="en-us_topic_0057973153_p63047142"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="61.870000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973153_p60373738"><a name="en-us_topic_0057973153_p60373738"></a><a name="en-us_topic_0057973153_p60373738"></a>Specifies the ECS group metadata.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973153_section4474257"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/os-server-groups
```

```
{
    "server_group": {
        "name": "test",
        "policies": ["anti-affinity"]
    }
}
```

## Example Response<a name="section1090114347313"></a>

```
{
    "server_group": {
        "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
        "name": "test",
        "policies": [
            "anti-affinity"
        ],
        "members": [],
        "metadata": {}
    }
}
```

## Returned Values<a name="en-us_topic_0057973153_section17661930132114"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

