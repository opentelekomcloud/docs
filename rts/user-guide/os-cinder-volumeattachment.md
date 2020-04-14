# OS::Cinder::VolumeAttachment<a name="EN-US_TOPIC_0088407140"></a>

Resource for associating volume to instance.

Resource for associating existing volume to instance. Also, the location where the volume is exposed on the instance can be specified.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Do not attach multiple volumes to one VM at the same time in the template.  

## Required Properties<a name="section1337122782211"></a>

<a name="table12338194282214"></a>
<table><thead align="left"><tr id="row1758184410475"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1133912423229"><a name="p1133912423229"></a><a name="p1133912423229"></a><strong id="b175478113489"><a name="b175478113489"></a><a name="b175478113489"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p163395423228"><a name="p163395423228"></a><a name="p163395423228"></a><strong id="b35489119484"><a name="b35489119484"></a><a name="b35489119484"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1558144424712"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p13339114262212"><a name="p13339114262212"></a><a name="p13339114262212"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p58654237"><a name="p58654237"></a><a name="p58654237"></a>The ID of the server to which the volume attaches.</p>
<p id="p58126086"><a name="p58126086"></a><a name="p58126086"></a>String value expected.</p>
<p id="p53372732"><a name="p53372732"></a><a name="p53372732"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1258164434719"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p63391042142215"><a name="p63391042142215"></a><a name="p63391042142215"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p28224024"><a name="p28224024"></a><a name="p28224024"></a>The ID of the volume to be attached.</p>
<p id="p52689624"><a name="p52689624"></a><a name="p52689624"></a>String value expected.</p>
<p id="p4444568"><a name="p4444568"></a><a name="p4444568"></a>Can be updated without replacement.</p>
<p id="p40001113"><a name="p40001113"></a><a name="p40001113"></a>Value must be of type cinder.volume</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section2089112102414"></a>

<a name="table0307015142417"></a>
<table><thead align="left"><tr id="row8865115213481"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p530861516247"><a name="p530861516247"></a><a name="p530861516247"></a><strong id="b1865205274813"><a name="b1865205274813"></a><a name="b1865205274813"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p143091315122418"><a name="p143091315122418"></a><a name="p143091315122418"></a><strong id="b486625284814"><a name="b486625284814"></a><a name="b486625284814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row686710525482"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p33091415152419"><a name="p33091415152419"></a><a name="p33091415152419"></a>mountpoint</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p29373004"><a name="p29373004"></a><a name="p29373004"></a>The location where the volume is exposed on the instance. This assignment may not be honored and it is advised that the path /dev/disk/by-id/virtio- be used instead.</p>
<p id="p30403143"><a name="p30403143"></a><a name="p30403143"></a>String value expected.</p>
<p id="p5192836"><a name="p5192836"></a><a name="p5192836"></a>Can be updated without replacement.</p>
<p id="p46735531"><a name="p46735531"></a><a name="p46735531"></a>Detailed information about resource.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section1644223219269"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Cinder::VolumeAttachment
    properties:
      instance_uuid: String
      mountpoint: String
      volume_id: String
```

