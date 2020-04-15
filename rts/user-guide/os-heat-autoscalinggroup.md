# OS::Heat::AutoScalingGroup<a name="EN-US_TOPIC_0088407209"></a>

An autoscaling group that can scale arbitrary resources.

An autoscaling group allows the creation of a desired count of similar resources, which are defined with the resource property in HOT format. If there is a need to create many of the same resources \(e.g. one hundred sets of Server, WaitCondition and WaitConditionHandle or even Neutron Nets\), AutoScalingGroup is a convenient and easy way to do that.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   During the scaling process, you are not allowed to create members. Otherwise, the scaling action fails.  
>-   Cross-AZ automatic scaling is not supported.  

## Required Properties<a name="section646202317"></a>

<a name="table1370913258315"></a>
<table><thead align="left"><tr id="row768174195315"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p5709625163111"><a name="p5709625163111"></a><a name="p5709625163111"></a><strong id="b149611230115312"><a name="b149611230115312"></a><a name="b149611230115312"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p5709132573111"><a name="p5709132573111"></a><a name="p5709132573111"></a><strong id="b096312309533"><a name="b096312309533"></a><a name="b096312309533"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1668113495313"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p370912514311"><a name="p370912514311"></a><a name="p370912514311"></a>max_size</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p15709202583113"><a name="p15709202583113"></a><a name="p15709202583113"></a>Maximum number of resources in the group.</p>
<p id="p11119901"><a name="p11119901"></a><a name="p11119901"></a>Integer value expected.</p>
<p id="p32970250"><a name="p32970250"></a><a name="p32970250"></a>Can be updated without replacement.</p>
<p id="p28296801"><a name="p28296801"></a><a name="p28296801"></a>The value must be at least 0.</p>
</td>
</tr>
<tr id="row76814411533"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p070952514317"><a name="p070952514317"></a><a name="p070952514317"></a>min_size</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p10339508"><a name="p10339508"></a><a name="p10339508"></a>Minimum number of resources in the group.</p>
<p id="p25946716"><a name="p25946716"></a><a name="p25946716"></a>Integer value expected.</p>
<p id="p32193857"><a name="p32193857"></a><a name="p32193857"></a>Can be updated without replacement.</p>
<p id="p21309260"><a name="p21309260"></a><a name="p21309260"></a>The value must be at least 0.</p>
</td>
</tr>
<tr id="row86815419536"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1670912517313"><a name="p1670912517313"></a><a name="p1670912517313"></a>resource</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p48328480"><a name="p48328480"></a><a name="p48328480"></a>Resource definition for the resources in the group, in HOT format. The value of this property is the definition of a resource just as if it had been declared in the template itself.</p>
<p id="p32303139"><a name="p32303139"></a><a name="p32303139"></a>Map value expected.</p>
<p id="p22292801"><a name="p22292801"></a><a name="p22292801"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section108679315345"></a>

