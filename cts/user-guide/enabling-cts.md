# Enabling CTS<a name="en-us_topic_0030598498"></a>

## **Scenarios**<a name="section60206522184734"></a>

You need to enable CTS before using it. A tracker will be automatically created after CTS is enabled. All traces recorded by CTS are associated with the tracker. Currently, only one tracker can be created for each cloud account.

Trace files need to be stored in OBS buckets. Therefore, before enabling CTS, you need to enable OBS and have full permissions on the OBS bucket to be used. By default, only the service owner who has enabled OBS can access OBS buckets and all objects contained, and the owner can grant permissions to other services and users by configuring an access policy.

The tracker created in a multi-project scenario can only track resources under the current project. If tracking cloud resources under another project is required, you need to create a tracker under the project.

This section describes how to enable CTS.

## **Prerequisites**<a name="section34518472181112"></a>

You have enabled OBS.

## **Procedure**<a name="section5355633918486"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Click  **Tracker**  in the left pane.
5.  Click  **Enable CTS**.
6.  Click  **Configure**  in the  **Operation**  column to set  **OBS Bucket**  and  **File Prefix**.  [Table 1](#table1478957894650)  lists the parameters to be specified.

    **Table  1**  Parameter description

    <a name="table1478957894650"></a>
    <table><thead align="left"><tr id="row6408293094650"><th class="cellrowborder" valign="top" width="27.32%" id="mcps1.2.4.1.1"><p id="p4996144794718"><a name="p4996144794718"></a><a name="p4996144794718"></a><strong id="b1866069292432"><a name="b1866069292432"></a><a name="b1866069292432"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.199999999999996%" id="mcps1.2.4.1.2"><p id="p4035852094718"><a name="p4035852094718"></a><a name="p4035852094718"></a><strong id="b5868369292435"><a name="b5868369292435"></a><a name="b5868369292435"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.479999999999999%" id="mcps1.2.4.1.3"><p id="p2308153794718"><a name="p2308153794718"></a><a name="p2308153794718"></a><strong id="b4151105892439"><a name="b4151105892439"></a><a name="b4151105892439"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1446027994650"><td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.1 "><p id="p4016463094718"><a name="p4016463094718"></a><a name="p4016463094718"></a>OBS Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.199999999999996%" headers="mcps1.2.4.1.2 "><p id="p5554085894718"><a name="p5554085894718"></a><a name="p5554085894718"></a>Name of the OBS bucket in which trace files are to be stored</p>
    <div class="note" id="note8550181441310"><a name="note8550181441310"></a><a name="note8550181441310"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p155141418138"><a name="p155141418138"></a><a name="p155141418138"></a>Each OBS bucket name must be globally unique. When a bucket is being created, the system checks in the central region whether the same name exists. Therefore, the bucket creation log is recorded in the central region. After a bucket is created, operation logs associated with the bucket are recorded in the region where the bucket resides.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.3 "><p id="p4808477794718"><a name="p4808477794718"></a><a name="p4808477794718"></a>buckert-001</p>
    </td>
    </tr>
    <tr id="row5870890594650"><td class="cellrowborder" valign="top" width="27.32%" headers="mcps1.2.4.1.1 "><p id="p1284746311350"><a name="p1284746311350"></a><a name="p1284746311350"></a>File Prefix</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.199999999999996%" headers="mcps1.2.4.1.2 "><p id="p1834979194718"><a name="p1834979194718"></a><a name="p1834979194718"></a>Used for identifying the logs stored in the OBS bucket. This parameter is optional. The value is a string of 0 to 64 characters, and can contain uppercase and lowercase letters, digits, hyphens (-), underscores (_), and dots (.). If a tracker is created, a value will be generated automatically in the same way as you specify the value manually.</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.479999999999999%" headers="mcps1.2.4.1.3 "><p id="p332119161140"><a name="p332119161140"></a><a name="p332119161140"></a>None</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

After CTS is enabled, you can view details of the created tracker on the  **Tracker**  page.

