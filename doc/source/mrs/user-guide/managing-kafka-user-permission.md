# Managing Kafka User Permission<a name="EN-US_TOPIC_0125375513"></a>

## Scenario<a name="scad388acfb3a4f5eb6712981519f4d14"></a>

For clusters with Kerberos authentication enabled, using Kafka requires relevant permission. MRS clusters can grant the use permission of Kafka to different users.

[Table 1](#tc2054cc5be6042d9953500a56d963883)  lists the default Kafka user groups.

**Table  1**  Default Kafka user groups

<a name="tc2054cc5be6042d9953500a56d963883"></a>
<table><thead align="left"><tr id="r3ec745256e13424d84442e977f51e337"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a5b5858a8a83347348a8c8029480fdfdb"><a name="a5b5858a8a83347348a8c8029480fdfdb"></a><a name="a5b5858a8a83347348a8c8029480fdfdb"></a><strong id="a294a4b86fdc34cd2b5d06e5fd29d2caa"><a name="a294a4b86fdc34cd2b5d06e5fd29d2caa"></a><a name="a294a4b86fdc34cd2b5d06e5fd29d2caa"></a>User Group</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aa61fe8a4824c43c49170965eb56ac295"><a name="aa61fe8a4824c43c49170965eb56ac295"></a><a name="aa61fe8a4824c43c49170965eb56ac295"></a><strong id="a95bfa5bdaf0740cfbcbc57aab379aa4e"><a name="a95bfa5bdaf0740cfbcbc57aab379aa4e"></a><a name="a95bfa5bdaf0740cfbcbc57aab379aa4e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rbecf4e8f7af140d4881cf46d1010a3bc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a1990ea09aa4540668014cc1003ffd1a1"><a name="a1990ea09aa4540668014cc1003ffd1a1"></a><a name="a1990ea09aa4540668014cc1003ffd1a1"></a>kafkaadmin</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ac70ee000f3074b1088559337a544e196"><a name="ac70ee000f3074b1088559337a544e196"></a><a name="ac70ee000f3074b1088559337a544e196"></a>Kafka administrator group. Users in this group have the permission to create, delete, read, and write all topics, and authorize other users.</p>
</td>
</tr>
<tr id="r2c7bdeb2de724927966705424e36685f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a537b1ace9bef4f6f945f8e57097df897"><a name="a537b1ace9bef4f6f945f8e57097df897"></a><a name="a537b1ace9bef4f6f945f8e57097df897"></a>kafkasuperuser</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="abed21e2f0f6b4068ade1102dd8de7d17"><a name="abed21e2f0f6b4068ade1102dd8de7d17"></a><a name="abed21e2f0f6b4068ade1102dd8de7d17"></a>Kafka super user group. Users in this group have the permission to read and write all topics.</p>
</td>
</tr>
<tr id="r7ec0d2bc09f740dbbba27503a4e72ce5"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ace7f3db85cab45a898aaf7f47c060274"><a name="ace7f3db85cab45a898aaf7f47c060274"></a><a name="ace7f3db85cab45a898aaf7f47c060274"></a>kafka</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0054328609_p85436155921"><a name="en-us_topic_0054328609_p85436155921"></a><a name="en-us_topic_0054328609_p85436155921"></a>Kafka common user group. Users in this group must be authorized by the users in <strong id="a744726aecd4c4d10abb9e1be063d7103"><a name="a744726aecd4c4d10abb9e1be063d7103"></a><a name="a744726aecd4c4d10abb9e1be063d7103"></a>kafkaadmin</strong> to read and write certain topics.</p>
</td>
</tr>
</tbody>
</table>

## Prerequisites<a name="s17a283ba364a4e41853112423529f0b8"></a>

-   The client has been updated.
-   A user in the  **kafkaadmin** group, for example **admin**, has been prepared.

## Procedure<a name="s171988b510164b1990278c6e6550831f"></a>

1.  On MRS Manager, choose  **Service**  \>  **ZooKeeper**  \>  **Instance**. Query the IP addresses of the ZooKeeper instances.

    Record the IP address of any ZooKeeper instance.

2.  Log in to the node where the client is installed.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Client Management](client_management).

3.  Run the following command to switch the user:

    **sudo su - omm**

4.  Run the following command to switch to the client directory, for example,  **/opt/client/Kafka/kafka/bin**.

    **cd /opt/client/Kafka/kafka/bin**

5.  Run the following command to configure the environment variables:

    **source /opt/client/bigdata\_env**

6.  Run the following command to authenticate the Kafka administrator account.

    **kinit** _Administrator account_

    For example,  **kinit admin**

7.  Manage Kafka user permission using the following commands:

    -   Query the permission list of a topic.

        **sh kafka-acls.sh --authorizer-properties zookeeper.connect=_IP address of the node where the ZooKeeper instance is located_:24002/kafka --list --topic** _**Topic name**_

    -   Add producer permission to a user.

        **sh kafka-acls.sh --authorizer-properties zookeeper.connect=**_**IP address of the node where the ZooKeeper instance is located**_**:24002/kafka --add --allow-principal User:**_**Username**_ **--producer --topic** _**Topic name**_

    -   Remove producer permission of a user.

        **sh kafka-acls.sh --authorizer-properties zookeeper.connect=**_**IP address of the node where the ZooKeeper instance is located**_**:24002/kafka --remove --allow-principal User:**_**Username**_ **--producer --topic** _**Topic name**_

    -   Add consumer permission to a user.

        **sh kafka-acls.sh --authorizer-properties zookeeper.connect=**_**IP address of the node where the ZooKeeper instance is located**_**:24002/kafka --add --allow-principal User:**_**Username**_ **--consumer --topic** _**Topic name**_ **--group** _**Consumer group name**_

    -   Remove consumer permission of a user.

        **sh kafka-acls.sh --authorizer-properties zookeeper.connect=**_**IP address of the node where the ZooKeeper instance is located**_**:24002/kafka --remove --allow-principal User:**_**Username**_ **--consumer --topic** _**Topic name**_ **--group** _**Consumer group name**_

    >![](/images/icon-note.gif) **NOTE:**   
    >You need to enter  **y**  twice to confirm the removal of permission.  


