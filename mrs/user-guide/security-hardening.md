# Security Hardening<a name="EN-US_TOPIC_0221415091"></a>

## Authentication and Encryption<a name="section9374144174716"></a>

**Security authentication**

Flink uses the following two authentication modes:

-   Kerberos authentication: It is used between the Flink YARN client and YARN ResourceManager, JobManager and ZooKeeper, JobManager and HDFS, TaskManager and HDFS, Kafka and TaskManager, as well as TaskManager and ZooKeeper.
-   Internal authentication mechanism of YARN: It is used between YARN ResourceManager and ApplicationMaster.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Flink JobManager and YARN ApplicationMaster are in the same process.  
    >-   If Kerberos authentication is enabled for the user's cluster, Kerberos authentication is required.  

    **Table  1**  Security authentication modes

    <a name="table73318320486"></a>
    <table><thead align="left"><tr id="row18541163234813"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p1954213211489"><a name="p1954213211489"></a><a name="p1954213211489"></a><strong id="b17541817174512"><a name="b17541817174512"></a><a name="b17541817174512"></a>Security Authentication Mode</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p20542332124818"><a name="p20542332124818"></a><a name="p20542332124818"></a><strong id="b6354413011231"><a name="b6354413011231"></a><a name="b6354413011231"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p05421432144816"><a name="p05421432144816"></a><a name="p05421432144816"></a><strong id="b438719213452"><a name="b438719213452"></a><a name="b438719213452"></a>Configuration</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1054263212483"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4542203215485"><a name="p4542203215485"></a><a name="p4542203215485"></a>Kerberos authentication</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p854218320486"><a name="p854218320486"></a><a name="p854218320486"></a>Currently, only keytab authentication is supported.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><a name="ol95421328486"></a><a name="ol95421328486"></a><ol id="ol95421328486"><li>Download the user keytab from the KDC server, and place the keytab to a folder on the host of the Flink client.</li><li>Configure following parameters in the <strong id="b6205183413469"><a name="b6205183413469"></a><a name="b6205183413469"></a>flink-conf.yaml</strong> file:<a name="ol19542163211486"></a><a name="ol19542163211486"></a><ol type="a" id="ol19542163211486"><li>Keytab file path<pre class="screen" id="screen154263219484"><a name="screen154263219484"></a><a name="screen154263219484"></a>security.kerberos.login.keytab: /home/flinkuser/keytab/abc222.keytab</pre>
    <p id="p1542632174816"><a name="p1542632174816"></a><a name="p1542632174816"></a>Note:</p>
    <p id="p6542163254811"><a name="p6542163254811"></a><a name="p6542163254811"></a><strong id="b199361221472"><a name="b199361221472"></a><a name="b199361221472"></a>/home/flinkuser/keytab/abc222.keytab</strong> indicates the user directory.</p>
    </li><li>Principal name<pre class="screen" id="screen954263284816"><a name="screen954263284816"></a><a name="screen954263284816"></a>security.kerberos.login.principal: abc222</pre>
    </li><li>In HA mode, if Zookeeper is configured, ZooKeeper Kerberos authentication must be configured as follows:<pre class="screen" id="screen135424325485"><a name="screen135424325485"></a><a name="screen135424325485"></a>zookeeper.sasl.disable: false
    security.kerberos.login.contexts: Client</pre>
    </li><li>If Kerberos authentication is required between the Kafka client and Kafka broker, configure it as follows:<pre class="screen" id="screen15542143214485"><a name="screen15542143214485"></a><a name="screen15542143214485"></a>security.kerberos.login.contexts: Client,KafkaClient</pre>
    </li></ol>
    </li></ol>
    </td>
    </tr>
    <tr id="row9543153217486"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25431332144813"><a name="p25431332144813"></a><a name="p25431332144813"></a>Internal authentication of YARN</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12543133212482"><a name="p12543133212482"></a><a name="p12543133212482"></a>The user does not need to configure this internal authentication mode.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1154353217482"><a name="p1154353217482"></a><a name="p1154353217482"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >One Flink cluster belongs to only one user. One user can create multiple Flink clusters.  

    **Encrypted transmission**

    Flink uses the following three encrypted transmission modes:

    -   Encrypted transmission inside YARN: It is used between the Flink YARN client and YARN ResourceManager, as well as YARN ResourceManager and JobManager.
    -   SSL transmission: It is used between the Flink YARN client and JobManager, JobManager and TaskManager, as well as TaskManagers.
    -   Encrypted transmission inside Hadoop: It is used between JobManager and HDFS, TaskManager and HDFS, JobManager and ZooKeeper, and TaskManager and ZooKeeper.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You do not need to configure encryption inside YARN and Hadoop, but need to configure SSL transmission.  


