# Querying All API Versions<a name="cce_02_0349"></a>

## Function<a name="se2e066518e534a58a022d07edfbd4a3f"></a>

This API is used to query all available API versions.

## URI<a name="s9ba079db556c4be7998a917fb1004946"></a>

GET /

## Request<a name="sfa7f4cd949044a198e9f9a0518344e7f"></a>

N/A

## Response<a name="s2eb2c416e8d344619301671f0baffc10"></a>

**Response parameters:**

[Table 1](#table986610460219)  describes the response parameters.

**Table  1**  Response parameters

<a name="table986610460219"></a>
<table><thead align="left"><tr id="row3867846192120"><th class="cellrowborder" valign="top" width="20.392039203920394%" id="mcps1.2.4.1.1"><p id="p1086764618217"><a name="p1086764618217"></a><a name="p1086764618217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.23212321232123%" id="mcps1.2.4.1.2"><p id="p10867184611219"><a name="p10867184611219"></a><a name="p10867184611219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.37583758375837%" id="mcps1.2.4.1.3"><p id="p08676468210"><a name="p08676468210"></a><a name="p08676468210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20867124611213"><td class="cellrowborder" valign="top" width="20.392039203920394%" headers="mcps1.2.4.1.1 "><p id="p2086715463216"><a name="p2086715463216"></a><a name="p2086715463216"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.4.1.2 "><p id="p178672046192113"><a name="p178672046192113"></a><a name="p178672046192113"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.37583758375837%" headers="mcps1.2.4.1.3 "><p id="p129231114292"><a name="p129231114292"></a><a name="p129231114292"></a>API version list.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Data structure of the versions field

<a name="tcce801e285854dccb353b947a7438f7e"></a>
<table><thead align="left"><tr id="rcfece3d94f00439c886626d8c9fd8ead"><th class="cellrowborder" valign="top" width="17.77%" id="mcps1.2.5.1.1"><p id="ae4b83b624fe9400280500de14f852957"><a name="ae4b83b624fe9400280500de14f852957"></a><a name="ae4b83b624fe9400280500de14f852957"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.870000000000001%" id="mcps1.2.5.1.2"><p id="p187612148111"><a name="p187612148111"></a><a name="p187612148111"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.5%" id="mcps1.2.5.1.3"><p id="af9564978f187443a837b5dc2ba197568"><a name="af9564978f187443a837b5dc2ba197568"></a><a name="af9564978f187443a837b5dc2ba197568"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.86000000000001%" id="mcps1.2.5.1.4"><p id="aaed6ccd6f45949ab97d3cd07a9006af8"><a name="aaed6ccd6f45949ab97d3cd07a9006af8"></a><a name="aaed6ccd6f45949ab97d3cd07a9006af8"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rf35ded239f3047f4af05feecded6115c"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p109666131210"><a name="p109666131210"></a><a name="p109666131210"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p796351019124"><a name="p796351019124"></a><a name="p796351019124"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p2816319131213"><a name="p2816319131213"></a><a name="p2816319131213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p19449832141215"><a name="p19449832141215"></a><a name="p19449832141215"></a>API version ID, for example, v3.</p>
</td>
</tr>
<tr id="r3a6b7a4ae3424f3589f19eae5b6cf393"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p169676110128"><a name="p169676110128"></a><a name="p169676110128"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p14963410101214"><a name="p14963410101214"></a><a name="p14963410101214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p28173196126"><a name="p28173196126"></a><a name="p28173196126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p18449163213123"><a name="p18449163213123"></a><a name="p18449163213123"></a>API URL.</p>
</td>
</tr>
<tr id="row12671143117576"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p16882636175719"><a name="p16882636175719"></a><a name="p16882636175719"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p1882153685714"><a name="p1882153685714"></a><a name="p1882153685714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p4882103615573"><a name="p4882103615573"></a><a name="p4882103615573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p6166165673612"><a name="p6166165673612"></a><a name="p6166165673612"></a>API mini version number.</p>
<a name="ul1058019424376"></a><a name="ul1058019424376"></a><ul id="ul1058019424376"><li>If the API version has mini versions, the parameter value is the lowest version number supported.</li><li>If the API version does not have API mini versions, the parameter is left blank.</li></ul>
</td>
</tr>
<tr id="rc87772ef04774dcb860fcae5b8403556"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p79671614122"><a name="p79671614122"></a><a name="p79671614122"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p64668816565"><a name="p64668816565"></a><a name="p64668816565"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p0817101941213"><a name="p0817101941213"></a><a name="p0817101941213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p184493325123"><a name="p184493325123"></a><a name="p184493325123"></a>API version status.</p>
<a name="ul1483715326178"></a><a name="ul1483715326178"></a><ul id="ul1483715326178"><li><strong id="b58371432181719"><a name="b58371432181719"></a><a name="b58371432181719"></a>CURRENT</strong>: The version is a mainstream version.</li><li><strong id="b1283123612175"><a name="b1283123612175"></a><a name="b1283123612175"></a>SUPPORTED</strong>: The version is not the latest one but it is still in use.</li><li><strong id="b18838163231715"><a name="b18838163231715"></a><a name="b18838163231715"></a>DEPRECATED</strong>: The version is deprecated and will probably be deleted.</li></ul>
</td>
</tr>
<tr id="row06881052171110"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p1596751131216"><a name="p1596751131216"></a><a name="p1596751131216"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p296361014129"><a name="p296361014129"></a><a name="p296361014129"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p1381761913126"><a name="p1381761913126"></a><a name="p1381761913126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p4449103219127"><a name="p4449103219127"></a><a name="p4449103219127"></a>Version release time in UTC. For example, the parameter value for v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="row268912525118"><td class="cellrowborder" valign="top" width="17.77%" headers="mcps1.2.5.1.1 "><p id="p13786204713575"><a name="p13786204713575"></a><a name="p13786204713575"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="12.870000000000001%" headers="mcps1.2.5.1.2 "><p id="p107861547115719"><a name="p107861547115719"></a><a name="p107861547115719"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.3 "><p id="p16786104712578"><a name="p16786104712578"></a><a name="p16786104712578"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.86000000000001%" headers="mcps1.2.5.1.4 "><p id="p1323821834016"><a name="p1323821834016"></a><a name="p1323821834016"></a>API version number.</p>
<a name="ul18313527114018"></a><a name="ul18313527114018"></a><ul id="ul18313527114018"><li>If the API version has mini versions, the parameter value is the highest version number supported.</li><li>If the API version does not have API mini versions, the parameter is left blank.</li></ul>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
{
    "versions": [
        {
            "id": "v3",
            "links": [
                {
                    "href": "https://container.eu-de.otc.t-systems.com/v3",
                    "rel": "self"
                }
            ],
            "min_version": "",
            "status": "CURRENT",
            "updated": "2018-09-15T00:00:00Z",
            "version": ""
        }
    ]
}
```

## Status Code<a name="sf5b489c1f62d4d909a30f683dc319340"></a>

[Table 3](#t8935d48c19714740abd2e888a39be462)  describes the status code of the API.

**Table  3**  Status code

<a name="t8935d48c19714740abd2e888a39be462"></a>
<table><thead align="left"><tr id="re974d044247140b79c213fc577abe0ae"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="a9465a1e476c948e4b40095738594daf3"><a name="a9465a1e476c948e4b40095738594daf3"></a><a name="a9465a1e476c948e4b40095738594daf3"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="a88c1c2f27be844b7b79dad7e1a5b06f2"><a name="a88c1c2f27be844b7b79dad7e1a5b06f2"></a><a name="a88c1c2f27be844b7b79dad7e1a5b06f2"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rb535f7f0f62341f7b636e54ce399b342"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="ad1d3b647d2f746cc88b562f3eb1ff493"><a name="ad1d3b647d2f746cc88b562f3eb1ff493"></a><a name="ad1d3b647d2f746cc88b562f3eb1ff493"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="a78dc15895d744bb9affa7db6de6e02e5"><a name="a78dc15895d744bb9affa7db6de6e02e5"></a><a name="a78dc15895d744bb9affa7db6de6e02e5"></a>The query operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

