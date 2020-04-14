# Acknowledging Consumption of Specified Messages<a name="EN-US_TOPIC_0128036918"></a>

## Function<a name="section26355580"></a>

This API is used to confirm the consumption of specified messages.

While a message is being consumed, it remains in the queue and cannot be consumed again within 30s. If the message fails to be consumed within 30s, it can be consumed again.

If a message is consumed, it cannot be consumed again by the consumer group. However, it is retained in the queue \(unless the queue is deleted\) and can be consumed by other consumer groups. The retention period is 72 hours by default and the message will be deleted 72 hours later.

After a batch of messages is consumed, consumers must acknowledge the message consumption in the exact order that the messages are consumed. DMS checks whether messages are successfully consumed in the same order. If a message has not been acknowledged as a consumed message or failed to be consumed, DMS stops checking and determines that all the subsequent messages fail to be consumed. Therefore, when a consumer fails to acknowledge the consumption of a message \(in a batch of messages\), you are advised to stop the consumer from consuming the rest of the messages, and acknowledge the consumption of messages that have been successfully consumed.

If the consumption of a message fails to be acknowledged, this message can be re-consumed and its consumption can also be acknowledged again. If dead letter messages are enabled and a message fails to be consumed for a preset number of times, the message will be sent to the dead letter queue and retained in the dead letter queue for a maximum of 72 hours. You can then consume the message from the dead letter queue.

## URI<a name="section35873632"></a>

POST /v1.0/\{project\_id\}/queues/\{queue\_id\}/groups/\{consumer\_group\_id\}/ack

