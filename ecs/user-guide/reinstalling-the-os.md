# Reinstalling the OS<a name="EN-US_TOPIC_0024911405"></a>

## Scenarios<a name="section60394636111543"></a>

If the OS of an ECS fails to start or requires optimization, reinstall the OS.

## Notes<a name="section37447471165714"></a>

After the OS is reinstalled, the password for logging in to the ECS is reset. To retrieve the password, perform the following operations:

-   For a Linux ECS, log in to it using the key and set a new password. For instructions about how to log in to an ECS using a key pair, see  [Login Using an SSH Key](login-using-an-ssh-key.md).
-   For a Windows ECS, retrieve the password by following the instructions provided in  [Obtaining the Password for Logging In to a Windows ECS](obtaining-the-password-for-logging-in-to-a-windows-ecs.md).

## Constraints<a name="section4500313111616"></a>

-   The EVS disk quota must be greater than 0.
-   If the target ECS is created using a private image, ensure that the private image is available.
-   H2 ECSs do not support OS reinstallation.

## Prerequisites<a name="section2641260214160"></a>

-   The target ECS is in the  **Stopped**  or  **Reinstallation failed**  state.
-   The target ECS has a system disk attached.
-   Necessary data has been backed up. \(Reinstalling the OS clears the data in all partitions of the EVS system disk, including the system partition.\)

## Procedure<a name="section58299059111554"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  <a name="li20776247143354"></a>Under  **Computing**, click  **Elastic Cloud Server**.
4.  Locate the row containing the target ECS. Click  **More**  in the  **Operation**  column and select  **Reinstall OS**.

    If the ECS is not stopped, stop the ECS before proceeding with reinstallation.

5.  \(Optional\) Select a  **License Type**  \(**Use license from the system**  or  **Bring your own license \(BYOL\)**\) if the reinstalled OS running on your ECS is billed. For more details, see  [License Type](license-type.md).

    The following OSs are billed:

    -   SUSE Linux Enterprise Server
    -   Oracle Enterprise Linux
    -   Red Hat Enterprise Linux
    -   Windows Server OS \(BYOL can be used on an ECS that is created on a DeH and runs a Windows Server OS.\)

6.  Configure the login mode.

    If the target ECS uses key pair authentication, you can replace the original key pair.

7.  Click  **OK**.
8.  <a name="li31062819143541"></a>On the  **ECS OS Reinstallation**  page, confirm the specifications and click  **Submit**.

    After the request is submitted, the ECS status changes to  **Reinstalling**. The reinstallation has been completed when the ECS status changes to  **Running**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >A temporary ECS is created during the reinstallation process. After reinstallation, this ECS will automatically be deleted. Do not perform any operation on the temporary ECS during the reinstallation process.  


## Follow-up Procedure<a name="section12556769105440"></a>

If the reinstallation is unsuccessful, perform steps  [3](#li20776247143354)  to  [8](#li31062819143541)  again to retry reinstalling the OS again.

If the second reinstallation attempt is unsuccessful, contact customer service for manual recovery at the backend.

