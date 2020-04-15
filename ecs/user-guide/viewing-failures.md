# Viewing Failures<a name="EN-US_TOPIC_0108255889"></a>

## Scenarios<a name="section49701611171023"></a>

The  **Failures**  area shows the tasks that failed to process due to an error, including the task name and status.  **Failures**  is displayed on the management console if a task failed. This section describes how to view failures.

## Failure Types<a name="section10360181317498"></a>

[Table 1](#table155141127195016)  lists the types of failures that can be recorded in the  **Failures**  area.

**Table  1**  Failure types

<a name="table155141127195016"></a>
<table><thead align="left"><tr id="row175151927105012"><th class="cellrowborder" valign="top" width="21.89%" id="mcps1.2.3.1.1"><p id="p8515182775012"><a name="p8515182775012"></a><a name="p8515182775012"></a>Failure Type</p>
</th>
<th class="cellrowborder" valign="top" width="78.11%" id="mcps1.2.3.1.2"><p id="p151572775011"><a name="p151572775011"></a><a name="p151572775011"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8515127155014"><td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.3.1.1 "><p id="p10515202705012"><a name="p10515202705012"></a><a name="p10515202705012"></a>Creation failures</p>
</td>
<td class="cellrowborder" valign="top" width="78.11%" headers="mcps1.2.3.1.2 "><p id="p1051542720507"><a name="p1051542720507"></a><a name="p1051542720507"></a>A task failed to process. For a failed task, the system rolls back and displays an error code, for example, <strong id="b8423527061285"><a name="b8423527061285"></a><a name="b8423527061285"></a>Ecs.0013 Insufficient EIP quota</strong>. See <a href="how-do-i-handle-error-messages-displayed-on-the-management-console.md">How Do I Handle Error Messages Displayed on the Management Console?</a> for troubleshooting.</p>
</td>
</tr>
<tr id="row1151562711507"><td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.3.1.1 "><p id="p251532717502"><a name="p251532717502"></a><a name="p251532717502"></a>Operation failures</p>
</td>
<td class="cellrowborder" valign="top" width="78.11%" headers="mcps1.2.3.1.2 "><a name="ul296746155113"></a><a name="ul296746155113"></a><ul id="ul296746155113"><li>Modifying ECS specifications<p id="p521432610491"><a name="p521432610491"></a><a name="p521432610491"></a>If an ECS specifications modification failed, this operation is recorded in <strong id="b87986958221659"><a name="b87986958221659"></a><a name="b87986958221659"></a>Failures</strong>.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section40936232171845"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  View  **Failures**  on the right side of common operations.

    **Figure  1**  Failures<a name="fig1678913358104"></a>  
    ![](figures/failures.png "failures")

5.  Click the number displayed in the  **Failures**  area to view details about the tasks.
    -   **Creation Failures**: show the tasks that are being created and those failed to create.
    -   **Operation Failures**: show the tasks with errors, including the operations performed on the tasks and error codes. Such information can be used for rapid fault locating.


