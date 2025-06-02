// OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE # OLD CODE #
//        String currentMeds = "";
//        String currentSpecies = "";
//        String currentFormula = "";
////        String currentDose = "";
//
//        boolean isMed = false;
//        boolean isSpecies = false;
//        boolean isFormula = false;
//        boolean isDose = false;
//        boolean isLine = false;
//
//        while (scannerForCAL.hasNextLine()) {
//            String line = scannerForCAL.nextLine();
//
//            //Breaking line into tokens
//            String[] tokens = line.split(" ");
//
//            if (tokens.length >= 4) {
//                // Saving the tokens to variables
//                currentMeds = tokens[0];
//                currentSpecies = tokens[1];
//                currentFormula = tokens[2];
//                currentDose = tokens[3];
//            } // end of Token if statement
//
//            //checking if med name and what was entered match
//            if (currentMeds.equalsIgnoreCase(meds)) {
//                isMed = true;
//            } else {
//                line = scannerForCAL.nextLine();
//            } // end of check Meds if statement
//
//            // if med name is correct:
//            //checking if species and what was entered match
//            if (isMed = true) {
//                if (currentSpecies.equalsIgnoreCase(species)) {
//                    isSpecies = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                } // end of check species = true if statement
//            }// end of isMed = true if statement
//
//            // if med name and species is correct:
//            //checking if formula and what was entered match
//            if (isMed == true && isSpecies == true) {
//                if (currentFormula.equalsIgnoreCase(formula)) {
//                    isFormula = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                }// end of check formula = true if statement
//            }// end of isMed && isSpecies = true if statement
//
//            // if med name and species and formula is correct:
//            //checking if dose and what was entered match
//            if (isMed == true && isSpecies == true && isFormula == true) {
//                if (currentDose.equalsIgnoreCase(dose)) {
//                    isDose = true;
//                } else {
//                    line = scannerForCAL.nextLine();
//                }// end of check dose = true if statement
//            }// end of isMed && isSpecies && isFormula = true if statement 
//
//        } // end of while hasNextLine loop