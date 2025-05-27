    def sanitize_filename(self, filename):
        """
        Sanitize the filename by removing or replacing invalid characters.
        """
        logger.debug("Sanitizing filename: {}", filename)
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode('ascii')
        filename = re.sub(r'[^\w\s-]', '', filename).strip().lower()
        filename = re.sub(r'[-\s]+', '_', filename)
        logger.debug("Sanitized filename: {}", filename)
        return filename

    def fetch_emails(self):
        try:
            with MailBox(self.imap_server).login(self.username, self.password) as mailbox:
                logger.info("Logged in to IMAP server: {}", self.imap_server)
                criteria = AND(seen=self.mark_as_seen)
                logger.debug("Fetching emails with criteria: {}", criteria)

                for msg in mailbox.fetch(criteria):
                    logger.info("Email fetched: Subject: {}, From: {}", msg.subject, msg.from_)
                    self.process_email(msg)
        except Exception as e:
            logger.error("An error occurred while fetching emails: {}", str(e))

    def process_email(self, msg):
        try:
            logger.debug("Processing email: {}", msg.subject)
            # Email processing logic here
            json_data = {
                'subject': msg.subject,
                'from': msg.from_,
                'date': msg.date.isoformat(),
                'text': msg.text,
                'html': msg.html,
                'attachments': [att.filename for att in msg.attachments]
            }
            filename = self.sanitize_filename(msg.subject) + '.json'
            self.save_json(json_data, filename)
            logger.info("Processed and saved email: {}", filename)
        except Exception as e:
            logger.error("An error occurred while processing email: {}", str(e))

    def save_json(self, data, filename):