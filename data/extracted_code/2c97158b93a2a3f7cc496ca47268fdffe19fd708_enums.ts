<script lang="ts">
  import type { ChatMessage } from '$lib/server/db/schema';
  import { ChatMessageFeedback } from '$lib/enums';

  const { 
    message, 
    updateChatMessage 
  } = $props<{
    message: ChatMessage;
    updateChatMessage: (changes: Partial<ChatMessage>) => void;
  }>();

  // State
  let feedback = $state<ChatMessageFeedback | null>(message.feedback || null);
  let isFeedbackSubmitted = $state(!!message.feedback);

  const onSaveFeedback = async (selectedFeedback: ChatMessageFeedback) => {
    if (!selectedFeedback) {
      console.log('MessageFeedback.onSaveFeedback: No feedback provided.');
      return;
    }

    feedback = selectedFeedback;

    const changes: Partial<ChatMessage> = {
      id: message.id,
      feedback,
    };
    await updateChatMessage(changes);
    isFeedbackSubmitted = true;
  };
</script>

<div class="message-feedback">
  {#if isFeedbackSubmitted}
    <div class="feedback-submitted">
      <span>Thanks! Feedback: <span class="feedback-value">{feedback}</span></span>
    </div>
  {:else}
    <div class="feedback-buttons">
      <button
        class="feedback-button"
        onclick={() => onSaveFeedback(ChatMessageFeedback.helpful)}
        title="This response was helpful"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
        </svg>
        Helpful
      </button>
      <button
        class="feedback-button"
        onclick={() => onSaveFeedback(ChatMessageFeedback.unhelpful)}
        title="This response was not helpful"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path>
        </svg>
        Not Helpful
      </button>
      <button
        class="feedback-button"
        onclick={() => onSaveFeedback(ChatMessageFeedback.wrong)}
        title="This response contains incorrect information"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="15" y1="9" x2="9" y2="15"></line>
          <line x1="9" y1="9" x2="15" y2="15"></line>
        </svg>
        Wrong
      </button>
    </div>
  {/if}
</div>

<style>
  /* Feedback UI styles */
  .message-feedback {
    margin-top: 0.3rem;
    padding-top: 0.2rem;
    padding-bottom: 0;
    margin-bottom: 0;
    border-top: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 0.85rem;
    display: flex;
    justify-content: flex-end;
  }

  .feedback-buttons {
    display: flex;
    gap: 0.3rem;
    flex-wrap: wrap;
    margin-bottom: 0;
  }

  .feedback-button {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.15rem 0.4rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    background-color: #f9f9f9;
    color: #555;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .feedback-button:hover {
    background-color: #e9e9e9;
    border-color: #ccc;
  }

  .feedback-button svg {
    width: 14px;
    height: 14px;
  }

  .feedback-submitted {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    color: #666;
    font-size: 0.75rem;
    margin-bottom: 0;
    padding-bottom: 0;
  }

  .feedback-value {
    font-weight: 500;
    color: #68859b;
    text-transform: capitalize;
  }
</style>