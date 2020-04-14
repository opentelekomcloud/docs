# Creating a Dump Task<a name="dis_01_0047"></a>

If a dump task is created for a DIS stream, data sent to the DIS stream can be automatically dumped to the selected target specified in the dump task.

1.  Use the account to log in to the DIS console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the page and select a region and project.
3.  In the navigation tree on the left, choose .
4.  Click the name of a stream that you want to view. On the displayed page, click the  **Dump Management**  tab. 
5.  Click  **Add Dump Task**. On the  **Add Dump Task**  page, configure dump parameters. Dump task parameters are described in  [Table 1](#table1544912219359).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >A maximum of five dump tasks can be created for each stream.  

6.  Click  **Create Now**.
7.  In the  **Operation**  column of the corresponding  **Task Name**, click  **More**  \>  **View Dump Log**  to view the dump task details of the stream.  [Table 2](#table104664221353)  describes the dump log parameters.

    **Table  1**  Dump task parameters

    <a name="table1544912219359"></a>
    <table><thead align="left"><tr id="row1837162220354"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p11371192223514"><a name="p11371192223514"></a><a name="p11371192223514"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.2"><p id="p1537112212356"><a name="p1537112212356"></a><a name="p1537112212356"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.3"><p id="p103711122163520"><a name="p103711122163520"></a><a name="p103711122163520"></a>Remarks</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row03711622153514"><td class="cellrowborder" colspan="3" valign="top" headers="mcps1.2.4.1.1 mcps1.2.4.1.2 mcps1.2.4.1.3 "><p id="p8371122183517"><a name="p8371122183517"></a><a name="p8371122183517"></a><strong id="b2701658134417"><a name="b2701658134417"></a><a name="b2701658134417"></a>Data Dumping</strong></p>
    <p id="p10371202216357"><a name="p10371202216357"></a><a name="p10371202216357"></a>Location to save data in the stream. </p>
    </td>
    </tr>
    <tr id="row918013142458"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p1019510143452"><a name="p1019510143452"></a><a name="p1019510143452"></a>Dump Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p141959143457"><a name="p141959143457"></a><a name="p141959143457"></a><strong id="b1468178171912"><a name="b1468178171912"></a><a name="b1468178171912"></a>OBS</strong>: After the streaming data is stored to DIS, it is then periodically imported to OBS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p1719521414457"><a name="p1719521414457"></a><a name="p1719521414457"></a>-</p>
    </td>
    </tr>
    <tr id="row837110225357"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p937182216353"><a name="p937182216353"></a><a name="p937182216353"></a>Task Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p15371132211357"><a name="p15371132211357"></a><a name="p15371132211357"></a>Name of the dump task. The names of dump tasks created for the same stream must be unique. A task name must be unique in the stream and is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p9371522113518"><a name="p9371522113518"></a><a name="p9371522113518"></a>-</p>
    </td>
    </tr>
    <tr id="row5371102263510"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p737111223354"><a name="p737111223354"></a><a name="p737111223354"></a>Dump Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p737182214358"><a name="p737182214358"></a><a name="p737182214358"></a>Name of the OBS bucket used to store data from the DIS stream. The bucket name is created when you create a bucket in OBS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p93712225357"><a name="p93712225357"></a><a name="p93712225357"></a>-</p>
    </td>
    </tr>
    <tr id="row1337116224359"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p3371142223516"><a name="p3371142223516"></a><a name="p3371142223516"></a>File Directory</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p73711822193518"><a name="p73711822193518"></a><a name="p73711822193518"></a>Directory created in OBS to store files from the DIS stream. Different directory levels are separated by a forward slash (/). The value cannot start with a forward slash.</p>
    <p id="p203713226352"><a name="p203713226352"></a><a name="p203713226352"></a>This directory name is 0 to 50 characters long.</p>
    <p id="p437115221351"><a name="p437115221351"></a><a name="p437115221351"></a>By default, this parameter is left unspecified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p183712022113519"><a name="p183712022113519"></a><a name="p183712022113519"></a>-</p>
    </td>
    </tr>
    <tr id="row937172223510"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p1237113227352"><a name="p1237113227352"></a><a name="p1237113227352"></a>Time Directory Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p1643163722112"><a name="p1643163722112"></a><a name="p1643163722112"></a>Directory format based on the time. Data will be saved to the directory in the format of time layer under the dump file directory in the OBS bucket.</p>
    <p id="p11371122113511"><a name="p11371122113511"></a><a name="p11371122113511"></a>For example, if the time directory is accurate to day, the data save path is "bucket name/dump file directory/year/month/day".</p>
    <div class="p" id="p103711522163519"><a name="p103711522163519"></a><a name="p103711522163519"></a>Possible values are as follows:<a name="ul33711722133517"></a><a name="ul33711722133517"></a><ul id="ul33711722133517"><li>N/A: If this field is left blank, the time directory format will not be used.</li><li>yyyy: year.</li><li>yyyy/MM: year and month.</li><li>yyyy/MM/dd: year, month, and day.</li><li>yyyy/MM/dd/HH: year, month, day, and hour.</li><li>yyyy/MM/dd/HH/mm: year, month, day, hour, and minute.</li></ul>
    </div>
    <p id="p103719228358"><a name="p103719228358"></a><a name="p103719228358"></a>You can only select but not enter a value in this field.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p1371322123511"><a name="p1371322123511"></a><a name="p1371322123511"></a>-</p>
    </td>
    </tr>
    <tr id="row1338782283515"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p153713229359"><a name="p153713229359"></a><a name="p153713229359"></a>Record Delimiter</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p037115226353"><a name="p037115226353"></a><a name="p037115226353"></a>Delimiter used to separate different dump records.</p>
    <div class="p" id="p538714226359"><a name="p538714226359"></a><a name="p538714226359"></a>Possible values are as follows:<a name="ul4387722103510"></a><a name="ul4387722103510"></a><ul id="ul4387722103510"><li>Comma (,)</li><li>Semicolon (;)</li><li>Vertical bar (|)</li><li>Newline (\n)</li><li>NULL</li></ul>
    </div>
    <p id="p103874223358"><a name="p103874223358"></a><a name="p103874223358"></a>You can only select but not enter a value in this field.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p43872227359"><a name="p43872227359"></a><a name="p43872227359"></a>-</p>
    </td>
    </tr>
    <tr id="row9387722163518"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p16387172216357"><a name="p16387172216357"></a><a name="p16387172216357"></a>Dump Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.2 "><p id="p4387172214359"><a name="p4387172214359"></a><a name="p4387172214359"></a>User-defined interval at which data is imported from the current DIS stream into OBS. If no data is pushed to the DIS stream during the current interval, no dump file package will be generated.</p>
    <p id="p1938732213352"><a name="p1938732213352"></a><a name="p1938732213352"></a>Value range: 30s to 900s</p>
    <p id="p173876227356"><a name="p173876227356"></a><a name="p173876227356"></a>Unit: second</p>
    <p id="p138716221355"><a name="p138716221355"></a><a name="p138716221355"></a>Default value: 300s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.3 "><p id="p1338782293511"><a name="p1338782293511"></a><a name="p1338782293511"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Dump log parameters

    <a name="table104664221353"></a>
    <table><thead align="left"><tr id="row04666222352"><th class="cellrowborder" valign="top" width="40.04%" id="mcps1.2.3.1.1"><p id="p0466022183515"><a name="p0466022183515"></a><a name="p0466022183515"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.96%" id="mcps1.2.3.1.2"><p id="p14466152283516"><a name="p14466152283516"></a><a name="p14466152283516"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10466132243518"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p446616229353"><a name="p446616229353"></a><a name="p446616229353"></a>Start Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p24661422173511"><a name="p24661422173511"></a><a name="p24661422173511"></a>Time when the dump log is created.</p>
    <div class="p" id="p2046622214354"><a name="p2046622214354"></a><a name="p2046622214354"></a>Format: YYYY/MM/dd HH:mm:ss GTM<a name="ul1446622220356"></a><a name="ul1446622220356"></a><ul id="ul1446622220356"><li>YYYY: year.</li><li>MM: month.</li><li>dd: date.</li><li>HH: hour.</li><li>mm: minute.</li><li>ss: second.</li><li>GMT: time zone.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row134667228356"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p15466922133519"><a name="p15466922133519"></a><a name="p15466922133519"></a>End Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p13466192263518"><a name="p13466192263518"></a><a name="p13466192263518"></a>Time when you finish creating the dump log.</p>
    <div class="p" id="p174668222357"><a name="p174668222357"></a><a name="p174668222357"></a>Format: YYYY/MM/dd HH:mm:ss GTM<a name="ul164666224355"></a><a name="ul164666224355"></a><ul id="ul164666224355"><li>YYYY: year.</li><li>MM: month.</li><li>dd: date.</li><li>HH: hour.</li><li>mm: minute.</li><li>ss: second.</li><li>GMT: time zone.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row6466162273519"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p144669224353"><a name="p144669224353"></a><a name="p144669224353"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><div class="p" id="p246692213519"><a name="p246692213519"></a><a name="p246692213519"></a>Dump status.<a name="ul246692293517"></a><a name="ul246692293517"></a><ul id="ul246692293517"><li>Succeeded</li><li>Failed</li><li>Abnormal</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row4466132223515"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p746632213518"><a name="p746632213518"></a><a name="p746632213518"></a>Dump File Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p17466172212356"><a name="p17466172212356"></a><a name="p17466172212356"></a>Name of the file that is dumped to the target service. The user records read from the stream are written into the file and then dumped to the target service (such as OBS) in the file format.</p>
    </td>
    </tr>
    <tr id="row746612228351"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p14667223353"><a name="p14667223353"></a><a name="p14667223353"></a>Records</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p346615221355"><a name="p346615221355"></a><a name="p346615221355"></a>Number of the records uploaded between the time when you start to create a dump log to the time when you finish creating it.</p>
    </td>
    </tr>
    <tr id="row184665227350"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p1646602217359"><a name="p1646602217359"></a><a name="p1646602217359"></a>Data Amount (bytes)</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p154661122193514"><a name="p154661122193514"></a><a name="p154661122193514"></a>Amount of the data uploaded between the time when you start to create the dump log to the time when you finish creating it.</p>
    <p id="p246692223510"><a name="p246692223510"></a><a name="p246692223510"></a>Unit: byte</p>
    </td>
    </tr>
    <tr id="row184661226353"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="p2466222173511"><a name="p2466222173511"></a><a name="p2466222173511"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="p296917314215"><a name="p296917314215"></a><a name="p296917314215"></a>Dump failure details.</p>
    <a name="ul1997723125"></a><a name="ul1997723125"></a><ul id="ul1997723125"><li>If <span class="parmname" id="parmname50799505165942"><a name="parmname50799505165942"></a><a name="parmname50799505165942"></a><b>Status</b></span> is <span class="parmvalue" id="parmvalue54542363165942"><a name="parmvalue54542363165942"></a><a name="parmvalue54542363165942"></a><b>Succeeded</b></span>, the column is not operable.</li><li>If <span class="parmname" id="parmname16405085165942"><a name="parmname16405085165942"></a><a name="parmname16405085165942"></a><b>Status</b></span> is <span class="parmvalue" id="parmvalue13428044165942"><a name="parmvalue13428044165942"></a><a name="parmvalue13428044165942"></a><b>Failed</b></span>, click <span class="uicontrol" id="uicontrol53743536165942"><a name="uicontrol53743536165942"></a><a name="uicontrol53743536165942"></a><b>View Details</b></span> to view dump details.</li><li>If <span class="parmname" id="parmname12499172518209"><a name="parmname12499172518209"></a><a name="parmname12499172518209"></a><b>Status</b></span> is <span class="parmvalue" id="parmvalue1349912512209"><a name="parmvalue1349912512209"></a><a name="parmvalue1349912512209"></a><b>Abnormal</b></span>, click <span class="uicontrol" id="uicontrol8499125112013"><a name="uicontrol8499125112013"></a><a name="uicontrol8499125112013"></a><b>View Details</b></span> to view dump details.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Modifying and Enabling Dump Tasks<a name="section11674458115116"></a>

After creating a stream and adding a dump task successfully, you can modify the attributes of the created stream.

1.  Log in to the DIS console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the page and select a region and project.
3.  In the navigation tree, choose  **Stream Management**.
4.  Click the name of a stream that you want to view. On the displayed page, click the  **Dump Management**  tab. Alternatively, in the  **Operation**  column of a stream that you want to view, click  **More**  and choose  **View Dump Task**  from the drop-down list.
5.  In the  **Operation**  column of the stream for which a dump task has been added, perform the following operations:
    1.  Choose  **More \> Modify**  to modify the dump task.
    2.  Choose  **More \> Start**  to start the dump task.
    3.  Choose  **More \> Pause**  to pause the dump task.


