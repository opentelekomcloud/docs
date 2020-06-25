# Creating an AS Group<a name="EN-US_TOPIC_0042018368"></a>

## Scenarios<a name="section2495449014355"></a>

An AS group consists of a collection of instances and AS policies that have similar attributes and apply to the same application scenario. An AS group is the basis for enabling or disabling AS policies and performing scaling actions. The pre-configured AS policy automatically adds or deletes instances to or from an AS group, or maintains a fixed number of instances in an AS group.

When creating an AS group, specify an AS configuration for it. Additionally, add one or more AS policies for the AS group.

Creating an AS group involves the configuration of the maximum, minimum, and expected numbers of instances and the associated load balancer.

## Notes<a name="section1657416306249"></a>

ECS types supported by different AZs may vary. When creating an AS group, you must choose a proper AS configuration according to the ECS type supported by the AZs used by the AS group.

-   If the ECS type specified in the AS configuration is supported by none of the AZs used by the AS group, the following situations will occur:
    -   If the AS group is disabled, it cannot be enabled.
    -   If the AS group is enabled, its status will become abnormal when instances are added to it.

-   If the ECS type specified in the AS configuration is supported only by certain AZs used by the AS group, the ECSs added by a scaling action are distributed only in the AZs supporting the ECS type. As a result, the instances in the AS group may not be evenly distributed.

