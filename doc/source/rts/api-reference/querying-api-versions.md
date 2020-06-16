# Querying API Versions<a name="EN-US_TOPIC_0084581283"></a>

## Function<a name="en-us_topic_0057973117_section21216187"></a>

This API is used to query all available versions.

## URI<a name="en-us_topic_0057973117_section56727960"></a>

GET /

## Request Parameter<a name="en-us_topic_0057973117_section40789600"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973117_section31562082"></a>

<a name="table15493522192814"></a>
<table><thead align="left"><tr id="row54931122132812"><th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.1"><p id="p17493122142817"><a name="p17493122142817"></a><a name="p17493122142817"></a><strong id="b1478562243010"><a name="b1478562243010"></a><a name="b1478562243010"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.46835316468353%" id="mcps1.1.5.1.2"><p id="p1887419221879"><a name="p1887419221879"></a><a name="p1887419221879"></a><strong id="b24485441227"><a name="b24485441227"></a><a name="b24485441227"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.3"><p id="p16493922112813"><a name="p16493922112813"></a><a name="p16493922112813"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.23517648235177%" id="mcps1.1.5.1.4"><p id="p1549342213284"><a name="p1549342213284"></a><a name="p1549342213284"></a><strong id="b12999639183115"><a name="b12999639183115"></a><a name="b12999639183115"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row64931422142810"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="p76822021112914"><a name="p76822021112914"></a><a name="p76822021112914"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p148751022374"><a name="p148751022374"></a><a name="p148751022374"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="p9561131172615"><a name="p9561131172615"></a><a name="p9561131172615"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="p645919381634"><a name="p645919381634"></a><a name="p645919381634"></a>Specifies the API version list.</p>
<p id="p15682182116296"><a name="p15682182116296"></a><a name="p15682182116296"></a>Each object in the list provides API version information, such as the ID, status, and links.</p>
</td>
</tr>
</tbody>
</table>

**versions**  structure information

<a name="table882418307561"></a>
<table><thead align="left"><tr id="row118281430125619"><th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.1"><p id="p1420873193710"><a name="p1420873193710"></a><a name="p1420873193710"></a><strong id="b249043013338"><a name="b249043013338"></a><a name="b249043013338"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.46835316468353%" id="mcps1.1.5.1.2"><p id="p720973113716"><a name="p720973113716"></a><a name="p720973113716"></a><strong id="b13209191816314"><a name="b13209191816314"></a><a name="b13209191816314"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.648235176482352%" id="mcps1.1.5.1.3"><p id="p1520953116376"><a name="p1520953116376"></a><a name="p1520953116376"></a><strong id="b157070521337"><a name="b157070521337"></a><a name="b157070521337"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.23517648235177%" id="mcps1.1.5.1.4"><p id="p9212231153715"><a name="p9212231153715"></a><a name="p9212231153715"></a><strong id="b916516550339"><a name="b916516550339"></a><a name="b916516550339"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4838430145613"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="p118381330105611"><a name="p118381330105611"></a><a name="p118381330105611"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p162781213816"><a name="p162781213816"></a><a name="p162781213816"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="p3841113085610"><a name="p3841113085610"></a><a name="p3841113085610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="p984316306564"><a name="p984316306564"></a><a name="p984316306564"></a>Specifies the API version.</p>
</td>
</tr>
<tr id="row19843183045616"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="p28455302565"><a name="p28455302565"></a><a name="p28455302565"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p3278111688"><a name="p3278111688"></a><a name="p3278111688"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="p10847153075618"><a name="p10847153075618"></a><a name="p10847153075618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="p9850133035618"><a name="p9850133035618"></a><a name="p9850133035618"></a>Specifies the API version status. Available values are as follows:</p>
<a name="ul385183011569"></a><a name="ul385183011569"></a><ul id="ul385183011569"><li><strong id="b842352706235943"><a name="b842352706235943"></a><a name="b842352706235943"></a>CURRENT</strong>: preferred API version</li><li><strong id="b1579833714369"><a name="b1579833714369"></a><a name="b1579833714369"></a>SUPPORTED</strong>: an earlier API version, which is still in use</li><li><strong id="b76883013373"><a name="b76883013373"></a><a name="b76883013373"></a>DEPRECATED</strong>: an obsolete API version to be deleted</li></ul>
</td>
</tr>
<tr id="row17854183055617"><td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.1 "><p id="p985413304568"><a name="p985413304568"></a><a name="p985413304568"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.46835316468353%" headers="mcps1.1.5.1.2 "><p id="p1027801680"><a name="p1027801680"></a><a name="p1027801680"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.648235176482352%" headers="mcps1.1.5.1.3 "><p id="p10854103045620"><a name="p10854103045620"></a><a name="p10854103045620"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="48.23517648235177%" headers="mcps1.1.5.1.4 "><p id="p10399164310311"><a name="p10399164310311"></a><a name="p10399164310311"></a>Specifies the API URL list.</p>
<p id="p158561830155616"><a name="p158561830155616"></a><a name="p158561830155616"></a>Each URL is a JSON object with one <strong id="b14306447115011"><a name="b14306447115011"></a><a name="b14306447115011"></a>href</strong> keyword for identifying the URL and one <strong id="b189711551175018"><a name="b189711551175018"></a><a name="b189711551175018"></a>rel</strong> keyword indicating the relationship between the API version and the involved stack.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973117_section15623289"></a>

None

## Response Example<a name="en-us_topic_0057973117_section6391877"></a>

```
{
    "versions": [
        {
            "status": "CURRENT",
            "id": "v1.0",
            "links": [
                {
                    "href": "http://x.x.x.x:8774/v1/",
                    "rel": "self"
                }
            ]
        }
    ]
}
```

## Return Code<a name="en-us_topic_0057973117_section57526895"></a>

The following code will be returned if the system is operating normally.

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.1.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a>Return Code</p>
</th>
<th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0057973117_p8637307194057"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0057973117_p28533244194057"></a>Multiple choices</p>
</td>
<td class="cellrowborder" valign="top" width="54.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0057973117_p29491459194057"></a>The requested resource has multiple available responses.</p>
</td>
</tr>
</tbody>
</table>

