
        initMessageQueue();
    }

    private void initMessageQueue() {
        messageQueue = new ArrayList<>();
        String[] namesOfSenderDialogueArrayJavaLoops = getResources().getStringArray(R.array.names_of_sender_dialogue_array_java_loops);
        String[] messagesDialogueArrayJavaLoops = getResources().getStringArray(R.array.messages_dialogue_array_java_loops);
        String[] delayMsDialogueArrayJavaLoops = getResources().getStringArray(R.array.delay_ms_dialogue_array_java_loops);
        for (int i = 0; i < namesOfSenderDialogueArrayJavaLoops.length; i++) {
            String nameOfSender = namesOfSenderDialogueArrayJavaLoops[i];
            String message = messagesDialogueArrayJavaLoops[i];
            long delayMs = Long.parseLong(delayMsDialogueArrayJavaLoops[i]);

            messageQueue.add(new Message(nameOfSender, message, delayMs, false));
        }
        messageQueue.add(0, new Message("player", "Muly: meow?", 500L, true));
        messageQueue.add(2, new Message("player", "Mulan: MEOW?", 3500L, true));
        messageQueue.add(4, new Message("player", "Muhang: meow", 6000L, true));
        messageQueue.add(6, new Message("player", "Mom: hello", 9000L, true));
        messageQueue.add(8, new Message("player", "Apsara: meow", 11000L, true));
        messageQueue.add(10, new Message("player", "Colin: silence", 16000L, true));
    }

    public void startMessageQueue() {
        for (Message messageToAdd : messageQueue) {
            Handler handler = new Handler(Looper.getMainLooper());
            handler.postDelayed(new Runnable() {
                @Override
                public void run() {
                    addMessageToRecycleView(messageToAdd);
                }
            }, messageToAdd.getDelayMs());
        }
    }

    private void addMessageToRecycleView(Message message) {
        int indexNewMessage = messages.size();
        messages.add(message);
        adapter.notifyItemInserted(indexNewMessage);