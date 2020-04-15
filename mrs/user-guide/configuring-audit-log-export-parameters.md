# Configuring Audit Log Export Parameters<a name="EN-US_TOPIC_0125376132"></a>

## Scenario<a name="section23966615171256"></a>

If MRS audit logs are stored in the system for a long time, the disk space for data directories may become insufficient. You can set export parameters to automatically export audit logs to a specified directory on the OBS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The audit logs to be exported include both the service and management audit logs.  
>-   Service audit logs are compressed automatically at 03:00 a.m. every day and save in  **/var/log/Bigdata/audit/bk/** on the active management node. The file name format is **<yyyy-MM-dd\_HH-mm-ss\>.tar.gz**. A maximum of seven log files can be saved by default. After the number of files has reached the maximum value, the earliest file will be deleted when a new one is generated.  
>-   When you export management audit logs, the logs that are generated between the time of the last successful export and the current time are exported. When the number of records in a management audit log reaches 100,000, the system dumps the first 90,000 records to a local file and retains the rest 10,000 records in the database. The log file is dumped to  **$\{BIGDATA\_DATA\_HOME\}/dbdata\_om/dumpData/iam/operatelog** on the active management node. The file name format is **OperateLog\_store\_YY\_MM\_DD\_HH\_MM\_SS.csv**. A maximum of 50 management audit logs can be saved.  

## Prerequisites<a name="section558878317137"></a>

-   You have obtained the AK and SK of the username. For details, see  **My Credential** \> **User Guide** \> **How Do I Manage Access Keys?**.
-   You have created a bucket in the OBS. For details, see  **Object Storage Service** \> **User Guide** \> **Quick Start** \> **Common Operations Using OBS Console** \> **Creating a Bucket**.

## Procedure<a name="section27949047171415"></a>

1.  On MRS Manager, click  **System**.
2.  Click  **Export Audit Log** in **Maintenance**.

    **Table  1**  Parameters for exporting audit logs

    <a name="table59139916171458"></a>
    <table><thead align="left"><tr id="row13611619171458"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.4.1.1"><p id="p28799367171458"><a name="p28799367171458"></a><a name="p28799367171458"></a><strong id="b4407975492214"><a name="b4407975492214"></a><a name="b4407975492214"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35%" id="mcps1.2.4.1.2"><p id="p51047354171458"><a name="p51047354171458"></a><a name="p51047354171458"></a><strong id="b201422092219"><a name="b201422092219"></a><a name="b201422092219"></a>Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.3"><p id="p41195047171458"><a name="p41195047171458"></a><a name="p41195047171458"></a><strong id="b4680620392223"><a name="b4680620392223"></a><a name="b4680620392223"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48464500171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p33310409171458"><a name="p33310409171458"></a><a name="p33310409171458"></a>Export Audit Log</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><a name="ul13788623171458"></a><a name="ul13788623171458"></a><ul id="ul13788623171458"><li><a name="image1487081217655"></a><a name="image1487081217655"></a><span><img id="image1487081217655" src="figures/wwx437827-中软基础平台部-datasight-image-8602897a-b990-4838-8c30-36b5459e48ff-57.png"></span>&nbsp;</li><li><a name="image99561931783"></a><a name="image99561931783"></a><span><img id="image99561931783" src="figures/wwx437827-中软基础平台部-datasight-image-dcd81e5f-3df4-40ac-a2e7-fe1afef5102f-58.png"></span>&nbsp;</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p4410636171458"><a name="p4410636171458"></a><a name="p4410636171458"></a>Mandatory</p>
    <p id="p94113692422"><a name="p94113692422"></a><a name="p94113692422"></a>Indicates whether to enable the audit log export function.</p>
    <a name="ul62002798163126"></a><a name="ul62002798163126"></a><ul id="ul62002798163126"><li><a name="image35774533163126"></a><a name="image35774533163126"></a><span><img id="image35774533163126" src="figures/wwx437827-中软基础平台部-datasight-image-8602897a-b990-4838-8c30-36b5459e48ff-59.png"></span>: Enabled</li></ul>
    <a name="ul1089276919373"></a><a name="ul1089276919373"></a><ul id="ul1089276919373"><li><a name="image13231465163119"></a><a name="image13231465163119"></a><span><img id="image13231465163119" src="figures/wwx437827-中软基础平台部-datasight-image-dcd81e5f-3df4-40ac-a2e7-fe1afef5102f-60.png"></span>: Disabled</li></ul>
    </td>
    </tr>
    <tr id="row14268268171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p14879036171458"><a name="p14879036171458"></a><a name="p14879036171458"></a>Start Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p195780479823"><a name="p195780479823"></a><a name="p195780479823"></a>7/24/2017 09:00:00 (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p26868368171458"><a name="p26868368171458"></a><a name="p26868368171458"></a>Mandatory</p>
    <p id="p4704184892519"><a name="p4704184892519"></a><a name="p4704184892519"></a>Indicates the start time for audit log export.</p>
    </td>
    </tr>
    <tr id="row55491030171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p65588417171458"><a name="p65588417171458"></a><a name="p65588417171458"></a>Period</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p11061565171458"><a name="p11061565171458"></a><a name="p11061565171458"></a>1 day (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p23571569171458"><a name="p23571569171458"></a><a name="p23571569171458"></a>Mandatory</p>
    <p id="p5693661792619"><a name="p5693661792619"></a><a name="p5693661792619"></a>Indicates the interval for exporting audit logs. The value ranges from 1 day to 5 days.</p>
    </td>
    </tr>
    <tr id="row10817536171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p3805244171458"><a name="p3805244171458"></a><a name="p3805244171458"></a>Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p39789381171458"><a name="p39789381171458"></a><a name="p39789381171458"></a>mrs-bucket (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p1714434171458"><a name="p1714434171458"></a><a name="p1714434171458"></a>Mandatory</p>
    <p id="p4718142492716"><a name="p4718142492716"></a><a name="p4718142492716"></a>Indicates the name of the OBS bucket to which audit logs are exported.</p>
    </td>
    </tr>
    <tr id="row15429912171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p41863359171458"><a name="p41863359171458"></a><a name="p41863359171458"></a>OBS Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p35488910171458"><a name="p35488910171458"></a><a name="p35488910171458"></a>opt/omm/oms/auditLog (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p56029486171458"><a name="p56029486171458"></a><a name="p56029486171458"></a>Mandatory</p>
    <p id="p5553073992828"><a name="p5553073992828"></a><a name="p5553073992828"></a>Indicates the OBS path for exporting audit logs.</p>
    </td>
    </tr>
    <tr id="row34503332171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p43306496171458"><a name="p43306496171458"></a><a name="p43306496171458"></a>AK</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p18165248171458"><a name="p18165248171458"></a><a name="p18165248171458"></a>XXX (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p62098956171458"><a name="p62098956171458"></a><a name="p62098956171458"></a>Mandatory</p>
    <p id="p1329014993013"><a name="p1329014993013"></a><a name="p1329014993013"></a>Indicates the user's <span id="ph23406790105425"><a name="ph23406790105425"></a><a name="ph23406790105425"></a>Access Key ID (</span>AK<span id="ph7585740105429"><a name="ph7585740105429"></a><a name="ph7585740105429"></a>)</span> information.</p>
    </td>
    </tr>
    <tr id="row22019699171458"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.1 "><p id="p38765181171458"><a name="p38765181171458"></a><a name="p38765181171458"></a>SK</p>
    </td>
    <td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.4.1.2 "><p id="p52971976171458"><a name="p52971976171458"></a><a name="p52971976171458"></a>XXX (example value)</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.3 "><p id="p62871676171458"><a name="p62871676171458"></a><a name="p62871676171458"></a>Mandatory</p>
    <p id="p2567497393052"><a name="p2567497393052"></a><a name="p2567497393052"></a>Indicates the user's <span id="ph44022441105455"><a name="ph44022441105455"></a><a name="ph44022441105455"></a>Secret Access Key (</span>SK<span id="ph47211929105437"><a name="ph47211929105437"></a><a name="ph47211929105437"></a>)</span> information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The OBS path is divided into  **service\_auditlog** and **manager\_auditlog**, which are used to save service and management audit logs, respectively.  


