## Sample Code

Verify **signing\_cert\_url**, **signature** (obtained in <a href="HTTPHTTPS Message Format.md">HTTP/HTTPS Message Format</a>), and **message** (contained in the message signature) to check the message validity, as shown in the following:

    private static void isMessageValid(String signing_cert_url, String signature, Map<String, String> message) {
	     InputStream in = null;
	     try {
			     URL url = new URL(signing_cert_url);
			     in = url.openStream();
			     CertificateFactory cf = CertificateFactory.getInstance("X.509");
			     X509Certificate cert = (X509Certificate) cf.generateCertificate(in);
			     Signature sig = Signature.getInstance(cert.getSigAlgName());
			     sig.initVerify(cert.getPublicKey());
			     sig.update(buildSignMessage(message).getBytes("UTF-8"));
			     byte[] sigByte = Base64.decodeBase64(signature);
			     if (sig.verify(sigByte)) {
				     System.out.println("Verify success");
				     } else {
				     System.out.println("Verify failed");
				     }
				 } catch (Exception e) {
				     throw new SecurityException("Verify method failed.", e);
				     } finally {
				     if (in != null) {
						     try {
						     in.close();
						     } catch (IOException e) {
						     e.printStackTrace();
						     }
				     }
	     }
    }

The following is a code example to create the message verification signature:

    private static String buildSignMessage(Map<String,String> msg) {
	     String type = msg.get("type");
	     String message = null;
	     if ("Notification".equals(type)){
	     message = buildNotificationMessage(msg);
	     } else if ("SubscriptionConfirmation".equals(type) ||
	     "UnsubscribeConfirmation".equals(type)){
	     message = buildSubscriptionMessage(msg);
	     }
	     return message;
	    }
    private static String buildSubscriptionMessage(Map\<String, String\> msg) {
	     String stringMessage = "message\n";
	     stringMessage += msg.get("message") + "\n";
	     stringMessage += "message_id\n";
	     stringMessage += msg.get("message_id") + "\n";
	     stringMessage += "subscribe_url\n";
	     stringMessage += msg.get("subscribe_url") + "\n";
	     stringMessage += "timestamp\n";
	     stringMessage += msg.get("timestamp") + "\n";
	     stringMessage += "topic_urn\n";
	     stringMessage += msg.get("topic_urn") + "\n";
	     stringMessage += "type\n";
	     stringMessage += msg.get("type") + "\n";
	     return stringMessage;
    }
    private static String buildNotificationMessage(Map<String, String> msg) {
	     String stringMessage = "message\n";
	     stringMessage += msg.get("message") + "\n";
	     stringMessage += "message_id\n";
	     stringMessage += msg.get("message_id") + "\n";
	     if (msg.get("subject") != null) {
	     stringMessage += "subject\n";
	     stringMessage += msg.get("subject") + "\n";
	     }
	     stringMessage += "timestamp\n";
	     stringMessage += msg.get("timestamp") + "\n";
	     stringMessage += "topic_urn\n";
	     stringMessage += msg.get("topic_urn") + "\n";
	     stringMessage += "type\n";
	     stringMessage += msg.get("type") + "\n";
	     return stringMessage;
	    }

    
