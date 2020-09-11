# Modifying an AS Group<a name="EN-US_TOPIC_0043063036"></a>

## Function<a name="section34759433"></a>

This interface is used to modify a specified AS group.

-   When the AS configuration of an AS group is changed, the existing instances created using the original AS configuration are not affected.
-   If no scaling action is being performed, you can modify its subnet and AZ configurations.
-   Changing the number of expected instances in an AS group will trigger a scaling action to add or remove instances to or from the AS group. The number of expected instances must be greater than or equal to the minimum number of instances and less than or equal to the maximum number of instances.

## URI<a name="section44399449"></a>

PUT /autoscaling-api/v1/\{project\_id\}/scaling\_group/\{scaling\_group\_id\}

**Table  1**  Parameter description

<a name="table28310238"></a>
<table><thead align="left"><tr id="row31275254"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p50267674"><a name="p50267674"></a><a name="p50267674"></a><strong id="b768465819379"><a name="b768465819379"></a><a name="b768465819379"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p45149794"><a name="p45149794"></a><a name="p45149794"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p33254711"><a name="p33254711"></a><a name="p33254711"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.43434343434344%" id="mcps1.2.5.1.4"><p id="p9277056"><a name="p9277056"></a><a name="p9277056"></a><strong id="b13207063815"><a name="b13207063815"></a><a name="b13207063815"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13244070"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p66136720"><a name="p66136720"></a><a name="p66136720"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p55474086"><a name="p55474086"></a><a name="p55474086"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p64216018"><a name="p64216018"></a><a name="p64216018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row38598983"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p39509941"><a name="p39509941"></a><a name="p39509941"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p46188627"><a name="p46188627"></a><a name="p46188627"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p50291273"><a name="p50291273"></a><a name="p50291273"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.2.5.1.4 "><p id="p47061312"><a name="p47061312"></a><a name="p47061312"></a>Specifies the AS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section64050727"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table12486093"></a>
    <table><thead align="left"><tr id="row16676820"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p8645166"><a name="p8645166"></a><a name="p8645166"></a><strong id="b456411103817"><a name="b456411103817"></a><a name="b456411103817"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p29169865"><a name="p29169865"></a><a name="p29169865"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p13948877"><a name="p13948877"></a><a name="p13948877"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p56117216"><a name="p56117216"></a><a name="p56117216"></a><strong id="b103671521381"><a name="b103671521381"></a><a name="b103671521381"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49200685"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p25832538"><a name="p25832538"></a><a name="p25832538"></a>scaling_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p12060815"><a name="p12060815"></a><a name="p12060815"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p37401973"><a name="p37401973"></a><a name="p37401973"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p9660979"><a name="p9660979"></a><a name="p9660979"></a>Specifies the AS group name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row19839955"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p63532554"><a name="p63532554"></a><a name="p63532554"></a>desire_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p45863212"><a name="p45863212"></a><a name="p45863212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p23932707"><a name="p23932707"></a><a name="p23932707"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p5823011191516"><a name="p5823011191516"></a><a name="p5823011191516"></a>Specifies the expected number of instances.</p>
    <p id="p5723319416347"><a name="p5723319416347"></a><a name="p5723319416347"></a>The value ranges from the minimum number of instances to the maximum number of instances.</p>
    </td>
    </tr>
    <tr id="row65748243"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p24007468"><a name="p24007468"></a><a name="p24007468"></a>min_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p65556790"><a name="p65556790"></a><a name="p65556790"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p8499801"><a name="p8499801"></a><a name="p8499801"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p17395260"><a name="p17395260"></a><a name="p17395260"></a>Specifies the minimum number of instances. </p>
    </td>
    </tr>
    <tr id="row22339613"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p64678211"><a name="p64678211"></a><a name="p64678211"></a>max_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p4443775"><a name="p4443775"></a><a name="p4443775"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p24401462"><a name="p24401462"></a><a name="p24401462"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p30361426"><a name="p30361426"></a><a name="p30361426"></a>Specifies the maximum number of instances, which is greater than or equal to the minimum number of instances. </p>
    </td>
    </tr>
    <tr id="row4817386"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p54663960"><a name="p54663960"></a><a name="p54663960"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p65704606"><a name="p65704606"></a><a name="p65704606"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p20472869"><a name="p20472869"></a><a name="p20472869"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p47689684"><a name="p47689684"></a><a name="p47689684"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400 and is 300 by default.</p>
    </td>
    </tr>
    <tr id="row4958285111193"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p16265823076"><a name="p16265823076"></a><a name="p16265823076"></a>available_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p3876440411196"><a name="p3876440411196"></a><a name="p3876440411196"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p5290898211196"><a name="p5290898211196"></a><a name="p5290898211196"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p38286709101131"><a name="p38286709101131"></a><a name="p38286709101131"></a>Specifies the AZ information. The ECS associated with a scaling action will be created in a specified AZ. If you do not specify an AZ, the system automatically specifies one.</p>
    <p id="p59122678111228"><a name="p59122678111228"></a><a name="p59122678111228"></a>For details, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Availability Zone</a>.</p>
    <p id="p2494105111919"><a name="p2494105111919"></a><a name="p2494105111919"></a>You can change the AZ of an AS group only when no scaling action is being performed in the group.</p>
    </td>
    </tr>
    <tr id="row26553979"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p3388666"><a name="p3388666"></a><a name="p3388666"></a>networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p6046518"><a name="p6046518"></a><a name="p6046518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p646575517388"><a name="p646575517388"></a><a name="p646575517388"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p66985236330"><a name="p66985236330"></a><a name="p66985236330"></a>Specifies network information. The system supports up to five subnets. The first subnet transferred serves as the primary NIC of the ECS by default.  This parameter is in data structure. For details, see <a href="#taf38c137c80e494e9a0fa6191f5e9561">Table 4</a>.</p>
    <p id="p21176303193430"><a name="p21176303193430"></a><a name="p21176303193430"></a>The value of this parameter can be changed only when all the following conditions are met:</p>
    <a name="ul19922205193445"></a><a name="ul19922205193445"></a><ul id="ul19922205193445"><li>No scaling actions are triggered in the AS group.</li><li>The number of instances in the AS group is 0.</li><li>The AS group is not in service.</li></ul>
    </td>
    </tr>
    <tr id="row21685017"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p11655939"><a name="p11655939"></a><a name="p11655939"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p4607022"><a name="p4607022"></a><a name="p4607022"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1164175816382"><a name="p1164175816382"></a><a name="p1164175816382"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p18141719380"><a name="p18141719380"></a><a name="p18141719380"></a>Specifies the security group. A maximum of one security group can be selected.  This parameter is in data structure. For details, see <a href="#tf7da6b502e2c44068fb6f36eddec74a1">Table 5</a>.</p>
    <p id="p27413374"><a name="p27413374"></a><a name="p27413374"></a>If the security group is specified both in the AS configuration and AS group, the security group specified in the AS configuration prevails. If the security group is not specified in either of them, the default security group is used. For your convenience, you are advised to specify the security group in the AS configuration. The value of this parameter can be changed only when all the following conditions are met:</p>
    <a name="ul1820189319381"></a><a name="ul1820189319381"></a><ul id="ul1820189319381"><li>No scaling actions are triggered in the AS group.</li><li>The number of instances in the AS group is 0.</li><li>The AS group is not in service.</li></ul>
    </td>
    </tr>
    <tr id="row47854229"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p50987349"><a name="p50987349"></a><a name="p50987349"></a>lb_listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p36334585"><a name="p36334585"></a><a name="p36334585"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p57420266"><a name="p57420266"></a><a name="p57420266"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p20895122411511"><a name="p20895122411511"></a><a name="p20895122411511"></a>Specifies the ID of a classic load balancer listener. The system supports the binding of up to six load balancer listeners, the IDs of which are separated using a comma (,). </p>
    <p id="p60106351193911"><a name="p60106351193911"></a><a name="p60106351193911"></a>The value of this parameter can be changed only when all the following conditions are met:</p>
    <a name="ul4086251193911"></a><a name="ul4086251193911"></a><ul id="ul4086251193911"><li>No scaling actions are triggered in the AS group.</li><li>The number of instances in the AS group is 0.</li><li>The AS group is not in service.</li></ul>
    </td>
    </tr>
    <tr id="row2395683017234"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4849866617237"><a name="p4849866617237"></a><a name="p4849866617237"></a>lbaas_listeners</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p3607788617237"><a name="p3607788617237"></a><a name="p3607788617237"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p3662761717237"><a name="p3662761717237"></a><a name="p3662761717237"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p172210118517"><a name="p172210118517"></a><a name="p172210118517"></a>Specifies information about an enhanced load balancer. The system supports the binding of up to six load balancers. This parameter is in list data structure. For details, see <a href="#table62452402171652">Table 3</a>. </p>
    <p id="p6406828317237"><a name="p6406828317237"></a><a name="p6406828317237"></a>This parameter is alternative to <strong id="b84235270610186"><a name="b84235270610186"></a><a name="b84235270610186"></a>lb_listener_id</strong>.</p>
    </td>
    </tr>
    <tr id="row50551688"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1046103"><a name="p1046103"></a><a name="p1046103"></a>health_periodic_audit_method</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p17625551"><a name="p17625551"></a><a name="p17625551"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p18383511"><a name="p18383511"></a><a name="p18383511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p672313117518"><a name="p672313117518"></a><a name="p672313117518"></a>Specifies the health check method for instances in the AS group. The health check methods include <strong id="b582845796161238"><a name="b582845796161238"></a><a name="b582845796161238"></a>ELB_AUDIT</strong> and <strong id="b1838261513161238"><a name="b1838261513161238"></a><a name="b1838261513161238"></a>NOVA_AUDIT</strong>. When load balancing is configured for an AS group, the default value is <strong id="b54238969164029"><a name="b54238969164029"></a><a name="b54238969164029"></a>ELB_AUDIT</strong>. Otherwise, the default value is <strong id="b909103728164036"><a name="b909103728164036"></a><a name="b909103728164036"></a>NOVA_AUDIT</strong>.</p>
    <a name="ul27231211175112"></a><a name="ul27231211175112"></a><ul id="ul27231211175112"><li><strong id="b622874993161245"><a name="b622874993161245"></a><a name="b622874993161245"></a>ELB_AUDIT</strong>: indicates the ELB health check, which takes effect in an AS group with a listener.</li><li><strong id="b842352706154542"><a name="b842352706154542"></a><a name="b842352706154542"></a>NOVA_AUDIT</strong>: indicates the ECS health check, which is the health check method delivered with AS.</li></ul>
    </td>
    </tr>
    <tr id="row46915732"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p42077948"><a name="p42077948"></a><a name="p42077948"></a>health_periodic_audit_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p52870641"><a name="p52870641"></a><a name="p52870641"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p54663514"><a name="p54663514"></a><a name="p54663514"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p65668512"><a name="p65668512"></a><a name="p65668512"></a>Specifies the health check period for the instances in the AS group. The value can be <strong id="b73017285468"><a name="b73017285468"></a><a name="b73017285468"></a>1</strong>, <strong id="b1747113014462"><a name="b1747113014462"></a><a name="b1747113014462"></a>5</strong>, <strong id="b164781632154616"><a name="b164781632154616"></a><a name="b164781632154616"></a>15</strong>, <strong id="b3754133416464"><a name="b3754133416464"></a><a name="b3754133416464"></a>60</strong>, or <strong id="b521216387464"><a name="b521216387464"></a><a name="b521216387464"></a>180</strong> in the unit of minutes.</p>
    <p id="p12748956131310"><a name="p12748956131310"></a><a name="p12748956131310"></a>If the value is set to <strong id="b0732182234616"><a name="b0732182234616"></a><a name="b0732182234616"></a>0</strong>, health check is performed every 10 seconds.</p>
    </td>
    </tr>
    <tr id="row54145697"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p23725308"><a name="p23725308"></a><a name="p23725308"></a>instance_terminate_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p42701800"><a name="p42701800"></a><a name="p42701800"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p36293772"><a name="p36293772"></a><a name="p36293772"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p1472612119514"><a name="p1472612119514"></a><a name="p1472612119514"></a>Specifies the instance removal policy.</p>
    <a name="ul137261112513"></a><a name="ul137261112513"></a><ul id="ul137261112513"><li><strong id="b34422810171421"><a name="b34422810171421"></a><a name="b34422810171421"></a>OLD_CONFIG_OLD_INSTANCE</strong> (default): The earlier-created instances based on the earlier-created AS configurations are removed first.</li><li><strong id="b50659714162554"><a name="b50659714162554"></a><a name="b50659714162554"></a>OLD_CONFIG_NEW_INSTANCE</strong>: The later-created instances based on the earlier-created AS configurations are removed first.</li><li><strong id="b21486085161946"><a name="b21486085161946"></a><a name="b21486085161946"></a>OLD_INSTANCE</strong>: The earlier-created instances are removed first.</li><li><strong id="b3854286164722"><a name="b3854286164722"></a><a name="b3854286164722"></a>NEW_INSTANCE</strong>: The later-created instances are removed first.</li></ul>
    </td>
    </tr>
    <tr id="row5077090415340"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2011844415347"><a name="p2011844415347"></a><a name="p2011844415347"></a>health_periodic_audit_grace_period</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p1898125315347"><a name="p1898125315347"></a><a name="p1898125315347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p6108652315347"><a name="p6108652315347"></a><a name="p6108652315347"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p20726151117518"><a name="p20726151117518"></a><a name="p20726151117518"></a>Specifies the grace period for instance health check. The unit is second and value range is 0-86400. The default value is <strong id="b842352706154816"><a name="b842352706154816"></a><a name="b842352706154816"></a>600</strong>.</p>
    <p id="p4726511155112"><a name="p4726511155112"></a><a name="p4726511155112"></a>The health check grace period starts after an instance is added to an AS group and is enabled. The AS group will start checking the instance status only after the grace period ends.</p>
    <p id="p9726131185116"><a name="p9726131185116"></a><a name="p9726131185116"></a>This parameter is valid only when the instance health check method of the AS group is <strong id="b842352706155131"><a name="b842352706155131"></a><a name="b842352706155131"></a>ELB_AUDIT</strong>.</p>
    </td>
    </tr>
    <tr id="row17267999"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p56530712"><a name="p56530712"></a><a name="p56530712"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p15584965"><a name="p15584965"></a><a name="p15584965"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p54422671"><a name="p54422671"></a><a name="p54422671"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p46160221"><a name="p46160221"></a><a name="p46160221"></a>Specifies the AS configuration ID, which can be obtained using the API for querying AS configurations. For details, see <a href="querying-as-configurations.md">Querying AS Configurations</a>.</p>
    </td>
    </tr>
    <tr id="row12788809"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1548885910447"><a name="p1548885910447"></a><a name="p1548885910447"></a>notifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p4663806310447"><a name="p4663806310447"></a><a name="p4663806310447"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1958678810447"><a name="p1958678810447"></a><a name="p1958678810447"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p4086519510335"><a name="p4086519510335"></a><a name="p4086519510335"></a>Specifies the notification mode.</p>
    <p id="p3224244310335"><a name="p3224244310335"></a><a name="p3224244310335"></a><strong id="b58832166171917"><a name="b58832166171917"></a><a name="b58832166171917"></a>EMAIL</strong> refers to notification by email.</p>
    </td>
    </tr>
    <tr id="row58308866162814"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p50573466162844"><a name="p50573466162844"></a><a name="p50573466162844"></a>delete_publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p2810113162844"><a name="p2810113162844"></a><a name="p2810113162844"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p26292563162844"><a name="p26292563162844"></a><a name="p26292563162844"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p49322874162844"><a name="p49322874162844"></a><a name="p49322874162844"></a>Specifies whether to delete the EIP bound to the ECS when deleting the ECS. If you do not want to delete the EIP, set this parameter to <strong id="b842352706184536"><a name="b842352706184536"></a><a name="b842352706184536"></a>false</strong>. Then, the system only unbinds the EIP from the ECS and reserves the EIP.</p>
    <a name="ul35729886162844"></a><a name="ul35729886162844"></a><ul id="ul35729886162844"><li><strong id="b842352706161021"><a name="b842352706161021"></a><a name="b842352706161021"></a>true</strong>: deletes the EIP bound to the ECS when deleting the ECS. </li><li><strong id="b27663993416118"><a name="b27663993416118"></a><a name="b27663993416118"></a>false</strong>: only unbinds the EIP bound to the ECS when deleting the ECS.</li></ul>
    </td>
    </tr>
    <tr id="row13588152792411"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2120131361912"><a name="p2120131361912"></a><a name="p2120131361912"></a>delete_volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p312016138190"><a name="p312016138190"></a><a name="p312016138190"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p4120111317191"><a name="p4120111317191"></a><a name="p4120111317191"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p108891816236"><a name="p108891816236"></a><a name="p108891816236"></a>Specifies whether to delete the data disks attached to the ECS when deleting the ECS. The value can be <strong id="b39009428140"><a name="b39009428140"></a><a name="b39009428140"></a>true</strong> or <strong id="b89011542181415"><a name="b89011542181415"></a><a name="b89011542181415"></a>false</strong>. The default value is <strong id="b14902114271412"><a name="b14902114271412"></a><a name="b14902114271412"></a>false</strong>.</p>
    <a name="ul0854204462211"></a><a name="ul0854204462211"></a><ul id="ul0854204462211"><li><strong id="b9824746131414"><a name="b9824746131414"></a><a name="b9824746131414"></a>true</strong>: deletes the data disks attached to the ECS when deleting the ECS. </li><li><strong id="b1079111614156"><a name="b1079111614156"></a><a name="b1079111614156"></a>false</strong>: only detaches the data disks attached to the ECS when deleting the ECS.</li></ul>
    </td>
    </tr>
    <tr id="row3123851094131"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2081174194134"><a name="p2081174194134"></a><a name="p2081174194134"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p802944294134"><a name="p802944294134"></a><a name="p802944294134"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p4640508094134"><a name="p4640508094134"></a><a name="p4640508094134"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p117281711175115"><a name="p117281711175115"></a><a name="p117281711175115"></a>Specifies the enterprise project ID, which is used to specify the enterprise project to which the AS group belongs.</p>
    <a name="ul381025535013"></a><a name="ul381025535013"></a><ul id="ul381025535013"><li>If the value is <strong id="b842352706111949"><a name="b842352706111949"></a><a name="b842352706111949"></a>0</strong> or left blank, the AS group belongs to the default enterprise project.</li><li>If the value is a UUID, the AS group belongs to the enterprise project corresponding to the UUID.</li></ul>
    <p id="p87281211175111"><a name="p87281211175111"></a><a name="p87281211175111"></a>If an enterprise project is configured for an AS group, ECSs created in this AS group also belong to this enterprise project. Otherwise, the default enterprise project will be used.</p>
    </td>
    </tr>
    <tr id="row6964412367"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1047921033619"><a name="p1047921033619"></a><a name="p1047921033619"></a>multi_az_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p18479171093618"><a name="p18479171093618"></a><a name="p18479171093618"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p144799109367"><a name="p144799109367"></a><a name="p144799109367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p647921019360"><a name="p647921019360"></a><a name="p647921019360"></a>Specifies the priority policy used to select target AZs when adjusting the number of instances in an AS group.</p>
    <a name="ul1847961013618"></a><a name="ul1847961013618"></a><ul id="ul1847961013618"><li><strong id="b1221764615315"><a name="b1221764615315"></a><a name="b1221764615315"></a>EQUILIBRIUM_DISTRIBUTE</strong> (default): When adjusting the number of instances, ensure that instances in each AZ in the <strong id="b1621812460536"><a name="b1621812460536"></a><a name="b1621812460536"></a>available_zones</strong> list is evenly distributed. If instances cannot be added in the target AZ, select another AZ based on the <strong id="b92181546185312"><a name="b92181546185312"></a><a name="b92181546185312"></a>PICK_FIRST</strong> policy.</li><li><strong id="b135661414155416"><a name="b135661414155416"></a><a name="b135661414155416"></a>PICK_FIRST</strong>: When adjusting the number of instances, target AZs are determined in the order in the <strong id="b456611425414"><a name="b456611425414"></a><a name="b456611425414"></a>available_zones</strong> list.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **lbaas\_listeners**  field description

    <a name="table62452402171652"></a>
    <table><thead align="left"><tr id="row45038761171652"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p24261034171652"><a name="p24261034171652"></a><a name="p24261034171652"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="p18986739171652"><a name="p18986739171652"></a><a name="p18986739171652"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p61530925171652"><a name="p61530925171652"></a><a name="p61530925171652"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p17949056171652"><a name="p17949056171652"></a><a name="p17949056171652"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55733269102632"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p17155857102634"><a name="p17155857102634"></a><a name="p17155857102634"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p47447185102634"><a name="p47447185102634"></a><a name="p47447185102634"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p18016757102634"><a name="p18016757102634"></a><a name="p18016757102634"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p50071206102634"><a name="p50071206102634"></a><a name="p50071206102634"></a>Specifies the backend ECS group ID.</p>
    <p id="p12237323102646"><a name="p12237323102646"></a><a name="p12237323102646"></a>The value of this parameter can be changed only when all the following conditions are met:</p>
    <a name="ul43027048102646"></a><a name="ul43027048102646"></a><ul id="ul43027048102646"><li>No scaling actions are triggered in the AS group.</li><li>The number of instances in the AS group is 0.</li><li>The AS group is not in service.</li></ul>
    </td>
    </tr>
    <tr id="row61114407171742"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p51319960171742"><a name="p51319960171742"></a><a name="p51319960171742"></a>protocol_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p63276134171742"><a name="p63276134171742"></a><a name="p63276134171742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p25093240171742"><a name="p25093240171742"></a><a name="p25093240171742"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p19286583171742"><a name="p19286583171742"></a><a name="p19286583171742"></a>Specifies the backend protocol ID, which is the port on which a backend ECS listens for traffic. The port ID ranges from 1 to 65535.</p>
    </td>
    </tr>
    <tr id="row36552334171745"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p7949116171745"><a name="p7949116171745"></a><a name="p7949116171745"></a>weight</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="p39898670171745"><a name="p39898670171745"></a><a name="p39898670171745"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p10566861171745"><a name="p10566861171745"></a><a name="p10566861171745"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p50609408171745"><a name="p50609408171745"></a><a name="p50609408171745"></a>Specifies the weight, which determines the portion of requests a backend ECS processes when being compared to other backend ECSs added to the same listener. The value of this parameter ranges from 0 to 100.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **networks**  field description

    <a name="taf38c137c80e494e9a0fa6191f5e9561"></a>
    <table><thead align="left"><tr id="en-us_topic_0043063023_r9061055fab7042ad84743683a2b5b98d"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="en-us_topic_0043063023_a679fce5df7a14f22afdcfabeadfa041d"><a name="en-us_topic_0043063023_a679fce5df7a14f22afdcfabeadfa041d"></a><a name="en-us_topic_0043063023_a679fce5df7a14f22afdcfabeadfa041d"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="en-us_topic_0043063023_p41814948203944"><a name="en-us_topic_0043063023_p41814948203944"></a><a name="en-us_topic_0043063023_p41814948203944"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0043063023_a2c0586869bf949e6af882694148874ed"><a name="en-us_topic_0043063023_a2c0586869bf949e6af882694148874ed"></a><a name="en-us_topic_0043063023_a2c0586869bf949e6af882694148874ed"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="en-us_topic_0043063023_a4774d878ba474479ad17a6d04d9c0b6e"><a name="en-us_topic_0043063023_a4774d878ba474479ad17a6d04d9c0b6e"></a><a name="en-us_topic_0043063023_a4774d878ba474479ad17a6d04d9c0b6e"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043063023_r801df159f0ca4d40b2c4abcd91800eee"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0043063023_af56439ac85cc4740ac47a13abbb60fba"><a name="en-us_topic_0043063023_af56439ac85cc4740ac47a13abbb60fba"></a><a name="en-us_topic_0043063023_af56439ac85cc4740ac47a13abbb60fba"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0043063023_p31567631203944"><a name="en-us_topic_0043063023_p31567631203944"></a><a name="en-us_topic_0043063023_p31567631203944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0043063023_ad129d99902cf4f55a062dafa6c161407"><a name="en-us_topic_0043063023_ad129d99902cf4f55a062dafa6c161407"></a><a name="en-us_topic_0043063023_ad129d99902cf4f55a062dafa6c161407"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0043063023_aba9652e07bf34af0a26c153ea5d73d9d"><a name="en-us_topic_0043063023_aba9652e07bf34af0a26c153ea5d73d9d"></a><a name="en-us_topic_0043063023_aba9652e07bf34af0a26c153ea5d73d9d"></a>Specifies the network ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **security\_groups**  field description

    <a name="tf7da6b502e2c44068fb6f36eddec74a1"></a>
    <table><thead align="left"><tr id="ra73f26b95ffa441598f51fb079dd0cdd"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="affa7f495ebd24391875fb1e296086cfe"><a name="affa7f495ebd24391875fb1e296086cfe"></a><a name="affa7f495ebd24391875fb1e296086cfe"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="a6d9ec4aea2004e81837d01097d8f403d"><a name="a6d9ec4aea2004e81837d01097d8f403d"></a><a name="a6d9ec4aea2004e81837d01097d8f403d"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="afab54c2dd65e49d494c4a7b5683e7503"><a name="afab54c2dd65e49d494c4a7b5683e7503"></a><a name="afab54c2dd65e49d494c4a7b5683e7503"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="a7930b80caa314af3a4740d413b14b4a9"><a name="a7930b80caa314af3a4740d413b14b4a9"></a><a name="a7930b80caa314af3a4740d413b14b4a9"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf36b86a995b84e1eb1f632bad05805c6"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="af92635b5e4f340c4ba09480ca7a06c26"><a name="af92635b5e4f340c4ba09480ca7a06c26"></a><a name="af92635b5e4f340c4ba09480ca7a06c26"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="a115a494962894e31a437b8d2f5a35648"><a name="a115a494962894e31a437b8d2f5a35648"></a><a name="a115a494962894e31a437b8d2f5a35648"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="aa71fee022c6345e893e3ac30d6e3b5c5"><a name="aa71fee022c6345e893e3ac30d6e3b5c5"></a><a name="aa71fee022c6345e893e3ac30d6e3b5c5"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="ad374c1abdfdf4b469feee15f54a8dd46"><a name="ad374c1abdfdf4b469feee15f54a8dd46"></a><a name="ad374c1abdfdf4b469feee15f54a8dd46"></a>Specifies the ID of the security group.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to change the name, AS configuration, expected number of instances, minimum number of instances, maximum number of instances, and cooldown period of the AS group with ID  **a8327883-6b07-4497-9c61-68d03ee193a1**.

    ```
    PUT https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group/a8327883-6b07-4497-9c61-68d03ee193a1
    
    {
        "scaling_group_name": "group_1",
        "scaling_configuration_id": "f8327883-6a07-4497-9a61-68c03e8e72a2",
        "enterprise_project_id": "c92b1a5d-6f20-43f2-b1b7-7ce35e58e413",
        "desire_instance_number": 1,
        "min_instance_number": 1,
        "max_instance_number": 3,
        "cool_down_time": 200,
        "multi_az_priority_policy": "PICK_FIRST"
    }
    ```


