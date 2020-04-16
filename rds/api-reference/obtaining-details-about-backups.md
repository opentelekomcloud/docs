# Obtaining Details About Backups<a name="rds_09_0005"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain details about backups.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section201140547419"></a>

This API is used to query full backups of MySQL, PostgreSQL, and Microsoft SQL Server databases and incremental backups of MySQL and PostgreSQL databases.

## URI<a name="section28961517113719"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/backups?instance\_id=\{instance\_id\}&backup\_id=\{backup\_id\}&backup\_type=\{backup\_type\}&offset=\{offset\}&limit=\{limit\}&begin\_time=\{begin \_time\}&end\_time=\{end\_time\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/backups?instance\_id=43e4feaab48f11e89039fa163ebaa7e4br01&backup\_id=c0c9f155c7b7423a9d30f0175998b63bbr01&backup\_type=auto&offset=0&limit=10&begin\_time=2018-08-06T10:41:14+0800&end\_time=2018-08-16T10:41:14+0800

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b23141829155914"><a name="b23141829155914"></a><a name="b23141829155914"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.38%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b133151329155912"><a name="b133151329155912"></a><a name="b133151329155912"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.93%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b193151329155914"><a name="b193151329155914"></a><a name="b193151329155914"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p1511718177816"><a name="p1511718177816"></a><a name="p1511718177816"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p64450739155220"><a name="p64450739155220"></a><a name="p64450739155220"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row116836431146"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p15683443151415"><a name="p15683443151415"></a><a name="p15683443151415"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p1568316439148"><a name="p1568316439148"></a><a name="p1568316439148"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p116832437149"><a name="p116832437149"></a><a name="p116832437149"></a>Specifies the backup ID.</p>
    </td>
    </tr>
    <tr id="row93931049203017"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p840844912305"><a name="p840844912305"></a><a name="p840844912305"></a>backup_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p134086490304"><a name="p134086490304"></a><a name="p134086490304"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p5408194916301"><a name="p5408194916301"></a><a name="p5408194916301"></a>Specifies the backup type. Value:</p>
    <a name="ul189282231193"></a><a name="ul189282231193"></a><ul id="ul189282231193"><li><strong id="b9681345131518"><a name="b9681345131518"></a><a name="b9681345131518"></a>auto</strong>: automated full backup</li><li><strong id="b96513542159"><a name="b96513542159"></a><a name="b96513542159"></a>manual</strong>: manual full backup</li><li><strong id="b143921216161"><a name="b143921216161"></a><a name="b143921216161"></a>fragment</strong>: differential full backup</li><li><strong id="b96431097168"><a name="b96431097168"></a><a name="b96431097168"></a>incremental</strong>: automated incremental backup</li></ul>
    </td>
    </tr>
    <tr id="row115851253324"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p7585625113212"><a name="p7585625113212"></a><a name="p7585625113212"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p14241079113"><a name="p14241079113"></a><a name="p14241079113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p19585152511326"><a name="p19585152511326"></a><a name="p19585152511326"></a>Specifies the index position. If <strong id="b1332842919590"><a name="b1332842919590"></a><a name="b1332842919590"></a>offset</strong> is set to <em id="i23281229155910"><a name="i23281229155910"></a><a name="i23281229155910"></a>N</em>, the resource query starts from the N+1 piece of data. The value is <strong id="b1232862914599"><a name="b1232862914599"></a><a name="b1232862914599"></a>0</strong> by default, indicating that the query starts from the first piece of data. The value must be a positive number.</p>
    </td>
    </tr>
    <tr id="row16990146131215"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p139904468126"><a name="p139904468126"></a><a name="p139904468126"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p4990946181217"><a name="p4990946181217"></a><a name="p4990946181217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p189901246201211"><a name="p189901246201211"></a><a name="p189901246201211"></a>Specifies the number of records to be queried. The default value is <strong id="b16325644124312"><a name="b16325644124312"></a><a name="b16325644124312"></a>100</strong>. The value cannot be a negative number. The minimum value is <strong id="b15325194411434"><a name="b15325194411434"></a><a name="b15325194411434"></a>1</strong> and the maximum value is <strong id="b732694416437"><a name="b732694416437"></a><a name="b732694416437"></a>100</strong>.</p>
    </td>
    </tr>
    <tr id="row820715219196"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p1250401361914"><a name="p1250401361914"></a><a name="p1250401361914"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p5426101961917"><a name="p5426101961917"></a><a name="p5426101961917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p1942671971913"><a name="p1942671971913"></a><a name="p1942671971913"></a>Specifies the start time for obtaining the backup list. The format of the start time is "yyyy-mm-ddThh:mm:ssZ".</p>
    <p id="p442615191195"><a name="p442615191195"></a><a name="p442615191195"></a><strong id="b457716103450"><a name="b457716103450"></a><a name="b457716103450"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b257731054515"><a name="b257731054515"></a><a name="b257731054515"></a>Z</strong> indicates the time zone offset.</p>
    <div class="note" id="note1546714962017"><a name="note1546714962017"></a><a name="note1546714962017"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9467189102011"><a name="p9467189102011"></a><a name="p9467189102011"></a>When <span class="parmname" id="parmname1170415591469"><a name="parmname1170415591469"></a><a name="parmname1170415591469"></a><b>begin_time</b></span> is not empty, <span class="parmname" id="parmname91712464711"><a name="parmname91712464711"></a><a name="parmname91712464711"></a><b>end_time</b></span> is mandatory.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row659875021813"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p1050431341917"><a name="p1050431341917"></a><a name="p1050431341917"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.4.1.2 "><p id="p14262196190"><a name="p14262196190"></a><a name="p14262196190"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.93%" headers="mcps1.2.4.1.3 "><p id="p1542651981915"><a name="p1542651981915"></a><a name="p1542651981915"></a>Specifies the end time for obtaining the backup list. The format of the end time is "yyyy-mm-ddThh:mm:ssZ" and the end time must be later than the start time.</p>
    <p id="p10426101991919"><a name="p10426101991919"></a><a name="p10426101991919"></a><strong id="b10336729175910"><a name="b10336729175910"></a><a name="b10336729175910"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b15336192916598"><a name="b15336192916598"></a><a name="b15336192916598"></a>Z</strong> indicates the time zone offset.</p>
    <div class="note" id="note10667645111414"><a name="note10667645111414"></a><a name="note10667645111414"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14667845141419"><a name="p14667845141419"></a><a name="p14667845141419"></a>When <span class="parmname" id="parmname1485717617479"><a name="parmname1485717617479"></a><a name="parmname1485717617479"></a><b>end_time</b></span> is not empty, <span class="parmname" id="parmname1530818954711"><a name="parmname1530818954711"></a><a name="parmname1530818954711"></a><b>begin_time</b></span> is mandatory.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section28070818101549"></a>

