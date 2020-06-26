# Error Code Reference<a name="dws_01_0068"></a>

If errors occur when DWS operation requests submitted on the management console are being processed, error information is displayed on the management console. The error information includes the returned error code and description.

## Error Code Description<a name="section372646321946"></a>

If an error occurs, find the error code and perform the corresponding operations listed in  [Table 1](#table65737292).

**Table  1**  Error codes

<a name="table65737292"></a>
<table><thead align="left"><tr id="row27077540"><th class="cellrowborder" valign="top" width="23.51%" id="mcps1.2.4.1.1"><p id="p45797138"><a name="p45797138"></a><a name="p45797138"></a><strong id="b3956735895621"><a name="b3956735895621"></a><a name="b3956735895621"></a>Error Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.98%" id="mcps1.2.4.1.2"><p id="p28644761"><a name="p28644761"></a><a name="p28644761"></a><strong id="b193467593711236"><a name="b193467593711236"></a><a name="b193467593711236"></a>Error Information</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.509999999999998%" id="mcps1.2.4.1.3"><p id="p25221318211340"><a name="p25221318211340"></a><a name="p25221318211340"></a><strong id="b1073672764112317"><a name="b1073672764112317"></a><a name="b1073672764112317"></a>Recommended Action</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row38524289"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p33459681"><a name="p33459681"></a><a name="p33459681"></a>DWS.6000</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p15876907"><a name="p15876907"></a><a name="p15876907"></a>Failed to create the cluster because of an internal error. Contact customer service or try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p10440458211340"><a name="p10440458211340"></a><a name="p10440458211340"></a>Check the remaining resource quota of the account. If the remaining resource quota is greater than the requested resources, contact customer service engineers or technical support engineers.</p>
</td>
</tr>
<tr id="row14499481"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p33607346"><a name="p33607346"></a><a name="p33607346"></a>DWS.6001</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p57263848211628"><a name="p57263848211628"></a><a name="p57263848211628"></a>Failed to scale out the cluster because of an internal error. Contact customer service or try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p20380581211340"><a name="p20380581211340"></a><a name="p20380581211340"></a>Check the remaining node quantity quota of the account. If the remaining node quantity quota is greater than the number of requested nodes, contact customer service engineers or technical support engineers.</p>
</td>
</tr>
<tr id="row3989940"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p54749715"><a name="p54749715"></a><a name="p54749715"></a>DWS.6002</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p5749380121175"><a name="p5749380121175"></a><a name="p5749380121175"></a>Failed to restart the cluster because of an internal error. Contact customer service or try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p30870268211340"><a name="p30870268211340"></a><a name="p30870268211340"></a>Contact customer service or try again later.</p>
</td>
</tr>
<tr id="row13553869"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p24121565"><a name="p24121565"></a><a name="p24121565"></a>DWS.6003</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p6446166821176"><a name="p6446166821176"></a><a name="p6446166821176"></a>Failed to restore the cluster because of an internal error. Contact customer service or try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p11191896211340"><a name="p11191896211340"></a><a name="p11191896211340"></a>Check the remaining quota of the account. If the remaining quota is greater than the requested quota, contact customer service engineers or technical support engineers.</p>
</td>
</tr>
<tr id="row10514501164329"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p37262524164333"><a name="p37262524164333"></a><a name="p37262524164333"></a>DWS.6004</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p401076921179"><a name="p401076921179"></a><a name="p401076921179"></a>Failed to create a DWS node. This is caused by an ECS exception and the error code is <strong id="b842352706115118"><a name="b842352706115118"></a><a name="b842352706115118"></a>${FailureReason}</strong>. Contact customer service or try again later.</p>
<div class="note" id="note3673743522248"><a name="note3673743522248"></a><a name="note3673743522248"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p676147422248"><a name="p676147422248"></a><a name="p676147422248"></a>Replace <strong id="b84235270614418_1"><a name="b84235270614418_1"></a><a name="b84235270614418_1"></a>${FailureReason}</strong> with the real-world ECS error code, for example, <span class="parmvalue" id="parmvalue110917238411369"><a name="parmvalue110917238411369"></a><a name="parmvalue110917238411369"></a><b>ECS.0219</b></span>.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p125801053182311"><a name="p125801053182311"></a><a name="p125801053182311"></a>For details about the ECS error codes and recommended actions, see <span class="filepath" id="filepath6603165452316"><a name="filepath6603165452316"></a><a name="filepath6603165452316"></a><b>How Do I Handle Error Messages Displayed on the Management Console?</b></span> in the Elastic Cloud Server User Guide FAQs.</p>
</td>
</tr>
<tr id="row60662409212011"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p11717962212011"><a name="p11717962212011"></a><a name="p11717962212011"></a>DWS.6005</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p61554770212011"><a name="p61554770212011"></a><a name="p61554770212011"></a>Failed to bind an EIP to a data warehouse cluster. This is caused by a VPC exception and the error code is <strong id="b1134129697192154"><a name="b1134129697192154"></a><a name="b1134129697192154"></a>${FailureReason}</strong>. Contact customer service or try again later.</p>
<div class="note" id="note6046368022253"><a name="note6046368022253"></a><a name="note6046368022253"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2650582222253"><a name="p2650582222253"></a><a name="p2650582222253"></a>Replace <strong id="b87421526819228_1"><a name="b87421526819228_1"></a><a name="b87421526819228_1"></a>${FailureReason}</strong> with the real-world VPC error code.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p112319414256"><a name="p112319414256"></a><a name="p112319414256"></a>For details about the VPC error codes, see <span class="filepath" id="filepath13660421252"><a name="filepath13660421252"></a><a name="filepath13660421252"></a><b>Error Codes</b></span> in the <em id="i271112404281"><a name="i271112404281"></a><a name="i271112404281"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row28587282153318"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p33868467153318"><a name="p33868467153318"></a><a name="p33868467153318"></a>DWS.6006</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p58991301153318"><a name="p58991301153318"></a><a name="p58991301153318"></a>Failed to bind the EIP. The error code is <strong id="b842352706155640"><a name="b842352706155640"></a><a name="b842352706155640"></a>${FailureReason}</strong>.</p>
<div class="note" id="note35211281168"><a name="note35211281168"></a><a name="note35211281168"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1954928111620"><a name="p1954928111620"></a><a name="p1954928111620"></a>Replace <strong id="b87421526819228_3"><a name="b87421526819228_3"></a><a name="b87421526819228_3"></a>${FailureReason}</strong> with the real-world VPC error code.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p88612293287"><a name="p88612293287"></a><a name="p88612293287"></a>For details about the VPC error codes, see <span class="filepath" id="filepath15864830122812"><a name="filepath15864830122812"></a><a name="filepath15864830122812"></a><b>Error Codes</b></span> in the <em id="i49684115296"><a name="i49684115296"></a><a name="i49684115296"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row63630986153323"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p53836230153323"><a name="p53836230153323"></a><a name="p53836230153323"></a>DWS.6007</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p65767334153323"><a name="p65767334153323"></a><a name="p65767334153323"></a>The EIP has been bound to other VMs. The error code is <strong id="b778846736155758"><a name="b778846736155758"></a><a name="b778846736155758"></a>${FailureReason}</strong>.</p>
<div class="note" id="note45361831101619"><a name="note45361831101619"></a><a name="note45361831101619"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p453911310163"><a name="p453911310163"></a><a name="p453911310163"></a>Replace <strong id="b87421526819228_5"><a name="b87421526819228_5"></a><a name="b87421526819228_5"></a>${FailureReason}</strong> with the real-world VPC error code.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p14462105719130"><a name="p14462105719130"></a><a name="p14462105719130"></a>Select another unbound EIP. </p>
</td>
</tr>
<tr id="row9357894153328"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.1 "><p id="p19791911153328"><a name="p19791911153328"></a><a name="p19791911153328"></a>DWS.6008</p>
</td>
<td class="cellrowborder" valign="top" width="46.98%" headers="mcps1.2.4.1.2 "><p id="p59640953153328"><a name="p59640953153328"></a><a name="p59640953153328"></a>Failed to create the private network domain name. The error code is <strong id="b523476388155855"><a name="b523476388155855"></a><a name="b523476388155855"></a>${FailureReason}</strong>.</p>
<div class="note" id="note1937621171514"><a name="note1937621171514"></a><a name="note1937621171514"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1293802161520"><a name="p1293802161520"></a><a name="p1293802161520"></a>Replace <strong id="b84235270614418_3"><a name="b84235270614418_3"></a><a name="b84235270614418_3"></a>${FailureReason}</strong> with the real-world DNS error code.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="29.509999999999998%" headers="mcps1.2.4.1.3 "><p id="p66187875153328"><a name="p66187875153328"></a><a name="p66187875153328"></a>Contact customer service personnel.</p>
</td>
</tr>
</tbody>
</table>

