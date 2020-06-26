# Step 3: Bind an EIP<a name="rds_02_0025"></a>

## Scenarios<a name="section1698131616110"></a>

By default, a DB instance is not publicly accessible \(not bound with an EIP\) after being created. You can bind an EIP to the DB instance for public access and can unbind the EIP from the DB instance as required.

## Precautions<a name="section380043142120"></a>

-   You need to  configure security groups  and enable specific IP addresses and ports to access the target DB instance. Before accessing the DB instance, you need to add an individual IP address or an IP address range that will access the DB instance to the inbound rule. For details, see section  [Step 2: Configure Security Group Rules](step-2-configure-security-group-rules.md).
-   Public accessibility reduces the security of DB instances. Therefore, exercise caution when enabling this function. To achieve a higher transmission rate and security level, you are advised to migrate your applications to the ECS that is in the same region as RDS.

## Binding an EIP<a name="section163851913174310"></a>

1.  On the  **Instance Management**  page, click the target DB instance.
2.  In the navigation pane on the left, choose  **EIPs**. On the displayed page, click  **Bind EIP**.
3.  In the displayed dialog box, select an EIP and click  **OK**.

    If no available EIPs are displayed, click  **View EIP**  and obtain an EIP.

4.  On the  **EIPs**  page, view the EIP that has been bound to the DB instance.

    You can also view the progress and result of binding an EIP to a DB instance on the  **Task Center**  page.


