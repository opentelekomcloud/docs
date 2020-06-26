# Obtaining the Link for Downloading a Backup File<a name="rds_09_0006"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain the link for downloading a backup file.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section1956333494215"></a>

This API is used to query full backups of MySQL, PostgreSQL, and Microsoft SQL Server databases and incremental backups of MySQL and PostgreSQL databases.

## URI<a name="section28961517113719"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/backup-files?backup\_id=\{backup\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/97b026aa9cc4417888c14c84a1ad9860/backup-files?backup\_id=c0c9f155c7b7423a9d30f0175998b63bbr01

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b589942714598"><a name="b589942714598"></a><a name="b589942714598"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.849999999999998%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b589932717595"><a name="b589932717595"></a><a name="b589932717595"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.46%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b7900142795915"><a name="b7900142795915"></a><a name="b7900142795915"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.46%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p35815231088"><a name="p35815231088"></a><a name="p35815231088"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row116836431146"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p15683443151415"><a name="p15683443151415"></a><a name="p15683443151415"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.849999999999998%" headers="mcps1.2.4.1.2 "><p id="p1568316439148"><a name="p1568316439148"></a><a name="p1568316439148"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.46%" headers="mcps1.2.4.1.3 "><p id="p116832437149"><a name="p116832437149"></a><a name="p116832437149"></a>Specifies the backup ID.</p>
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
    <table><thead align="left"><tr id="row48728718"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p54712068"><a name="p54712068"></a><a name="p54712068"></a><strong id="b16909172775920"><a name="b16909172775920"></a><a name="b16909172775920"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a><strong id="b991015276593"><a name="b991015276593"></a><a name="b991015276593"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p570775"><a name="p570775"></a><a name="p570775"></a><strong id="b14910132712593"><a name="b14910132712593"></a><a name="b14910132712593"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46232835"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>files</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p24228398437"><a name="p24228398437"></a><a name="p24228398437"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p4491214"><a name="p4491214"></a><a name="p4491214"></a>Indicates the list of backup files.</p>
    <p id="p14951152394619"><a name="p14951152394619"></a><a name="p14951152394619"></a>For details, see <a href="#table52869820">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1115175204712"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p611517554719"><a name="p611517554719"></a><a name="p611517554719"></a>bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p2756199134714"><a name="p2756199134714"></a><a name="p2756199134714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1011512524711"><a name="p1011512524711"></a><a name="p1011512524711"></a>Indicates the name of the bucket where the file is located.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  files field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b1291717278595"><a name="b1291717278595"></a><a name="b1291717278595"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b191792765916"><a name="b191792765916"></a><a name="b191792765916"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b1918152714598"><a name="b1918152714598"></a><a name="b1918152714598"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row938736142915"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p92797519305"><a name="p92797519305"></a><a name="p92797519305"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p52796523018"><a name="p52796523018"></a><a name="p52796523018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p72791658307"><a name="p72791658307"></a><a name="p72791658307"></a>Indicates the file name.</p>
    </td>
    </tr>
    <tr id="row144491595298"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p4279155173020"><a name="p4279155173020"></a><a name="p4279155173020"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p11279125203010"><a name="p11279125203010"></a><a name="p11279125203010"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p16279165203010"><a name="p16279165203010"></a><a name="p16279165203010"></a>Indicates the file size in KB.</p>
    </td>
    </tr>
    <tr id="row14746325132919"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p42659508172"><a name="p42659508172"></a><a name="p42659508172"></a>download_link</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p726525091715"><a name="p726525091715"></a><a name="p726525091715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p112651850111716"><a name="p112651850111716"></a><a name="p112651850111716"></a>Indicates the link for downloading the backup file.</p>
    </td>
    </tr>
    <tr id="row168721916122920"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p29686511175"><a name="p29686511175"></a><a name="p29686511175"></a>link_expired_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.4.1.2 "><p id="p79681651201718"><a name="p79681651201718"></a><a name="p79681651201718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p727911543019"><a name="p727911543019"></a><a name="p727911543019"></a>Indicates the link expiration time. The format is "yyyy-mm-ddThh:mm:ssZ". <strong id="b19925327145917"><a name="b19925327145917"></a><a name="b19925327145917"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b149251727195919"><a name="b149251727195919"></a><a name="b149251727195919"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
       "files": [
        {
            "name": "43e4feaab48f11e89039fa163ebaa7e4br01.xxx",
            "size": 2803,
            "download_link":"https://obs.domainname.com/rdsbucket.username.1/xxxxxx",
            "link_expired_time":"2018-08-016T10:15:14+0800"
         }
         ],
        "bucket": "rdsbucket.bucketname"
    }
    
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

