# Creating an AS Group Quickly<a name="EN-US_TOPIC_0042018359"></a>

If you use AS for the first time, it is recommended that you follow the wizard-based process to create an AS group, AS configuration, and AS policy.

## Prerequisites<a name="section20344593"></a>

-   You have created the required VPCs, subnets, security groups, and load balancers.
-   You have obtained the keys for logging in to the instances added by a scaling action.

## Procedure<a name="section48883615"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click  **Create AS Group**.
5.  Set basic information about the AS group, such as  **Name**,  **Max. Instances**,  **Min. Instances**, and  **Expected Instances**.  [Table 1](#table2153361016143)  lists the parameters.

    **Table  1**  AS group parameters

    <a name="table2153361016143"></a>
    <table><thead align="left"><tr id="row18270305"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p3499754"><a name="p3499754"></a><a name="p3499754"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.2"><p id="p15044627"><a name="p15044627"></a><a name="p15044627"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.3"><p id="p10655236"><a name="p10655236"></a><a name="p10655236"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5184165310418"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p51849531448"><a name="p51849531448"></a><a name="p51849531448"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p17184175316413"><a name="p17184175316413"></a><a name="p17184175316413"></a>A region is where an AS group resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p12184135316415"><a name="p12184135316415"></a><a name="p12184135316415"></a>N/A</p>
    </td>
    </tr>
    <tr id="row19614145145315"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1261415516531"><a name="p1261415516531"></a><a name="p1261415516531"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p10805969403"><a name="p10805969403"></a><a name="p10805969403"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.</p>
    <p id="p116651349185417"><a name="p116651349185417"></a><a name="p116651349185417"></a>To enhance application availability, the system evenly distributes your instances between AZs if multiple AZs have been selected.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p961495112536"><a name="p961495112536"></a><a name="p961495112536"></a>N/A</p>
    </td>
    </tr>
    <tr id="row54028730202125"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p14251001202125"><a name="p14251001202125"></a><a name="p14251001202125"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p13480457202125"><a name="p13480457202125"></a><a name="p13480457202125"></a>Specifies the name of the AS group to be created.</p>
    <p id="p28009099142054"><a name="p28009099142054"></a><a name="p28009099142054"></a>The name contains 1 to 64 characters and consists of only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p18175250202125"><a name="p18175250202125"></a><a name="p18175250202125"></a>N/A</p>
    </td>
    </tr>
    <tr id="row57767782"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p48678752"><a name="p48678752"></a><a name="p48678752"></a>Max. Instances or Min. Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p50664859"><a name="p50664859"></a><a name="p50664859"></a>Specifies the maximum or minimum number of ECSs in an AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p10212927"><a name="p10212927"></a><a name="p10212927"></a>10 or 5</p>
    </td>
    </tr>
    <tr id="row24807479"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p63248778"><a name="p63248778"></a><a name="p63248778"></a>Expected Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p22877402"><a name="p22877402"></a><a name="p22877402"></a>Specifies the expected number of ECSs in an AS group.</p>
    <p id="p4570028"><a name="p4570028"></a><a name="p4570028"></a>After an AS group is created, you can change this value, which will trigger a scaling action.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p34627969"><a name="p34627969"></a><a name="p34627969"></a>6</p>
    </td>
    </tr>
    <tr id="row16313497"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p46324881"><a name="p46324881"></a><a name="p46324881"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p61327894"><a name="p61327894"></a><a name="p61327894"></a>Provides a network for your ECSs.</p>
    <p id="p15080136"><a name="p15080136"></a><a name="p15080136"></a>All ECSs in an AS group belong to the same VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p13531531"><a name="p13531531"></a><a name="p13531531"></a>N/A</p>
    </td>
    </tr>
    <tr id="row9914165244816"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p8914125264813"><a name="p8914125264813"></a><a name="p8914125264813"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p1404647118"><a name="p1404647118"></a><a name="p1404647118"></a>You can select a maximum of five subnets. The AS group automatically binds all NICs to the created ECSs. The first subnet is used by the primary NIC of the ECS by default, and other subnets are used by extension NICs of the ECS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p11915352104810"><a name="p11915352104810"></a><a name="p11915352104810"></a>N/A</p>
    </td>
    </tr>
    <tr id="row6128980"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p102720515599"><a name="p102720515599"></a><a name="p102720515599"></a>Load Balancing</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p1609475215599"><a name="p1609475215599"></a><a name="p1609475215599"></a>This parameter is optional. A load balancer automatically distributes access traffic to all instances in an AS group to balance their service load. It enables higher levels of fault tolerance in your applications and expands application service capabilities.</p>
    <div class="note" id="note1063504415599"><a name="note1063504415599"></a><a name="note1063504415599"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1817818563313"></a><a name="ul1817818563313"></a><ul id="ul1817818563313"><li class="textintable">Up to three load balancers can be added to an AS group.</li><li class="textintable">After multiple load balancers are added to an AS group, multiple services can be concurrently listened to, thereby improving service scalability. If <strong id="b1781123361216"><a name="b1781123361216"></a><a name="b1781123361216"></a>ELB health check</strong> is selected for <strong id="b2781233161216"><a name="b2781233161216"></a><a name="b2781233161216"></a>Health Check Method</strong>, when any one of the listeners detects that an instance becomes faulty, AS will replace the faulty instance with a functional one.</li></ul>
    </div></div>
    <p id="p3542840015599"><a name="p3542840015599"></a><a name="p3542840015599"></a>If you select <strong id="b1069545173117"><a name="b1069545173117"></a><a name="b1069545173117"></a>Classic load balancer</strong>, configure the following parameters:</p>
    <a name="ul4982997994510"></a><a name="ul4982997994510"></a><ul id="ul4982997994510"><li><strong id="b8423527061090"><a name="b8423527061090"></a><a name="b8423527061090"></a>Load Balancer</strong></li><li><strong id="b8423527061093"><a name="b8423527061093"></a><a name="b8423527061093"></a>Listener</strong></li></ul>
    <div class="p" id="p23417149454"><a name="p23417149454"></a><a name="p23417149454"></a>If you select <strong id="b10687551124510"><a name="b10687551124510"></a><a name="b10687551124510"></a>Enhanced load balancer</strong>, configure the following parameters:<a name="ul1865661654415"></a><a name="ul1865661654415"></a><ul id="ul1865661654415"><li><strong id="b324122138"><a name="b324122138"></a><a name="b324122138"></a>Load Balancer</strong></li><li><strong id="b842352706194411"><a name="b842352706194411"></a><a name="b842352706194411"></a>Backend ECS Group</strong></li></ul>
    <a name="ul16565169449"></a><a name="ul16565169449"></a><ul id="ul16565169449"><li><strong id="b84235270610935"><a name="b84235270610935"></a><a name="b84235270610935"></a>Backend Port</strong>: specifies the port on which a backend ECS listens for traffic.</li><li><strong id="b842352706101430"><a name="b842352706101430"></a><a name="b842352706101430"></a>Weight</strong>: determines the portion of requests a backend ECS processes compared to other backend ECSs added to the same listener.<p id="p5656316104419"><a name="p5656316104419"></a><a name="p5656316104419"></a>For more information about load balancing, see <em id="i84235269719113"><a name="i84235269719113"></a><a name="i84235269719113"></a>Elastic Load Balancing User Guide</em><em id="i189657412275"><a name="i189657412275"></a><a name="i189657412275"></a></em><em id="i8599108122716"><a name="i8599108122716"></a><a name="i8599108122716"></a></em>.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p40893240"><a name="p40893240"></a><a name="p40893240"></a>N/A</p>
    </td>
    </tr>
    <tr id="row32922880"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p49507636"><a name="p49507636"></a><a name="p49507636"></a>Health Check Method</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p2129537693230"><a name="p2129537693230"></a><a name="p2129537693230"></a>When a health check detects a faulty ECS, AS removes the faulty ECS from the AS group and adds a new one. The health check is implemented using any of the following methods:</p>
    <a name="ul50695543"></a><a name="ul50695543"></a><ul id="ul50695543"><li><strong id="b8423527069724"><a name="b8423527069724"></a><a name="b8423527069724"></a>ECS health check</strong>: checks ECS running status. If an ECS is stopped or deleted, it is considered as abnormal. This method is selected by default. Using this method, the AS group periodically determines the running status of each ECS based on the health check result. If the health check result shows that an ECS is faulty, AS removes the ECS from the AS group.</li><li><strong id="b162239179229"><a name="b162239179229"></a><a name="b162239179229"></a>ELB health check</strong>: determines ECS running status using a load balancing listener. This health check method is available only when the AS group uses a load balancing listener. When a load balancing listener detects that an ECS is faulty, AS removes the ECS from the AS group.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p31815862"><a name="p31815862"></a><a name="p31815862"></a>N/A</p>
    </td>
    </tr>
    <tr id="row17907308"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p41205809"><a name="p41205809"></a><a name="p41205809"></a>Health Check Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p49336210"><a name="p49336210"></a><a name="p49336210"></a>Specifies the health check period for an AS group. You can set a proper health check interval, such as 10 seconds, 1 minute, 5 minutes, 15 minutes, 1 hour, and 3 hours based on the site requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p36810105"><a name="p36810105"></a><a name="p36810105"></a>5 minutes</p>
    </td>
    </tr>
    <tr id="row8530240449"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2329205817411"><a name="p2329205817411"></a><a name="p2329205817411"></a>Health Check Grace Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p7668329374"><a name="p7668329374"></a><a name="p7668329374"></a>Specifies the grace period for instance health check. The unit is second and value range is 0 to 86400. The default value is <strong id="b842352706193228"><a name="b842352706193228"></a><a name="b842352706193228"></a>600</strong>.</p>
    <p id="p14340158248"><a name="p14340158248"></a><a name="p14340158248"></a>The health check grace period starts after an instance is added to an AS group and enabled. The AS group will start checking status of the instance only after the grace period ends.</p>
    <p id="p15344155815417"><a name="p15344155815417"></a><a name="p15344155815417"></a>This parameter is available only when ELB health check mode is selected for the AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p10349258543"><a name="p10349258543"></a><a name="p10349258543"></a>600s</p>
    </td>
    </tr>
    <tr id="row62855489"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p58129833"><a name="p58129833"></a><a name="p58129833"></a>Instance Removal Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p10896009"><a name="p10896009"></a><a name="p10896009"></a>Specifies the priority for removing instances from an AS group. If specified conditions are met, scaling actions are triggered to remove instances. AS supports the following instance removal policies:</p>
    <a name="ul30955222"></a><a name="ul30955222"></a><ul id="ul30955222"><li><strong id="b1023183614247"><a name="b1023183614247"></a><a name="b1023183614247"></a>Oldest instance created from oldest AS configuration</strong>: The oldest instance created based on the oldest configuration is removed from the AS group first.</li><li><strong id="b13624219132513"><a name="b13624219132513"></a><a name="b13624219132513"></a>Newest instance created from oldest AS configuration</strong>: The latest instance created based on the oldest configuration is removed from the AS group first.</li><li><strong id="b2096324362518"><a name="b2096324362518"></a><a name="b2096324362518"></a>Oldest instance</strong>: The oldest instance is removed from the AS group first.</li><li><strong id="b19891253142514"><a name="b19891253142514"></a><a name="b19891253142514"></a>Newest instance</strong>: The latest instance is removed from the AS group first.</li></ul>
    <div class="note" id="note51385802143421"><a name="note51385802143421"></a><a name="note51385802143421"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul6692505618408"></a><a name="ul6692505618408"></a><ul id="ul6692505618408"><li>Removing instances will preferentially ensure that the remaining instances are evenly distributed in AZs.</li><li>A manually added ECS is removed in the lowest priority. AS does not delete a manually added ECS when removing it. If multiple manually added ECSs must be removed, AS preferentially removes the earliest-added ECS.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p8807292"><a name="p8807292"></a><a name="p8807292"></a>N/A</p>
    </td>
    </tr>
    <tr id="row854292414461"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1154232474619"><a name="p1154232474619"></a><a name="p1154232474619"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p145423243462"><a name="p145423243462"></a><a name="p145423243462"></a>If <strong id="b862064610239"><a name="b862064610239"></a><a name="b862064610239"></a>EIP</strong> has been selected in an AS configuration for an AS group, an EIP is automatically bound to the ECS added by a scaling action to the AS group. If you select <strong id="b133641112102410"><a name="b133641112102410"></a><a name="b133641112102410"></a>Release</strong>, the EIP bound to an ECS is released when the ECS is removed from the AS group. Otherwise, the system unbinds the EIP from the ECS, but does not release it when the ECS is removed from the AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p1654210245466"><a name="p1654210245466"></a><a name="p1654210245466"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1330886492213"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5669743892232"><a name="p5669743892232"></a><a name="p5669743892232"></a>Notification Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p2908979192232"><a name="p2908979192232"></a><a name="p2908979192232"></a>This parameter is optional. If this parameter is selected, the system will notify you of scaling action results by email after a scaling action is complete.</p>
    <p id="p6048153592232"><a name="p6048153592232"></a><a name="p6048153592232"></a>The mailbox is specified when you register yourself on the cloud.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p5732292232"><a name="p5732292232"></a><a name="p5732292232"></a>N/A</p>
    </td>
    </tr>
    <tr id="row122816103111"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p52286143113"><a name="p52286143113"></a><a name="p52286143113"></a>Enterprise Project</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p1122901133119"><a name="p1122901133119"></a><a name="p1122901133119"></a>Specifies the enterprise project to which the AS group belongs. If an enterprise project is configured for an AS group, ECSs created in this AS group also belong to this enterprise project. If you do not specify an enterprise project, the <strong id="b842352706182723"><a name="b842352706182723"></a><a name="b842352706182723"></a>default</strong> enterprise project will be used.</p>
    <div class="note" id="note298918593115"><a name="note298918593115"></a><a name="note298918593115"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul4643153182612"></a><a name="ul4643153182612"></a><ul id="ul4643153182612"><li>Value <strong id="b197756316123"><a name="b197756316123"></a><a name="b197756316123"></a>default</strong> indicates the default enterprise project. Resources that are not allocated to any enterprise projects under your account are displayed in the default enterprise project.</li><li>Enterprise project is an upgraded version of IAM. It allocates and manages resources of different projects.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p12290118317"><a name="p12290118317"></a><a name="p12290118317"></a>N/A</p>
    </td>
    </tr>
    <tr id="row14293910144812"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p4491552134813"><a name="p4491552134813"></a><a name="p4491552134813"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p12120173110500"><a name="p12120173110500"></a><a name="p12120173110500"></a>Configure notifications and tags.</p>
    <p id="p152801338145112"><a name="p152801338145112"></a><a name="p152801338145112"></a>You can select <strong id="b5227185151517"><a name="b5227185151517"></a><a name="b5227185151517"></a>Do not configure</strong> or <strong id="b322912551514"><a name="b322912551514"></a><a name="b322912551514"></a>Configure now</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p1249165218483"><a name="p1249165218483"></a><a name="p1249165218483"></a>N/A</p>
    </td>
    </tr>
    <tr id="row18192144581718"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1119294571711"><a name="p1119294571711"></a><a name="p1119294571711"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p82451944172217"><a name="p82451944172217"></a><a name="p82451944172217"></a>If you have many resources of the same type, you can use a tag to manage resources flexibly. You can identify specified resources quickly using the tags allocated to them.</p>
    <p id="p044392582310"><a name="p044392582310"></a><a name="p044392582310"></a>Each tag contains a key and a value. You can specify the key and value for each tag.</p>
    <a name="ul217912412241"></a><a name="ul217912412241"></a><ul id="ul217912412241"><li>Key<a name="ul198769234258"></a><a name="ul198769234258"></a><ul id="ul198769234258"><li>The value cannot be empty.</li><li>An AS group has a unique key.</li><li>The value consists of at most 36 characters.  Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </li><li>Value<a name="ul592481672615"></a><a name="ul592481672615"></a><ul id="ul592481672615"><li>The value can be an empty character string.</li><li>A key can have only one value.</li><li>The value consists of at most 43 characters.  Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="p9192145151715"><a name="p9192145151715"></a><a name="p9192145151715"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Next**.
7.  On the displayed page, you can use an existing AS configuration or create an AS configuration. For details, see  [Using an Existing ECS to Create an AS Configuration](using-an-existing-ecs-to-create-an-as-configuration.md)  and  [Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md).
8.  Click  **Next**.
9.  \(Optional\) Add an AS policy to an AS group.

    On the displayed page, click  **Add AS Policy**.

    Configure the required parameters, such as the  **Policy Type**,  **Scaling Action**, and  **Cooldown Period**. For details, see  [Dynamically Expanding Resources](dynamically-expanding-resources.md)  and  [Expanding Resources as Planned](expanding-resources-as-planned.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If a scaling action is triggered by an AS policy, the cooldown period is that which is configured for that AS policy.  
    >-   If a scaling action is triggered by manually changing the expected number of instances or by other actions, the cooldown period is that which is configured for the AS group.   

10. Click  **Create Now**.
11. Check the AS group, AS configuration, and AS policy information.   Click  **Submit**.
12. Confirm the creation result and go back to the  **AS Groups**  page as prompted.

    After the AS group is created, its status changes to  **Enabled**.


