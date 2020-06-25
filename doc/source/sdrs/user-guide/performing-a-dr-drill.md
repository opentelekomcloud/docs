# Performing a DR Drill<a name="EN-US_TOPIC_0122528555"></a>

## Scenarios<a name="section171315582320"></a>

DR drills can be used to simulate fault scenarios, specify the emergency recovery solutions, and verify whether the solutions are applicable and effective. The existing services will not be affected during the DR drill. When a real fault occurs, you can use the solutions to rapidly restore services, enhancing service continuity.

SDRS provides the DR drill function. You can perform DR drills in a drill VPC \(different from the VPC of the DR site\). This function allows you to use the disk snapshots of the DR site servers to create drill servers with the server specifications and disk types same as the DR site servers.

>![](/images/icon-note.gif) **NOTE:**   
>After the DR drill server is created, the production site server and DR drill server will independently run at the same time \(data will not be synchronized between these two servers\).  

To ensure that a failover can be properly performed if a disaster happens, you are recommended to perform DR drills regularly to verify that:

-   The production site data and DR site data are consistent at the moment when you create a DR drill.
-   The services at the DR site can run properly after a failover.

    **Figure  1**  Performing a DR drill<a name="fig135261922851"></a>  
    ![](figures/performing-a-dr-drill.png "performing-a-dr-drill")


## Notes<a name="section1613910364214"></a>

-   If the DR site server of the protection group is added to Enterprise Project, the created DR drill server will not be automatically added to Enterprise Project. You need to manually add it to Enterprise Project if needed.
-   When you use a created drill VPC to create a drill, the subnet ACL rule of the drill VPC will be different from that of the VPC of the protection group. You need to manually set them to be the same one if needed.
-   When you create a DR drill, if the VPC of the protection group has a customized routing table and subnets configured, the corresponding routing table will not be automatically created for the drill VPC. You need to manually create it if needed.
-   If the DR site server runs Windows and uses the key login mode, ensure that the key pair of the DR site server exists when you create a DR drill. Otherwise, the DR drill server may fail to create, causing the DR drill creation failure.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the key pair of the DR site server has been deleted, create a key pair with the same name.  

-   When you create a DR drill, if the DR site server runs Linux and uses the key login mode, the key pair information will not be displayed on the details page of the DR drill server after the DR drill server is created. You can use the key pair of the DR site server to log in to the DR drill server.
-   After you create a DR drill, modifications to the  **Hostname**,  **Name**,  **Agency**,  **ECS Group**,  **Security Group**,  **Tags**, and  **Auto Recovery**  configurations of the DR site server before the drill will not synchronize to the DR drill server. You can log in to the management console and manually add the configuration items to the DR drill server.
-   If the synchronization progress of replication pairs in the protection group is not 100%, the created DR drill server may fail to start. You are advised to perform a DR drill after all replication pairs are synchronized.

## **Prerequisites**<a name="section67593181295"></a>

-   The protection group is in the  **Available**,  **Protecting**,  **Failover complete**,  **Enabling protection failed**,  **Disabling protection failed**,  **Planned failover failed**,  **Re-enabling protection failed**, or  **Failover failed**  state.
-   Do not perform a DR drill before the first time data synchronization between the production site server and DR site server completes. Otherwise, the drill server may not start properly.

## Procedure<a name="section37751719193414"></a>

1.  Log in to the management console. 
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group to which a DR drill is to be added, click  **DR Drills**.

    The operation page for the protection group is displayed.

4.  On the  **DR Drills**  tab, click  **Create DR Drill**.

    The  **Create DR Drill**  dialog box is displayed.

5.  Configure  **Name**  and  **Drill VPC**.

    **Table  1**  Parameter description

    <a name="table17278611195315"></a>
    <table><thead align="left"><tr id="row18279121110532"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1673616279539"><a name="p1673616279539"></a><a name="p1673616279539"></a><strong id="b842352706211121"><a name="b842352706211121"></a><a name="b842352706211121"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p6737152714535"><a name="p6737152714535"></a><a name="p6737152714535"></a><strong id="b8423527061662"><a name="b8423527061662"></a><a name="b8423527061662"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p197371427125317"><a name="p197371427125317"></a><a name="p197371427125317"></a><strong>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1527915119539"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57403279534"><a name="p57403279534"></a><a name="p57403279534"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p177411527185315"><a name="p177411527185315"></a><a name="p177411527185315"></a>Specifies the DR drill name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p374242715310"><a name="p374242715310"></a><a name="p374242715310"></a>DR drill servername</p>
    </td>
    </tr>
    <tr id="row1627921117530"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p274392717539"><a name="p274392717539"></a><a name="p274392717539"></a>Drill VPC </p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p0743927135319"><a name="p0743927135319"></a><a name="p0743927135319"></a>The VPC is used for a DR drill and cannot be the same as the VPC of the DR site server. Specifies the drill VPC. The value can be <strong id="b4824517172910"><a name="b4824517172910"></a><a name="b4824517172910"></a>Automatically create</strong> or <strong id="b8236221162915"><a name="b8236221162915"></a><a name="b8236221162915"></a>Use existing</strong>.</p>
    <a name="ul3372115552310"></a><a name="ul3372115552310"></a><ul id="ul3372115552310"><li><strong id="b5214123211294"><a name="b5214123211294"></a><a name="b5214123211294"></a>Automatically create</strong>: The system automatically creates a drill VPC and subnets for the protection group.</li><li><strong id="b982383817298"><a name="b982383817298"></a><a name="b982383817298"></a>Use existing</strong>: The system uses an existing VPC as the drill VPC. If you select to use an existing VPC, the subnet CIDR block of the drill VPC must be consistent with that of the production group VPC.</li></ul>
    <div class="note" id="note1476474313238"><a name="note1476474313238"></a><a name="note1476474313238"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7764843112313"><a name="p7764843112313"></a><a name="p7764843112313"></a>The drill VPC cannot be the same as the VPC of the protection group.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4744172725315"><a name="p4744172725315"></a><a name="p4744172725315"></a>vpc-f9f7</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

    After a DR drill is created, you can log in to the DR drill server and check whether services are running properly.


