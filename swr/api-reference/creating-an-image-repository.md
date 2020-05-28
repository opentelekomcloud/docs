# Creating an Image Repository<a name="EN-US_TOPIC_0198655138"></a>

## Function<a name="section14905762191056"></a>

Create an image repository in an organization. An image repository holds multiple image tags of the same image.

## URI<a name="section10482810165331"></a>

POST /v2/manage/namespaces/\{_namespace_\}/repos

For details about parameters, see  [Table 1](#table155961192716).

**Table  1**  Parameter description

<a name="table155961192716"></a>
<table><thead align="left"><tr id="row66016114276"><th class="cellrowborder" valign="top" width="18.828117188281173%" id="mcps1.2.5.1.1"><p id="p1969191112717"><a name="p1969191112717"></a><a name="p1969191112717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.868413158684133%" id="mcps1.2.5.1.2"><p id="p14796031194218"><a name="p14796031194218"></a><a name="p14796031194218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.96800319968003%" id="mcps1.2.5.1.3"><p id="p1311119571031"><a name="p1311119571031"></a><a name="p1311119571031"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.33546645335467%" id="mcps1.2.5.1.4"><p id="p20214193316271"><a name="p20214193316271"></a><a name="p20214193316271"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12601115273"><td class="cellrowborder" valign="top" width="18.828117188281173%" headers="mcps1.2.5.1.1 "><p id="p8692191132719"><a name="p8692191132719"></a><a name="p8692191132719"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="15.868413158684133%" headers="mcps1.2.5.1.2 "><p id="p48011931194218"><a name="p48011931194218"></a><a name="p48011931194218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.96800319968003%" headers="mcps1.2.5.1.3 "><p id="p1611814571310"><a name="p1611814571310"></a><a name="p1611814571310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.33546645335467%" headers="mcps1.2.5.1.4 "><p id="p76671718914"><a name="p76671718914"></a><a name="p76671718914"></a>Enter 1 to 64 characters, starting with a lowercase letter and ending with a lowercase letter or digit. Only lowercase letters, digits, periods (.), underscores (_), and hyphens (-) are allowed. Periods, underscores, and hyphens cannot be placed next to each other. A maximum of two consecutive underscores are allowed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

**Request parameters**

**Table  2**  Request body parameter description

<a name="table11376833191926"></a>
<table><thead align="left"><tr id="row52628819191926"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.5.1.1"><p id="p35075914191926"><a name="p35075914191926"></a><a name="p35075914191926"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.38%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.2.5.1.4"><p id="p8799102517581"><a name="p8799102517581"></a><a name="p8799102517581"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62468224193942"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.5.1.1 "><p id="p26761358193942"><a name="p26761358193942"></a><a name="p26761358193942"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.5.1.2 "><p id="p105058419438"><a name="p105058419438"></a><a name="p105058419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p5626157663"><a name="p5626157663"></a><a name="p5626157663"></a>Image repository name. Enter 1 to 128 characters, starting and ending with a lowercase letter or digit. Only lowercase letters, digits, periods (.), underscores (_), and hyphens (-) are allowed. Periods, underscores, and hyphens cannot be placed next to each other. A maximum of two consecutive underscores are allowed.</p>
</td>
</tr>
<tr id="row51617974191926"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.5.1.1 "><p id="p20306355191926"><a name="p20306355191926"></a><a name="p20306355191926"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.5.1.2 "><p id="p2351162432"><a name="p2351162432"></a><a name="p2351162432"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.5.1.3 "><p id="p81732214106"><a name="p81732214106"></a><a name="p81732214106"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p14154153317228"><a name="p14154153317228"></a><a name="p14154153317228"></a>Repository category. The value can be <strong id="b118675141534"><a name="b118675141534"></a><a name="b118675141534"></a>app_server</strong>, <strong id="b13400131716534"><a name="b13400131716534"></a><a name="b13400131716534"></a>linux</strong>, <strong id="b107662025314"><a name="b107662025314"></a><a name="b107662025314"></a>framework_app</strong>, <strong id="b33461322195312"><a name="b33461322195312"></a><a name="b33461322195312"></a>database</strong>, <strong id="b67021924105318"><a name="b67021924105318"></a><a name="b67021924105318"></a>lang</strong>, <strong id="b119191926145315"><a name="b119191926145315"></a><a name="b119191926145315"></a>other</strong>, <strong id="b1043815291536"><a name="b1043815291536"></a><a name="b1043815291536"></a>windows</strong>, <strong id="b43503313536"><a name="b43503313536"></a><a name="b43503313536"></a>arm</strong>.</p>
</td>
</tr>
<tr id="row53129815191916"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.5.1.1 "><p id="p8547791191916"><a name="p8547791191916"></a><a name="p8547791191916"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.5.1.2 "><p id="p1989631624318"><a name="p1989631624318"></a><a name="p1989631624318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.5.1.3 "><p id="p174341428132912"><a name="p174341428132912"></a><a name="p174341428132912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p11800112545817"><a name="p11800112545817"></a><a name="p11800112545817"></a>Repository description.</p>
</td>
</tr>
<tr id="row3469276610418"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.5.1.1 "><p id="p5865065310418"><a name="p5865065310418"></a><a name="p5865065310418"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.5.1.2 "><p id="p471339810418"><a name="p471339810418"></a><a name="p471339810418"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="19.38%" headers="mcps1.2.5.1.3 "><p id="p5904142612438"><a name="p5904142612438"></a><a name="p5904142612438"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p810148165818"><a name="p810148165818"></a><a name="p810148165818"></a>Whether the repository is public. When the value is <strong id="b15625143419591"><a name="b15625143419591"></a><a name="b15625143419591"></a>true</strong>, it indicates the repository is public. When the value is <strong id="b163811859165710"><a name="b163811859165710"></a><a name="b163811859165710"></a>false</strong>, it indicates the repository is private.</p>
</td>
</tr>
</tbody>
</table>

**Request example**

```
{
    "repository": "busybox",
    "category": "linux",
    "description": "this is a busybox repository",
    "is_public": true
}
```

## Response<a name="section46271297104114"></a>

N/A

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 3](#table1537514248301).

**Table  3**  Status code

<a name="table1537514248301"></a>
<table><thead align="left"><tr id="row183751324163014"><th class="cellrowborder" valign="top" width="20.64%" id="mcps1.2.3.1.1"><p id="p1437512453016"><a name="p1437512453016"></a><a name="p1437512453016"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="79.36%" id="mcps1.2.3.1.2"><p id="p23751724153018"><a name="p23751724153018"></a><a name="p23751724153018"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row837511241306"><td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.3.1.1 "><p id="p53752024103012"><a name="p53752024103012"></a><a name="p53752024103012"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="79.36%" headers="mcps1.2.3.1.2 "><p id="p5375162413308"><a name="p5375162413308"></a><a name="p5375162413308"></a>Created successfully.</p>
</td>
</tr>
<tr id="row13375142417305"><td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.3.1.1 "><p id="p11375724133011"><a name="p11375724133011"></a><a name="p11375724133011"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="79.36%" headers="mcps1.2.3.1.2 "><p id="p13761324103020"><a name="p13761324103020"></a><a name="p13761324103020"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row615125910308"><td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.3.1.1 "><p id="p2015111596307"><a name="p2015111596307"></a><a name="p2015111596307"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="79.36%" headers="mcps1.2.3.1.2 "><p id="p1215115593304"><a name="p1215115593304"></a><a name="p1215115593304"></a>The repository already exists.</p>
</td>
</tr>
<tr id="row837612433016"><td class="cellrowborder" valign="top" width="20.64%" headers="mcps1.2.3.1.1 "><p id="p937619249301"><a name="p937619249301"></a><a name="p937619249301"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="79.36%" headers="mcps1.2.3.1.2 "><p id="p33761245309"><a name="p33761245309"></a><a name="p33761245309"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

