        // Save the reservation first
        Reservation savedReservation = reservationRepository.save(reservation);

        // --- Send Confirmation Email ---
        try {
            // Fetch User details to get email
            Optional<User> userOpt = userRepository.findById(savedReservation.getCustomerId().toHexString()); //

            // Fetch Restaurant details
            Optional<Restaurant> restaurantOpt = restaurantRepository.findById(savedReservation.getRestaurantId().toHexString()); //

            // Fetch Table details
            Optional<Table> tableOpt = tableRepository.findById(savedReservation.getTableId().toHexString()); //


            if (userOpt.isPresent() && restaurantOpt.isPresent() && tableOpt.isPresent()) {
                User user = userOpt.get();
                Restaurant restaurant = restaurantOpt.get();
                Table table = tableOpt.get();

                String recipientEmail = user.getEmail(); //
                String subject = "Your Booking Confirmation at " + restaurant.getName(); //

                // Compose a simple email body
                String messageBody = String.format(
                        "Dear %s,\n\n" +
                                "Your booking is confirmed!\n\n" +
                                "Restaurant: %s\n" +
                                "Address: %s, %s\n" + //
                                "Table Number: %s\n" + //
                                "Date: %s\n" + //
                                "Time: %s - %s\n" + //
                                "Party Size: %d\n\n" + //
                                "Reservation ID: %s\n\n" + //
                                "Thank you for using BookTable!",
                        user.getName(), //
                        restaurant.getName(), //
                        restaurant.getAddressStreet(), restaurant.getAddressCity(), //
                        table.getTableNumber(), //
                        savedReservation.getDate().toString(), //
                        savedReservation.getStartSlotTime().toString(), //
                        savedReservation.getEndSlotTime().toString(), //
                        savedReservation.getPartySize(), //
                        savedReservation.getId().toHexString() //
                );

                // Send the email using the injected service
                mailjetEmailService.sendEmail(recipientEmail, subject, messageBody); //
                System.out.println("Booking confirmation email sent to " + recipientEmail);

            } else {
                // Log if user, restaurant, or table details are missing
                if (!userOpt.isPresent()) log.error("Could not find user with ID: {}", savedReservation.getCustomerId());
                if (!restaurantOpt.isPresent()) log.error("Could not find restaurant with ID: {}", savedReservation.getRestaurantId());
                if (!tableOpt.isPresent()) log.error("Could not find table with ID: {}", savedReservation.getTableId());
            }

        } catch (Exception e) {
            // Log the error, but don't necessarily fail the entire booking process
            log.error("Failed to send booking confirmation email: {}", e.getMessage(), e);
        }
        // --- End of Email Sending Logic ---

        return savedReservation; // Return the saved reservation object