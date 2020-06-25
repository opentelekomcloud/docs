# Creating an AS Group<a name="EN-US_TOPIC_0043063023"></a>

## Function<a name="section21784493"></a>

An AS group consists of a collection of instances that apply to the same scenario. It is the basis for enabling or disabling AS policies and performing scaling actions. An AS group specifies parameters, such as the maximum number of instances, expected number of instances, minimum number of instances, VPC, subnet, and load balancing.

-   Each user can create a maximum of 25 AS groups by default.
-   If ELB is configured, AS automatically binds or unbinds a load balancer to or from an instance when the instance is added or removed from the AS group.
-   If an AS group uses ELB health check, the listening ports on the load balancers must be enabled for the instances in the AS group. Enable the listening ports in security groups. 

## URI<a name="section61842715"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_group

**Table  1**  Parameter description

<a name="table4718148"></a>
<table><thead align="left"><tr id="row62417507"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.1"><p id="p22653281"><a name="p22653281"></a><a name="p22653281"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.2"><p id="p22976439"><a name="p22976439"></a><a name="p22976439"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p49152270"><a name="p49152270"></a><a name="p49152270"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p21910925"><a name="p21910925"></a><a name="p21910925"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29954525"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.1 "><p id="p1221320251318"><a name="p1221320251318"></a><a name="p1221320251318"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p36889359"><a name="p36889359"></a><a name="p36889359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p35248064"><a name="p35248064"></a><a name="p35248064"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section19713524"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table147283118511"></a>
    <table><thead align="left"><tr id="row1971971119513"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.1"><p id="p271981175113"><a name="p271981175113"></a><a name="p271981175113"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.2"><p id="p3719161114518"><a name="p3719161114518"></a><a name="p3719161114518"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p1971971112515"><a name="p1971971112515"></a><a name="p1971971112515"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.554455445544555%" id="mcps1.2.5.1.4"><p id="p7719141125110"><a name="p7719141125110"></a><a name="p7719141125110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row572015117517"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1871951175116"><a name="p1871951175116"></a><a name="p1871951175116"></a>scaling_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p15719411165112"><a name="p15719411165112"></a><a name="p15719411165112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p1572019119513"><a name="p1572019119513"></a><a name="p1572019119513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p177201011155120"><a name="p177201011155120"></a><a name="p177201011155120"></a>Specifies the AS group name. The name contains only letters, digits, underscores (_), and hyphens (-), and cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row13720101125119"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p4720161114511"><a name="p4720161114511"></a><a name="p4720161114511"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p10720181195114"><a name="p10720181195114"></a><a name="p10720181195114"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p1172081115118"><a name="p1172081115118"></a><a name="p1172081115118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p1872071118516"><a name="p1872071118516"></a><a name="p1872071118516"></a>Specifies the AS configuration ID, which can be obtained using the API for querying AS configurations. For details, see <a href="querying-as-configurations.md">Querying AS Configurations</a>.</p>
    </td>
    </tr>
    <tr id="row157209117514"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1372051114519"><a name="p1372051114519"></a><a name="p1372051114519"></a>desire_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p17201711195118"><a name="p17201711195118"></a><a name="p17201711195118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p872061115113"><a name="p872061115113"></a><a name="p872061115113"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p1720191110516"><a name="p1720191110516"></a><a name="p1720191110516"></a>Specifies the expected number of instances. The default value is the minimum number of instances.</p>
    <p id="p18720611165111"><a name="p18720611165111"></a><a name="p18720611165111"></a>The value ranges from the minimum number of instances to the maximum number of instances.</p>
    </td>
    </tr>
    <tr id="row12721161115115"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1172012115510"><a name="p1172012115510"></a><a name="p1172012115510"></a>min_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p1720311195118"><a name="p1720311195118"></a><a name="p1720311195118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p117201111185113"><a name="p117201111185113"></a><a name="p117201111185113"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p107217119510"><a name="p107217119510"></a><a name="p107217119510"></a>Specifies the minimum number of instances. The default value is <strong id="b84235270612310"><a name="b84235270612310"></a><a name="b84235270612310"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row1572131135116"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p072118112512"><a name="p072118112512"></a><a name="p072118112512"></a>max_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p97211311115113"><a name="p97211311115113"></a><a name="p97211311115113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p147211911185114"><a name="p147211911185114"></a><a name="p147211911185114"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p372116118513"><a name="p372116118513"></a><a name="p372116118513"></a>Specifies the maximum number of instances. The default value is <strong id="b84235270612321"><a name="b84235270612321"></a><a name="b84235270612321"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row18721101135112"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p672111110515"><a name="p672111110515"></a><a name="p672111110515"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p167211411195114"><a name="p167211411195114"></a><a name="p167211411195114"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p47211011205118"><a name="p47211011205118"></a><a name="p47211011205118"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p14721131145111"><a name="p14721131145111"></a><a name="p14721131145111"></a>Specifies the cooldown period (in seconds). The value ranges from 0 to 86400 and is 300 by default.</p>
    <p id="p8060118"><a name="p8060118"></a><a name="p8060118"></a>After a scaling action is triggered, the system starts the cooldown period. During the cooldown period, scaling actions triggered by alarms will be denied. Scheduled, periodic, and manual scaling actions are not affected.</p>
    </td>
    </tr>
    <tr id="row672221111511"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p14721811105111"><a name="p14721811105111"></a><a name="p14721811105111"></a>lb_listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p37213119510"><a name="p37213119510"></a><a name="p37213119510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p3721611125116"><a name="p3721611125116"></a><a name="p3721611125116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p20895122411511"><a name="p20895122411511"></a><a name="p20895122411511"></a>Specifies the ID of a classic load balancer listener. The system supports the binding of up to six load balancer listeners, the IDs of which are separated using a comma (,). </p>
    <p id="p1560095562314"><a name="p1560095562314"></a><a name="p1560095562314"></a>This parameter is alternative to <strong id="b84235270610186"><a name="b84235270610186"></a><a name="b84235270610186"></a>lbaas_listeners</strong>.</p>
    </td>
    </tr>
    <tr id="row1872231185115"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p197228111512"><a name="p197228111512"></a><a name="p197228111512"></a>lbaas_listeners</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p19722611145120"><a name="p19722611145120"></a><a name="p19722611145120"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p1393644073714"><a name="p1393644073714"></a><a name="p1393644073714"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p172210118517"><a name="p172210118517"></a><a name="p172210118517"></a>Specifies information about an enhanced load balancer. The system supports the binding of up to six load balancers. This parameter is in list data structure. For details, see <a href="#table154023755417">Table 3</a>. </p>
    <p id="p1772211115117"><a name="p1772211115117"></a><a name="p1772211115117"></a>This parameter is alternative to <strong id="b1120902053"><a name="b1120902053"></a><a name="b1120902053"></a>lb_listener_id</strong>.</p>
    </td>
    </tr>
    <tr id="row16722211115118"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p57221411125116"><a name="p57221411125116"></a><a name="p57221411125116"></a>available_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p67221511135117"><a name="p67221511135117"></a><a name="p67221511135117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p117221011175115"><a name="p117221011175115"></a><a name="p117221011175115"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p3722181114516"><a name="p3722181114516"></a><a name="p3722181114516"></a>Specifies the AZ information. The ECS associated with a scaling action will be created in a specified AZ. If you do not specify an AZ, the system automatically specifies one. For details, see <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Availability Zone</a>.</p>
    </td>
    </tr>
    <tr id="row972281135114"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p87221811195114"><a name="p87221811195114"></a><a name="p87221811195114"></a>networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p1446924373712"><a name="p1446924373712"></a><a name="p1446924373712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p347824310372"><a name="p347824310372"></a><a name="p347824310372"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p87221511205113"><a name="p87221511205113"></a><a name="p87221511205113"></a>Specifies network information. The system supports up to five subnets. The first subnet transferred serves as the primary NIC of the ECS by default.  This parameter is in data structure. For details, see <a href="#table16283330203725">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row972231195110"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p272271125110"><a name="p272271125110"></a><a name="p272271125110"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p872212119515"><a name="p872212119515"></a><a name="p872212119515"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p5722151135117"><a name="p5722151135117"></a><a name="p5722151135117"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p1272251135116"><a name="p1272251135116"></a><a name="p1272251135116"></a>Specifies the security group. A maximum of one security group can be selected.  This parameter is in data structure. For details, see <a href="#table25481545203427">Table 5</a>.</p>
    <p id="p17221511155111"><a name="p17221511155111"></a><a name="p17221511155111"></a>If the security group is specified both in the AS configuration and AS group, the security group specified in the AS configuration prevails. If the security group is not specified in either of them, the default security group is used. For your convenience, you are advised to specify the security group in the AS configuration.</p>
    </td>
    </tr>
    <tr id="row77231111185119"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p177221911175110"><a name="p177221911175110"></a><a name="p177221911175110"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p2722511175113"><a name="p2722511175113"></a><a name="p2722511175113"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p157231611125114"><a name="p157231611125114"></a><a name="p157231611125114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p1723811115118"><a name="p1723811115118"></a><a name="p1723811115118"></a>Specifies the VPC ID, which can be obtained using the API for querying VPCs. For details, see "Querying VPCs" in <em id="i7422111614"><a name="i7422111614"></a><a name="i7422111614"></a>Virtual Private Network API Reference</em>.</p>
    </td>
    </tr>
    <tr id="row15723111165117"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p772361185111"><a name="p772361185111"></a><a name="p772361185111"></a>health_periodic_audit_method</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p7723181111516"><a name="p7723181111516"></a><a name="p7723181111516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p472391175111"><a name="p472391175111"></a><a name="p472391175111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p672313117518"><a name="p672313117518"></a><a name="p672313117518"></a>Specifies the health check method for instances in the AS group. The health check methods include <strong id="b582845796161238"><a name="b582845796161238"></a><a name="b582845796161238"></a>ELB_AUDIT</strong> and <strong id="b1838261513161238"><a name="b1838261513161238"></a><a name="b1838261513161238"></a>NOVA_AUDIT</strong>. When load balancing is configured for an AS group, the default value is <strong id="b54238969164029"><a name="b54238969164029"></a><a name="b54238969164029"></a>ELB_AUDIT</strong>. Otherwise, the default value is <strong id="b909103728164036"><a name="b909103728164036"></a><a name="b909103728164036"></a>NOVA_AUDIT</strong>.</p>
    <a name="ul27231211175112"></a><a name="ul27231211175112"></a><ul id="ul27231211175112"><li><strong id="b622874993161245"><a name="b622874993161245"></a><a name="b622874993161245"></a>ELB_AUDIT</strong>: indicates the ELB health check, which takes effect in an AS group with a listener.</li><li><strong id="b842352706154542"><a name="b842352706154542"></a><a name="b842352706154542"></a>NOVA_AUDIT</strong>: indicates the ECS health check, which is the health check method delivered with AS.</li></ul>
    </td>
    </tr>
    <tr id="row5724311175118"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p1072314114512"><a name="p1072314114512"></a><a name="p1072314114512"></a>health_periodic_audit_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p13724171120513"><a name="p13724171120513"></a><a name="p13724171120513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p14724111135119"><a name="p14724111135119"></a><a name="p14724111135119"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p187241111205115"><a name="p187241111205115"></a><a name="p187241111205115"></a>Specifies the instance health check period. The value can be <strong id="b93456224220"><a name="b93456224220"></a><a name="b93456224220"></a>1</strong>, <strong id="b83541247429"><a name="b83541247429"></a><a name="b83541247429"></a>5</strong>, <strong id="b142305794212"><a name="b142305794212"></a><a name="b142305794212"></a>15</strong>, <strong id="b3558111154213"><a name="b3558111154213"></a><a name="b3558111154213"></a>60</strong>, or <strong id="b22555162429"><a name="b22555162429"></a><a name="b22555162429"></a>180</strong> in the unit of minutes. If this parameter is not specified, the default value is <strong id="b1088514499417"><a name="b1088514499417"></a><a name="b1088514499417"></a>5</strong>.</p>
    <p id="p157241911135110"><a name="p157241911135110"></a><a name="p157241911135110"></a>If the value is set to <strong id="b78041444104211"><a name="b78041444104211"></a><a name="b78041444104211"></a>0</strong>, health check is performed every 10 seconds.</p>
    </td>
    </tr>
    <tr id="row13726191118514"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p19724611205116"><a name="p19724611205116"></a><a name="p19724611205116"></a>health_periodic_audit_grace_period</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p8724181105110"><a name="p8724181105110"></a><a name="p8724181105110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p17241711185115"><a name="p17241711185115"></a><a name="p17241711185115"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p20726151117518"><a name="p20726151117518"></a><a name="p20726151117518"></a>Specifies the grace period for instance health check. The unit is second and value range is 0-86400. The default value is <strong id="b842352706154816"><a name="b842352706154816"></a><a name="b842352706154816"></a>600</strong>.</p>
    <p id="p4726511155112"><a name="p4726511155112"></a><a name="p4726511155112"></a>The health check grace period starts after an instance is added to an AS group and is enabled. The AS group will start checking the instance status only after the grace period ends.</p>
    <p id="p9726131185116"><a name="p9726131185116"></a><a name="p9726131185116"></a>This parameter is valid only when the instance health check method of the AS group is <strong id="b842352706155131"><a name="b842352706155131"></a><a name="b842352706155131"></a>ELB_AUDIT</strong>.</p>
    </td>
    </tr>
    <tr id="row3726411195112"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p10726161195118"><a name="p10726161195118"></a><a name="p10726161195118"></a>instance_terminate_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p7726111175114"><a name="p7726111175114"></a><a name="p7726111175114"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p672601119519"><a name="p672601119519"></a><a name="p672601119519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p1472612119514"><a name="p1472612119514"></a><a name="p1472612119514"></a>Specifies the instance removal policy.</p>
    <a name="ul137261112513"></a><a name="ul137261112513"></a><ul id="ul137261112513"><li><strong id="b34422810171421"><a name="b34422810171421"></a><a name="b34422810171421"></a>OLD_CONFIG_OLD_INSTANCE</strong> (default): The earlier-created instances based on the earlier-created AS configurations are removed first.</li><li><strong id="b50659714162554"><a name="b50659714162554"></a><a name="b50659714162554"></a>OLD_CONFIG_NEW_INSTANCE</strong>: The later-created instances based on the earlier-created AS configurations are removed first.</li><li><strong id="b4987808161754"><a name="b4987808161754"></a><a name="b4987808161754"></a>OLD_INSTANCE</strong>: The earlier-created instances are removed first.</li><li><strong id="b3854286164722"><a name="b3854286164722"></a><a name="b3854286164722"></a>NEW_INSTANCE</strong>: The later-created instances are removed first.</li></ul>
    </td>
    </tr>
    <tr id="row19727511155112"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p11726101115511"><a name="p11726101115511"></a><a name="p11726101115511"></a>notifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p8726181165110"><a name="p8726181165110"></a><a name="p8726181165110"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p147271311155118"><a name="p147271311155118"></a><a name="p147271311155118"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p3727181125117"><a name="p3727181125117"></a><a name="p3727181125117"></a>Specifies the notification mode.</p>
    <p id="p7727611125118"><a name="p7727611125118"></a><a name="p7727611125118"></a><strong id="b27819784164749"><a name="b27819784164749"></a><a name="b27819784164749"></a>EMAIL</strong> refers to notification by email.</p>
    </td>
    </tr>
    <tr id="row272741165118"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p167274119512"><a name="p167274119512"></a><a name="p167274119512"></a>delete_publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p5727131117518"><a name="p5727131117518"></a><a name="p5727131117518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p5727111119516"><a name="p5727111119516"></a><a name="p5727111119516"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><div class="p" id="p1063119062315"><a name="p1063119062315"></a><a name="p1063119062315"></a>Specifies whether to delete the EIP bound to the ECS when deleting the ECS. The value can be <strong id="b842352706184734"><a name="b842352706184734"></a><a name="b842352706184734"></a>true</strong> or <strong id="b842352706184738"><a name="b842352706184738"></a><a name="b842352706184738"></a>false</strong>. The default value is <strong id="b842352706184742"><a name="b842352706184742"></a><a name="b842352706184742"></a>false</strong>.<a name="ul4934185211225"></a><a name="ul4934185211225"></a><ul id="ul4934185211225"><li><strong id="b842352706161021"><a name="b842352706161021"></a><a name="b842352706161021"></a>true</strong>: deletes the EIP bound to the ECS when deleting the ECS. </li><li><strong id="b581811527596"><a name="b581811527596"></a><a name="b581811527596"></a>false</strong>: only unbinds the EIP bound to the ECS when deleting the ECS.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1920147191919"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p2120131361912"><a name="p2120131361912"></a><a name="p2120131361912"></a>delete_volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p312016138190"><a name="p312016138190"></a><a name="p312016138190"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p4120111317191"><a name="p4120111317191"></a><a name="p4120111317191"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><div class="p" id="p108891816236"><a name="p108891816236"></a><a name="p108891816236"></a>Specifies whether to delete the data disks attached to the ECS when deleting the ECS. The value can be <strong id="b301331329"><a name="b301331329"></a><a name="b301331329"></a>true</strong> or <strong id="b811135525"><a name="b811135525"></a><a name="b811135525"></a>false</strong>. The default value is <strong id="b798195437"><a name="b798195437"></a><a name="b798195437"></a>false</strong>.<a name="ul0854204462211"></a><a name="ul0854204462211"></a><ul id="ul0854204462211"><li><strong id="b2077369061"><a name="b2077369061"></a><a name="b2077369061"></a>true</strong>: deletes the data disks attached to the ECS when deleting the ECS. </li><li><strong id="b14499165285311"><a name="b14499165285311"></a><a name="b14499165285311"></a>false</strong>: only detaches the data disks attached to the ECS when deleting the ECS.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row18728211195118"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p13727171115114"><a name="p13727171115114"></a><a name="p13727171115114"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p8727121120518"><a name="p8727121120518"></a><a name="p8727121120518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p10727111195110"><a name="p10727111195110"></a><a name="p10727111195110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p117281711175115"><a name="p117281711175115"></a><a name="p117281711175115"></a>Specifies the enterprise project ID, which is used to specify the enterprise project to which the AS group belongs.</p>
    <a name="ul381025535013"></a><a name="ul381025535013"></a><ul id="ul381025535013"><li>If the value is <strong id="b842352706111949"><a name="b842352706111949"></a><a name="b842352706111949"></a>0</strong> or left blank, the AS group belongs to the default enterprise project.</li><li>If the value is a UUID, the AS group belongs to the enterprise project corresponding to the UUID.</li></ul>
    <p id="p87281211175111"><a name="p87281211175111"></a><a name="p87281211175111"></a>If an enterprise project is configured for an AS group, ECSs created in this AS group also belong to this enterprise project. Otherwise, the default enterprise project will be used.</p>
    </td>
    </tr>
    <tr id="row54865725419"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.1 "><p id="p249115717542"><a name="p249115717542"></a><a name="p249115717542"></a>multi_az_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.2 "><p id="p13511912195520"><a name="p13511912195520"></a><a name="p13511912195520"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p1551121275510"><a name="p1551121275510"></a><a name="p1551121275510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.554455445544555%" headers="mcps1.2.5.1.4 "><p id="p25111112195515"><a name="p25111112195515"></a><a name="p25111112195515"></a>Specifies the priority policy used to select target AZs when adjusting the number of instances in an AS group.</p>
    <a name="ul0511201275510"></a><a name="ul0511201275510"></a><ul id="ul0511201275510"><li><strong id="b1679111149568"><a name="b1679111149568"></a><a name="b1679111149568"></a>EQUILIBRIUM_DISTRIBUTE</strong> (default): When adjusting the number of instances, ensure that instances in each AZ in the <strong id="b8719121212126"><a name="b8719121212126"></a><a name="b8719121212126"></a>available_zones</strong> list is evenly distributed. If instances cannot be added in the target AZ, select another AZ based on the <strong id="b10812013151319"><a name="b10812013151319"></a><a name="b10812013151319"></a>PICK_FIRST</strong> policy.</li><li><strong id="b695074451311"><a name="b695074451311"></a><a name="b695074451311"></a>PICK_FIRST</strong>: When adjusting the number of instances, target AZs are determined in the order in the <strong id="b9352143919184"><a name="b9352143919184"></a><a name="b9352143919184"></a>available_zones</strong> list.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **lbaas\_listeners**  field description

    <a name="table154023755417"></a>
    <table><thead align="left"><tr id="row174011876548"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p164014710549"><a name="p164014710549"></a><a name="p164014710549"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.2"><p id="p7401577544"><a name="p7401577544"></a><a name="p7401577544"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p104016716548"><a name="p104016716548"></a><a name="p104016716548"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p174015735419"><a name="p174015735419"></a><a name="p174015735419"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row164021277541"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p34019719547"><a name="p34019719547"></a><a name="p34019719547"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p8401167115418"><a name="p8401167115418"></a><a name="p8401167115418"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p18402107195416"><a name="p18402107195416"></a><a name="p18402107195416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p64020713547"><a name="p64020713547"></a><a name="p64020713547"></a>Specifies the backend ECS group ID.</p>
    </td>
    </tr>
    <tr id="row1340215715415"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p19402777542"><a name="p19402777542"></a><a name="p19402777542"></a>protocol_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p740297195419"><a name="p740297195419"></a><a name="p740297195419"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p04022078549"><a name="p04022078549"></a><a name="p04022078549"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p114021472547"><a name="p114021472547"></a><a name="p114021472547"></a>Specifies the backend protocol ID, which is the port on which a backend ECS listens for traffic. The port ID ranges from 1 to 65535.</p>
    </td>
    </tr>
    <tr id="row124029745419"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p14023716543"><a name="p14023716543"></a><a name="p14023716543"></a>weight</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p134021778545"><a name="p134021778545"></a><a name="p134021778545"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p1940213711546"><a name="p1940213711546"></a><a name="p1940213711546"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p34021974545"><a name="p34021974545"></a><a name="p34021974545"></a>Specifies the weight, which determines the portion of requests a backend ECS processes when being compared to other backend ECSs added to the same listener. The value of this parameter ranges from 0 to 100. The default value is <strong id="b8423527061634"><a name="b8423527061634"></a><a name="b8423527061634"></a>1</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **networks**  field description

    <a name="table16283330203725"></a>
    <table><thead align="left"><tr id="r9061055fab7042ad84743683a2b5b98d"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="a679fce5df7a14f22afdcfabeadfa041d"><a name="a679fce5df7a14f22afdcfabeadfa041d"></a><a name="a679fce5df7a14f22afdcfabeadfa041d"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p41814948203944"><a name="p41814948203944"></a><a name="p41814948203944"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="a2c0586869bf949e6af882694148874ed"><a name="a2c0586869bf949e6af882694148874ed"></a><a name="a2c0586869bf949e6af882694148874ed"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="a4774d878ba474479ad17a6d04d9c0b6e"><a name="a4774d878ba474479ad17a6d04d9c0b6e"></a><a name="a4774d878ba474479ad17a6d04d9c0b6e"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r801df159f0ca4d40b2c4abcd91800eee"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="af56439ac85cc4740ac47a13abbb60fba"><a name="af56439ac85cc4740ac47a13abbb60fba"></a><a name="af56439ac85cc4740ac47a13abbb60fba"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p31567631203944"><a name="p31567631203944"></a><a name="p31567631203944"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ad129d99902cf4f55a062dafa6c161407"><a name="ad129d99902cf4f55a062dafa6c161407"></a><a name="ad129d99902cf4f55a062dafa6c161407"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="aba9652e07bf34af0a26c153ea5d73d9d"><a name="aba9652e07bf34af0a26c153ea5d73d9d"></a><a name="aba9652e07bf34af0a26c153ea5d73d9d"></a>Specifies the network ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **security\_groups**  field description

    <a name="table25481545203427"></a>
    <table><thead align="left"><tr id="r0cd4feaf0dd34dbea5d88f1e2b5e52de"><th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.1"><p id="adb89aff830c241f1a8ba24a05025ec7d"><a name="adb89aff830c241f1a8ba24a05025ec7d"></a><a name="adb89aff830c241f1a8ba24a05025ec7d"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.588235294117645%" id="mcps1.2.5.1.2"><p id="p62623656203950"><a name="p62623656203950"></a><a name="p62623656203950"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.686274509803921%" id="mcps1.2.5.1.3"><p id="a5a70f90bbb614578b2e69d51730603b8"><a name="a5a70f90bbb614578b2e69d51730603b8"></a><a name="a5a70f90bbb614578b2e69d51730603b8"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.11764705882353%" id="mcps1.2.5.1.4"><p id="a984b04e2931047e2ab76977321772cc5"><a name="a984b04e2931047e2ab76977321772cc5"></a><a name="a984b04e2931047e2ab76977321772cc5"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd4f0b565f1b44c55a666b8609ebaf71a"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="a333dfdd572ba4d87b073ffdf4f5fa7c3"><a name="a333dfdd572ba4d87b073ffdf4f5fa7c3"></a><a name="a333dfdd572ba4d87b073ffdf4f5fa7c3"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.588235294117645%" headers="mcps1.2.5.1.2 "><p id="p39351407203950"><a name="p39351407203950"></a><a name="p39351407203950"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.686274509803921%" headers="mcps1.2.5.1.3 "><p id="a59b78bb0a82c4f1c897a4180831bc790"><a name="a59b78bb0a82c4f1c897a4180831bc790"></a><a name="a59b78bb0a82c4f1c897a4180831bc790"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.11764705882353%" headers="mcps1.2.5.1.4 "><p id="a36b8ec84f3b34629ae6133fec28f88fd"><a name="a36b8ec84f3b34629ae6133fec28f88fd"></a><a name="a36b8ec84f3b34629ae6133fec28f88fd"></a>Specifies the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    The following example shows how to create an AS group:

    -   The AS group is named  **GroupNameTest**.
    -   The AS configuration ID is  **47683a91-93ee-462a-a7d7-484c006f4440**.
    -   The VPC ID is  **a8327883-6b07-4497-9c61-68d03ee193a**, and the network ID is  **3cd35bca-5a10-416f-8994-f79169559870**.
    -   The maximum number of instances is  **10**, the expected number of instances is  **0**, and the minimum number of instances is  **0**.
    -   The health check method is  **ECS health check**.
    -   When adjusting the number of instances, select target AZ based on the PICK FIRST policy.

    The request example is as follows:

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group
    
    {
        "scaling_group_name": "GroupNameTest",
        "scaling_configuration_id": "47683a91-93ee-462a-a7d7-484c006f4440",
        "desire_instance_number": 0,
        "min_instance_number": 0,
        "max_instance_number": 10,
        "health_periodic_audit_method": "NOVA_AUDIT",
        "vpc_id": "a8327883-6b07-4497-9c61-68d03ee193a",
        "available_zones": ["XXXa","XXXb"],
        "networks": [
            {
                "id": "3cd35bca-5a10-416f-8994-f79169559870"
            }
        ],
    
        "enterprise_project_id": "c92b1a5d-6f20-43f2-b1b7-7ce35e58e413",
        "multi_az_priority_policy": "PICK_FIRST"
    }
    ```


## Response Message<a name="section53291640"></a>

-   Response parameters

    **Table  6**  Response parameter

    <a name="table187606212210"></a>
    <table><thead align="left"><tr id="row07608232110"><th class="cellrowborder" valign="top" width="23.07%" id="mcps1.2.4.1.1"><p id="p107601628217"><a name="p107601628217"></a><a name="p107601628217"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.04%" id="mcps1.2.4.1.2"><p id="p15760102102117"><a name="p15760102102117"></a><a name="p15760102102117"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.88999999999999%" id="mcps1.2.4.1.3"><p id="p1976062152119"><a name="p1976062152119"></a><a name="p1976062152119"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row076013214211"><td class="cellrowborder" valign="top" width="23.07%" headers="mcps1.2.4.1.1 "><p id="p107601025216"><a name="p107601025216"></a><a name="p107601025216"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.04%" headers="mcps1.2.4.1.2 "><p id="p11760192132118"><a name="p11760192132118"></a><a name="p11760192132118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p276032192116"><a name="p276032192116"></a><a name="p276032192116"></a>Specifies the AS group ID.</p>
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


## Returned Values<a name="section9862716"></a>

-   Normal

    200

-   Abnormal

    <a name="table50474807"></a>
    <table><thead align="left"><tr id="row48020839"><th class="cellrowborder" valign="top" width="32.33%" id="mcps1.1.3.1.1"><p id="p64482741"><a name="p64482741"></a><a name="p64482741"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="67.67%" id="mcps1.1.3.1.2"><p id="p55719536"><a name="p55719536"></a><a name="p55719536"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16988543"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p33894731"><a name="p33894731"></a><a name="p33894731"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p61118651"><a name="p61118651"></a><a name="p61118651"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row13196948"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p62319862"><a name="p62319862"></a><a name="p62319862"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p14744048"><a name="p14744048"></a><a name="p14744048"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row65587574"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p10993288"><a name="p10993288"></a><a name="p10993288"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p18041159"><a name="p18041159"></a><a name="p18041159"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row28152706"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p65776751"><a name="p65776751"></a><a name="p65776751"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p26316604"><a name="p26316604"></a><a name="p26316604"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row35522846"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p58778271"><a name="p58778271"></a><a name="p58778271"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p63419476"><a name="p63419476"></a><a name="p63419476"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row33904373"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p61899732"><a name="p61899732"></a><a name="p61899732"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p47822428"><a name="p47822428"></a><a name="p47822428"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row27748670"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p33049813"><a name="p33049813"></a><a name="p33049813"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p59789225"><a name="p59789225"></a><a name="p59789225"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1232117"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p32692654"><a name="p32692654"></a><a name="p32692654"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p30859352"><a name="p30859352"></a><a name="p30859352"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row9298719"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p14998773"><a name="p14998773"></a><a name="p14998773"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p6941071"><a name="p6941071"></a><a name="p6941071"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row62469641"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p26876165"><a name="p26876165"></a><a name="p26876165"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p29485753"><a name="p29485753"></a><a name="p29485753"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row64045192"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p20278084"><a name="p20278084"></a><a name="p20278084"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p31912141"><a name="p31912141"></a><a name="p31912141"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row18773818"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p44284256"><a name="p44284256"></a><a name="p44284256"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p30254983"><a name="p30254983"></a><a name="p30254983"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row3859394"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p44175501"><a name="p44175501"></a><a name="p44175501"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p21445804"><a name="p21445804"></a><a name="p21445804"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row58794511"><td class="cellrowborder" valign="top" width="32.33%" headers="mcps1.1.3.1.1 "><p id="p64734920"><a name="p64734920"></a><a name="p64734920"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.67%" headers="mcps1.1.3.1.2 "><p id="p9037129"><a name="p9037129"></a><a name="p9037129"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).

