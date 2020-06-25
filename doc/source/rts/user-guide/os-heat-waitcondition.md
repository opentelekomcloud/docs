# OS::Heat::WaitCondition<a name="EN-US_TOPIC_0088407107"></a>

Resource for handling signals received by WaitConditionHandle.

Resource takes WaitConditionHandle and starts to create. Resource is in CREATE\_IN\_PROGRESS status until WaitConditionHandle doesnt receive sufficient number of successful signals \(this number can be specified with count property\) and successfully creates after that, or fails due to timeout.

## Required Properties<a name="section26857465918"></a>

<a name="table185461036171010"></a>
<table><thead align="left"><tr id="row2684645192311"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p354718362102"><a name="p354718362102"></a><a name="p354718362102"></a><strong id="b1374016536175"><a name="b1374016536175"></a><a name="b1374016536175"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p13547183614105"><a name="p13547183614105"></a><a name="p13547183614105"></a><strong id="b6741195311173"><a name="b6741195311173"></a><a name="b6741195311173"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row196843451231"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p3547163611017"><a name="p3547163611017"></a><a name="p3547163611017"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p39598216"><a name="p39598216"></a><a name="p39598216"></a>A reference to the wait condition handle used to signal this wait condition.</p>
<p id="p20839629"><a name="p20839629"></a><a name="p20839629"></a>String value expected.</p>
<p id="p53338937"><a name="p53338937"></a><a name="p53338937"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1668412459232"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1654715368103"><a name="p1654715368103"></a><a name="p1654715368103"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p18998541194812"><a name="p18998541194812"></a><a name="p18998541194812"></a>The number of seconds to wait for the correct number of signals to arrive.</p>
<p id="p28053194"><a name="p28053194"></a><a name="p28053194"></a>Number value expected.</p>
<p id="p51152156"><a name="p51152156"></a><a name="p51152156"></a>Updates cause replacement.</p>
<p id="p57716227"><a name="p57716227"></a><a name="p57716227"></a>The value must be in the range 1 to 43200, include 1 and 43200.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section14981554791"></a>

<a name="table10827458151219"></a>
<table><thead align="left"><tr id="row48181228142619"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p158286583120"><a name="p158286583120"></a><a name="p158286583120"></a><strong id="b20819122811263"><a name="b20819122811263"></a><a name="b20819122811263"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p3828058201216"><a name="p3828058201216"></a><a name="p3828058201216"></a><strong id="b20819102872612"><a name="b20819102872612"></a><a name="b20819102872612"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row78191828122615"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p158292584121"><a name="p158292584121"></a><a name="p158292584121"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p38882490"><a name="p38882490"></a><a name="p38882490"></a>The number of success signals that must be received before the stack creation process continues.</p>
<p id="p14398096"><a name="p14398096"></a><a name="p14398096"></a>Integer value expected.</p>
<p id="p62474000"><a name="p62474000"></a><a name="p62474000"></a>Can be updated without replacement.</p>
<p id="p25395093"><a name="p25395093"></a><a name="p25395093"></a>Defaults to "1".</p>
<p id="p27229246"><a name="p27229246"></a><a name="p27229246"></a>The value must be at least 1.</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section651173191012"></a>

<a name="table1488223317134"></a>
<table><thead align="left"><tr id="row1114217219275"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p12883183371311"><a name="p12883183371311"></a><a name="p12883183371311"></a><strong id="b16143824274"><a name="b16143824274"></a><a name="b16143824274"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p588418335134"><a name="p588418335134"></a><a name="p588418335134"></a><strong id="b1014418210273"><a name="b1014418210273"></a><a name="b1014418210273"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19144112102711"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1788516332137"><a name="p1788516332137"></a><a name="p1788516332137"></a>data</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p19886123321314"><a name="p19886123321314"></a><a name="p19886123321314"></a>JSON string containing data associated with wait condition signals sent to the handle.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section1477111314109"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::WaitCondition
    properties:
      count: Integer
      handle: String
      timeout: Number
```

