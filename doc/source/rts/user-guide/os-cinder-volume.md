# OS::Cinder::Volume<a name="EN-US_TOPIC_0088407127"></a>

A resource that implements Cinder volumes.

Cinder volume is a storage in the form of block devices. It can be used, for example, for providing storage to instance. Volume supports creation from snapshot, backup or image. Also volume can be created only by size.

## Optional Properties<a name="section2780161584715"></a>

<a name="table182121749185010"></a>
<table><thead align="left"><tr id="row9738201917282"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p32131349195011"><a name="p32131349195011"></a><a name="p32131349195011"></a><strong id="b2835135715404"><a name="b2835135715404"></a><a name="b2835135715404"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p102131349135019"><a name="p102131349135019"></a><a name="p102131349135019"></a><strong id="b283718574403"><a name="b283718574403"></a><a name="b283718574403"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47384199289"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p7213949145015"><a name="p7213949145015"></a><a name="p7213949145015"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p52131049165016"><a name="p52131049165016"></a><a name="p52131049165016"></a>The availability zone in which the volume will be created.</p>
<p id="p6470538205319"><a name="p6470538205319"></a><a name="p6470538205319"></a>String value expected.</p>
<p id="p18339247105316"><a name="p18339247105316"></a><a name="p18339247105316"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1073881917283"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1921314498508"><a name="p1921314498508"></a><a name="p1921314498508"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p6741173743613"><a name="p6741173743613"></a><a name="p6741173743613"></a>If specified, the volume to create from the backup.</p>
<p id="p122132049195017"><a name="p122132049195017"></a><a name="p122132049195017"></a><span>The parameter </span><strong id="b16176241172917"><a name="b16176241172917"></a><a name="b16176241172917"></a>backup_restore</strong><span> can specify how to restore the backup.</span></p>
<p id="p15282137155518"><a name="p15282137155518"></a><a name="p15282137155518"></a>String value expected.</p>
<p id="p544417428568"><a name="p544417428568"></a><a name="p544417428568"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1052841012612"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p2637732193520"><a name="p2637732193520"></a><a name="p2637732193520"></a>backup_restore</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1663773215354"><a name="p1663773215354"></a><a name="p1663773215354"></a>The method of restoring a backup during the creation of a volume. The value is <strong id="b144503262313"><a name="b144503262313"></a><a name="b144503262313"></a>heat</strong> or <strong id="b6488132963114"><a name="b6488132963114"></a><a name="b6488132963114"></a>vbs</strong>. The default value is <strong id="b1531883353113"><a name="b1531883353113"></a><a name="b1531883353113"></a>heat</strong>.</p>
<a name="ul156832015113711"></a><a name="ul156832015113711"></a><ul id="ul156832015113711"><li>When specified as <strong id="b12613182463215"><a name="b12613182463215"></a><a name="b12613182463215"></a>heat</strong>, the native recovery method is used, which is to restore a volume from backup.</li><li>When specified as <strong id="b17640151833416"><a name="b17640151833416"></a><a name="b17640151833416"></a>vbs</strong>, after the volume is created, the API of the VBS service is called for recovery.</li></ul>
<p id="p12120171113371"><a name="p12120171113371"></a><a name="p12120171113371"></a>String value expected.</p>
<p id="p1839911113388"><a name="p1839911113388"></a><a name="p1839911113388"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row4738171902812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p142131149195015"><a name="p142131149195015"></a><a name="p142131149195015"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p17213134914504"><a name="p17213134914504"></a><a name="p17213134914504"></a>A description of the volume.</p>
<p id="p814821217571"><a name="p814821217571"></a><a name="p814821217571"></a>String value expected.</p>
<p id="p18284181985714"><a name="p18284181985714"></a><a name="p18284181985714"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row17738131915281"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p14213164918502"><a name="p14213164918502"></a><a name="p14213164918502"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p16213154985018"><a name="p16213154985018"></a><a name="p16213154985018"></a>If specified, the name or ID of the image to create the volume from.</p>
<p id="p15912143219587"><a name="p15912143219587"></a><a name="p15912143219587"></a>String value expected.</p>
<p id="p74367347581"><a name="p74367347581"></a><a name="p74367347581"></a>Updates cause replacement.</p>
<p id="p1369484220588"><a name="p1369484220588"></a><a name="p1369484220588"></a>Value must be of type glance.image</p>
<div class="note" id="note152681349113912"><a name="note152681349113912"></a><a name="note152681349113912"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p8269174913919"><a name="p8269174913919"></a><a name="p8269174913919"></a><strong id="b18656133615382"><a name="b18656133615382"></a><a name="b18656133615382"></a>image</strong>, <strong id="b9574114010385"><a name="b9574114010385"></a><a name="b9574114010385"></a>imageRef</strong>, <strong id="b113501245133818"><a name="b113501245133818"></a><a name="b113501245133818"></a>snapshot_id</strong> and <strong id="b5650249143818"><a name="b5650249143818"></a><a name="b5650249143818"></a>source_volid</strong> cannot appear at the same time, otherwise the stack will fail to create.</p>
</div></div>
</td>
</tr>
<tr id="row1738131972812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1721318492505"><a name="p1721318492505"></a><a name="p1721318492505"></a>imageRef</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p9213114915017"><a name="p9213114915017"></a><a name="p9213114915017"></a>The ID of the image to create the volume from.</p>
<p id="p1398743312594"><a name="p1398743312594"></a><a name="p1398743312594"></a>String value expected.</p>
<p id="p20657124116596"><a name="p20657124116596"></a><a name="p20657124116596"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1273831912818"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p321324912507"><a name="p321324912507"></a><a name="p321324912507"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p142141349195017"><a name="p142141349195017"></a><a name="p142141349195017"></a>Key/value pairs to associate with the volume.</p>
<p id="p568720204019"><a name="p568720204019"></a><a name="p568720204019"></a>Map value expected.</p>
<p id="p82312081240"><a name="p82312081240"></a><a name="p82312081240"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1373841972816"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1821414975010"><a name="p1821414975010"></a><a name="p1821414975010"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p182143493501"><a name="p182143493501"></a><a name="p182143493501"></a>A name used to distinguish the volume.</p>
<p id="p42831935241"><a name="p42831935241"></a><a name="p42831935241"></a>String value expected.</p>
<p id="p144811443249"><a name="p144811443249"></a><a name="p144811443249"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1473814196285"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p72141449145018"><a name="p72141449145018"></a><a name="p72141449145018"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p121414911501"><a name="p121414911501"></a><a name="p121414911501"></a>The size of the volume in GB. On update only increase in size is supported.</p>
<a name="ul32754391217"></a><a name="ul32754391217"></a><ul id="ul32754391217"><li><span>This parameter is ignored when </span><strong id="b1927583918118"><a name="b1927583918118"></a><a name="b1927583918118"></a>backup_id</strong><span> is specified and </span><strong id="b5275239216"><a name="b5275239216"></a><a name="b5275239216"></a>backup_restore</strong><span> is set to </span><strong id="b19579125610211"><a name="b19579125610211"></a><a name="b19579125610211"></a>heat</strong><span>.</span></li><li><span>This parameter is not required when </span><strong id="b927514396119"><a name="b927514396119"></a><a name="b927514396119"></a>source_volid</strong><span> or </span><strong id="b17275339413"><a name="b17275339413"></a><a name="b17275339413"></a>snapshot_id</strong><span> is specified.</span></li></ul>
<p id="p989320121356"><a name="p989320121356"></a><a name="p989320121356"></a>Integer value expected.</p>
<p id="p195541721956"><a name="p195541721956"></a><a name="p195541721956"></a>Can be updated without replacement.</p>
<p id="p174352261554"><a name="p174352261554"></a><a name="p174352261554"></a>The value must be at least 1.</p>
</td>
</tr>
<tr id="row473811917282"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1521424918505"><a name="p1521424918505"></a><a name="p1521424918505"></a>snapshot_id</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1321418491500"><a name="p1321418491500"></a><a name="p1321418491500"></a>If specified, the snapshot to create the volume from.</p>
<p id="p1767110491051"><a name="p1767110491051"></a><a name="p1767110491051"></a>String value expected.</p>
<p id="p798314916611"><a name="p798314916611"></a><a name="p798314916611"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1173951919284"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p14214124965020"><a name="p14214124965020"></a><a name="p14214124965020"></a>source_volid</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p1421484919509"><a name="p1421484919509"></a><a name="p1421484919509"></a>If specified, the volume to use as source.</p>
<p id="p17801114118613"><a name="p17801114118613"></a><a name="p17801114118613"></a>String value expected.</p>
<p id="p208013411864"><a name="p208013411864"></a><a name="p208013411864"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row1873901942812"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p19214949135011"><a name="p19214949135011"></a><a name="p19214949135011"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p121454910504"><a name="p121454910504"></a><a name="p121454910504"></a>If specified, the type of volume to use, mapping to a specific backend.</p>
<p id="p2260508"><a name="p2260508"></a><a name="p2260508"></a>String value expected.</p>
<p id="p20344575"><a name="p20344575"></a><a name="p20344575"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row2739141972815"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p id="p1466219131272"><a name="p1466219131272"></a><a name="p1466219131272"></a>multiattach</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p37297904"><a name="p37297904"></a><a name="p37297904"></a>Whether allow the volume to be attached more than once.</p>
<p id="p136824"><a name="p136824"></a><a name="p136824"></a>Boolean value expected.</p>
<p id="p1231422"><a name="p1231422"></a><a name="p1231422"></a>Updates cause replacement.</p>
<p id="p11082803"><a name="p11082803"></a><a name="p11082803"></a>Defaults to "False".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1453812821011"></a>

