# What Is the Difference Between Storing Data into DIS and Dumping Data Elsewhere?<a name="dis_faq_0007"></a>

After DIS is enabled, data is stored to DIS by default. After a dump task is added, the data can be dumped to other resources.  [Table 1](#tdc4c4ec0b2454cfeb8421d92412355e6)  describes the specific differences.

-   Data is stored to DIS by default.
-   If  **Dump Destination**  is set to  **OBS**, data is stored in DIS and periodically imported to Object Storage Service \(OBS\).

**Table  1**  Difference between storing data into DIS and dumping data elsewhere

<a name="tdc4c4ec0b2454cfeb8421d92412355e6"></a>
<table><thead align="left"><tr id="ra5e764ab2e3c412f8de1da2b545dc2d2"><th class="cellrowborder" valign="top" width="49.91%" id="mcps1.2.3.1.1"><p id="en-us_topic_0065509540_p191302521636"><a name="en-us_topic_0065509540_p191302521636"></a><a name="en-us_topic_0065509540_p191302521636"></a>DIS Storage</p>
</th>
<th class="cellrowborder" valign="top" width="50.09%" id="mcps1.2.3.1.2"><p id="en-us_topic_0065509540_p60465551636"><a name="en-us_topic_0065509540_p60465551636"></a><a name="en-us_topic_0065509540_p60465551636"></a>OBS Storage</p>
</th>
</tr>
</thead>
<tbody><tr id="r3d792835a81045cf8820184da52ef9c8"><td class="cellrowborder" valign="top" width="49.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0065509540_p101109991636"><a name="en-us_topic_0065509540_p101109991636"></a><a name="en-us_topic_0065509540_p101109991636"></a>You can store data into DIS without applying for storage resources.</p>
</td>
<td class="cellrowborder" valign="top" width="50.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0065509540_p136845631636"><a name="en-us_topic_0065509540_p136845631636"></a><a name="en-us_topic_0065509540_p136845631636"></a>You must apply for OBS resources before dumping data to OBS.</p>
</td>
</tr>
<tr id="r36c63084fda14bd1b5f7a592e4b598c5"><td class="cellrowborder" valign="top" width="49.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0065509540_p439351481636"><a name="en-us_topic_0065509540_p439351481636"></a><a name="en-us_topic_0065509540_p439351481636"></a>No additional payment is required.</p>
</td>
<td class="cellrowborder" valign="top" width="50.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0065509540_p19772551636"><a name="en-us_topic_0065509540_p19772551636"></a><a name="en-us_topic_0065509540_p19772551636"></a>Additional cost for the use of OBS. For details, see the OBS price details.</p>
</td>
</tr>
<tr id="rf058a4d0c9b84be3931c7805d217ea32"><td class="cellrowborder" valign="top" width="49.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0065509540_p321332191636"><a name="en-us_topic_0065509540_p321332191636"></a><a name="en-us_topic_0065509540_p321332191636"></a>Data is temporarily stored in DIS for up to 168 hours.</p>
</td>
<td class="cellrowborder" valign="top" width="50.09%" headers="mcps1.2.3.1.2 "><p id="a14448ac051514c68924ee1639a6969aa"><a name="a14448ac051514c68924ee1639a6969aa"></a><a name="a14448ac051514c68924ee1639a6969aa"></a>Data is stored in OBS until your OBS bucket expires.</p>
</td>
</tr>
<tr id="r32d7cd41e5524dd29e229ec366844ab9"><td class="cellrowborder" valign="top" width="49.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0065509540_p655628081636"><a name="en-us_topic_0065509540_p655628081636"></a><a name="en-us_topic_0065509540_p655628081636"></a>Data is stored only in DIS.</p>
</td>
<td class="cellrowborder" valign="top" width="50.09%" headers="mcps1.2.3.1.2 "><p id="ae6148d573f8c427491bb58101c8f4914"><a name="ae6148d573f8c427491bb58101c8f4914"></a><a name="ae6148d573f8c427491bb58101c8f4914"></a>Data is stored in DIS and periodically dumped to OBS.</p>
</td>
</tr>
</tbody>
</table>