<a name="table2487101423416"></a>
<table><thead align="left"><tr id="row587594535416"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p17490181414345"><a name="p17490181414345"></a><a name="p17490181414345"></a><strong id="b1846100115514"><a name="b1846100115514"></a><a name="b1846100115514"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1849017147342"><a name="p1849017147342"></a><a name="p1849017147342"></a><strong id="b124620016551"><a name="b124620016551"></a><a name="b124620016551"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11876845195411"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1549171443410"><a name="p1549171443410"></a><a name="p1549171443410"></a>cooldown</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1595722"><a name="p1595722"></a><a name="p1595722"></a>Cooldown period, in seconds.</p>
<p id="p14361499"><a name="p14361499"></a><a name="p14361499"></a>Integer value expected.</p>
<p id="p62144632"><a name="p62144632"></a><a name="p62144632"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1387684510540"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p9494814133411"><a name="p9494814133411"></a><a name="p9494814133411"></a>desired_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p550398"><a name="p550398"></a><a name="p550398"></a>Desired initial number of resources.</p>
<p id="p4953586"><a name="p4953586"></a><a name="p4953586"></a>Integer value expected.</p>
<p id="p44582277"><a name="p44582277"></a><a name="p44582277"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1876154510549"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3907191573513"><a name="p3907191573513"></a><a name="p3907191573513"></a>rolling_updates</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p54394676"><a name="p54394676"></a><a name="p54394676"></a>Policy for rolling updates for this scaling group.</p>
<p id="p19790043"><a name="p19790043"></a><a name="p19790043"></a>Map value expected.</p>
<p id="p43892660"><a name="p43892660"></a><a name="p43892660"></a>Can be updated without replacement.</p>
<p id="p59489626"><a name="p59489626"></a><a name="p59489626"></a>Defaults to "{max_batch_size: 1, min_in_service: 0, pause_time: 0}".</p>
<p id="p53930390"><a name="p53930390"></a><a name="p53930390"></a>Map properties:</p>
<a name="ul15611462"></a><a name="ul15611462"></a><ul id="ul15611462"><li>max_batch_size<p id="p56568871"><a name="p56568871"></a><a name="p56568871"></a>The maximum number of resources to replace at once.</p>
<p id="p39357794"><a name="p39357794"></a><a name="p39357794"></a>Integer value expected.</p>
<p id="p18675833"><a name="p18675833"></a><a name="p18675833"></a>Can be updated without replacement.</p>
<p id="p33864771"><a name="p33864771"></a><a name="p33864771"></a>Defaults to "1".</p>
<p id="p765484693615"><a name="p765484693615"></a><a name="p765484693615"></a>The value must be at least 1.</p>
</li><li>min_in_service<p id="p38099490"><a name="p38099490"></a><a name="p38099490"></a>The minimum number of resources in service while rolling updates are being executed.</p>
<p id="p7351090"><a name="p7351090"></a><a name="p7351090"></a>Integer value expected.</p>
<p id="p66159813"><a name="p66159813"></a><a name="p66159813"></a>Can be updated without replacement.</p>
<p id="p58567413"><a name="p58567413"></a><a name="p58567413"></a>Defaults to "0".</p>
<p id="p1136611418372"><a name="p1136611418372"></a><a name="p1136611418372"></a>The value must be at least 0.</p>
</li><li>pause_time<p id="p26116900"><a name="p26116900"></a><a name="p26116900"></a>The number of seconds to wait between batches of updates.</p>
<p id="p33725514"><a name="p33725514"></a><a name="p33725514"></a>Number value expected.</p>
<p id="p35094170"><a name="p35094170"></a><a name="p35094170"></a>Can be updated without replacement.</p>
<p id="p47412079"><a name="p47412079"></a><a name="p47412079"></a>Defaults to "0".</p>
<p id="p028613322375"><a name="p028613322375"></a><a name="p028613322375"></a>The value must be at least 0.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section32861237123815"></a>

<a name="table14260243133815"></a>
<table><thead align="left"><tr id="row361310562579"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p92611043163811"><a name="p92611043163811"></a><a name="p92611043163811"></a><strong id="b9614356175720"><a name="b9614356175720"></a><a name="b9614356175720"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p8261184310386"><a name="p8261184310386"></a><a name="p8261184310386"></a><strong id="b136161568578"><a name="b136161568578"></a><a name="b136161568578"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row0617125614573"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1826110431383"><a name="p1826110431383"></a><a name="p1826110431383"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1126154323818"><a name="p1126154323818"></a><a name="p1126154323818"></a>A map of resource names to the specified attribute of each individual resource that is part of the AutoScalingGroup. This map specifies output parameters that are available once the AutoScalingGroup has been instantiated.</p>
</td>
</tr>
<tr id="row662175614574"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p3261543173812"><a name="p3261543173812"></a><a name="p3261543173812"></a>outputs_list</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p8261184317387"><a name="p8261184317387"></a><a name="p8261184317387"></a>A list of the specified attribute of each individual resource that is part of the AutoScalingGroup. This list of attributes is available as an output once the AutoScalingGroup has been instantiated. Detailed information about resource.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section69831159164010"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::AutoScalingGroup
    properties:
      cooldown: Integer
      desired_capacity: Integer
      max_size: Integer
      min_size: Integer
      resource: {...}
      rolling_updates: {"max_batch_size": Integer, "pause_time": Number, "min_in_service": Integer}
```