To configure SSL transmission, configure the  **flink-conf.yaml**  file on the client:

1.  Turn on the SSL switch and set SSL encryption algorithms.  [Table 2](#table20761742165017)  describes the parameters. Set the parameters based on site requirements.

    **Table  2**  Parameter description

    <a name="table20761742165017"></a>
    <table><thead align="left"><tr id="row8213942175017"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p1021494255016"><a name="p1021494255016"></a><a name="p1021494255016"></a><strong id="b6268528311231"><a name="b6268528311231"></a><a name="b6268528311231"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p021494212504"><a name="p021494212504"></a><a name="p021494212504"></a><strong id="b8151132101512"><a name="b8151132101512"></a><a name="b8151132101512"></a>Example Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p15214242115010"><a name="p15214242115010"></a><a name="p15214242115010"></a><strong id="b39030756165858"><a name="b39030756165858"></a><a name="b39030756165858"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122141542115019"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1521494245019"><a name="p1521494245019"></a><a name="p1521494245019"></a>security.ssl.internal.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p42141642205012"><a name="p42141642205012"></a><a name="p42141642205012"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1214174285015"><a name="p1214174285015"></a><a name="p1214174285015"></a>Switch to enable internal SSL</p>
    </td>
    </tr>
    <tr id="row52145425502"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p20214142145018"><a name="p20214142145018"></a><a name="p20214142145018"></a>akka.ssl.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p20214542175017"><a name="p20214542175017"></a><a name="p20214542175017"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1021420421502"><a name="p1021420421502"></a><a name="p1021420421502"></a>Switch to enable Akka SSL</p>
    </td>
    </tr>
    <tr id="row22141042195010"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p11214144211500"><a name="p11214144211500"></a><a name="p11214144211500"></a>blob.service.ssl.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p92141942175012"><a name="p92141942175012"></a><a name="p92141942175012"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1221434255020"><a name="p1221434255020"></a><a name="p1221434255020"></a>Switch to enable SSL of the BLOB channels</p>
    </td>
    </tr>
    <tr id="row18214174265013"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p021420427500"><a name="p021420427500"></a><a name="p021420427500"></a>taskmanager.data.ssl.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p13214114213505"><a name="p13214114213505"></a><a name="p13214114213505"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p2021417428505"><a name="p2021417428505"></a><a name="p2021417428505"></a>Switch to enable SSL for communications between TaskManagers</p>
    </td>
    </tr>
    <tr id="row14214114216505"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p15214154245017"><a name="p15214154245017"></a><a name="p15214154245017"></a>security.ssl.algorithms</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1521464210509"><a name="p1521464210509"></a><a name="p1521464210509"></a>TLS_RSA_WITH_AES128CBC_SHA256</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p821464295012"><a name="p821464295012"></a><a name="p821464295012"></a>SSL encryption algorithms</p>
    </td>
    </tr>
    </tbody>
    </table>

    The following parameters do not exist in the default Flink configuration of MRS. If you want to enable SSL for external connections, you need to add the following parameters. After SSL for external connection is enabled, the native Flink page cannot be accessed using a YARN proxy, because the YARN open-source version cannot process HTTPS requests using a proxy. However, you can create a Windows VM in the same VPC of the cluster and access the native Flink page from the VM.

    **Table  3**  Parameter description

    <a name="table17417185916285"></a>
    <table><thead align="left"><tr id="row18415185918287"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p11415195942819"><a name="p11415195942819"></a><a name="p11415195942819"></a><strong id="b1870237142716"><a name="b1870237142716"></a><a name="b1870237142716"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p6415115914280"><a name="p6415115914280"></a><a name="p6415115914280"></a><strong id="b3688123832710"><a name="b3688123832710"></a><a name="b3688123832710"></a>Example Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p1441511592283"><a name="p1441511592283"></a><a name="p1441511592283"></a><strong id="b171141841182718"><a name="b171141841182718"></a><a name="b171141841182718"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9416959162818"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p164151359182816"><a name="p164151359182816"></a><a name="p164151359182816"></a>security.ssl.rest.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p941625919283"><a name="p941625919283"></a><a name="p941625919283"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1741610591288"><a name="p1741610591288"></a><a name="p1741610591288"></a>Switch to enable external SSL. If this parameter is set to <strong id="b16582319172815"><a name="b16582319172815"></a><a name="b16582319172815"></a>true</strong>, set the related parameters by referring to <a href="#table8420145910282">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row141635915288"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p164161859102818"><a name="p164161859102818"></a><a name="p164161859102818"></a>security.ssl.rest.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p341695912813"><a name="p341695912813"></a><a name="p341695912813"></a>${path}/flink.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p17416175912814"><a name="p17416175912814"></a><a name="p17416175912814"></a>Path for storing the keystore</p>
    </td>
    </tr>
    <tr id="row9416859132813"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p641616599289"><a name="p641616599289"></a><a name="p641616599289"></a>security.ssl.rest.keystore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p641618593281"><a name="p641618593281"></a><a name="p641618593281"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p641616598283"><a name="p641616598283"></a><a name="p641616598283"></a>Password of the keystore. The value <strong id="b1999032402914"><a name="b1999032402914"></a><a name="b1999032402914"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row15416759182818"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1841645922810"><a name="p1841645922810"></a><a name="p1841645922810"></a>security.ssl.rest.key-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p54165592282"><a name="p54165592282"></a><a name="p54165592282"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p194160599283"><a name="p194160599283"></a><a name="p194160599283"></a>Password of the SSL key. The value <strong id="b2070542113015"><a name="b2070542113015"></a><a name="b2070542113015"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row19417165910283"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1041705972818"><a name="p1041705972818"></a><a name="p1041705972818"></a>security.ssl.rest.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1441715914281"><a name="p1441715914281"></a><a name="p1441715914281"></a>${path}/flink.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p641755918287"><a name="p641755918287"></a><a name="p641755918287"></a>Path for storing the truststore</p>
    </td>
    </tr>
    <tr id="row1941717594287"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1417259192817"><a name="p1417259192817"></a><a name="p1417259192817"></a>security.ssl.rest.truststore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p7417259192816"><a name="p7417259192816"></a><a name="p7417259192816"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p441765992819"><a name="p441765992819"></a><a name="p441765992819"></a>Password of the truststore. The value <strong id="b132344515306"><a name="b132344515306"></a><a name="b132344515306"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Enabling SSL for data transmission between TaskManagers may pose great impact on system performance. You need to take both security and performance into consideration.  

2.  In the  **bin**  directory of the Flink client, run the  **sh generate\_keystore.sh <password\>**  command. The configuration items in  [Table 4](#table5419125952810)  are set by default. You can also set the configuration items manually.

    **Table  4**  Parameter description

    <a name="table5419125952810"></a>
    <table><thead align="left"><tr id="row16418359182816"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p124173594288"><a name="p124173594288"></a><a name="p124173594288"></a><strong id="b20814059173412"><a name="b20814059173412"></a><a name="b20814059173412"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p14418115914285"><a name="p14418115914285"></a><a name="p14418115914285"></a><strong id="b54814211355"><a name="b54814211355"></a><a name="b54814211355"></a>Example Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p2418859142813"><a name="p2418859142813"></a><a name="p2418859142813"></a><strong id="b37815314359"><a name="b37815314359"></a><a name="b37815314359"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row124183594285"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p18418659192818"><a name="p18418659192818"></a><a name="p18418659192818"></a>security.ssl.internal.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p10418175922815"><a name="p10418175922815"></a><a name="p10418175922815"></a>${path}/flink.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p241885913287"><a name="p241885913287"></a><a name="p241885913287"></a>Path for storing the <strong id="b1649532103511"><a name="b1649532103511"></a><a name="b1649532103511"></a>keystore</strong> file. <strong id="b11458115594316"><a name="b11458115594316"></a><a name="b11458115594316"></a>flink.keystore</strong> indicates the name of the <strong id="b33375374410"><a name="b33375374410"></a><a name="b33375374410"></a>keystore</strong> file generated by the <strong id="b1264111034420"><a name="b1264111034420"></a><a name="b1264111034420"></a>generate_keystore.sh*</strong> tool.</p>
    </td>
    </tr>
    <tr id="row5418205952817"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1641895982816"><a name="p1641895982816"></a><a name="p1641895982816"></a>security.ssl.internal.keystore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p3418759142816"><a name="p3418759142816"></a><a name="p3418759142816"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p14418165912285"><a name="p14418165912285"></a><a name="p14418165912285"></a>Password of the keystore. The value <strong id="b17790151344417"><a name="b17790151344417"></a><a name="b17790151344417"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row74184593285"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p2418175972820"><a name="p2418175972820"></a><a name="p2418175972820"></a>security.ssl.internal.key-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p441814590283"><a name="p441814590283"></a><a name="p441814590283"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p9418195912814"><a name="p9418195912814"></a><a name="p9418195912814"></a>Password of the SSL key. The value <strong id="b1647414226446"><a name="b1647414226446"></a><a name="b1647414226446"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row24181259102812"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p194182059102819"><a name="p194182059102819"></a><a name="p194182059102819"></a>security.ssl.internal.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p18418115917287"><a name="p18418115917287"></a><a name="p18418115917287"></a>${path}/flink.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1341810591288"><a name="p1341810591288"></a><a name="p1341810591288"></a>Path for storing the <strong id="b85501727174418"><a name="b85501727174418"></a><a name="b85501727174418"></a>truststore</strong> file. <strong id="b135516278444"><a name="b135516278444"></a><a name="b135516278444"></a>flink.truststore</strong> indicates the name of the <strong id="b3553102715447"><a name="b3553102715447"></a><a name="b3553102715447"></a>truststore</strong> file generated by the <strong id="b1355542718448"><a name="b1355542718448"></a><a name="b1355542718448"></a>generate_keystore.sh*</strong> tool.</p>
    </td>
    </tr>
    <tr id="row4419115992815"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p154187599286"><a name="p154187599286"></a><a name="p154187599286"></a>security.ssl.internal.truststore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p2041975952814"><a name="p2041975952814"></a><a name="p2041975952814"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p9419159192820"><a name="p9419159192820"></a><a name="p9419159192820"></a>Password of the truststore. The value <strong id="b14570124419450"><a name="b14570124419450"></a><a name="b14570124419450"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    </tbody>
    </table>

    If SSL for external connections is enabled, that is,  **security.ssl.rest.enabled**  is set to  **true**, the following parameters need to be set:

    **Table  5**  Parameter description

    <a name="table8420145910282"></a>
    <table><thead align="left"><tr id="row154195594286"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p1941918596289"><a name="p1941918596289"></a><a name="p1941918596289"></a><strong id="b14629828104614"><a name="b14629828104614"></a><a name="b14629828104614"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p12419165911284"><a name="p12419165911284"></a><a name="p12419165911284"></a><strong id="b14840629144617"><a name="b14840629144617"></a><a name="b14840629144617"></a>Example Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p641945952818"><a name="p641945952818"></a><a name="p641945952818"></a><strong id="b716733114615"><a name="b716733114615"></a><a name="b716733114615"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16872032172510"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p159497328252"><a name="p159497328252"></a><a name="p159497328252"></a>security.ssl.rest.enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p39495328259"><a name="p39495328259"></a><a name="p39495328259"></a>true</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p149491032112517"><a name="p149491032112517"></a><a name="p149491032112517"></a>Switch to enable external SSL. If this parameter is set to <strong id="b16384153454615"><a name="b16384153454615"></a><a name="b16384153454615"></a>true</strong>, set the related parameters by referring to <a href="#table8420145910282">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row14191859112815"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1941995902814"><a name="p1941995902814"></a><a name="p1941995902814"></a>security.ssl.rest.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1341995912289"><a name="p1341995912289"></a><a name="p1341995912289"></a>${path}/flink.keystore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p94199592287"><a name="p94199592287"></a><a name="p94199592287"></a>Path for storing the keystore</p>
    </td>
    </tr>
    <tr id="row114201259112818"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p14196593285"><a name="p14196593285"></a><a name="p14196593285"></a>security.ssl.rest.keystore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1641965942815"><a name="p1641965942815"></a><a name="p1641965942815"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p10419105992819"><a name="p10419105992819"></a><a name="p10419105992819"></a>Password of the keystore. The value <strong id="b174161645194619"><a name="b174161645194619"></a><a name="b174161645194619"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row942045912810"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p342085915283"><a name="p342085915283"></a><a name="p342085915283"></a>security.ssl.rest.key-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p842085914285"><a name="p842085914285"></a><a name="p842085914285"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p64204596285"><a name="p64204596285"></a><a name="p64204596285"></a>Password of the SSL key. The value <strong id="b746512507469"><a name="b746512507469"></a><a name="b746512507469"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    <tr id="row1420105917283"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p2420195912818"><a name="p2420195912818"></a><a name="p2420195912818"></a>security.ssl.rest.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p442065932818"><a name="p442065932818"></a><a name="p442065932818"></a>${path}/flink.truststore</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1242075915281"><a name="p1242075915281"></a><a name="p1242075915281"></a>Path for storing the truststore</p>
    </td>
    </tr>
    <tr id="row174204599283"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p54207591286"><a name="p54207591286"></a><a name="p54207591286"></a>security.ssl.rest.truststore-password</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p14204598287"><a name="p14204598287"></a><a name="p14204598287"></a>123456</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1420145910286"><a name="p1420145910286"></a><a name="p1420145910286"></a>Password of the truststore. The value <strong id="b236915574462"><a name="b236915574462"></a><a name="b236915574462"></a>123456</strong> indicates a user-defined password.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **path**  indicates a user-defined directory that is used to store configuration files of the SSL keystore and truststore. The commands vary according to the relative path and absolute path. The details are as follows:

    -   Configure the file path storing the  **keystore**  or  **truststore**  file to a relative path, and the Flink client directory where the command is executed can directly access this relative path. Flink can transfer the  **keystore**  and  **truststore**  files using either of the following methods:
        -   Add the  **-t**  option to the  **CLI yarn-session.sh**  command of Flink to transfer the  **keystore**  and  **truststore**  files to execution nodes. The following is an example.

            ```
            ./bin/yarn-session.sh -t ssl/ -n 2
            ```

        -   Add the  **-yt**  option to the  **flink run**  command to transfer the  **keystore**  and  **truststore**  files to execution nodes. The following is an example.

            ```
            ./bin/flink run -yt ssl/ -ys 3 -yn 3 -m yarn-cluster -c org.apache.flink.examples.java.wordcount.WordCount /opt/client/Flink/flink/examples/batch/WordCount.jar
            ```

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >-   In the preceding example,  **ssl/**  is the sub-directory of the Flink client directory and is used to store configuration files of the SSL keystore and truststore.  
            >-   The relative path of  **ssl/**  must be accessible from the current path where the Flink client command is executed.  


    -   If the  **keystore**  or  **truststore**  file path is an absolute path, the  **keystore**  and  **truststore**  files must exist in the absolute path on Flink Client and all nodes. In addition, the user who submits the job must have permission to read the files.

        Either of the following methods can be used to run applications. The  **-t**  or  **-yt**  option does not need to be added to transfer the  **keystore**  and  **truststore**  files.

        -   Run the  **CLI yarn-session.sh**  command of Flink to execute applications. The following is an example.

            ```
            ./bin/yarn-session.sh -n 2
            ```

        -   Run the  **flink run**  command to execute applications. The following is an example.

            ```
            ./bin/flink run  -ys 3 -yn 3 -m yarn-cluster -c org.apache.flink.examples.java.wordcount.WordCount /opt/client/Flink/flink/examples/batch/WordCount.jar
            ```




## ACL<a name="section172894244814"></a>

In HA mode of Flink, ZooKeeper can be used to manage clusters and discover services. Zookeeper supports SASL ACL. Only users who have passed the SASL \(Kerberos\) authentication have permission to operate files on ZooKeeper. To enable SASL ACL, configure the following parameters in the Flink configuration file.

```
high-availability.zookeeper.client.acl: creator
zookeeper.sasl.disable: false
```

For details about the configuration items, see  [Table 10](configuring-and-managing-flink.md#table4784519778).

## Web security<a name="section1690964819512"></a>

**Encoding Specifications**

Note: The same encoding mode is used on the web service client and server to prevent garbled characters and to implement input verification.

Security hardening: Response messages of web servers are encoded using UTF-8.

Whitelist-based Filtering of IP Addresses

Note: To prevent unauthorized users from logging in to the web servers, add an IP filter on the web servers to filter out invalid requests of source IP addresses.

Security: Add  **jobmanager.web.allow-access-address**  to enable the IP filter. By default, only YARN users are supported.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Flink does not involve security risks of client storage, WebWorker, WebRTC, and WebSocket.  

Preventing Absolute Paths of Files Being Sent to the Client

Note: If an absolute path is sent to a client, the directory structure of the server is exposed, helping attackers traverse and attack the system.

Security hardening: If the Flink configuration file contains a parameter starting with a slash \(/\), delete the first-level directory.

## Security Statement<a name="section8304769570"></a>

-   All security functions of Flink are provided by the open source community or self-developed. Security features, such as authentication and SSL encrypted transmission, that need to be configured by users, may affect performance.
-   As a big data computing and analysis platform, Flink does not detect sensitive information. Therefore, users need to ensure that the input data is anonymized.
-   Users need to evaluate whether configurations are secure as required.
-   For any security-related problems, contact customer service.