## Procedure<a name="section3293739142316"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select a region and a project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click  **Create AS Group**.
5.  Set parameters, such as  **Name**,  **Max. Instances**,  **Min. Instances**, and  **Expected Instances**.  [Table 1](#table63081199191521)  describes the key parameters to be configured.

    **Table  1**  AS group parameters

    <a name="table63081199191521"></a>
    <table><thead align="left"><tr id="en-us_topic_0042018359_row18270305"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0042018359_p3499754"><a name="en-us_topic_0042018359_p3499754"></a><a name="en-us_topic_0042018359_p3499754"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.2"><p id="en-us_topic_0042018359_p15044627"><a name="en-us_topic_0042018359_p15044627"></a><a name="en-us_topic_0042018359_p15044627"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.3"><p id="en-us_topic_0042018359_p10655236"><a name="en-us_topic_0042018359_p10655236"></a><a name="en-us_topic_0042018359_p10655236"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0042018359_row5184165310418"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p51849531448"><a name="en-us_topic_0042018359_p51849531448"></a><a name="en-us_topic_0042018359_p51849531448"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p17184175316413"><a name="en-us_topic_0042018359_p17184175316413"></a><a name="en-us_topic_0042018359_p17184175316413"></a>A region is where an AS group resides.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p12184135316415"><a name="en-us_topic_0042018359_p12184135316415"></a><a name="en-us_topic_0042018359_p12184135316415"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row19614145145315"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p1261415516531"><a name="en-us_topic_0042018359_p1261415516531"></a><a name="en-us_topic_0042018359_p1261415516531"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p10805969403"><a name="en-us_topic_0042018359_p10805969403"></a><a name="en-us_topic_0042018359_p10805969403"></a>An AZ is a physical region where resources use independent power supply and networks. AZs are physically isolated but interconnected through an internal network.</p>
    <p id="en-us_topic_0042018359_p116651349185417"><a name="en-us_topic_0042018359_p116651349185417"></a><a name="en-us_topic_0042018359_p116651349185417"></a>To enhance application availability, the system evenly distributes your instances between AZs if multiple AZs have been selected.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p961495112536"><a name="en-us_topic_0042018359_p961495112536"></a><a name="en-us_topic_0042018359_p961495112536"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row54028730202125"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p14251001202125"><a name="en-us_topic_0042018359_p14251001202125"></a><a name="en-us_topic_0042018359_p14251001202125"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p13480457202125"><a name="en-us_topic_0042018359_p13480457202125"></a><a name="en-us_topic_0042018359_p13480457202125"></a>Specifies the name of the AS group to be created.</p>
    <p id="en-us_topic_0042018359_p28009099142054"><a name="en-us_topic_0042018359_p28009099142054"></a><a name="en-us_topic_0042018359_p28009099142054"></a>The name contains 1 to 64 characters and consists of only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p18175250202125"><a name="en-us_topic_0042018359_p18175250202125"></a><a name="en-us_topic_0042018359_p18175250202125"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row57767782"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p48678752"><a name="en-us_topic_0042018359_p48678752"></a><a name="en-us_topic_0042018359_p48678752"></a>Max. Instances or Min. Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p50664859"><a name="en-us_topic_0042018359_p50664859"></a><a name="en-us_topic_0042018359_p50664859"></a>Specifies the maximum or minimum number of ECSs in an AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p10212927"><a name="en-us_topic_0042018359_p10212927"></a><a name="en-us_topic_0042018359_p10212927"></a>10 or 5</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row24807479"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p63248778"><a name="en-us_topic_0042018359_p63248778"></a><a name="en-us_topic_0042018359_p63248778"></a>Expected Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p22877402"><a name="en-us_topic_0042018359_p22877402"></a><a name="en-us_topic_0042018359_p22877402"></a>Specifies the expected number of ECSs in an AS group.</p>
    <p id="en-us_topic_0042018359_p4570028"><a name="en-us_topic_0042018359_p4570028"></a><a name="en-us_topic_0042018359_p4570028"></a>After an AS group is created, you can change this value, which will trigger a scaling action.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p34627969"><a name="en-us_topic_0042018359_p34627969"></a><a name="en-us_topic_0042018359_p34627969"></a>6</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row16313497"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p46324881"><a name="en-us_topic_0042018359_p46324881"></a><a name="en-us_topic_0042018359_p46324881"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p61327894"><a name="en-us_topic_0042018359_p61327894"></a><a name="en-us_topic_0042018359_p61327894"></a>Provides a network for your ECSs.</p>
    <p id="en-us_topic_0042018359_p15080136"><a name="en-us_topic_0042018359_p15080136"></a><a name="en-us_topic_0042018359_p15080136"></a>All ECSs in an AS group belong to the same VPC.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p13531531"><a name="en-us_topic_0042018359_p13531531"></a><a name="en-us_topic_0042018359_p13531531"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row9914165244816"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p8914125264813"><a name="en-us_topic_0042018359_p8914125264813"></a><a name="en-us_topic_0042018359_p8914125264813"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p1404647118"><a name="en-us_topic_0042018359_p1404647118"></a><a name="en-us_topic_0042018359_p1404647118"></a>You can select a maximum of five subnets. The AS group automatically binds all NICs to the created ECSs. The first subnet is used by the primary NIC of the ECS by default, and other subnets are used by extension NICs of the ECS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p11915352104810"><a name="en-us_topic_0042018359_p11915352104810"></a><a name="en-us_topic_0042018359_p11915352104810"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row6128980"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p102720515599"><a name="en-us_topic_0042018359_p102720515599"></a><a name="en-us_topic_0042018359_p102720515599"></a>Load Balancing</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p1609475215599"><a name="en-us_topic_0042018359_p1609475215599"></a><a name="en-us_topic_0042018359_p1609475215599"></a>This parameter is optional. A load balancer automatically distributes access traffic to all instances in an AS group to balance their service load. It enables higher levels of fault tolerance in your applications and expands application service capabilities.</p>
    <div class="note" id="en-us_topic_0042018359_note1063504415599"><a name="en-us_topic_0042018359_note1063504415599"></a><a name="en-us_topic_0042018359_note1063504415599"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0042018359_ul1817818563313"></a><a name="en-us_topic_0042018359_ul1817818563313"></a><ul id="en-us_topic_0042018359_ul1817818563313"><li class="textintable">Up to three load balancers can be added to an AS group.</li><li class="textintable">After multiple load balancers are added to an AS group, multiple services can be concurrently listened to, thereby improving service scalability. If <strong id="en-us_topic_0042018359_b1781123361216"><a name="en-us_topic_0042018359_b1781123361216"></a><a name="en-us_topic_0042018359_b1781123361216"></a>ELB health check</strong> is selected for <strong id="en-us_topic_0042018359_b2781233161216"><a name="en-us_topic_0042018359_b2781233161216"></a><a name="en-us_topic_0042018359_b2781233161216"></a>Health Check Method</strong>, when any one of the listeners detects that an instance becomes faulty, AS will replace the faulty instance with a functional one.</li></ul>
    </div></div>
    <p id="en-us_topic_0042018359_p3542840015599"><a name="en-us_topic_0042018359_p3542840015599"></a><a name="en-us_topic_0042018359_p3542840015599"></a>If you select <strong id="en-us_topic_0042018359_b1069545173117"><a name="en-us_topic_0042018359_b1069545173117"></a><a name="en-us_topic_0042018359_b1069545173117"></a>Classic load balancer</strong>, configure the following parameters:</p>
    <a name="en-us_topic_0042018359_ul4982997994510"></a><a name="en-us_topic_0042018359_ul4982997994510"></a><ul id="en-us_topic_0042018359_ul4982997994510"><li><strong id="en-us_topic_0042018359_b8423527061090"><a name="en-us_topic_0042018359_b8423527061090"></a><a name="en-us_topic_0042018359_b8423527061090"></a>Load Balancer</strong></li><li><strong id="en-us_topic_0042018359_b8423527061093"><a name="en-us_topic_0042018359_b8423527061093"></a><a name="en-us_topic_0042018359_b8423527061093"></a>Listener</strong></li></ul>
    <div class="p" id="en-us_topic_0042018359_p23417149454"><a name="en-us_topic_0042018359_p23417149454"></a><a name="en-us_topic_0042018359_p23417149454"></a>If you select <strong id="en-us_topic_0042018359_b10687551124510"><a name="en-us_topic_0042018359_b10687551124510"></a><a name="en-us_topic_0042018359_b10687551124510"></a>Enhanced load balancer</strong>, configure the following parameters:<a name="en-us_topic_0042018359_ul1865661654415"></a><a name="en-us_topic_0042018359_ul1865661654415"></a><ul id="en-us_topic_0042018359_ul1865661654415"><li><strong id="en-us_topic_0042018359_b324122138"><a name="en-us_topic_0042018359_b324122138"></a><a name="en-us_topic_0042018359_b324122138"></a>Load Balancer</strong></li><li><strong id="en-us_topic_0042018359_b842352706194411"><a name="en-us_topic_0042018359_b842352706194411"></a><a name="en-us_topic_0042018359_b842352706194411"></a>Backend ECS Group</strong></li></ul>
    <a name="en-us_topic_0042018359_ul16565169449"></a><a name="en-us_topic_0042018359_ul16565169449"></a><ul id="en-us_topic_0042018359_ul16565169449"><li><strong id="en-us_topic_0042018359_b84235270610935"><a name="en-us_topic_0042018359_b84235270610935"></a><a name="en-us_topic_0042018359_b84235270610935"></a>Backend Port</strong>: specifies the port on which a backend ECS listens for traffic.</li><li><strong id="en-us_topic_0042018359_b842352706101430"><a name="en-us_topic_0042018359_b842352706101430"></a><a name="en-us_topic_0042018359_b842352706101430"></a>Weight</strong>: determines the portion of requests a backend ECS processes compared to other backend ECSs added to the same listener.<p id="en-us_topic_0042018359_p5656316104419"><a name="en-us_topic_0042018359_p5656316104419"></a><a name="en-us_topic_0042018359_p5656316104419"></a>For more information about load balancing, see <em id="en-us_topic_0042018359_i84235269719113"><a name="en-us_topic_0042018359_i84235269719113"></a><a name="en-us_topic_0042018359_i84235269719113"></a>Elastic Load Balancing User Guide</em><em id="en-us_topic_0042018359_i189657412275"><a name="en-us_topic_0042018359_i189657412275"></a><a name="en-us_topic_0042018359_i189657412275"></a></em><em id="en-us_topic_0042018359_i8599108122716"><a name="en-us_topic_0042018359_i8599108122716"></a><a name="en-us_topic_0042018359_i8599108122716"></a></em>.</p>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p40893240"><a name="en-us_topic_0042018359_p40893240"></a><a name="en-us_topic_0042018359_p40893240"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row32922880"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p49507636"><a name="en-us_topic_0042018359_p49507636"></a><a name="en-us_topic_0042018359_p49507636"></a>Health Check Method</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p2129537693230"><a name="en-us_topic_0042018359_p2129537693230"></a><a name="en-us_topic_0042018359_p2129537693230"></a>When a health check detects a faulty ECS, AS removes the faulty ECS from the AS group and adds a new one. The health check is implemented using any of the following methods:</p>
    <a name="en-us_topic_0042018359_ul50695543"></a><a name="en-us_topic_0042018359_ul50695543"></a><ul id="en-us_topic_0042018359_ul50695543"><li><strong id="en-us_topic_0042018359_b8423527069724"><a name="en-us_topic_0042018359_b8423527069724"></a><a name="en-us_topic_0042018359_b8423527069724"></a>ECS health check</strong>: checks ECS running status. If an ECS is stopped or deleted, it is considered as abnormal. This method is selected by default. Using this method, the AS group periodically determines the running status of each ECS based on the health check result. If the health check result shows that an ECS is faulty, AS removes the ECS from the AS group.</li><li><strong id="en-us_topic_0042018359_b162239179229"><a name="en-us_topic_0042018359_b162239179229"></a><a name="en-us_topic_0042018359_b162239179229"></a>ELB health check</strong>: determines ECS running status using a load balancing listener. This health check method is available only when the AS group uses a load balancing listener. When a load balancing listener detects that an ECS is faulty, AS removes the ECS from the AS group.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p31815862"><a name="en-us_topic_0042018359_p31815862"></a><a name="en-us_topic_0042018359_p31815862"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row17907308"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p41205809"><a name="en-us_topic_0042018359_p41205809"></a><a name="en-us_topic_0042018359_p41205809"></a>Health Check Interval</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p49336210"><a name="en-us_topic_0042018359_p49336210"></a><a name="en-us_topic_0042018359_p49336210"></a>Specifies the health check period for an AS group. You can set a proper health check interval, such as 10 seconds, 1 minute, 5 minutes, 15 minutes, 1 hour, and 3 hours based on the site requirements.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p36810105"><a name="en-us_topic_0042018359_p36810105"></a><a name="en-us_topic_0042018359_p36810105"></a>5 minutes</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row8530240449"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p2329205817411"><a name="en-us_topic_0042018359_p2329205817411"></a><a name="en-us_topic_0042018359_p2329205817411"></a>Health Check Grace Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p7668329374"><a name="en-us_topic_0042018359_p7668329374"></a><a name="en-us_topic_0042018359_p7668329374"></a>Specifies the grace period for instance health check. The unit is second and value range is 0 to 86400. The default value is <strong id="en-us_topic_0042018359_b842352706193228"><a name="en-us_topic_0042018359_b842352706193228"></a><a name="en-us_topic_0042018359_b842352706193228"></a>600</strong>.</p>
    <p id="en-us_topic_0042018359_p14340158248"><a name="en-us_topic_0042018359_p14340158248"></a><a name="en-us_topic_0042018359_p14340158248"></a>The health check grace period starts after an instance is added to an AS group and enabled. The AS group will start checking status of the instance only after the grace period ends.</p>
    <p id="en-us_topic_0042018359_p15344155815417"><a name="en-us_topic_0042018359_p15344155815417"></a><a name="en-us_topic_0042018359_p15344155815417"></a>This parameter is available only when ELB health check mode is selected for the AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p10349258543"><a name="en-us_topic_0042018359_p10349258543"></a><a name="en-us_topic_0042018359_p10349258543"></a>600s</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row62855489"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p58129833"><a name="en-us_topic_0042018359_p58129833"></a><a name="en-us_topic_0042018359_p58129833"></a>Instance Removal Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p10896009"><a name="en-us_topic_0042018359_p10896009"></a><a name="en-us_topic_0042018359_p10896009"></a>Specifies the priority for removing instances from an AS group. If specified conditions are met, scaling actions are triggered to remove instances. AS supports the following instance removal policies:</p>
    <a name="en-us_topic_0042018359_ul30955222"></a><a name="en-us_topic_0042018359_ul30955222"></a><ul id="en-us_topic_0042018359_ul30955222"><li><strong id="en-us_topic_0042018359_b1023183614247"><a name="en-us_topic_0042018359_b1023183614247"></a><a name="en-us_topic_0042018359_b1023183614247"></a>Oldest instance created from oldest AS configuration</strong>: The oldest instance created based on the oldest configuration is removed from the AS group first.</li><li><strong id="en-us_topic_0042018359_b13624219132513"><a name="en-us_topic_0042018359_b13624219132513"></a><a name="en-us_topic_0042018359_b13624219132513"></a>Newest instance created from oldest AS configuration</strong>: The latest instance created based on the oldest configuration is removed from the AS group first.</li><li><strong id="en-us_topic_0042018359_b2096324362518"><a name="en-us_topic_0042018359_b2096324362518"></a><a name="en-us_topic_0042018359_b2096324362518"></a>Oldest instance</strong>: The oldest instance is removed from the AS group first.</li><li><strong id="en-us_topic_0042018359_b19891253142514"><a name="en-us_topic_0042018359_b19891253142514"></a><a name="en-us_topic_0042018359_b19891253142514"></a>Newest instance</strong>: The latest instance is removed from the AS group first.</li></ul>
    <div class="note" id="en-us_topic_0042018359_note51385802143421"><a name="en-us_topic_0042018359_note51385802143421"></a><a name="en-us_topic_0042018359_note51385802143421"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0042018359_ul6692505618408"></a><a name="en-us_topic_0042018359_ul6692505618408"></a><ul id="en-us_topic_0042018359_ul6692505618408"><li>Removing instances will preferentially ensure that the remaining instances are evenly distributed in AZs.</li><li>A manually added ECS is removed in the lowest priority. AS does not delete a manually added ECS when removing it. If multiple manually added ECSs must be removed, AS preferentially removes the earliest-added ECS.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p8807292"><a name="en-us_topic_0042018359_p8807292"></a><a name="en-us_topic_0042018359_p8807292"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row854292414461"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p1154232474619"><a name="en-us_topic_0042018359_p1154232474619"></a><a name="en-us_topic_0042018359_p1154232474619"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p145423243462"><a name="en-us_topic_0042018359_p145423243462"></a><a name="en-us_topic_0042018359_p145423243462"></a>If <strong id="en-us_topic_0042018359_b862064610239"><a name="en-us_topic_0042018359_b862064610239"></a><a name="en-us_topic_0042018359_b862064610239"></a>EIP</strong> has been selected in an AS configuration for an AS group, an EIP is automatically bound to the ECS added by a scaling action to the AS group. If you select <strong id="en-us_topic_0042018359_b133641112102410"><a name="en-us_topic_0042018359_b133641112102410"></a><a name="en-us_topic_0042018359_b133641112102410"></a>Release</strong>, the EIP bound to an ECS is released when the ECS is removed from the AS group. Otherwise, the system unbinds the EIP from the ECS, but does not release it when the ECS is removed from the AS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p1654210245466"><a name="en-us_topic_0042018359_p1654210245466"></a><a name="en-us_topic_0042018359_p1654210245466"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row1330886492213"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p5669743892232"><a name="en-us_topic_0042018359_p5669743892232"></a><a name="en-us_topic_0042018359_p5669743892232"></a>Notification Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p2908979192232"><a name="en-us_topic_0042018359_p2908979192232"></a><a name="en-us_topic_0042018359_p2908979192232"></a>This parameter is optional. If this parameter is selected, the system will notify you of scaling action results by email after a scaling action is complete.</p>
    <p id="en-us_topic_0042018359_p6048153592232"><a name="en-us_topic_0042018359_p6048153592232"></a><a name="en-us_topic_0042018359_p6048153592232"></a>The mailbox is specified when you register yourself on the cloud.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p5732292232"><a name="en-us_topic_0042018359_p5732292232"></a><a name="en-us_topic_0042018359_p5732292232"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row122816103111"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p52286143113"><a name="en-us_topic_0042018359_p52286143113"></a><a name="en-us_topic_0042018359_p52286143113"></a>Enterprise Project</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p1122901133119"><a name="en-us_topic_0042018359_p1122901133119"></a><a name="en-us_topic_0042018359_p1122901133119"></a>Specifies the enterprise project to which the AS group belongs. If an enterprise project is configured for an AS group, ECSs created in this AS group also belong to this enterprise project. If you do not specify an enterprise project, the <strong id="en-us_topic_0042018359_b842352706182723"><a name="en-us_topic_0042018359_b842352706182723"></a><a name="en-us_topic_0042018359_b842352706182723"></a>default</strong> enterprise project will be used.</p>
    <div class="note" id="en-us_topic_0042018359_note298918593115"><a name="en-us_topic_0042018359_note298918593115"></a><a name="en-us_topic_0042018359_note298918593115"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0042018359_ul4643153182612"></a><a name="en-us_topic_0042018359_ul4643153182612"></a><ul id="en-us_topic_0042018359_ul4643153182612"><li>Value <strong id="en-us_topic_0042018359_b197756316123"><a name="en-us_topic_0042018359_b197756316123"></a><a name="en-us_topic_0042018359_b197756316123"></a>default</strong> indicates the default enterprise project. Resources that are not allocated to any enterprise projects under your account are displayed in the default enterprise project.</li><li>Enterprise project is an upgraded version of IAM. It allocates and manages resources of different projects.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p12290118317"><a name="en-us_topic_0042018359_p12290118317"></a><a name="en-us_topic_0042018359_p12290118317"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row14293910144812"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p4491552134813"><a name="en-us_topic_0042018359_p4491552134813"></a><a name="en-us_topic_0042018359_p4491552134813"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p12120173110500"><a name="en-us_topic_0042018359_p12120173110500"></a><a name="en-us_topic_0042018359_p12120173110500"></a>Configure notifications and tags.</p>
    <p id="en-us_topic_0042018359_p152801338145112"><a name="en-us_topic_0042018359_p152801338145112"></a><a name="en-us_topic_0042018359_p152801338145112"></a>You can select <strong id="en-us_topic_0042018359_b5227185151517"><a name="en-us_topic_0042018359_b5227185151517"></a><a name="en-us_topic_0042018359_b5227185151517"></a>Do not configure</strong> or <strong id="en-us_topic_0042018359_b322912551514"><a name="en-us_topic_0042018359_b322912551514"></a><a name="en-us_topic_0042018359_b322912551514"></a>Configure now</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p1249165218483"><a name="en-us_topic_0042018359_p1249165218483"></a><a name="en-us_topic_0042018359_p1249165218483"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0042018359_row18192144581718"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0042018359_p1119294571711"><a name="en-us_topic_0042018359_p1119294571711"></a><a name="en-us_topic_0042018359_p1119294571711"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0042018359_p82451944172217"><a name="en-us_topic_0042018359_p82451944172217"></a><a name="en-us_topic_0042018359_p82451944172217"></a>If you have many resources of the same type, you can use a tag to manage resources flexibly. You can identify specified resources quickly using the tags allocated to them.</p>
    <p id="en-us_topic_0042018359_p044392582310"><a name="en-us_topic_0042018359_p044392582310"></a><a name="en-us_topic_0042018359_p044392582310"></a>Each tag contains a key and a value. You can specify the key and value for each tag.</p>
    <a name="en-us_topic_0042018359_ul217912412241"></a><a name="en-us_topic_0042018359_ul217912412241"></a><ul id="en-us_topic_0042018359_ul217912412241"><li>Key<a name="en-us_topic_0042018359_ul198769234258"></a><a name="en-us_topic_0042018359_ul198769234258"></a><ul id="en-us_topic_0042018359_ul198769234258"><li>The value cannot be empty.</li><li>An AS group has a unique key.</li><li>The value consists of at most 36 characters.  Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </li><li>Value<a name="en-us_topic_0042018359_ul592481672615"></a><a name="en-us_topic_0042018359_ul592481672615"></a><ul id="en-us_topic_0042018359_ul592481672615"><li>The value can be an empty character string.</li><li>A key can have only one value.</li><li>The value consists of at most 43 characters.  Only digits, letters, underscores (_), and hyphens (-) are allowed.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0042018359_p9192145151715"><a name="en-us_topic_0042018359_p9192145151715"></a><a name="en-us_topic_0042018359_p9192145151715"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Next**. On the  **Add AS Configuration**  page, you can choose to use an existing AS configuration or create one. For details, see  [Using an Existing ECS to Create an AS Configuration](using-an-existing-ecs-to-create-an-as-configuration.md)  and  [Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md).
7.  Click  **Create Now**.
8.  Check the AS group and AS configuration information.  Click  **Submit**.
9.  You can add AS policies. For details, see  [Creating an AS Policy](creating-an-as-policy.md).

