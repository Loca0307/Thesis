    # Apply GaussianBlur to reduce noise
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Apply thresholding to get a binary image
    _, binary_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Increase contrast
    alpha = 1.5  # Simple contrast control
    beta = 0    # Simple brightness control
    contrasted_img = cv2.convertScaleAbs(binary_img, alpha=alpha, beta=beta)

    # Sharpen the image
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened_img = cv2.filter2D(contrasted_img, -1, kernel)

    # Save the processed image for debugging
    cv2.imwrite("Debugging/debug_preprocessed_for_ocr.png", sharpened_img)