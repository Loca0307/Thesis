        from TransmissionThread import TransmissionThread
        from ListeningThread import ListeningThread

        self.taskHandlerThread = taskHandlerThread
        self.acceptedRequestsQueue = AcceptedRequestQueue()
        self.acceptedRequestsQueue.start()