None

## Response<a name="section28521534113742"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table11854613"></a>
    <table><thead align="left"><tr id="row48728718"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p54712068"><a name="p54712068"></a><a name="p54712068"></a><strong id="b8342629155915"><a name="b8342629155915"></a><a name="b8342629155915"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a><strong id="b1334322955920"><a name="b1334322955920"></a><a name="b1334322955920"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p570775"><a name="p570775"></a><a name="p570775"></a><strong id="b734317290590"><a name="b734317290590"></a><a name="b734317290590"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46232835"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p24228398437"><a name="p24228398437"></a><a name="p24228398437"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p4491214"><a name="p4491214"></a><a name="p4491214"></a>Indicates the backup list.</p>
    <p id="p19557583458"><a name="p19557583458"></a><a name="p19557583458"></a>For details, see <a href="#table52869820">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1115175204712"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p611517554719"><a name="p611517554719"></a><a name="p611517554719"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p2756199134714"><a name="p2756199134714"></a><a name="p2756199134714"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1011512524711"><a name="p1011512524711"></a><a name="p1011512524711"></a>Indicates the total number of records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  backups field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b1235192919593"><a name="b1235192919593"></a><a name="b1235192919593"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b1235262920592"><a name="b1235262920592"></a><a name="b1235262920592"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b2035242915595"><a name="b2035242915595"></a><a name="b2035242915595"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8307988"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p127914503011"><a name="p127914503011"></a><a name="p127914503011"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p027913523010"><a name="p027913523010"></a><a name="p027913523010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p172799513012"><a name="p172799513012"></a><a name="p172799513012"></a>Indicates the backup ID.</p>
    </td>
    </tr>
    <tr id="row938736142915"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p92797519305"><a name="p92797519305"></a><a name="p92797519305"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p52796523018"><a name="p52796523018"></a><a name="p52796523018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p72791658307"><a name="p72791658307"></a><a name="p72791658307"></a>Indicates the backup name.</p>
    </td>
    </tr>
    <tr id="row144491595298"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p4279155173020"><a name="p4279155173020"></a><a name="p4279155173020"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p11279125203010"><a name="p11279125203010"></a><a name="p11279125203010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p72791553309"><a name="p72791553309"></a><a name="p72791553309"></a>Indicates the backup type. Value:</p>
    <a name="ul139214209182"></a><a name="ul139214209182"></a><ul id="ul139214209182"><li><strong id="rds_09_0005_b9681345131518"><a name="rds_09_0005_b9681345131518"></a><a name="rds_09_0005_b9681345131518"></a>auto</strong>: automated full backup</li><li><strong id="rds_09_0005_b96513542159"><a name="rds_09_0005_b96513542159"></a><a name="rds_09_0005_b96513542159"></a>manual</strong>: manual full backup</li><li><strong id="rds_09_0005_b143921216161"><a name="rds_09_0005_b143921216161"></a><a name="rds_09_0005_b143921216161"></a>fragment</strong>: differential full backup</li><li><strong id="rds_09_0005_b96431097168"><a name="rds_09_0005_b96431097168"></a><a name="rds_09_0005_b96431097168"></a>incremental</strong>: automated incremental backup</li></ul>
    </td>
    </tr>
    <tr id="row1351211233292"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p2027911543018"><a name="p2027911543018"></a><a name="p2027911543018"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p72791059304"><a name="p72791059304"></a><a name="p72791059304"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1327935123018"><a name="p1327935123018"></a><a name="p1327935123018"></a>Indicates the backup size in kB.</p>
    </td>
    </tr>
    <tr id="row14746325132919"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p192791152308"><a name="p192791152308"></a><a name="p192791152308"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p22798533017"><a name="p22798533017"></a><a name="p22798533017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p10279105193013"><a name="p10279105193013"></a><a name="p10279105193013"></a>Indicates the backup status. Value:</p>
    <a name="ul132531445184"></a><a name="ul132531445184"></a><ul id="ul132531445184"><li>BUILDING: Backup in progress</li><li>COMPLETED: Backup completed</li><li>FAILED: Backup failed</li><li>DELETING: Backup being deleted</li></ul>
    </td>
    </tr>
    <tr id="row168721916122920"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p527917513306"><a name="p527917513306"></a><a name="p527917513306"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p1527919573018"><a name="p1527919573018"></a><a name="p1527919573018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p727911543019"><a name="p727911543019"></a><a name="p727911543019"></a>Indicates the backup start time in the "yyyy-mm-ddThh:mm:ssZ" format.</p>
    <p id="p92795593018"><a name="p92795593018"></a><a name="p92795593018"></a><strong id="b113651829165920"><a name="b113651829165920"></a><a name="b113651829165920"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b23657292598"><a name="b23657292598"></a><a name="b23657292598"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row1938722120299"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1227912514309"><a name="p1227912514309"></a><a name="p1227912514309"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p627916517309"><a name="p627916517309"></a><a name="p627916517309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p9750141761712"><a name="p9750141761712"></a><a name="p9750141761712"></a>Indicates the backup end time.</p>
    <a name="ul99235321713"></a><a name="ul99235321713"></a><ul id="ul99235321713"><li>In a full backup, it indicates the full backup end time.</li><li>In a MySQL incremental backup, it indicates the time when the last transaction in the backup file is submitted.</li></ul>
    <p id="p2027975153016"><a name="p2027975153016"></a><a name="p2027975153016"></a>The format is yyyy-mm-ddThh:mm:ssZ. <strong id="b842352706151812"><a name="b842352706151812"></a><a name="b842352706151812"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706153833"><a name="b842352706153833"></a><a name="b842352706153833"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row16168101920298"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p327925163018"><a name="p327925163018"></a><a name="p327925163018"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p1427918593019"><a name="p1427918593019"></a><a name="p1427918593019"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p15279195123012"><a name="p15279195123012"></a><a name="p15279195123012"></a>Indicates the database version.</p>
    <p id="p279492744510"><a name="p279492744510"></a><a name="p279492744510"></a>For details, see <a href="#table32267243">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row1912113128299"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p32795583015"><a name="p32795583015"></a><a name="p32795583015"></a>databases</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p527912519305"><a name="p527912519305"></a><a name="p527912519305"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1627917517304"><a name="p1627917517304"></a><a name="p1627917517304"></a>Indicates a list of self-built Microsoft SQL Server databases that support partial backups.</p>
    <p id="p48331337114511"><a name="p48331337114511"></a><a name="p48331337114511"></a>For details, see <a href="#table4541911203517">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row11777181462914"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p62796513300"><a name="p62796513300"></a><a name="p62796513300"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p10279255302"><a name="p10279255302"></a><a name="p10279255302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p827914583018"><a name="p827914583018"></a><a name="p827914583018"></a>Indicates the ID of the DB instance for which the backup is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  datastore field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b143751929165911"><a name="b143751929165911"></a><a name="b143751929165911"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b19376122914598"><a name="b19376122914598"></a><a name="b19376122914598"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b103771029125911"><a name="b103771029125911"></a><a name="b103771029125911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1051011533343"><a name="p1051011533343"></a><a name="p1051011533343"></a>Indicates the DB engine. Its value can be any of the following and is case-insensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row130794519346"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p104325063513"><a name="p104325063513"></a><a name="p104325063513"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p194327013514"><a name="p194327013514"></a><a name="p194327013514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p043213063517"><a name="p043213063517"></a><a name="p043213063517"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  databases field data structure description

    <a name="table4541911203517"></a>
    <table><thead align="left"><tr id="row1855714116356"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p255718115359"><a name="p255718115359"></a><a name="p255718115359"></a><strong id="b938442914597"><a name="b938442914597"></a><a name="b938442914597"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p4557181118353"><a name="p4557181118353"></a><a name="p4557181118353"></a><strong id="b143851729135912"><a name="b143851729135912"></a><a name="b143851729135912"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p1255717116353"><a name="p1255717116353"></a><a name="p1255717116353"></a><strong id="b5385112917590"><a name="b5385112917590"></a><a name="b5385112917590"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row125579116351"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1155714112354"><a name="p1155714112354"></a><a name="p1155714112354"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p4557101117355"><a name="p4557101117355"></a><a name="p4557101117355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p3573151117359"><a name="p3573151117359"></a><a name="p3573151117359"></a>Indicates the name of the self-built database.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    Obtaining a backup list of a MySQL DB instance:

    ```
    {
    	"backups": [{
    		"id": "43e4feaab48f11e89039fa163ebaa7e4br01",
    		"name": "xxxx.xxx",
    		"type": "auto",
    		"size": 2803,
    		"status": "COMPLETED",
    		"begin_time": "2018-08-06T12:41:14+0800",
    		"end_time": "2018-08-06T12:43:14+0800",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.6"
    		},
    		"instance_id": "a48e43ff268f4c0e879652d65e63d0fbin01"
    	}],
    	"total_count": 1
    }
    ```

    Obtaining a backup list of a PostgreSQL DB instance:

    ```
    {
    	"backups": [{
    		"id": "43e4feaab48f11e89039fa163ebaa7e4br03",
    		"name": "xxxx.xxx",
    		"type": "incremental",
    		"size": 2803,
    		"status": "COMPLETED",
    		"begin_time": "2018 - 08 - 06 T12: 41: 14 + 0800",
    		"end_time": "2018 - 08 - 06 T12: 43: 14 + 0800",
    		"datastore": {
    			"type": "PostgreSQL",
    			"version": "9.6"
    		},
    		"instance_id": "a48e43ff268f4c0e879652d65e63d0fbin03 "
    	}],
    	"total_count": 1
    }
    ```

    Obtaining a backup list of a Microsoft SQL Server DB instance:

    ```
    {
    	"backups": [{
    		"id ": "43e4feaab48f11e89039fa163ebaa7e4br04",
    		"name": "xxxx.xxx",
    		"type": "manual",
    		"size": 2803,
    		"status": "COMPLETED",
    		"begin_time": "2018-08-06T12:41:14+0800",
    		"end_time": "2018-08-06T12:43:14+0800",
    		"datastore": {
    			"type": "SQLServer",
    			"version": "2014_WEB"
    		},
    		"databases": [{
    			"name": "user01"
    		}, {
    			"name": "user02"
    		}],
    		"instance_id": "a48e43ff268f4c0e879652d65e63d0fbin04"
    	}],
    	"total_count": 1
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

