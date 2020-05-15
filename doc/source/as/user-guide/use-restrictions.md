# Use Restrictions<a name="EN-US_TOPIC_0192950173"></a>

AS has the following restrictions:

-   Only applications that are stateless and can be horizontally scaled can run on instances in an AS group.
-   AS automatically releases instances. Therefore, the instances in AS groups cannot be used to save application status information \(such as session statuses\) and related data \(such as database data and logs\). If the application status or related data must be saved, you can store the information on separate servers.
-   AS does not support capacity expansion or deduction of instance vCPUs and memory.
-   AS requires authentication provided by Identity and Access Management \(IAM\).

    AutoScaling Administrator requires permissions of Tenant Guest, Server Administrator, CES Administrator, and ELB Administrator.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the Cloud Eye administrator is not available, you can only use an existing alarm to create an alarm policy. If the ELB administrator is not available, you can still use existing load balancers.  

-   AS resources must comply with quota requirements listed in  [Table 1](#en-us_topic_0190954113_en-us_topic_0026721513_d0e195).

    **Table  1**  Quota list

    <a name="en-us_topic_0190954113_en-us_topic_0026721513_d0e195"></a>
    <table><thead align="left"><tr id="en-us_topic_0190954113_en-us_topic_0026721513_row10238520"><th class="cellrowborder" valign="top" width="18.48%" id="mcps1.2.4.1.1"><p id="en-us_topic_0190954113_en-us_topic_0026721513_p24013807"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p24013807"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p24013807"></a><strong id="b199344131376"><a name="b199344131376"></a><a name="b199344131376"></a>Category</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63.22%" id="mcps1.2.4.1.2"><p id="en-us_topic_0190954113_en-us_topic_0026721513_p66070243"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p66070243"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p66070243"></a><strong id="b19188919183716"><a name="b19188919183716"></a><a name="b19188919183716"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.3"><p id="en-us_topic_0190954113_en-us_topic_0026721513_p50089467"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p50089467"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p50089467"></a><strong id="b3158172820376"><a name="b3158172820376"></a><a name="b3158172820376"></a>Default Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0190954113_en-us_topic_0026721513_row4890297"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p60569775"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p60569775"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p60569775"></a>AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p7204713"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p7204713"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p7204713"></a>Maximum number of AS groups that a user can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p46710863"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p46710863"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p46710863"></a>25</p>
    </td>
    </tr>
    <tr id="en-us_topic_0190954113_en-us_topic_0026721513_row28025763"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p55494360"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p55494360"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p55494360"></a>AS configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p65858198"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p65858198"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p65858198"></a>Maximum number of AS configurations that a user can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p32913796"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p32913796"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p32913796"></a>100</p>
    </td>
    </tr>
    <tr id="en-us_topic_0190954113_en-us_topic_0026721513_row36292894"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p54043292"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p54043292"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p54043292"></a>AS policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p15430535"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p15430535"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p15430535"></a>Maximum number of AS policies that can be added to an AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p41913798"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p41913798"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p41913798"></a>50</p>
    </td>
    </tr>
    <tr id="en-us_topic_0190954113_en-us_topic_0026721513_row20625874"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p60083059"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p60083059"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p60083059"></a>Instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p34889605"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p34889605"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p34889605"></a>Maximum number of instances that can be added to an AS group</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0190954113_en-us_topic_0026721513_p7485743"><a name="en-us_topic_0190954113_en-us_topic_0026721513_p7485743"></a><a name="en-us_topic_0190954113_en-us_topic_0026721513_p7485743"></a>200</p>
    </td>
    </tr>
    <tr id="en-us_topic_0190954113_row641416965611"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0190954113_p74578551223"><a name="en-us_topic_0190954113_p74578551223"></a><a name="en-us_topic_0190954113_p74578551223"></a>Bandwidth scaling policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.22%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0190954113_p84140917569"><a name="en-us_topic_0190954113_p84140917569"></a><a name="en-us_topic_0190954113_p84140917569"></a>Maximum number of bandwidth scaling policies that you can create</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0190954113_p104150918564"><a name="en-us_topic_0190954113_p104150918564"></a><a name="en-us_topic_0190954113_p104150918564"></a>50</p>
    </td>
    </tr>
    </tbody>
    </table>


