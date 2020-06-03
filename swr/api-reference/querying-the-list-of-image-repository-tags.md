# Querying the List of Image Repository Tags<a name="EN-US_TOPIC_0198655161"></a>

## Function<a name="section14905762191056"></a>

Query all image tags of an image repository.

## URI<a name="section10482810165331"></a>

GET /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/tags

For details about parameters, see  [Table 1](#table11843162810214).

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="18.43%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.970000000000002%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="24.3%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="38.3%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.2 "><p id="p1974818208111"><a name="p1974818208111"></a><a name="p1974818208111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.3%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.3%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.2 "><p id="p1774832016116"><a name="p1774832016116"></a><a name="p1774832016116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.3%" headers="mcps1.2.5.1.3 "><p id="p15466162817454"><a name="p15466162817454"></a><a name="p15466162817454"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.3%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name</p>
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
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="19.678032196780322%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.137886211378863%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.18408159184082%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23391130131913"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p43401630141910"><a name="p43401630141910"></a><a name="p43401630141910"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p1224112114332"><a name="p1224112114332"></a><a name="p1224112114332"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p20340730191918"><a name="p20340730191918"></a><a name="p20340730191918"></a>ID.</p>
</td>
</tr>
<tr id="row697982791918"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p10980112717192"><a name="p10980112717192"></a><a name="p10980112717192"></a>repo_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p496822951117"><a name="p496822951117"></a><a name="p496822951117"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p14980192714197"><a name="p14980192714197"></a><a name="p14980192714197"></a>Repository ID.</p>
</td>
</tr>
<tr id="row17668249354"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p3602231570"><a name="p3602231570"></a><a name="p3602231570"></a>Tag</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p1296910299118"><a name="p1296910299118"></a><a name="p1296910299118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p206025311878"><a name="p206025311878"></a><a name="p206025311878"></a>Image tag name.</p>
</td>
</tr>
<tr id="row176816213207"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p1568212212204"><a name="p1568212212204"></a><a name="p1568212212204"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p196912911117"><a name="p196912911117"></a><a name="p196912911117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p1968202192013"><a name="p1968202192013"></a><a name="p1968202192013"></a>Image ID.</p>
</td>
</tr>
<tr id="row2590104211156"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p1592204251517"><a name="p1592204251517"></a><a name="p1592204251517"></a>manifest</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p196992913116"><a name="p196992913116"></a><a name="p196992913116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p145923427155"><a name="p145923427155"></a><a name="p145923427155"></a>Image manifest.</p>
</td>
</tr>
<tr id="row411720412429"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p8361449104214"><a name="p8361449104214"></a><a name="p8361449104214"></a>digest</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p29696292119"><a name="p29696292119"></a><a name="p29696292119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p33651491427"><a name="p33651491427"></a><a name="p33651491427"></a>SHA value of an image.</p>
</td>
</tr>
<tr id="row19747155313423"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p55111044437"><a name="p55111044437"></a><a name="p55111044437"></a>schema</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p197451837201119"><a name="p197451837201119"></a><a name="p197451837201119"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p05141147434"><a name="p05141147434"></a><a name="p05141147434"></a>Docker protocol version. The value can be <strong id="b740155745519"><a name="b740155745519"></a><a name="b740155745519"></a>1</strong> or <strong id="b341175713559"><a name="b341175713559"></a><a name="b341175713559"></a>2</strong>.</p>
</td>
</tr>
<tr id="row27392900174724"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p66029311173"><a name="p66029311173"></a><a name="p66029311173"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p67459370116"><a name="p67459370116"></a><a name="p67459370116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p9603163112712"><a name="p9603163112712"></a><a name="p9603163112712"></a>Image address for docker pull.</p>
</td>
</tr>
<tr id="row207081451715"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p1701714191712"><a name="p1701714191712"></a><a name="p1701714191712"></a>internal_path</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p8745113717113"><a name="p8745113717113"></a><a name="p8745113717113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p07051481718"><a name="p07051481718"></a><a name="p07051481718"></a>Intra-cluster image address for docker pull.</p>
</td>
</tr>
<tr id="row12917712114013"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p15603531879"><a name="p15603531879"></a><a name="p15603531879"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p15745103701117"><a name="p15745103701117"></a><a name="p15745103701117"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p136038314714"><a name="p136038314714"></a><a name="p136038314714"></a>Image size. The value ranges from 0 to 9,223,372,036,854,775,807.</p>
</td>
</tr>
<tr id="row6189161112289"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p519041132810"><a name="p519041132810"></a><a name="p519041132810"></a>is_trusted</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p1374543771117"><a name="p1374543771117"></a><a name="p1374543771117"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p13191811182818"><a name="p13191811182818"></a><a name="p13191811182818"></a>By default, the value is set to <strong id="b17706183718379"><a name="b17706183718379"></a><a name="b17706183718379"></a>false</strong>.</p>
</td>
</tr>
<tr id="row24091911193911"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p13603531378"><a name="p13603531378"></a><a name="p13603531378"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p1350184631112"><a name="p1350184631112"></a><a name="p1350184631112"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p760315313710"><a name="p760315313710"></a><a name="p760315313710"></a>Time when an image is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row10790853193918"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p14603631778"><a name="p14603631778"></a><a name="p14603631778"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p16351164611111"><a name="p16351164611111"></a><a name="p16351164611111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p1360316317716"><a name="p1360316317716"></a><a name="p1360316317716"></a>Time when an image is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row1627112185506"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p427119188502"><a name="p427119188502"></a><a name="p427119188502"></a>deleted</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p2035134610115"><a name="p2035134610115"></a><a name="p2035134610115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p1327116186505"><a name="p1327116186505"></a><a name="p1327116186505"></a>Time when an image was deleted.</p>
</td>
</tr>
<tr id="row3268162949"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p152692021741"><a name="p152692021741"></a><a name="p152692021741"></a>scanned</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p16269524413"><a name="p16269524413"></a><a name="p16269524413"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p327016219413"><a name="p327016219413"></a><a name="p327016219413"></a>This parameter is not supported currently.</p>
</td>
</tr>
<tr id="row9791454416"><td class="cellrowborder" valign="top" width="19.678032196780322%" headers="mcps1.2.4.1.1 "><p id="p380185949"><a name="p380185949"></a><a name="p380185949"></a>tag_type</p>
</td>
<td class="cellrowborder" valign="top" width="21.137886211378863%" headers="mcps1.2.4.1.2 "><p id="p280355411"><a name="p280355411"></a><a name="p280355411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59.18408159184082%" headers="mcps1.2.4.1.3 "><p id="p1280751411"><a name="p1280751411"></a><a name="p1280751411"></a>This parameter is not supported currently.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
[
    {
        "id": 0,
        "repo_id": 0,
        "Tag": "latest",
        "image_id": "741f24a795d6d93d7c6edd11780d63c13e16c39615dd9d223378a57a836f2ee6",
        "manifest": "{\"schemaVersion\":2,\"mediaType\":\"application/vnd.docker.distribution.manifest.v2+json\",\"config\":{\"mediaType\":\"application/vnd.docker.container.image.v1+json\",\"size\":1862,\"digest\":\"sha256:741f24a795d6d93d7c6edd11780d63c13e16c39615dd9d223378a57a836f2ee6\"},\"layers\":[{\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":1292800,\"digest\":\"sha256:8ac8bfaff55af948c796026ee867448c5b5b5d9dd3549f4006d9759b25d4a893\"},{\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":10240,\"digest\":\"sha256:77ddbf3a9fe11e81761a0f9df43a28e3e6f29bbb53c0c8cf71cd7efa69729aed\"}]}",
        "digest": "sha256:57b605845a6367c34bfb6ea6477f16852f59aa1861a2b51d10ab77ae0a1dc9c3",
        "schema": 2,
        "path": "192.158.24.86/namespace/busybox:latest",
        "internal_path": "10.125.0.198:20202/namespace/busybox:latest",
        "size": 1304902,
        "is_trusted": false,
        "created": "2018-07-06T06:18:55Z",
        "updated": "2018-07-06T06:18:55Z",
        "deleted": null,
        "scanned": false,
        "tag_type": 0
    }
]
```

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 3](#table1984564864716).

**Table  3**  Status code

<a name="table1984564864716"></a>
<table><thead align="left"><tr id="row1984554824718"><th class="cellrowborder" valign="top" width="22.06%" id="mcps1.2.3.1.1"><p id="p4846548124714"><a name="p4846548124714"></a><a name="p4846548124714"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="77.94%" id="mcps1.2.3.1.2"><p id="p984612486479"><a name="p984612486479"></a><a name="p984612486479"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1484619482477"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.3.1.1 "><p id="p88461948154710"><a name="p88461948154710"></a><a name="p88461948154710"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="77.94%" headers="mcps1.2.3.1.2 "><p id="p13846748154710"><a name="p13846748154710"></a><a name="p13846748154710"></a>All tags in the image repository are successfully queried.</p>
</td>
</tr>
<tr id="row98468489472"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.3.1.1 "><p id="p14846134812476"><a name="p14846134812476"></a><a name="p14846134812476"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="77.94%" headers="mcps1.2.3.1.2 "><p id="p08461448114716"><a name="p08461448114716"></a><a name="p08461448114716"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row9846114818471"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.3.1.1 "><p id="p188468486471"><a name="p188468486471"></a><a name="p188468486471"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="77.94%" headers="mcps1.2.3.1.2 "><p id="p11846134819473"><a name="p11846134819473"></a><a name="p11846134819473"></a>The repository does not exist.</p>
</td>
</tr>
<tr id="row16846248114719"><td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.2.3.1.1 "><p id="p2846248184714"><a name="p2846248184714"></a><a name="p2846248184714"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="77.94%" headers="mcps1.2.3.1.2 "><p id="p5846154810474"><a name="p5846154810474"></a><a name="p5846154810474"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

