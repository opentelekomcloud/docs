# Updating the Brief Information on an Image Repository<a name="EN-US_TOPIC_0198655150"></a>

## Function<a name="section14905762191056"></a>

Update the brief information on an image repository, including its category, whether it is a public or private image, and its description.

## URI<a name="section10482810165331"></a>

PATCH /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}

For details about parameters, see  [Table 1](#table16521054337).

**Table  1**  Parameter description

<a name="table16521054337"></a>
<table><thead align="left"><tr id="row1752154439"><th class="cellrowborder" valign="top" width="17.18%" id="mcps1.2.5.1.1"><p id="p125216541336"><a name="p125216541336"></a><a name="p125216541336"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.02%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="29.970000000000002%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.83%" id="mcps1.2.5.1.4"><p id="p552195419316"><a name="p552195419316"></a><a name="p552195419316"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row452654236"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p66113272413"><a name="p66113272413"></a><a name="p66113272413"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.2 "><p id="p105058419438"><a name="p105058419438"></a><a name="p105058419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="29.970000000000002%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.83%" headers="mcps1.2.5.1.4 "><p id="p1204822152314"><a name="p1204822152314"></a><a name="p1204822152314"></a>Organization name.</p>
</td>
</tr>
<tr id="row11521554933"><td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.5.1.1 "><p id="p16614273417"><a name="p16614273417"></a><a name="p16614273417"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="19.02%" headers="mcps1.2.5.1.2 "><p id="p8875201913"><a name="p8875201913"></a><a name="p8875201913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="29.970000000000002%" headers="mcps1.2.5.1.3 "><p id="p557753134314"><a name="p557753134314"></a><a name="p557753134314"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.83%" headers="mcps1.2.5.1.4 "><p id="p9922191815234"><a name="p9922191815234"></a><a name="p9922191815234"></a>Image repository name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

**Request parameters**

**Table  2**  Request body parameter description

<a name="table11376833191926"></a>
<table><thead align="left"><tr id="row52628819191926"><th class="cellrowborder" valign="top" width="17.66%" id="mcps1.2.5.1.1"><p id="p35075914191926"><a name="p35075914191926"></a><a name="p35075914191926"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.1%" id="mcps1.2.5.1.2"><p id="p202771511163517"><a name="p202771511163517"></a><a name="p202771511163517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.759999999999998%" id="mcps1.2.5.1.3"><p id="p1627751113354"><a name="p1627751113354"></a><a name="p1627751113354"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.480000000000004%" id="mcps1.2.5.1.4"><p id="p8799102517581"><a name="p8799102517581"></a><a name="p8799102517581"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51617974191926"><td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.2.5.1.1 "><p id="p20306355191926"><a name="p20306355191926"></a><a name="p20306355191926"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.5.1.2 "><p id="p107093127914"><a name="p107093127914"></a><a name="p107093127914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.5.1.3 "><p id="p81732214106"><a name="p81732214106"></a><a name="p81732214106"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p14154153317228"><a name="p14154153317228"></a><a name="p14154153317228"></a>Repository category. The value can be <strong id="b781963411011"><a name="b781963411011"></a><a name="b781963411011"></a>app_server</strong>, <strong id="b38201334181019"><a name="b38201334181019"></a><a name="b38201334181019"></a>linux</strong>, <strong id="b11820163415103"><a name="b11820163415103"></a><a name="b11820163415103"></a>framework_app</strong>, <strong id="b1182113342102"><a name="b1182113342102"></a><a name="b1182113342102"></a>database</strong>, <strong id="b1782213419102"><a name="b1782213419102"></a><a name="b1782213419102"></a>lang</strong>, <strong id="b18221134151017"><a name="b18221134151017"></a><a name="b18221134151017"></a>other</strong>, <strong id="b88232034111016"><a name="b88232034111016"></a><a name="b88232034111016"></a>windows</strong>, <strong id="b13823193481012"><a name="b13823193481012"></a><a name="b13823193481012"></a>arm</strong>.</p>
</td>
</tr>
<tr id="row53129815191916"><td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.2.5.1.1 "><p id="p8547791191916"><a name="p8547791191916"></a><a name="p8547791191916"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.5.1.2 "><p id="p1670971216919"><a name="p1670971216919"></a><a name="p1670971216919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.5.1.3 "><p id="p174341428132912"><a name="p174341428132912"></a><a name="p174341428132912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p11800112545817"><a name="p11800112545817"></a><a name="p11800112545817"></a>Repository description.</p>
</td>
</tr>
<tr id="row3469276610418"><td class="cellrowborder" valign="top" width="17.66%" headers="mcps1.2.5.1.1 "><p id="p5865065310418"><a name="p5865065310418"></a><a name="p5865065310418"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.5.1.2 "><p id="p370910129916"><a name="p370910129916"></a><a name="p370910129916"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="19.759999999999998%" headers="mcps1.2.5.1.3 "><p id="p5904142612438"><a name="p5904142612438"></a><a name="p5904142612438"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p810148165818"><a name="p810148165818"></a><a name="p810148165818"></a>Whether the repository is public. When the value is <strong id="b44203392108"><a name="b44203392108"></a><a name="b44203392108"></a>true</strong>, it indicates the repository is public. When the value is <strong id="b1643031205010"><a name="b1643031205010"></a><a name="b1643031205010"></a>false</strong>, it indicates the repository is private.</p>
</td>
</tr>
</tbody>
</table>

**Request example**

```
{
    "category": "linux",
    "description": "this is a busybox repository",
    "is_public": true
}
```

## Response<a name="section46271297104114"></a>

N/A

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 3](#table69017321572).

**Table  3**  Status code

<a name="table69017321572"></a>
<table><thead align="left"><tr id="row13902732879"><th class="cellrowborder" valign="top" width="23.5%" id="mcps1.2.3.1.1"><p id="p189029321477"><a name="p189029321477"></a><a name="p189029321477"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="76.5%" id="mcps1.2.3.1.2"><p id="p8902532779"><a name="p8902532779"></a><a name="p8902532779"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1190213320715"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p179026321175"><a name="p179026321175"></a><a name="p179026321175"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p1890233210713"><a name="p1890233210713"></a><a name="p1890233210713"></a>The brief information about the image repository is successfully updated.</p>
</td>
</tr>
<tr id="row179029321470"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p490220329714"><a name="p490220329714"></a><a name="p490220329714"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p4902143218720"><a name="p4902143218720"></a><a name="p4902143218720"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row1990243213715"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p490263216714"><a name="p490263216714"></a><a name="p490263216714"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p690263216716"><a name="p690263216716"></a><a name="p690263216716"></a>The repository does not exist.</p>
</td>
</tr>
<tr id="row2090313216713"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p129030329719"><a name="p129030329719"></a><a name="p129030329719"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p090314328715"><a name="p090314328715"></a><a name="p090314328715"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

