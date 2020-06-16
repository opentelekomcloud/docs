# Adding Instances to and Removing Them from a Security Group<a name="SecurityGroup_0017"></a>

## Scenarios<a name="section1284185020245"></a>

After a security group is created, you can add instances, including servers and extension NICs, to the security group to protect the instances. If the instances are not required, you can also remove them from the security group.

You can add multiple instances to or remove them from a security group.

## Adding Instances to a Security Group<a name="section7737145418298"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Groups**  page, click  **Manage Instance**  in the  **Operation**  column.
6.  On the  **Servers**  tab, click  **Add**  and add one or more servers to the current security group.
7.  On the  **Extension NICs**  tab, click  **Add**  and add one or more extension NICs to the current security group.
8.  Click  **OK**.

## Removing Instances from a Security Group<a name="section147074331319"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Groups**  page, click  **Manage Instance**  in the  **Operation**  column.
6.  On the  **Servers**  tab, locate the target server and click  **Remove**  in the  **Operation**  column to remove the server from current security group.
7.  On the  **Extension NICs**  tab, locate the target extension NIC and click  **Remove**  in the  **Operation**  column to remove the NIC from the current security group.
8.  Click  **Yes**.

**Removing multiple instances from a security group**

Select multiple servers and click  **Remove**  above the server list to remove the selected servers from the current security group all at once.

Select multiple extension NICs and click  **Remove**  above the extension NIC list to remove the selected extension NICs from the current security group all at once.

