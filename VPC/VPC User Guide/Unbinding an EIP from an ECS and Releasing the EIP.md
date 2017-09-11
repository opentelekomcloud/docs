## Unbinding an EIP from an ECS and Releasing the EIP

### Scenarios

If you no longer need the EIP, unbind it from the ECS and release the EIP to
release network resources.

-   EIPs assigned and bound to ECSs in the Elastic Load Balance (ELB) service
    are displayed in the EIP list of the VPC service, but you cannot unbind
    these EIPs from ECSs.

-   Only EIPs that are not bound to ECSs can be released. To release EIPs that
    are bound to ECSs, you must first unbind them.

### Procedure 

**Unbind an EIP.**

1.  Log in to the management console.

2.  On the console homepage, under **Network**, click **Virtual Private Cloud**.

3.  In the navigation pane on the left, choose **Elastic IP Address**.

4.  On the **Elastic IP Address** page, locate the row that contains the target
    EIP, and click **Unbind**.

**Release an EIP.**

1.  On the **Elastic IP Address** page, locate the row that contains the target
    EIP, and click **Release**.

2.  Click **OK**.
