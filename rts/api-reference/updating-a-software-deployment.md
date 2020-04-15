# Updating a Software Deployment<a name="EN-US_TOPIC_0085277561"></a>

## Function<a name="en-us_topic_0085081138_section5314816"></a>

This API is used to update a software deployment.

## URI<a name="en-us_topic_0085081138_section47833347"></a>

PUT /v1/\{project\_id\}/software\_deployments/\{deployment\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b5150351141219"><a name="b5150351141219"></a><a name="b5150351141219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b1825716521129"><a name="b1825716521129"></a><a name="b1825716521129"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b111820534120"><a name="b111820534120"></a><a name="b111820534120"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b138185491217"><a name="b138185491217"></a><a name="b138185491217"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1874564042214"><a name="p1874564042214"></a><a name="p1874564042214"></a>deployment_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p17747124020225"><a name="p17747124020225"></a><a name="p17747124020225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p157491540122216"><a name="p157491540122216"></a><a name="p157491540122216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p197517404224"><a name="p197517404224"></a><a name="p197517404224"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081138_section27846943"></a>

<a name="en-us_topic_0085081138_table2851385316"></a>
<table><thead align="left"><tr id="en-us_topic_0085081138_row711513185311"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b18547192981511"><a name="b18547192981511"></a><a name="b18547192981511"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b564933121515"><a name="b564933121515"></a><a name="b564933121515"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b12378332157"><a name="b12378332157"></a><a name="b12378332157"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b17195143418150"><a name="b17195143418150"></a><a name="b17195143418150"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b1610993510159"><a name="b1610993510159"></a><a name="b1610993510159"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081138_row416813155310"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p12188103812162"><a name="en-us_topic_0085081138_p12188103812162"></a><a name="en-us_topic_0085081138_p12188103812162"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1298110236165"><a name="p1298110236165"></a><a name="p1298110236165"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p1318823810163"><a name="en-us_topic_0085081138_p1318823810163"></a><a name="en-us_topic_0085081138_p1318823810163"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p11188103819161"><a name="en-us_topic_0085081138_p11188103819161"></a><a name="en-us_topic_0085081138_p11188103819161"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p6188123831616"><a name="en-us_topic_0085081138_p6188123831616"></a><a name="en-us_topic_0085081138_p6188123831616"></a>Specifies the stack action that triggers this software deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row116363254168"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p9188173810163"><a name="en-us_topic_0085081138_p9188173810163"></a><a name="en-us_topic_0085081138_p9188173810163"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p2981102312167"><a name="p2981102312167"></a><a name="p2981102312167"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p31884387162"><a name="en-us_topic_0085081138_p31884387162"></a><a name="en-us_topic_0085081138_p31884387162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p218817388167"><a name="en-us_topic_0085081138_p218817388167"></a><a name="en-us_topic_0085081138_p218817388167"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p1188153812166"><a name="en-us_topic_0085081138_p1188153812166"></a><a name="en-us_topic_0085081138_p1188153812166"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row1994022918164"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p4188138171611"><a name="en-us_topic_0085081138_p4188138171611"></a><a name="en-us_topic_0085081138_p4188138171611"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p18981132381612"><a name="p18981132381612"></a><a name="p18981132381612"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p15188123811161"><a name="en-us_topic_0085081138_p15188123811161"></a><a name="en-us_topic_0085081138_p15188123811161"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p9188203819162"><a name="en-us_topic_0085081138_p9188203819162"></a><a name="en-us_topic_0085081138_p9188203819162"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p14188538191618"><a name="en-us_topic_0085081138_p14188538191618"></a><a name="en-us_topic_0085081138_p14188538191618"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row1094112961619"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p81881138111613"><a name="en-us_topic_0085081138_p81881138111613"></a><a name="en-us_topic_0085081138_p81881138111613"></a>output_values</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p9981202311168"><a name="p9981202311168"></a><a name="p9981202311168"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p1318813891615"><a name="en-us_topic_0085081138_p1318813891615"></a><a name="en-us_topic_0085081138_p1318813891615"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p8188103871615"><a name="en-us_topic_0085081138_p8188103871615"></a><a name="en-us_topic_0085081138_p8188103871615"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p918816389164"><a name="en-us_topic_0085081138_p918816389164"></a><a name="en-us_topic_0085081138_p918816389164"></a>Specifies output data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row1893103510165"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p1018815386167"><a name="en-us_topic_0085081138_p1018815386167"></a><a name="en-us_topic_0085081138_p1018815386167"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p19811223121613"><a name="p19811223121613"></a><a name="p19811223121613"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p9188938131613"><a name="en-us_topic_0085081138_p9188938131613"></a><a name="en-us_topic_0085081138_p9188938131613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p618873871614"><a name="en-us_topic_0085081138_p618873871614"></a><a name="en-us_topic_0085081138_p618873871614"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p71881638181614"><a name="en-us_topic_0085081138_p71881638181614"></a><a name="en-us_topic_0085081138_p71881638181614"></a>Specifies the status of software deployments. Valid values include <strong id="b560815901613"><a name="b560815901613"></a><a name="b560815901613"></a>COMPLETE</strong>, <strong id="b186085910168"><a name="b186085910168"></a><a name="b186085910168"></a>IN_PROGRESS</strong>, and <strong id="b3609139171614"><a name="b3609139171614"></a><a name="b3609139171614"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row7931183591614"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0085081138_p191881438121617"><a name="en-us_topic_0085081138_p191881438121617"></a><a name="en-us_topic_0085081138_p191881438121617"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p6981023141615"><a name="p6981023141615"></a><a name="p6981023141615"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0085081138_p018813387168"><a name="en-us_topic_0085081138_p018813387168"></a><a name="en-us_topic_0085081138_p018813387168"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0085081138_p1118833819168"><a name="en-us_topic_0085081138_p1118833819168"></a><a name="en-us_topic_0085081138_p1118833819168"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0085081138_p171882389164"><a name="en-us_topic_0085081138_p171882389164"></a><a name="en-us_topic_0085081138_p171882389164"></a>Specifies the cause of the software deployment status.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0085081138_section49295902"></a>

<a name="table1432514514366"></a>
<table><thead align="left"><tr id="row20325345193613"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p160141785915"><a name="p160141785915"></a><a name="p160141785915"></a><strong id="b12974333175"><a name="b12974333175"></a><a name="b12974333175"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p8605161715915"><a name="p8605161715915"></a><a name="p8605161715915"></a><strong id="b553815441179"><a name="b553815441179"></a><a name="b553815441179"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.3"><p id="p1360731719594"><a name="p1360731719594"></a><a name="p1360731719594"></a><strong id="b181104611172"><a name="b181104611172"></a><a name="b181104611172"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p3612161795912"><a name="p3612161795912"></a><a name="p3612161795912"></a><strong id="b236941512184"><a name="b236941512184"></a><a name="b236941512184"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12325745203612"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="p4325345133618"><a name="p4325345133618"></a><a name="p4325345133618"></a>software_deployment</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p38245401910"><a name="p38245401910"></a><a name="p38245401910"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="p1325713190378"><a name="p1325713190378"></a><a name="p1325713190378"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p82611619123714"><a name="p82611619123714"></a><a name="p82611619123714"></a>Specifies the software deployment resource object.</p>
</td>
</tr>
</tbody>
</table>

**software\_deployment**  structure information

<a name="en-us_topic_0085081138_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081138_row14014710"><th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.1"><p id="p14318132117594"><a name="p14318132117594"></a><a name="p14318132117594"></a><strong id="b17157105191812"><a name="b17157105191812"></a><a name="b17157105191812"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p73201021125910"><a name="p73201021125910"></a><a name="p73201021125910"></a><strong id="b149135321810"><a name="b149135321810"></a><a name="b149135321810"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.3"><p id="p20323521125914"><a name="p20323521125914"></a><a name="p20323521125914"></a><strong id="b38055541814"><a name="b38055541814"></a><a name="b38055541814"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p83342021195910"><a name="p83342021195910"></a><a name="p83342021195910"></a><strong id="b5540155201915"><a name="b5540155201915"></a><a name="b5540155201915"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081138_row20801079"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p174621855178"><a name="en-us_topic_0085081138_p174621855178"></a><a name="en-us_topic_0085081138_p174621855178"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p962513651615"><a name="p962513651615"></a><a name="p962513651615"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p194623517176"><a name="en-us_topic_0085081138_p194623517176"></a><a name="en-us_topic_0085081138_p194623517176"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p11462145141718"><a name="en-us_topic_0085081138_p11462145141718"></a><a name="en-us_topic_0085081138_p11462145141718"></a>Specifies the stack action that triggers this software deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row20715858"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p4462185101712"><a name="en-us_topic_0085081138_p4462185101712"></a><a name="en-us_topic_0085081138_p4462185101712"></a>config_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p16625536151611"><a name="p16625536151611"></a><a name="p16625536151611"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p44624515173"><a name="en-us_topic_0085081138_p44624515173"></a><a name="en-us_topic_0085081138_p44624515173"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p946255131715"><a name="en-us_topic_0085081138_p946255131715"></a><a name="en-us_topic_0085081138_p946255131715"></a>Specifies the ID of the software configuration running on a server.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row26021030"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p646220520171"><a name="en-us_topic_0085081138_p646220520171"></a><a name="en-us_topic_0085081138_p646220520171"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p962513617167"><a name="p962513617167"></a><a name="p962513617167"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p9462175151719"><a name="en-us_topic_0085081138_p9462175151719"></a><a name="en-us_topic_0085081138_p9462175151719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p53600188338"><a name="p53600188338"></a><a name="p53600188338"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen5185623143317"><a name="screen5185623143317"></a><a name="screen5185623143317"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081138_row45386595"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p16462135131716"><a name="en-us_topic_0085081138_p16462135131716"></a><a name="en-us_topic_0085081138_p16462135131716"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p76251636101619"><a name="p76251636101619"></a><a name="p76251636101619"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p2462115191714"><a name="en-us_topic_0085081138_p2462115191714"></a><a name="en-us_topic_0085081138_p2462115191714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p1446255201715"><a name="en-us_topic_0085081138_p1446255201715"></a><a name="en-us_topic_0085081138_p1446255201715"></a>Specifies the software deployment UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row23709572"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p1846217512178"><a name="en-us_topic_0085081138_p1846217512178"></a><a name="en-us_topic_0085081138_p1846217512178"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p1262523671613"><a name="p1262523671613"></a><a name="p1262523671613"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p10462185141714"><a name="en-us_topic_0085081138_p10462185141714"></a><a name="en-us_topic_0085081138_p10462185141714"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p184621251175"><a name="en-us_topic_0085081138_p184621251175"></a><a name="en-us_topic_0085081138_p184621251175"></a>Specifies input data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row1676488279"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p0462957175"><a name="en-us_topic_0085081138_p0462957175"></a><a name="en-us_topic_0085081138_p0462957175"></a>output_values</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p162543631613"><a name="p162543631613"></a><a name="p162543631613"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p164622054174"><a name="en-us_topic_0085081138_p164622054174"></a><a name="en-us_topic_0085081138_p164622054174"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p546218561713"><a name="en-us_topic_0085081138_p546218561713"></a><a name="en-us_topic_0085081138_p546218561713"></a>Specifies output data stored in the form of a key-value pair.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row876414818717"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p1346255161713"><a name="en-us_topic_0085081138_p1346255161713"></a><a name="en-us_topic_0085081138_p1346255161713"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p262503621616"><a name="p262503621616"></a><a name="p262503621616"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p646218511717"><a name="en-us_topic_0085081138_p646218511717"></a><a name="en-us_topic_0085081138_p646218511717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p04635517176"><a name="en-us_topic_0085081138_p04635517176"></a><a name="en-us_topic_0085081138_p04635517176"></a>Specifies the server ID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row576428579"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p11463353174"><a name="en-us_topic_0085081138_p11463353174"></a><a name="en-us_topic_0085081138_p11463353174"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p262520365168"><a name="p262520365168"></a><a name="p262520365168"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p746318515172"><a name="en-us_topic_0085081138_p746318515172"></a><a name="en-us_topic_0085081138_p746318515172"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p94638512174"><a name="en-us_topic_0085081138_p94638512174"></a><a name="en-us_topic_0085081138_p94638512174"></a>Specifies the status of software deployments. Valid values include <strong id="b43633141919"><a name="b43633141919"></a><a name="b43633141919"></a>COMPLETE</strong>, <strong id="b144334193"><a name="b144334193"></a><a name="b144334193"></a>IN_PROGRESS</strong>, and <strong id="b16513339196"><a name="b16513339196"></a><a name="b16513339196"></a>FAILED</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row17648812714"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p7463105201719"><a name="en-us_topic_0085081138_p7463105201719"></a><a name="en-us_topic_0085081138_p7463105201719"></a>status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p56259363161"><a name="p56259363161"></a><a name="p56259363161"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p44636519171"><a name="en-us_topic_0085081138_p44636519171"></a><a name="en-us_topic_0085081138_p44636519171"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081138_p7463954171"><a name="en-us_topic_0085081138_p7463954171"></a><a name="en-us_topic_0085081138_p7463954171"></a>Specifies the cause of the software deployment status.</p>
</td>
</tr>
<tr id="en-us_topic_0085081138_row196812121172"><td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081138_p54631551171"><a name="en-us_topic_0085081138_p54631551171"></a><a name="en-us_topic_0085081138_p54631551171"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p116251836111612"><a name="p116251836111612"></a><a name="p116251836111612"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081138_p1846385111718"><a name="en-us_topic_0085081138_p1846385111718"></a><a name="en-us_topic_0085081138_p1846385111718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p5338268335"><a name="p5338268335"></a><a name="p5338268335"></a>Specifies the update time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen414393112332"><a name="screen414393112332"></a><a name="screen414393112332"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081138_section41009935"></a>

```
PUT /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments/3d5ec2a8-7004-43b6-a7f6-542bdbe9d434
{
    "status": "COMPLETE",
    "output_values": {
        "deploy_stdout": "Writing to /tmp/baaaaa\nWritten to /tmp/baaaaa\n",
        "deploy_stderr": "+ echo Writing to /tmp/baaaaa\n+ echo fooooo\n+ cat /tmp/baaaaa\n+ echo -n The file /tmp/baaaaa contains fooooo for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE\n+ echo Written to /tmp/baaaaa\n+ echo Output to stderr\nOutput to stderr\n",
        "deploy_status_code": 0,
        "result": "The file /tmp/baaaaa contains fooooo for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE"
    },
    "status_reason": "Outputs received"
}
```

## Response Example<a name="en-us_topic_0085081138_section33545101"></a>

```
{
    "software_deployment": {
        "status": "COMPLETE",
        "server_id": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
        "config_id": "3d5ec2a8-7004-43b6-a7f6-542bdbe9d434",
        "output_values": {
            "deploy_stdout": "Writing to /tmp/baaaaa\nWritten to /tmp/baaaaa\n",
            "deploy_stderr": "+ echo Writing to /tmp/baaaaa\n+ echo fooooo\n+ cat /tmp/baaaaa\n+ echo -n The file /tmp/baaaaa contains fooooo for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE\n+ echo Written to /tmp/baaaaa\n+ echo Output to stderr\nOutput to stderr\n",
            "deploy_status_code": 0,
            "result": "The file /tmp/baaaaa contains fooooo for server ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5 during CREATE"
        },
        "input_values": null,
        "action": "CREATE",
        "status_reason": "Outputs received",
        "id": "06e87bcc-33a2-4bce-aebd-533e698282d3",
        "creation_time": "2015-01-31T15:12:36Z",
        "updated_time": "2015-01-31T15:18:21Z"
    }
}
```

## Return Code<a name="en-us_topic_0085081138_section33470456"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table3304326164315"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_p129561510144"><a name="en-us_topic_0084581290_p129561510144"></a><a name="en-us_topic_0084581290_p129561510144"></a><strong id="en-us_topic_0084581290_b1552942884813"><a name="en-us_topic_0084581290_b1552942884813"></a><a name="en-us_topic_0084581290_b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_p4959810444"><a name="en-us_topic_0084581290_p4959810444"></a><a name="en-us_topic_0084581290_p4959810444"></a><strong id="en-us_topic_0084581290_b956007905"><a name="en-us_topic_0084581290_b956007905"></a><a name="en-us_topic_0084581290_b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_p9959161020418"><a name="en-us_topic_0084581290_p9959161020418"></a><a name="en-us_topic_0084581290_p9959161020418"></a><strong id="en-us_topic_0084581290_b359171417"><a name="en-us_topic_0084581290_b359171417"></a><a name="en-us_topic_0084581290_b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p896118101840"><a name="en-us_topic_0084581290_p896118101840"></a><a name="en-us_topic_0084581290_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1296211015416"><a name="en-us_topic_0084581290_p1296211015416"></a><a name="en-us_topic_0084581290_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p9963110146"><a name="en-us_topic_0084581290_p9963110146"></a><a name="en-us_topic_0084581290_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p18134027201912"><a name="en-us_topic_0084581290_p18134027201912"></a><a name="en-us_topic_0084581290_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1713419274191"><a name="en-us_topic_0084581290_p1713419274191"></a><a name="en-us_topic_0084581290_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p11134162718196"><a name="en-us_topic_0084581290_p11134162718196"></a><a name="en-us_topic_0084581290_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p125520290312"><a name="en-us_topic_0084581290_p125520290312"></a><a name="en-us_topic_0084581290_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p19789174972712"><a name="en-us_topic_0084581290_p19789174972712"></a><a name="en-us_topic_0084581290_p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p779364918272"><a name="en-us_topic_0084581290_p779364918272"></a><a name="en-us_topic_0084581290_p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p196546319198"><a name="en-us_topic_0084581290_p196546319198"></a><a name="en-us_topic_0084581290_p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

