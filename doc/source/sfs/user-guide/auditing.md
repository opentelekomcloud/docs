# Auditing<a name="sfs_01_0050"></a>

## Scenarios<a name="section11657123312211"></a>

Cloud Trace Service \(CTS\) records operations of SFS resources, facilitating query, audit, and backtracking.

## Prerequisites<a name="section149848566220"></a>

You have enabled CTS and the tracker is normal. For details about how to enable CTS, see section "Enabling CTS" in the  _Cloud Trace Service User Guide._

## Operations<a name="section2270183331019"></a>

**Table  1**  SFS operations traced by CTS

<a name="table19033961114053"></a>
<table><thead align="left"><tr id="en-us_topic_0100240354_row35006313114053"><th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.1"><p id="en-us_topic_0100240354_p16939117114053"><a name="en-us_topic_0100240354_p16939117114053"></a><a name="en-us_topic_0100240354_p16939117114053"></a><strong id="b842352706145343"><a name="b842352706145343"></a><a name="b842352706145343"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240354_p29891200114053"><a name="en-us_topic_0100240354_p29891200114053"></a><a name="en-us_topic_0100240354_p29891200114053"></a><strong id="b842352706202940"><a name="b842352706202940"></a><a name="b842352706202940"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.78%" id="mcps1.2.4.1.3"><p id="en-us_topic_0100240354_p5268173114053"><a name="en-us_topic_0100240354_p5268173114053"></a><a name="en-us_topic_0100240354_p5268173114053"></a><strong id="b842352706203028"><a name="b842352706203028"></a><a name="b842352706203028"></a>Trace</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0100240354_row24068858114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p28078359114444"><a name="en-us_topic_0100240354_p28078359114444"></a><a name="en-us_topic_0100240354_p28078359114444"></a>Creating a shared file system</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p10575199114451"><a name="en-us_topic_0100240354_p10575199114451"></a><a name="en-us_topic_0100240354_p10575199114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p1723951111453"><a name="en-us_topic_0100240354_p1723951111453"></a><a name="en-us_topic_0100240354_p1723951111453"></a>createShare</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row44387699114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p920237114444"><a name="en-us_topic_0100240354_p920237114444"></a><a name="en-us_topic_0100240354_p920237114444"></a>Modifying a shared file system</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p58910191114451"><a name="en-us_topic_0100240354_p58910191114451"></a><a name="en-us_topic_0100240354_p58910191114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p1824643011453"><a name="en-us_topic_0100240354_p1824643011453"></a><a name="en-us_topic_0100240354_p1824643011453"></a>updateShareInfo</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row61431010114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p66873716114444"><a name="en-us_topic_0100240354_p66873716114444"></a><a name="en-us_topic_0100240354_p66873716114444"></a>Deleting a shared file system</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p62965520114451"><a name="en-us_topic_0100240354_p62965520114451"></a><a name="en-us_topic_0100240354_p62965520114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p1409300311453"><a name="en-us_topic_0100240354_p1409300311453"></a><a name="en-us_topic_0100240354_p1409300311453"></a>deleteShare</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row14359181114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p29903724114444"><a name="en-us_topic_0100240354_p29903724114444"></a><a name="en-us_topic_0100240354_p29903724114444"></a>Adding a share access rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p66510197114451"><a name="en-us_topic_0100240354_p66510197114451"></a><a name="en-us_topic_0100240354_p66510197114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p614308711453"><a name="en-us_topic_0100240354_p614308711453"></a><a name="en-us_topic_0100240354_p614308711453"></a>addShareACL</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row39986691114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p56543009114444"><a name="en-us_topic_0100240354_p56543009114444"></a><a name="en-us_topic_0100240354_p56543009114444"></a>Deleting a share access rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p33333977114451"><a name="en-us_topic_0100240354_p33333977114451"></a><a name="en-us_topic_0100240354_p33333977114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p4912579911453"><a name="en-us_topic_0100240354_p4912579911453"></a><a name="en-us_topic_0100240354_p4912579911453"></a>deleteShareACL</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row10624731114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p15011430114444"><a name="en-us_topic_0100240354_p15011430114444"></a><a name="en-us_topic_0100240354_p15011430114444"></a>Expanding a shared file system</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p7060671114451"><a name="en-us_topic_0100240354_p7060671114451"></a><a name="en-us_topic_0100240354_p7060671114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p4368302811453"><a name="en-us_topic_0100240354_p4368302811453"></a><a name="en-us_topic_0100240354_p4368302811453"></a>extendShare</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row44204148114053"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p4588311114444"><a name="en-us_topic_0100240354_p4588311114444"></a><a name="en-us_topic_0100240354_p4588311114444"></a>Shrinking a shared file system</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p46955826114451"><a name="en-us_topic_0100240354_p46955826114451"></a><a name="en-us_topic_0100240354_p46955826114451"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p3532643511453"><a name="en-us_topic_0100240354_p3532643511453"></a><a name="en-us_topic_0100240354_p3532643511453"></a>shrinkShare</p>
</td>
</tr>
</tbody>
</table>

## Querying Traces<a name="section1294519941119"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0113383875.jpg)  in the upper left corner and select a region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  In the navigation pane on the left, choose  **Trace List**.
5.  On the trace list page, click  **Filter**. In the displayed box, specify  **Trace Source**,  **Resource Type**, and  **Search By**, and click  **Query**  to query the specified traces.

    For details about other operations, see section "Querying Real-Time Traces" in the  _Cloud Trace Service User Guide_.


## Disabling or Enabling a Tracker<a name="section198761857144117"></a>

This section describes how to disable an existing tracker on the CTS console. After the tracker is disabled, the system will stop recording operations, but you can still view existing operation records.

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0113383875.jpg)  in the upper left corner and select a region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Click  **Tracker**  in the left pane.
5.  Click  **Disable**  on the right of the tracker information.
6.  Click  **OK**.
7.  After the tracker is disabled, the available operation changes from  **Disable**  to  **Enable**. To enable the tracker again, click  **Enable**  and then click  **OK**. The system will start recording operations again.