## Response Message<a name="section39585636"></a>

-   Response parameters

    **Table  6**  Response parameters

    <a name="table47120742"></a>
    <table><thead align="left"><tr id="row20687433"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p65069390"><a name="p65069390"></a><a name="p65069390"></a><strong id="b112624104382"><a name="b112624104382"></a><a name="b112624104382"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.2"><p id="p36129223"><a name="p36129223"></a><a name="p36129223"></a><strong id="b208624111385"><a name="b208624111385"></a><a name="b208624111385"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p40785949"><a name="p40785949"></a><a name="p40785949"></a><strong id="b19174147385"><a name="b19174147385"></a><a name="b19174147385"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15327543"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p33571453"><a name="p33571453"></a><a name="p33571453"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.2 "><p id="p34933209"><a name="p34933209"></a><a name="p34933209"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p11017648"><a name="p11017648"></a><a name="p11017648"></a>Specifies the AS group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "scaling_group_id": "a8327883-6b07-4497-9c61-68d03ee193a1"
    }
    ```


## Returned Values<a name="section20726409"></a>

-   Normal

    200

-   Abnormal

    <a name="table14252720"></a>
    <table><thead align="left"><tr id="row63718061"><th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.1"><p id="p60889336"><a name="p60889336"></a><a name="p60889336"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.2"><p id="p33089196"><a name="p33089196"></a><a name="p33089196"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62979183"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p1040236"><a name="p1040236"></a><a name="p1040236"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p17150281"><a name="p17150281"></a><a name="p17150281"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row20134803"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p20306340"><a name="p20306340"></a><a name="p20306340"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p34200809"><a name="p34200809"></a><a name="p34200809"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row39371826"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p35001377"><a name="p35001377"></a><a name="p35001377"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p16539321"><a name="p16539321"></a><a name="p16539321"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row14636163"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p44678570"><a name="p44678570"></a><a name="p44678570"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p62194446"><a name="p62194446"></a><a name="p62194446"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row22879106"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p41268299"><a name="p41268299"></a><a name="p41268299"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p54397957"><a name="p54397957"></a><a name="p54397957"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row19819572"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p61881498"><a name="p61881498"></a><a name="p61881498"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p46345412"><a name="p46345412"></a><a name="p46345412"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row14455526"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p30046962"><a name="p30046962"></a><a name="p30046962"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p17884854"><a name="p17884854"></a><a name="p17884854"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row26745965"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p18939577"><a name="p18939577"></a><a name="p18939577"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p57710802"><a name="p57710802"></a><a name="p57710802"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row49635175"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p61026205"><a name="p61026205"></a><a name="p61026205"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p44175572"><a name="p44175572"></a><a name="p44175572"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row62035831"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p58846418"><a name="p58846418"></a><a name="p58846418"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p1830529"><a name="p1830529"></a><a name="p1830529"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row16474764"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p59387477"><a name="p59387477"></a><a name="p59387477"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p45656294"><a name="p45656294"></a><a name="p45656294"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row8253465"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p64550954"><a name="p64550954"></a><a name="p64550954"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p61244824"><a name="p61244824"></a><a name="p61244824"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row14332509"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p20082593"><a name="p20082593"></a><a name="p20082593"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p16077300"><a name="p16077300"></a><a name="p16077300"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row10477980"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.1 "><p id="p43410060"><a name="p43410060"></a><a name="p43410060"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.2 "><p id="p26553952"><a name="p26553952"></a><a name="p26553952"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

