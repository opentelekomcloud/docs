# Logging In to a BMS Remotely Using MSTSC<a name="EN-US_TOPIC_0079188786"></a>

## Prerequisites<a name="section33044631113942"></a>

-   The BMS must be in  **Running**  state.
-   You have obtained the password for logging in to the Windows BMS. For details, see  [Obtaining the Password of a Windows BMS](obtaining-the-password-of-a-windows-bms.md).
-   You have bound an EIP to the BMS. For details, see  [Binding an EIP to a BMS](binding-an-eip-to-a-bms.md).
-   You have configured the inbound rules of the security group. For details, see  [Adding Security Group Rules](adding-security-group-rules.md).
-   The network connection between the login tool and the target BMS is normal. For example, the default port 3389 is not blocked by the firewall.

## Procedure<a name="section51511406581"></a>

The following procedure describes how to log in to a Windows BMS using  **mstsc.exe**.

1.  On the local PC, click  **Start**.
2.  In the  **Search programs and files**  box, enter  **mstsc.exe**  and press  **Enter**.
3.  Enter the EIP and username of the Windows BMS, click  **Connect**, enter the password as prompted, and click  **OK**  to log in to the BMS.

