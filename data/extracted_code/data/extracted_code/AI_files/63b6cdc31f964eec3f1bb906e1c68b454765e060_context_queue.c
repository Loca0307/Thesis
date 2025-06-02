
/*
    @brief Destroys a buffer queue and releases its resources.
    @param self A pointer to the buffer queue to be destroyed.
*/
void bufferqueueDestory(buffer_queue_t *self);

/*
    @brief Pushes an sbuf_t pointer onto the back of the queue.
    @param self A pointer to the buffer queue.
    @param b A pointer to the sbuf_t to be added to the queue.
*/
void bufferqueuePush(buffer_queue_t *self, sbuf_t *b);

/*
    @brief Pops an sbuf_t pointer from the front of the queue.
    @param self A pointer to the buffer queue.
    @return A pointer to the sbuf_t at the front of the queue, or NULL if the queue is empty.
*/
sbuf_t *bufferqueuePop(buffer_queue_t *self);

/*
    @brief Gets the number of elements in the queue.
    @param self A pointer to the buffer queue.
    @return The number of sbuf_t pointers currently in the queue.
*/
size_t bufferqueueLen(buffer_queue_t *self);