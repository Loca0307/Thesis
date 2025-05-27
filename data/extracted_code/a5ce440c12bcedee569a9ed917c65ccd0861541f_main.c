        // Wait for something to consume (producer will signal this)
        sem_wait(&semProd);

        pthread_mutex_lock(&bufferLock);
        // Consume from buffer
        int num = ringBuffer[rp];
        rp = (rp + 1) % BUFFER_SIZE;
        printf("[CONS] Read %d from buffer\n", num);
        pthread_mutex_unlock(&bufferLock);

        // Signal the producer that there's space in the buffer
        sem_post(&semCons);

        counter++;