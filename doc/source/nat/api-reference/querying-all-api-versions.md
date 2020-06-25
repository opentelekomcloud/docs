# Querying All API Versions<a name="nat_api_0025"></a>

## Function<a name="section66578044"></a>

This API is used to query all API versions of NAT Gateway.

## API Format<a name="section42428029"></a>

GET/

## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

[Table 1](#table26246518152631)  lists response parameters.

**Table  1**  Response parameters

<a name="table26246518152631"></a>
<table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1143665616354"><a name="p1143665616354"></a><a name="p1143665616354"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p543845610355"><a name="p543845610355"></a><a name="p543845610355"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p11440156143517"><a name="p11440156143517"></a><a name="p11440156143517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="p244212561357"><a name="p244212561357"></a><a name="p244212561357"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56174697152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p4445556153516"><a name="p4445556153516"></a><a name="p4445556153516"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1044685612352"><a name="p1044685612352"></a><a name="p1044685612352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p444855610353"><a name="p444855610353"></a><a name="p444855610353"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p344911569354"><a name="p344911569354"></a><a name="p344911569354"></a>Specifies the list of all versions.</p>
</td>
</tr>
<tr id="row4615503152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p8452756123518"><a name="p8452756123518"></a><a name="p8452756123518"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1045395620354"><a name="p1045395620354"></a><a name="p1045395620354"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p3442103723411"><a name="p3442103723411"></a><a name="p3442103723411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p045585620357"><a name="p045585620357"></a><a name="p045585620357"></a>Specifies the version ID, for example, <strong id="b84235270619258"><a name="b84235270619258"></a><a name="b84235270619258"></a>v1</strong>.</p>
</td>
</tr>
<tr id="row9239644152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p9460175653518"><a name="p9460175653518"></a><a name="p9460175653518"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p44601856133514"><a name="p44601856133514"></a><a name="p44601856133514"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p14983184716501"><a name="p14983184716501"></a><a name="p14983184716501"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p746525619351"><a name="p746525619351"></a><a name="p746525619351"></a>Specifies the API URL.</p>
</td>
</tr>
<tr id="row19267144531214"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p16283354130"><a name="p16283354130"></a><a name="p16283354130"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p139117297139"><a name="p139117297139"></a><a name="p139117297139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p13242332181317"><a name="p13242332181317"></a><a name="p13242332181317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p2269104581219"><a name="p2269104581219"></a><a name="p2269104581219"></a>Specifies the reference address of the current API version.</p>
</td>
</tr>
<tr id="row113965641213"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p2139956101218"><a name="p2139956101218"></a><a name="p2139956101218"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1994102917139"><a name="p1994102917139"></a><a name="p1994102917139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p102571942143410"><a name="p102571942143410"></a><a name="p102571942143410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p513917563125"><a name="p513917563125"></a><a name="p513917563125"></a>Specifies the relationship between the current API version and the referenced address.</p>
</td>
</tr>
<tr id="row12929787152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p13468556113518"><a name="p13468556113518"></a><a name="p13468556113518"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p164706561359"><a name="p164706561359"></a><a name="p164706561359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1431114320349"><a name="p1431114320349"></a><a name="p1431114320349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p11474856173511"><a name="p11474856173511"></a><a name="p11474856173511"></a>Specifies the version. If APIs of this version support minor versions, set this parameter to the supported maximum minor version. If the minor versions are not supported, leave this parameter blank.</p>
</td>
</tr>
<tr id="row39341340152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p647516561358"><a name="p647516561358"></a><a name="p647516561358"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p447812565352"><a name="p447812565352"></a><a name="p447812565352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p18478184413411"><a name="p18478184413411"></a><a name="p18478184413411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p191992371020"><a name="p191992371020"></a><a name="p191992371020"></a>Specifies the version status.</p>
<p id="p104811756113517"><a name="p104811756113517"></a><a name="p104811756113517"></a>The value can be:</p>
<a name="ul195405275217"></a><a name="ul195405275217"></a><ul id="ul195405275217"><li><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates that the version is the primary version.</li><li><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</li><li><strong id="b84235270619220"><a name="b84235270619220"></a><a name="b84235270619220"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
</td>
</tr>
<tr id="row398200152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p7486145617358"><a name="p7486145617358"></a><a name="p7486145617358"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1487135693517"><a name="p1487135693517"></a><a name="p1487135693517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1648104515342"><a name="p1648104515342"></a><a name="p1648104515342"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p13841214736"><a name="p13841214736"></a><a name="p13841214736"></a>Specifies the time when the API version was released.</p>
<p id="p24932056163517"><a name="p24932056163517"></a><a name="p24932056163517"></a>The value must be UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="row61549520152631"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p2495115693510"><a name="p2495115693510"></a><a name="p2495115693510"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p14966566355"><a name="p14966566355"></a><a name="p14966566355"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p134991256203512"><a name="p134991256203512"></a><a name="p134991256203512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p205014565351"><a name="p205014565351"></a><a name="p205014565351"></a>If APIs of this version support minor versions, set this parameter to the supported minimum minor version. If not, leave this parameter blank.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section33573539387"></a>

-   Example response

```
{
  "versions": [
    {
      "id": "v2.0",
      "links": [
        {
          "href": "https://x.x.x.x/v2.0/",
          "rel": "self"
        }
      ],
      "min_version": "",
      "status": "CURRENT",
      "updated": "2018-09-30T00:00:00Z",
      "version": ""
    }
  ]
}
```

## Status Code<a name="section11326181114390"></a>

See  [Status Codes](status-codes.md).

