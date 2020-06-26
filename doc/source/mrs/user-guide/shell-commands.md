# Shell Commands<a name="EN-US_TOPIC_0221415094"></a>

Before running Flink shell commands, perform the following operations:

1.  Install a Flink client in a directory, for example,  **/opt/client**.
2.  Run the following command to initialize environment variables:

    **source /opt/client/bigdata\_env**

3.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If the Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** _Service user_ 

4.  Run the commands according to  [Table 1](#table65101640171215).

    **Table  1**  Flink shell command reference

    <a name="table65101640171215"></a>
    <table><thead align="left"><tr id="row266514404129"><th class="cellrowborder" valign="top" width="19.01190119011901%" id="mcps1.2.4.1.1"><p id="p2149115918167"><a name="p2149115918167"></a><a name="p2149115918167"></a><strong id="b856277103216"><a name="b856277103216"></a><a name="b856277103216"></a>Command</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.65476547654765%" id="mcps1.2.4.1.2"><p id="p1149105911160"><a name="p1149105911160"></a><a name="p1149105911160"></a><strong id="b52271310133216"><a name="b52271310133216"></a><a name="b52271310133216"></a>Parameter Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41492597169"><a name="p41492597169"></a><a name="p41492597169"></a><strong id="b1839821720327"><a name="b1839821720327"></a><a name="b1839821720327"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1666534011216"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p76657406128"><a name="p76657406128"></a><a name="p76657406128"></a>yarn-session.sh</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p866544013122"><a name="p866544013122"></a><a name="p866544013122"></a>Mandatory</p>
    <p id="p1666114051213"><a name="p1666114051213"></a><a name="p1666114051213"></a><strong id="b464744823212"><a name="b464744823212"></a><a name="b464744823212"></a>-n,--container &lt;arg&gt;</strong>: Indicates the number of TaskManagers contained in a YARN cluster that need to be started.</p>
    <p id="p18666134031218"><a name="p18666134031218"></a><a name="p18666134031218"></a>Optional</p>
    <p id="p196669401122"><a name="p196669401122"></a><a name="p196669401122"></a><strong id="b205343619370"><a name="b205343619370"></a><a name="b205343619370"></a>-D &lt;arg&gt;</strong>: Indicates dynamic parameter configuration.</p>
    <p id="p156661540141215"><a name="p156661540141215"></a><a name="p156661540141215"></a><strong id="b172306251374"><a name="b172306251374"></a><a name="b172306251374"></a>-d,--detached</strong>: Disables the interactive mode and starts a separate Flink YARN session.</p>
    <p id="p5666174051214"><a name="p5666174051214"></a><a name="p5666174051214"></a><strong id="b189311353819"><a name="b189311353819"></a><a name="b189311353819"></a>-id,--applicationId &lt;arg&gt;</strong>: Binds to a running YARN session.</p>
    <p id="p4666124011215"><a name="p4666124011215"></a><a name="p4666124011215"></a><strong id="b3789238193811"><a name="b3789238193811"></a><a name="b3789238193811"></a>-j,--jar &lt;arg&gt;</strong>: Sets the path of the user's JAR file.</p>
    <p id="p1166624051218"><a name="p1166624051218"></a><a name="p1166624051218"></a><strong id="b869755612385"><a name="b869755612385"></a><a name="b869755612385"></a>-jm,--jobManagerMemory &lt;arg&gt;</strong>: Sets memory for JobManagers.</p>
    <p id="p1366624081213"><a name="p1366624081213"></a><a name="p1366624081213"></a><strong id="b8699112620396"><a name="b8699112620396"></a><a name="b8699112620396"></a>-nm,--name &lt;arg&gt;</strong>: Customizes a name for a YARN application.</p>
    <p id="p13666340171211"><a name="p13666340171211"></a><a name="p13666340171211"></a><strong id="b101031486396"><a name="b101031486396"></a><a name="b101031486396"></a>-q,--query</strong>: Queries available YARN resources.</p>
    <p id="p15666154041213"><a name="p15666154041213"></a><a name="p15666154041213"></a><strong id="b11956132674011"><a name="b11956132674011"></a><a name="b11956132674011"></a>-qu,--queue &lt;arg&gt;</strong>: Specifies a YARN queue.</p>
    <p id="p13666154016129"><a name="p13666154016129"></a><a name="p13666154016129"></a><strong id="b18341746194012"><a name="b18341746194012"></a><a name="b18341746194012"></a>-s,--slots &lt;arg&gt;</strong>: Sets the number of slots for each TaskManager.</p>
    <p id="p266618404129"><a name="p266618404129"></a><a name="p266618404129"></a><strong id="b138821154113"><a name="b138821154113"></a><a name="b138821154113"></a>-t,--ship &lt;arg&gt;</strong>: Specifies the directory of the file to be sent.</p>
    <p id="p106661040151219"><a name="p106661040151219"></a><a name="p106661040151219"></a><strong id="b1012902894119"><a name="b1012902894119"></a><a name="b1012902894119"></a>-tm,--taskManagerMemory &lt;arg&gt;</strong>: Sets memory for TaskManagers.</p>
    <p id="p186668401122"><a name="p186668401122"></a><a name="p186668401122"></a><strong id="b4975354154112"><a name="b4975354154112"></a><a name="b4975354154112"></a>-z,--zookeeperNamespace &lt;args&gt;</strong>: Specifies the namespace of ZooKeeper. <strong id="b755916154219"><a name="b755916154219"></a><a name="b755916154219"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1866634041219"><a name="p1866634041219"></a><a name="p1866634041219"></a>Start a resident Flink cluster to receive tasks from the Flink client.</p>
    </td>
    </tr>
    <tr id="row566634012127"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p17666174011213"><a name="p17666174011213"></a><a name="p17666174011213"></a>flink run</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p1166619405122"><a name="p1166619405122"></a><a name="p1166619405122"></a><strong id="b78155585420"><a name="b78155585420"></a><a name="b78155585420"></a>-c,--class &lt;classname&gt;</strong>: Specifies a class as an entry point for program running.</p>
    <p id="p116661540121211"><a name="p116661540121211"></a><a name="p116661540121211"></a><strong id="b760711245430"><a name="b760711245430"></a><a name="b760711245430"></a>-C,--classpath &lt;url&gt;</strong>: Specifies <strong id="b17317163510436"><a name="b17317163510436"></a><a name="b17317163510436"></a>classpath</strong>.</p>
    <p id="p466644016122"><a name="p466644016122"></a><a name="p466644016122"></a><strong id="b1874812402432"><a name="b1874812402432"></a><a name="b1874812402432"></a>-d,--detached</strong>: Runs a job in detached mode.</p>
    <p id="p466611406123"><a name="p466611406123"></a><a name="p466611406123"></a><strong id="b9624122811449"><a name="b9624122811449"></a><a name="b9624122811449"></a>-m,--jobmanager &lt;host:port&gt;</strong>: Specifies a JobManager.</p>
    <p id="p9666040101211"><a name="p9666040101211"></a><a name="p9666040101211"></a><strong id="b7104104224419"><a name="b7104104224419"></a><a name="b7104104224419"></a>-p,--parallelism &lt;parallelism&gt;</strong>: Specifies the job DOP, which will overwrite the DOP parameter configured in the configuration file.</p>
    <p id="p1666617401121"><a name="p1666617401121"></a><a name="p1666617401121"></a><strong id="b16650625204517"><a name="b16650625204517"></a><a name="b16650625204517"></a>-q,--sysoutLogging</strong>: Disables the function of outputting Flink logs to the console.</p>
    <p id="p4666164041210"><a name="p4666164041210"></a><a name="p4666164041210"></a><strong id="b363715145466"><a name="b363715145466"></a><a name="b363715145466"></a>-s,--fromSavepoint &lt;savepointPath&gt;</strong>: Specifies a savepoint path for recovering jobs.</p>
    <p id="p14666154051215"><a name="p14666154051215"></a><a name="p14666154051215"></a><strong id="b9723102418487"><a name="b9723102418487"></a><a name="b9723102418487"></a>-z,--zookeeperNamespace &lt;zookeeperNamespace&gt;</strong>: Specifies the namespace of ZooKeeper.</p>
    <p id="p666624031220"><a name="p666624031220"></a><a name="p666624031220"></a><strong id="b18644521164917"><a name="b18644521164917"></a><a name="b18644521164917"></a>-yD &lt;arg&gt;</strong>: Indicates dynamic parameter configuration.</p>
    <p id="p36666403129"><a name="p36666403129"></a><a name="p36666403129"></a><strong id="b4848164212491"><a name="b4848164212491"></a><a name="b4848164212491"></a>-yd,--yarndetached</strong>: Starts YARN in detached mode.</p>
    <p id="p2666140151214"><a name="p2666140151214"></a><a name="p2666140151214"></a><strong id="b5353471507"><a name="b5353471507"></a><a name="b5353471507"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds to a job running in the YARN session.</p>
    <p id="p11666134091215"><a name="p11666134091215"></a><a name="p11666134091215"></a><strong id="b1947812713510"><a name="b1947812713510"></a><a name="b1947812713510"></a>-yj,--yarnjar &lt;arg&gt;</strong>: Sets the path of the Flink JAR file.</p>
    <p id="p12666240121218"><a name="p12666240121218"></a><a name="p12666240121218"></a><strong id="b67371510135213"><a name="b67371510135213"></a><a name="b67371510135213"></a>-yjm,--yarnjobManagerMemory &lt;arg&gt;</strong>: Sets memory (MB) for JobManagers.</p>
    <p id="p11666640161217"><a name="p11666640161217"></a><a name="p11666640161217"></a><strong id="b291102735219"><a name="b291102735219"></a><a name="b291102735219"></a>-yn,--yarncontainer &lt;arg&gt;</strong>: Specifies the number of containers required for starting a cluster.</p>
    <p id="p0666134071220"><a name="p0666134071220"></a><a name="p0666134071220"></a><strong id="b59951333185218"><a name="b59951333185218"></a><a name="b59951333185218"></a>-ynm,--yarnname &lt;arg&gt;</strong>: Customizes a name for a YARN application.</p>
    <p id="p166604012125"><a name="p166604012125"></a><a name="p166604012125"></a><strong id="b116091756135217"><a name="b116091756135217"></a><a name="b116091756135217"></a>-yq,--yarnquery</strong>: Queries available YARN resources (memory and CPUs).</p>
    <p id="p26661240121211"><a name="p26661240121211"></a><a name="p26661240121211"></a><strong id="b38761615314"><a name="b38761615314"></a><a name="b38761615314"></a>-yqu,--yarnqueue &lt;arg&gt;</strong>: Specifies a YARN queue.</p>
    <p id="p86669405127"><a name="p86669405127"></a><a name="p86669405127"></a><strong id="b124187514534"><a name="b124187514534"></a><a name="b124187514534"></a>-ys,--yarnslots</strong>: Sets the number of slots for each TaskManager.</p>
    <p id="p26665407124"><a name="p26665407124"></a><a name="p26665407124"></a><strong id="b1996118217549"><a name="b1996118217549"></a><a name="b1996118217549"></a>-yt,--yarnship &lt;arg&gt;</strong>: Specifies the path of the file to be sent.</p>
    <p id="p966624015128"><a name="p966624015128"></a><a name="p966624015128"></a><strong id="b879919635416"><a name="b879919635416"></a><a name="b879919635416"></a>-ytm,--yarntaskManagerMemory &lt;arg&gt;</strong>: Sets memory (MB) for TaskManagers.</p>
    <p id="p7666154041216"><a name="p7666154041216"></a><a name="p7666154041216"></a><strong id="b9965203445412"><a name="b9965203445412"></a><a name="b9965203445412"></a>-yz,--yarnzookeeperNamespace &lt;arg&gt;</strong>: Specifies the namespace of ZooKeeper. The value must be the same as the value of <strong id="b01381445556"><a name="b01381445556"></a><a name="b01381445556"></a>yarn-session.sh -z</strong>.</p>
    <p id="p8666134011217"><a name="p8666134011217"></a><a name="p8666134011217"></a><strong id="b1849319725515"><a name="b1849319725515"></a><a name="b1849319725515"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20666144013122"><a name="p20666144013122"></a><a name="p20666144013122"></a>Submit a Flink job.</p>
    <p id="p6666164041220"><a name="p6666164041220"></a><a name="p6666164041220"></a>1. The <strong id="b20543112195718"><a name="b20543112195718"></a><a name="b20543112195718"></a>-y*</strong> parameter is used in <strong id="b559311276579"><a name="b559311276579"></a><a name="b559311276579"></a>yarn-cluster</strong> mode.</p>
    <p id="p866617403121"><a name="p866617403121"></a><a name="p866617403121"></a>2. If the parameter is not <strong id="b2285252583"><a name="b2285252583"></a><a name="b2285252583"></a>-y*</strong>, you need to run the <strong id="b14887181235811"><a name="b14887181235811"></a><a name="b14887181235811"></a>yarn-session</strong> command to start the Flink cluster before running the command to submit a task.</p>
    </td>
    </tr>
    <tr id="row196662400129"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p146666406129"><a name="p146666406129"></a><a name="p146666406129"></a>flink info</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p166661040141215"><a name="p166661040141215"></a><a name="p166661040141215"></a><strong id="b8991134713583"><a name="b8991134713583"></a><a name="b8991134713583"></a>-c,--class &lt;classname&gt;</strong>: Specifies a class as an entry point for program running.</p>
    <p id="p6666194051216"><a name="p6666194051216"></a><a name="p6666194051216"></a><strong id="b15366641105919"><a name="b15366641105919"></a><a name="b15366641105919"></a>-p,--parallelism &lt;parallelism&gt;</strong>: Specifies the DOP for program running.</p>
    <p id="p1666540181218"><a name="p1666540181218"></a><a name="p1666540181218"></a><strong id="b1662431614011"><a name="b1662431614011"></a><a name="b1662431614011"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds a job to a YARN session.</p>
    <p id="p1766615404129"><a name="p1766615404129"></a><a name="p1766615404129"></a><strong id="b18890233608"><a name="b18890233608"></a><a name="b18890233608"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15666940161210"><a name="p15666940161210"></a><a name="p15666940161210"></a>Display the execution plan of the running program (JSON).</p>
    </td>
    </tr>
    <tr id="row1966620404121"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p26661440181210"><a name="p26661440181210"></a><a name="p26661440181210"></a>flink list</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p1666704016124"><a name="p1666704016124"></a><a name="p1666704016124"></a><strong id="b075195820016"><a name="b075195820016"></a><a name="b075195820016"></a>-m,--jobmanager &lt;host:port&gt;</strong>: Specifies a JobManager.</p>
    <p id="p1966716406124"><a name="p1966716406124"></a><a name="p1966716406124"></a><strong id="b2061105016114"><a name="b2061105016114"></a><a name="b2061105016114"></a>-r,--running:</strong> Displays only jobs in the running state.</p>
    <p id="p1066718409128"><a name="p1066718409128"></a><a name="p1066718409128"></a><strong id="b194315581918"><a name="b194315581918"></a><a name="b194315581918"></a>-s,--scheduled</strong>: Displays only jobs in the scheduled state.</p>
    <p id="p7667104031218"><a name="p7667104031218"></a><a name="p7667104031218"></a><strong id="b698371427"><a name="b698371427"></a><a name="b698371427"></a>-z,--zookeeperNamespace &lt;zookeeperNamespace&gt;</strong>: Specifies the namespace of ZooKeeper.</p>
    <p id="p8667840141220"><a name="p8667840141220"></a><a name="p8667840141220"></a><strong id="b14915111920219"><a name="b14915111920219"></a><a name="b14915111920219"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds a job to a YARN session.</p>
    <p id="p76671940201213"><a name="p76671940201213"></a><a name="p76671940201213"></a><strong id="b199481551212"><a name="b199481551212"></a><a name="b199481551212"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1066710408129"><a name="p1066710408129"></a><a name="p1066710408129"></a>Query running programs in the cluster.</p>
    </td>
    </tr>
    <tr id="row196671040171216"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p76674408126"><a name="p76674408126"></a><a name="p76674408126"></a>flink stop</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p206671040131217"><a name="p206671040131217"></a><a name="p206671040131217"></a><strong id="b161702121132"><a name="b161702121132"></a><a name="b161702121132"></a>-m,--jobmanager &lt;host:port&gt;</strong>: Specifies a JobManager.</p>
    <p id="p066724011128"><a name="p066724011128"></a><a name="p066724011128"></a><strong id="b8569131416317"><a name="b8569131416317"></a><a name="b8569131416317"></a>-z,--zookeeperNamespace &lt;zookeeperNamespace&gt;</strong>: Specifies the namespace of ZooKeeper.</p>
    <p id="p366710405126"><a name="p366710405126"></a><a name="p366710405126"></a><strong id="b1892481510312"><a name="b1892481510312"></a><a name="b1892481510312"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds a job to a YARN session.</p>
    <p id="p1766713402129"><a name="p1766713402129"></a><a name="p1766713402129"></a><strong id="b4417817231"><a name="b4417817231"></a><a name="b4417817231"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6310236191215"><a name="p6310236191215"></a><a name="p6310236191215"></a>Forcibly stop a running job (only streaming jobs are supported, and StoppableFunction must be implemented on the source side in service code).</p>
    </td>
    </tr>
    <tr id="row20667144020128"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p66671140171214"><a name="p66671140171214"></a><a name="p66671140171214"></a>flink cancel</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p176671640161210"><a name="p176671640161210"></a><a name="p176671640161210"></a><strong id="b9560033548"><a name="b9560033548"></a><a name="b9560033548"></a>-m,--jobmanager &lt;host:port&gt;</strong>: Specifies a JobManager.</p>
    <p id="p3667204017121"><a name="p3667204017121"></a><a name="p3667204017121"></a><strong id="b589511491549"><a name="b589511491549"></a><a name="b589511491549"></a>-s,--withSavepoint &lt;targetDirectory&gt;</strong>: Triggers a savepoint when a job is canceled. The default directory is <strong id="b20304077520"><a name="b20304077520"></a><a name="b20304077520"></a>state.savepoints.dir</strong>.</p>
    <p id="p14667040201212"><a name="p14667040201212"></a><a name="p14667040201212"></a><strong id="b54141682056"><a name="b54141682056"></a><a name="b54141682056"></a>-z,--zookeeperNamespace &lt;zookeeperNamespace&gt;</strong>: Specifies the namespace of ZooKeeper.</p>
    <p id="p466717409125"><a name="p466717409125"></a><a name="p466717409125"></a><strong id="b1588914101751"><a name="b1588914101751"></a><a name="b1588914101751"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds a job to a YARN session.</p>
    <p id="p266714019127"><a name="p266714019127"></a><a name="p266714019127"></a><strong id="b174971127515"><a name="b174971127515"></a><a name="b174971127515"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14667174010127"><a name="p14667174010127"></a><a name="p14667174010127"></a>Cancel a running job.</p>
    </td>
    </tr>
    <tr id="row2667340161211"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p36673402126"><a name="p36673402126"></a><a name="p36673402126"></a>flink savepoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p1466719406125"><a name="p1466719406125"></a><a name="p1466719406125"></a><strong id="b114771027855"><a name="b114771027855"></a><a name="b114771027855"></a>-d,--dispose &lt;arg&gt;</strong>: Specifies a directory for storing savepoints.</p>
    <p id="p116677406121"><a name="p116677406121"></a><a name="p116677406121"></a><strong id="b14296362518"><a name="b14296362518"></a><a name="b14296362518"></a>-m,--jobmanager &lt;host:port&gt;</strong>: Specifies a JobManager.</p>
    <p id="p76673402128"><a name="p76673402128"></a><a name="p76673402128"></a><strong id="b68432381352"><a name="b68432381352"></a><a name="b68432381352"></a>-z,--zookeeperNamespace &lt;zookeeperNamespace&gt;</strong>: Specifies the namespace of ZooKeeper.</p>
    <p id="p206678404125"><a name="p206678404125"></a><a name="p206678404125"></a><strong id="b1311082313717"><a name="b1311082313717"></a><a name="b1311082313717"></a>-yid,--yarnapplicationId &lt;arg&gt;</strong>: Binds a job to a YARN session.</p>
    <p id="p1667114012124"><a name="p1667114012124"></a><a name="p1667114012124"></a><strong id="b6933624974"><a name="b6933624974"></a><a name="b6933624974"></a>-h</strong>: Gets help information.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26671340111212"><a name="p26671340111212"></a><a name="p26671340111212"></a>Trigger a savepoint.</p>
    </td>
    </tr>
    <tr id="row196671440191210"><td class="cellrowborder" valign="top" width="19.01190119011901%" headers="mcps1.2.4.1.1 "><p id="p1966894016124"><a name="p1966894016124"></a><a name="p1966894016124"></a><strong id="b666864041212"><a name="b666864041212"></a><a name="b666864041212"></a>source</strong><em id="i18668104081219"><a name="i18668104081219"></a><a name="i18668104081219"></a>Client installation directory</em><strong id="b566844018122"><a name="b566844018122"></a><a name="b566844018122"></a>/bigdata_env</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="47.65476547654765%" headers="mcps1.2.4.1.2 "><p id="p19668124071210"><a name="p19668124071210"></a><a name="p19668124071210"></a>None</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p106686404129"><a name="p106686404129"></a><a name="p106686404129"></a>Import client environment variables.</p>
    <p id="p866810404126"><a name="p866810404126"></a><a name="p866810404126"></a>Restriction: If the user uses a custom script (such as <strong id="b1522216444812"><a name="b1522216444812"></a><a name="b1522216444812"></a>A.sh</strong>) and invokes this command in the script, parameters cannot be imported to the <strong id="b164715550817"><a name="b164715550817"></a><a name="b164715550817"></a>A.sh</strong> script. If parameters need to be imported to <strong id="b999411812915"><a name="b999411812915"></a><a name="b999411812915"></a>A.sh</strong>, the user needs to use the secondary invocation method. </p>
    <p id="p15668840141212"><a name="p15668840141212"></a><a name="p15668840141212"></a>For example, if the <strong id="b183700262910"><a name="b183700262910"></a><a name="b183700262910"></a>B.sh</strong> command is invoked in <strong id="b920133119910"><a name="b920133119910"></a><a name="b920133119910"></a>A.sh</strong>, invoke the command in <strong id="b1807194517913"><a name="b1807194517913"></a><a name="b1807194517913"></a>B.sh</strong>. Parameters can be imported to <strong id="b121066351011"><a name="b121066351011"></a><a name="b121066351011"></a>A.sh</strong> but cannot be imported to <strong id="b038193241018"><a name="b038193241018"></a><a name="b038193241018"></a>B.sh</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


