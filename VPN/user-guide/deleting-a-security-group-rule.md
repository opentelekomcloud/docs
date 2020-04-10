# Deleting a Security Group Rule<a name="vpn_03_0803"></a>

## Scenarios<a name="en-us_topic_0118534007_s3e580453202e40bf842d4254f7841130"></a>

If the source of an inbound security group rule or destination of an outbound security group rule needs to be changed, you need to first delete the security group rule and add a new one.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Security group rules use whitelists. Deleting a security group rule may result in ECS access failures. Exercise caution when deleting security group rules.  

## Procedure<a name="en-us_topic_0118534007_sc03d1dcd3a3d47e385befc1e6dc65979"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Groups**  page, click the security group name.
6.  If you do not need a security group rule, locate the row that contains the target rule, and click  **Delete**.
7.  Click  **Yes**  in the displayed dialog box.

**Deleting Multiple Security Group Rules at Once.**

You can also select multiple security group rules and click  **Delete**  above the security group rule list to delete multiple rules at a time.

