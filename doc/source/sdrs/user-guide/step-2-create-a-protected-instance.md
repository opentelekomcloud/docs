# Step 2: Create a Protected Instance<a name="EN-US_TOPIC_0110037558"></a>

## Scenarios<a name="section1078504973319"></a>

You can create protected instances using the servers that you want to perform DR protection. If the current production site encounters an unexpected large-scale server failure, you can call the related protection group API to perform a failover, ensuring that services running on protected instances are not affected.

Select a protection group for each server to be replicated and create a protected instance using the server. When you create a protected instance, the server and disk will be created at the DR site for the production site server and disk. The server specifications can be configured as required. Specifically, the specifications of the DR site server can be different from those of the production site server. The disks of the production site and DR site are of the same specifications and can automatically form a replication pair.

The server at the DR site is in the Stopped state after the protected instance created. These automatically created resources, including the DR site servers and disks, cannot be used before a planned failover or failover.

**Figure  1**  Creating a protected instance<a name="fig1679017015306"></a>  
![](figures/creating-a-protected-instance.png "creating-a-protected-instance")

## Notes<a name="section112247299141"></a>

-   If a production site server has been added to an ECS group, you are not allowed to specify a DeH to create the DR site server for the production site server.
-   When a protected instance is created, the default name of the server at the DR site is the same as that of the server at the production site, but their IDs are different.
-   To modify a server name, switch to the protected instance details page and click the server name to switch to the server details page.
-   After you create a protected instance and enable protection for the protection group, modifications to the  **Hostname**,  **Name**,  **Agency**,  **ECS Group**,  **Security Group**,  **Tags**, and  **Auto Recovery**  configurations of the production site server will not synchronize to the DR site server. You can log in to the management console and manually add the configuration items to the servers at the DR site.
-   If protection is enabled for servers created during capacity expansion of an Auto Scaling \(AS\) group, these servers cannot be deleted when the capacity of the AS group is reduced.
-   If the server at the production site runs Windows and you choose the key login mode, ensure that the key pair of the server exists when you create a protected instance. Otherwise, the server at the DR site may fail to create, causing the protected instance creation failure.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the key pair of the server at the production site has been deleted, create a key pair with the same name.  

-   When you create a protected instance, if the production site server runs Linux and uses the key login mode, the key pair information will not be displayed on the details page of the DR site server after the DR site server is created. You can use the key pair of the production site server to log in to the DR site server.
-   If the production site server is added to Enterprise Project, the created DR site server will not be automatically added to Enterprise Project. You need to manually add it to Enterprise Project if needed.

## **Prerequisites**<a name="section69384216261"></a>

-   The protection group is in the  **Available**  or  **Protecting**  state.
-   No shared disk is attached to the production site server.

    If some services need to use shared disks, perform steps in  [Creating a Replication Pair](creating-a-replication-pair.md)  to create a replication pair for the shared disks. Then, perform steps in  [Attaching a Replication Pair](attaching-a-replication-pair.md)  to attach the replication pair to the protected instance.

-   No protected instances have been created for the production site server.
-   Resources of the target specifications for the server to be protected are not sold out at the DR site.
-   The server that you use to create a protected instance and the protection group are in the same VPC.

## Procedure<a name="section141312551333"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group for which protected instances are to be added, click  **Protected Instances**.

    The operation page for the protection group is displayed.

4.  On the  **Protected Instances**  tab, click  **Create Protected Instance**.

    The  **Create Protected Instance**  page is displayed.

    **Figure  2**  Creating a protected instance<a name="fig213754162419"></a>  
    ![](figures/creating-a-protected-instance-1.png "creating-a-protected-instance-1")