[Table 1](#d0e2680)  describes the parameters of this API. 

**Table  1**  Parameter description

<a name="d0e2680"></a>
<table><thead align="left"><tr id="row36592919"><th class="cellrowborder" valign="top" width="27.26%" id="mcps1.2.5.1.1"><p id="p11236435"><a name="p11236435"></a><a name="p11236435"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p37736068"><a name="p37736068"></a><a name="p37736068"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.3"><p id="p334771911720"><a name="p334771911720"></a><a name="p334771911720"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="38.53%" id="mcps1.2.5.1.4"><p id="p36722706"><a name="p36722706"></a><a name="p36722706"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21749220"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.5.1.1 "><p id="p16856419"><a name="p16856419"></a><a name="p16856419"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p23192694"><a name="p23192694"></a><a name="p23192694"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p636522811720"><a name="p636522811720"></a><a name="p636522811720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.5.1.4 "><p id="p66668934"><a name="p66668934"></a><a name="p66668934"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row63149496"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.5.1.1 "><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p60827539"><a name="p60827539"></a><a name="p60827539"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p302882591720"><a name="p302882591720"></a><a name="p302882591720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.5.1.4 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row51426113"><td class="cellrowborder" valign="top" width="27.26%" headers="mcps1.2.5.1.1 "><p id="p887613395810"><a name="p887613395810"></a><a name="p887613395810"></a>consumer_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p50473818"><a name="p50473818"></a><a name="p50473818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p2576515117159"><a name="p2576515117159"></a><a name="p2576515117159"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.5.1.4 "><p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Indicates the consumer group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section54427232"></a>

**Request parameters**

[Table 2](#d0e2731)  and  [Table 3](#table3384803163458)  list the parameter description.

**Table  2**  Request parameters

<a name="d0e2731"></a>
<table><thead align="left"><tr id="row42565233"><th class="cellrowborder" valign="top" width="22.93%" id="mcps1.2.5.1.1"><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.669999999999998%" id="mcps1.2.5.1.2"><p id="p30516772"><a name="p30516772"></a><a name="p30516772"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="26.32%" id="mcps1.2.5.1.3"><p id="p55939488"><a name="p55939488"></a><a name="p55939488"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.5.1.4"><p id="p34804713"><a name="p34804713"></a><a name="p34804713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row609510"><td class="cellrowborder" valign="top" width="22.93%" headers="mcps1.2.5.1.1 "><p id="p49370368"><a name="p49370368"></a><a name="p49370368"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p1007929816347"><a name="p1007929816347"></a><a name="p1007929816347"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="26.32%" headers="mcps1.2.5.1.3 "><p id="p51609257"><a name="p51609257"></a><a name="p51609257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.4 "><p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>Indicates the message confirmation arrays.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  message parameter description

<a name="table3384803163458"></a>
<table><thead align="left"><tr id="row66556591163458"><th class="cellrowborder" valign="top" width="18.040000000000003%" id="mcps1.2.5.1.1"><p id="p22374828163458"><a name="p22374828163458"></a><a name="p22374828163458"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.160000000000004%" id="mcps1.2.5.1.2"><p id="p421769163458"><a name="p421769163458"></a><a name="p421769163458"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.490000000000002%" id="mcps1.2.5.1.3"><p id="p34163310163458"><a name="p34163310163458"></a><a name="p34163310163458"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.31%" id="mcps1.2.5.1.4"><p id="p15764740163458"><a name="p15764740163458"></a><a name="p15764740163458"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49053518163458"><td class="cellrowborder" valign="top" width="18.040000000000003%" headers="mcps1.2.5.1.1 "><p id="p13912022163458"><a name="p13912022163458"></a><a name="p13912022163458"></a>handler</p>
</td>
<td class="cellrowborder" valign="top" width="16.160000000000004%" headers="mcps1.2.5.1.2 "><p id="p53132011163458"><a name="p53132011163458"></a><a name="p53132011163458"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.490000000000002%" headers="mcps1.2.5.1.3 "><p id="p8725620163458"><a name="p8725620163458"></a><a name="p8725620163458"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p35686618163458"><a name="p35686618163458"></a><a name="p35686618163458"></a>Indicates the ID returned during the consumption. </p>
</td>
</tr>
<tr id="row34773880184251"><td class="cellrowborder" valign="top" width="18.040000000000003%" headers="mcps1.2.5.1.1 "><p id="p44529466184251"><a name="p44529466184251"></a><a name="p44529466184251"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.160000000000004%" headers="mcps1.2.5.1.2 "><p id="p61936167184323"><a name="p61936167184323"></a><a name="p61936167184323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.490000000000002%" headers="mcps1.2.5.1.3 "><p id="p50773616184323"><a name="p50773616184323"></a><a name="p50773616184323"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p395259361074"><a name="p395259361074"></a><a name="p395259361074"></a>Indicates the message consumption status.</p>
<p id="p145254154316"><a name="p145254154316"></a><a name="p145254154316"></a>The value can be <strong id="b91078182111"><a name="b91078182111"></a><a name="b91078182111"></a>success</strong> or <strong id="b710781813114"><a name="b710781813114"></a><a name="b710781813114"></a>fail</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

```
{
  "message": [
    {
      "handler": "eyJjb25zdW1lckdyb3VwIjoibXFzX2NvbnN1bWVyXzMiLCJjb25zdW1lckluc3RhbmNlIjoicmVzdC1jb25zdW1lci1hMWM5YTRlMy1mNTY5LTQyYTgtOTQ1Ni1hYmU0NDVmZjUxYzkiLCJjb3VudCI6MSwib2Zmc2V0IjowLCJvZmZzZXRJbmRleCI6LTEsInBhcnRpdGlvbiI6MiwidG9waWMiOiJxLWI3OGE5MGFlMmExMzRiNGI4YjJiYTMwYWNhYjRlMjNhLTA3NWFlN2RhLTZjZTUtNDk2Ni05NDBjLTE3YzE5ZmI1MTc1ZSJ9",
      "status": "success"
    }
  ]
}
```

## Response<a name="section20083047"></a>

**Response parameters**

[Table 4](#d0e2557)  describes the response parameters.

**Table  4**  Response parameters

<a name="d0e2557"></a>
<table><thead align="left"><tr id="row26059286"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p30427456"><a name="p30427456"></a><a name="p30427456"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p48704899"><a name="p48704899"></a><a name="p48704899"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p52782726"><a name="p52782726"></a><a name="p52782726"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47542385"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a>success</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a>Indicates the number of messages that are successfully acknowledged. The value <strong id="b1579749214"><a name="b1579749214"></a><a name="b1579749214"></a>N</strong> indicates that the first <em id="i209071015124"><a name="i209071015124"></a><a name="i209071015124"></a>N</em> messages are successfully acknowledged.</p>
</td>
</tr>
<tr id="row40091191163720"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p25276400163720"><a name="p25276400163720"></a><a name="p25276400163720"></a>fail</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p34122502163720"><a name="p34122502163720"></a><a name="p34122502163720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p12459314163720"><a name="p12459314163720"></a><a name="p12459314163720"></a>Indicates the number of messages that failed to be acknowledged. The value <strong id="b12723104119216"><a name="b12723104119216"></a><a name="b12723104119216"></a>N</strong> indicates that the last <em id="i12866559219"><a name="i12866559219"></a><a name="i12866559219"></a>N</em> messages failed to be acknowledged.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "success": 1, 
  "fail": 2
}
```

## Status Code<a name="section46529701"></a>

[Table 5](#d0e2845)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  5**  Status code

<a name="d0e2845"></a>
<table><thead align="left"><tr id="row15748167"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p533144"><a name="p533144"></a><a name="p533144"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p43184669"><a name="p43184669"></a><a name="p43184669"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8297278"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p990949"><a name="p990949"></a><a name="p990949"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p13158007"><a name="p13158007"></a><a name="p13158007"></a>The consumption of the message is successfully acknowledged.</p>
</td>
</tr>
</tbody>
</table>

