# Querying the List of Image Sharing Domains<a name="EN-US_TOPIC_0198655143"></a>

## Function<a name="section14905762191056"></a>

Query the list of image sharing domains.

## URI<a name="section10482810165331"></a>

GET /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access-domains

For details about parameters, see  [Table 1](#table11843162810214).

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="18.4%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.2.5.1.2"><p id="p3467112312474"><a name="p3467112312474"></a><a name="p3467112312474"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.74%" id="mcps1.2.5.1.3"><p id="p12469202344715"><a name="p12469202344715"></a><a name="p12469202344715"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.39%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.5.1.2 "><p id="p289883118229"><a name="p289883118229"></a><a name="p289883118229"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.74%" headers="mcps1.2.5.1.3 "><p id="p69291145134715"><a name="p69291145134715"></a><a name="p69291145134715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.39%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.5.1.2 "><p id="p1189833112228"><a name="p1189833112228"></a><a name="p1189833112228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.74%" headers="mcps1.2.5.1.3 "><p id="p1840713471471"><a name="p1840713471471"></a><a name="p1840713471471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50.39%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

N/A

## Response<a name="section1262713444552"></a>

**Response parameters**

**Table  2**  Response body parameter description

<a name="table45446245174724"></a>
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="20.477952204779523%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.28807119288071%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.233976602339766%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23391130131913"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p43401630141910"><a name="p43401630141910"></a><a name="p43401630141910"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p2041912381137"><a name="p2041912381137"></a><a name="p2041912381137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p20340730191918"><a name="p20340730191918"></a><a name="p20340730191918"></a>Organization.</p>
</td>
</tr>
<tr id="row697982791918"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p10980112717192"><a name="p10980112717192"></a><a name="p10980112717192"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p14191338171310"><a name="p14191338171310"></a><a name="p14191338171310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p14980192714197"><a name="p14980192714197"></a><a name="p14980192714197"></a>Image repository.</p>
</td>
</tr>
<tr id="row17668249354"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p4111525165410"><a name="p4111525165410"></a><a name="p4111525165410"></a>access_domain</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p7419103815132"><a name="p7419103815132"></a><a name="p7419103815132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p206025311878"><a name="p206025311878"></a><a name="p206025311878"></a>Name of the domain for image sharing.</p>
</td>
</tr>
<tr id="row176816213207"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p1568212212204"><a name="p1568212212204"></a><a name="p1568212212204"></a>permit</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p10419538141320"><a name="p10419538141320"></a><a name="p10419538141320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p1968202192013"><a name="p1968202192013"></a><a name="p1968202192013"></a>Permission.</p>
</td>
</tr>
<tr id="row411720412429"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p820345065419"><a name="p820345065419"></a><a name="p820345065419"></a>deadline</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p1441933861312"><a name="p1441933861312"></a><a name="p1441933861312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p33651491427"><a name="p33651491427"></a><a name="p33651491427"></a>End date.</p>
</td>
</tr>
<tr id="row19747155313423"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p9463481556"><a name="p9463481556"></a><a name="p9463481556"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p1241963813133"><a name="p1241963813133"></a><a name="p1241963813133"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p05141147434"><a name="p05141147434"></a><a name="p05141147434"></a>Description.</p>
</td>
</tr>
<tr id="row27392900174724"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p18944193920576"><a name="p18944193920576"></a><a name="p18944193920576"></a>creator_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p4392134851314"><a name="p4392134851314"></a><a name="p4392134851314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p368285415720"><a name="p368285415720"></a><a name="p368285415720"></a>Creator ID.</p>
</td>
</tr>
<tr id="row12917712114013"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p15603531879"><a name="p15603531879"></a><a name="p15603531879"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p1939244881314"><a name="p1939244881314"></a><a name="p1939244881314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p136038314714"><a name="p136038314714"></a><a name="p136038314714"></a>Name of the creator.</p>
</td>
</tr>
<tr id="row24091911193911"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p13603531378"><a name="p13603531378"></a><a name="p13603531378"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p239224819132"><a name="p239224819132"></a><a name="p239224819132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p760315313710"><a name="p760315313710"></a><a name="p760315313710"></a>Time when an image is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row10790853193918"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p14603631778"><a name="p14603631778"></a><a name="p14603631778"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p53927483135"><a name="p53927483135"></a><a name="p53927483135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p1360316317716"><a name="p1360316317716"></a><a name="p1360316317716"></a>Time when an image is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row1627112185506"><td class="cellrowborder" valign="top" width="20.477952204779523%" headers="mcps1.2.4.1.1 "><p id="p427119188502"><a name="p427119188502"></a><a name="p427119188502"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.28807119288071%" headers="mcps1.2.4.1.2 "><p id="p9392348171312"><a name="p9392348171312"></a><a name="p9392348171312"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.233976602339766%" headers="mcps1.2.4.1.3 "><p id="p11674184218407"><a name="p11674184218407"></a><a name="p11674184218407"></a>Status. <strong id="b12883187101410"><a name="b12883187101410"></a><a name="b12883187101410"></a>true</strong>: valid <strong id="b18988741412"><a name="b18988741412"></a><a name="b18988741412"></a>false</strong>: expired</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
[
    {
        "namespace": "otc",
        "repository": "paas",
        "access_domain": "swr",
        "permit": "read",
        "deadline": "2018-10-01T16:00:00.000Z",
        "description": "description",
        "creator_id": "fb3f175c1fd146ab8cdae3272be6107b",
        "creator_name": "otc",
        "created": "2017-04-08T14:12:23Z",
        "updated": "2017-04-13T21:01:11Z",
        "status": false
    }
]
```

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 3](#table1984564864716).

**Table  3**  Status code

<a name="table1984564864716"></a>
<table><thead align="left"><tr id="row1984554824718"><th class="cellrowborder" valign="top" width="21.8%" id="mcps1.2.3.1.1"><p id="p4846548124714"><a name="p4846548124714"></a><a name="p4846548124714"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="78.2%" id="mcps1.2.3.1.2"><p id="p984612486479"><a name="p984612486479"></a><a name="p984612486479"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1484619482477"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.3.1.1 "><p id="p88461948154710"><a name="p88461948154710"></a><a name="p88461948154710"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="78.2%" headers="mcps1.2.3.1.2 "><p id="p13846748154710"><a name="p13846748154710"></a><a name="p13846748154710"></a>The domain list of image sharing queried successfully.</p>
</td>
</tr>
<tr id="row98468489472"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.3.1.1 "><p id="p14846134812476"><a name="p14846134812476"></a><a name="p14846134812476"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="78.2%" headers="mcps1.2.3.1.2 "><p id="p08461448114716"><a name="p08461448114716"></a><a name="p08461448114716"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row141518196387"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.3.1.1 "><p id="p10415101913816"><a name="p10415101913816"></a><a name="p10415101913816"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="78.2%" headers="mcps1.2.3.1.2 "><p id="p16415121953810"><a name="p16415121953810"></a><a name="p16415121953810"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row16846248114719"><td class="cellrowborder" valign="top" width="21.8%" headers="mcps1.2.3.1.1 "><p id="p2846248184714"><a name="p2846248184714"></a><a name="p2846248184714"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="78.2%" headers="mcps1.2.3.1.2 "><p id="p5846154810474"><a name="p5846154810474"></a><a name="p5846154810474"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

