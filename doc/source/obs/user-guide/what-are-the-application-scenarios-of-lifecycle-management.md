# What Are the Application Scenarios of Lifecycle Management?<a name="obs_faq_0027"></a>

Lifecycle management applies to the following scenarios:

-   Some periodically uploaded files need only to be retained for one week or one month, and can be deleted once they have expired.
-   Documents are seldom accessed after a certain period of time. These files need to be transitioned to  **Warm**  or  **Cold**  storage or be deleted.

If you want to delete a large number of objects from a bucket, you can configure a lifecycle rule to implement automatic deletion upon expiration or schedule the time for automatic deletion. On the  **Lifecycle Rule**  page, create rules and configure parameters by referring to  [Table 1](#table115262311380):

**Table  1**  Parameters for deletion upon expiration

<a name="table115262311380"></a>
<table><thead align="left"><tr id="row1153112313387"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p41531923183818"><a name="p41531923183818"></a><a name="p41531923183818"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p115372393815"><a name="p115372393815"></a><a name="p115372393815"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row1915320235383"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2153172303812"><a name="p2153172303812"></a><a name="p2153172303812"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1515314236385"><a name="p1515314236385"></a><a name="p1515314236385"></a>Enable</p>
</td>
</tr>
<tr id="row191531623103811"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p14153122315384"><a name="p14153122315384"></a><a name="p14153122315384"></a>Rule Name</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p9153162343812"><a name="p9153162343812"></a><a name="p9153162343812"></a>Example: <strong id="b1175142713449"><a name="b1175142713449"></a><a name="b1175142713449"></a>rule-delete</strong></p>
</td>
</tr>
<tr id="row1715382373818"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p215352318387"><a name="p215352318387"></a><a name="p215352318387"></a>Applies To</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p181533233380"><a name="p181533233380"></a><a name="p181533233380"></a>You can apply the deletion rule to the entire bucket or to objects that share the same name prefix in the bucket.</p>
</td>
</tr>
<tr id="row19153192319388"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11538237386"><a name="p11538237386"></a><a name="p11538237386"></a>Current Version</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p15153723103812"><a name="p15153723103812"></a><a name="p15153723103812"></a>Expiration Time</p>
<p id="p192911652124011"><a name="p192911652124011"></a><a name="p192911652124011"></a>Days: 1</p>
</td>
</tr>
<tr id="row10153182310387"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p445763184115"><a name="p445763184115"></a><a name="p445763184115"></a>Historical Version</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p945714344114"><a name="p945714344114"></a><a name="p945714344114"></a>Expiration Time</p>
<p id="p6457113154118"><a name="p6457113154118"></a><a name="p6457113154118"></a>Days: 1</p>
</td>
</tr>
</tbody>
</table>

One day later, objects in the bucket are successfully deleted based on the rule. If you do not need this lifecycle rule, you can disable it or delete it.

