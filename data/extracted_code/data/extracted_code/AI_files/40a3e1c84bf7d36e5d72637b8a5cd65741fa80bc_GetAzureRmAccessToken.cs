            catch (Exception e)
            {
                WriteDebug("Exception occurred while checking environment variable AZUREPS_OUTPUT_PLAINTEXT_AZACCESSTOKEN: " + e.ToString());
                //Throw exception when the caller doesn't have permission.
                //Use SecureString only when AZUREPS_OUTPUT_PLAINTEXT_AZACCESSTOKEN is successfully set.
            }
            if (usePlainText)