<a name="table38885312115"></a>
<table><thead align="left"><tr id="row4177155963617"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p20888531111114"><a name="p20888531111114"></a><a name="p20888531111114"></a><strong id="b1728955134017"><a name="b1728955134017"></a><a name="b1728955134017"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p2088843121111"><a name="p2088843121111"></a><a name="p2088843121111"></a><strong id="b529412513401"><a name="b529412513401"></a><a name="b529412513401"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1177559183618"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p688911315116"><a name="p688911315116"></a><a name="p688911315116"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p2889103118118"><a name="p2889103118118"></a><a name="p2889103118118"></a>The availability zone in which the volume is located.</p>
</td>
</tr>
<tr id="row517755923618"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p88894311111"><a name="p88894311111"></a><a name="p88894311111"></a>bootable</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p14890173191114"><a name="p14890173191114"></a><a name="p14890173191114"></a>Boolean indicating if the volume can be booted or not.</p>
</td>
</tr>
<tr id="row91771259173612"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p089003117112"><a name="p089003117112"></a><a name="p089003117112"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p6891113113113"><a name="p6891113113113"></a><a name="p6891113113113"></a>The timestamp indicating volume creation.</p>
</td>
</tr>
<tr id="row191771559103611"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p2089123191114"><a name="p2089123191114"></a><a name="p2089123191114"></a>display_description</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p15891193115118"><a name="p15891193115118"></a><a name="p15891193115118"></a>Description of the volume.</p>
</td>
</tr>
<tr id="row10177115973619"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p8891153119118"><a name="p8891153119118"></a><a name="p8891153119118"></a>display_name</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p15891231141119"><a name="p15891231141119"></a><a name="p15891231141119"></a>Name of the volume.</p>
</td>
</tr>
<tr id="row17177145913610"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p489119317117"><a name="p489119317117"></a><a name="p489119317117"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p128917310118"><a name="p128917310118"></a><a name="p128917310118"></a>Key/value pairs associated with the volume.</p>
</td>
</tr>
<tr id="row1177185943616"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1689216313119"><a name="p1689216313119"></a><a name="p1689216313119"></a>metadata_values</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1189215314119"><a name="p1189215314119"></a><a name="p1189215314119"></a>Key/value pairs associated with the volume in raw dict form.</p>
</td>
</tr>
<tr id="row1717765913620"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p17892183131114"><a name="p17892183131114"></a><a name="p17892183131114"></a>multiattach</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p48922314116"><a name="p48922314116"></a><a name="p48922314116"></a>Boolean indicating whether allow the volume to be attached more than once.</p>
</td>
</tr>
<tr id="row12177359153611"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p7892193161115"><a name="p7892193161115"></a><a name="p7892193161115"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p189313113113"><a name="p189313113113"></a><a name="p189313113113"></a>The size of the volume in GB.</p>
</td>
</tr>
<tr id="row917919597369"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p19893931181115"><a name="p19893931181115"></a><a name="p19893931181115"></a>snapshot_id</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p789333113113"><a name="p789333113113"></a><a name="p789333113113"></a>The snapshot the volume was created from, if any.</p>
</td>
</tr>
<tr id="row91791759143616"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p389343131113"><a name="p389343131113"></a><a name="p389343131113"></a>source_volid</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p48931231111114"><a name="p48931231111114"></a><a name="p48931231111114"></a>The volume used as source, if any.</p>
</td>
</tr>
<tr id="row1017919599366"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p118931131141114"><a name="p118931131141114"></a><a name="p118931131141114"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p5893931111114"><a name="p5893931111114"></a><a name="p5893931111114"></a>The current status of the volume.</p>
</td>
</tr>
<tr id="row217912591362"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p14261444161614"><a name="p14261444161614"></a><a name="p14261444161614"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p426104415162"><a name="p426104415162"></a><a name="p426104415162"></a>The type of the volume mapping to a backend, if any.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section185551447131812"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Cinder::Volume
    properties:
      availability_zone: String
      backup_id: String
      description: String
      image: String
      metadata: {...}
      name: String
      size: Integer
      volume_type: String
```