5.  Configure the basic information about the protected instance, as described in  [Table 1](#table14113172215131).

    **Table  1**  Parameter description

    <a name="table14113172215131"></a>
    <table><thead align="left"><tr id="row711682216134"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p111164221133"><a name="p111164221133"></a><a name="p111164221133"></a><strong id="b842352706211121"><a name="b842352706211121"></a><a name="b842352706211121"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.4.1.2"><p id="p5116172261316"><a name="p5116172261316"></a><a name="p5116172261316"></a><strong id="b84235270695711"><a name="b84235270695711"></a><a name="b84235270695711"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.3"><p id="p1211612224133"><a name="p1211612224133"></a><a name="p1211612224133"></a><strong>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16116152218134"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1111622216136"><a name="p1111622216136"></a><a name="p1111622216136"></a>Protection Group Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p1635361519186"><a name="p1635361519186"></a><a name="p1635361519186"></a>Indicates the name of the protection group to which the protected instance to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p71162022131317"><a name="p71162022131317"></a><a name="p71162022131317"></a>protection_group_001</p>
    </td>
    </tr>
    <tr id="row132183175150"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1822071712155"><a name="p1822071712155"></a><a name="p1822071712155"></a>Protection Group ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p102202017161516"><a name="p102202017161516"></a><a name="p102202017161516"></a>Indicates the ID of the protection group to which the protected instance to be created belongs.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p1722010175156"><a name="p1722010175156"></a><a name="p1722010175156"></a>2a663c5c-4774-4775-a321-562a1ea163e3</p>
    </td>
    </tr>
    <tr id="row2116722191312"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p121161122161311"><a name="p121161122161311"></a><a name="p121161122161311"></a>DR Direction</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p121169227135"><a name="p121169227135"></a><a name="p121169227135"></a>Indicates the replication direction of the protection group to which the protected instance to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p11826358193017"><a name="p11826358193017"></a><a name="p11826358193017"></a>eu-de-01 -&gt; eu-de-02</p>
    </td>
    </tr>
    <tr id="row446619382712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1646673172720"><a name="p1646673172720"></a><a name="p1646673172720"></a>Production Site</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p7466173152719"><a name="p7466173152719"></a><a name="p7466173152719"></a>Indicates the AZ of the production site server. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p124661430277"><a name="p124661430277"></a><a name="p124661430277"></a>az-01</p>
    </td>
    </tr>
    <tr id="row33787144198"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1937831410194"><a name="p1937831410194"></a><a name="p1937831410194"></a>Deployment Model</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p189707173281"><a name="p189707173281"></a><a name="p189707173281"></a>Indicates the deployment model of the protection group to which the protected instance to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p5970191712814"><a name="p5970191712814"></a><a name="p5970191712814"></a>VPC migration</p>
    </td>
    </tr>
    <tr id="row1620211262191"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9202326111918"><a name="p9202326111918"></a><a name="p9202326111918"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p79701417102820"><a name="p79701417102820"></a><a name="p79701417102820"></a>Indicates the VPC of the protection group to which the protected instance to be created belongs. You do not need to configure it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p1597021702813"><a name="p1597021702813"></a><a name="p1597021702813"></a>vpc1</p>
    </td>
    </tr>
    <tr id="row1811682219137"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1011682221320"><a name="p1011682221320"></a><a name="p1011682221320"></a>Production Site Server</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p30123162814"><a name="p30123162814"></a><a name="p30123162814"></a>This parameter is mandatory.</p>
    <p id="p70183152814"><a name="p70183152814"></a><a name="p70183152814"></a>In the server list, select the server and specifications to be used to create the protected instance. </p>
    <div class="note" id="note842223882911"><a name="note842223882911"></a><a name="note842223882911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul8355134911610"></a><a name="ul8355134911610"></a><ul id="ul8355134911610"><li>If <strong id="b39451965615"><a name="b39451965615"></a><a name="b39451965615"></a>Server Type</strong> of the protection group is <strong id="b4785151220565"><a name="b4785151220565"></a><a name="b4785151220565"></a>ECS</strong>, select the DR site server specifications. The specifications of the production site server and DR site server can be different. Select the specifications from the <strong id="b376725914336"><a name="b376725914336"></a><a name="b376725914336"></a>DR Site Server Specifications</strong> drop-down list.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p190133110284"><a name="p190133110284"></a><a name="p190133110284"></a>ecs-test &gt; s3.small.1</p>
    </td>
    </tr>
    <tr id="row6491123874013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1749153864010"><a name="p1749153864010"></a><a name="p1749153864010"></a>DR Site VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p04822184210"><a name="p04822184210"></a><a name="p04822184210"></a>Indicates the VPC of the DR site server.</p>
    <p id="p365219384111"><a name="p365219384111"></a><a name="p365219384111"></a>Its value is the same as the <strong id="b842352706164937"><a name="b842352706164937"></a><a name="b842352706164937"></a>VPC</strong> value and do not need to be configured.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p104915383406"><a name="p104915383406"></a><a name="p104915383406"></a>vpc1</p>
    </td>
    </tr>
    <tr id="row1498954271619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p398964210165"><a name="p398964210165"></a><a name="p398964210165"></a>Protected Instance Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p59621429297"><a name="p59621429297"></a><a name="p59621429297"></a>This parameter is mandatory.</p>
    <p id="p1896211212297"><a name="p1896211212297"></a><a name="p1896211212297"></a>Enter the protected instance name. It is used for protected instance classification and search.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p11365203619469"><a name="p11365203619469"></a><a name="p11365203619469"></a>Protected-Instance-test</p>
    </td>
    </tr>
    <tr id="row567517599146"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9676259161418"><a name="p9676259161418"></a><a name="p9676259161418"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.2 "><p id="p45151214131718"><a name="p45151214131718"></a><a name="p45151214131718"></a>This parameter is optional.</p>
    <p id="p4995133681710"><a name="p4995133681710"></a><a name="p4995133681710"></a>Tags are identifiers of protected instances. You can add tags for protected instances, and classify and search the protected instances based on these tags. You can add up to 10 tags for each server.</p>
    <p id="en-us_topic_0013859510_p31281231165424"><a name="en-us_topic_0013859510_p31281231165424"></a><a name="en-us_topic_0013859510_p31281231165424"></a>For details, see <a href="managing-protected-instance-tags.md">Managing Protected Instance Tags</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.3 "><p id="p66771959191415"><a name="p66771959191415"></a><a name="p66771959191415"></a>Organization/Marketing</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**.
7.  On the  **Confirm**  page, you can confirm the protected instance information.
    -   If you do not need to modify the information, click  **Submit**.
    -   If you need to modify the information, click  **Previous**.

8.  Click  **Back to Protection Group Details Page**  and view the protected instances of the protection group.

    If the protected instance status changes to  **Available**  or  **Protecting**, the protected instance has been created successfully.

    >![](/images/icon-note.gif) **NOTE:**   
    >After a protected instance is created, the system automatically creates replication pairs for the disks of the protected instance and backs up all the disks.  
    >Query the replication pairs.  
    >1.  Switch to the operation page for the protection group.  
    >2.  Click the  **Replication Pairs**  tab.  
    >    On this tab, you can query the statuses of the replication pairs, target protected instance, and production site disk.  


