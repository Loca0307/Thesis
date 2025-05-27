    // Implemented by ChatGPT to help with properly copying even and odd numbers into their respective Arrays.
    int evenIndex = 0, oddIndex = 0;
	for (int i = 0; i < size; i++){
        if (*(arr + i) % 2 == 0){
            *(arr_even + evenIndex) =  *(arr + i); 
            evenIndex++;
        } else {
            *(arr_odd + oddIndex) = *(arr + i);
            oddIndex++;
        }
    }