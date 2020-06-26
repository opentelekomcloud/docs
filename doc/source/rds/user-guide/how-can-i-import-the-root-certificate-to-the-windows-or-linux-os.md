# How Can I Import the Root Certificate to the Windows or Linux OS?<a name="rds_faq_0052"></a>

## Importing the Root Certificate to the Windows OS<a name="sce3d5c4bd5504fcf92fbe808714492e9"></a>

1.  Click  **Start**  and choose  **Run**. In the displayed  **Run**  dialog box, enter  **MMC**  and press  **Enter**.
2.  On the displayed console, choose  **File**  \>  **Add/Remove Snap-in**.
3.  In the left  **Available snap-ins**  pane of the displayed  **Add or Remove Snap-ins**  dialog box, select  **Certificates**  and click  **Add**.
4.  In the displayed  **Certificates snap-in**  dialog box, select  **Computer account**  and click  **Next**.
5.  In the displayed  **Select Computer**  dialog box, click  **Finish**.
6.  In the  **Add or Remove Snap-ins**  dialog box, click  **OK**.
7.  On the console, double-click  **Certificates**.
8.  Right-click  **Trusted Root Certification Authorities**  and choose  **All Tasks**  \>  **Import**.
9.  In the displayed  **Certificate Import Wizard**  dialog box, click  **Next**.
10. Click  **Browse**  to change the file type to  **All Files \(\*.\*\)**.
11. Locate the downloaded root certificate ca.pem file and click  **Open**. Then, click  **Next**.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >You must change the file type to  **All Files \(\*.\*\)**  because  **.pem**  is not a standard certificate extension name.  

12. Click  **Next**.
13. Click  **Finish**.
14. Click  **OK**  to complete the import of the root certificate.

## Importing the Root Certificate to the Linux OS<a name="section77264333593"></a>

You can use a connection tool \(such as WinSCP or PuTTY\) to upload the certificate to any directory of the Linux OS.

