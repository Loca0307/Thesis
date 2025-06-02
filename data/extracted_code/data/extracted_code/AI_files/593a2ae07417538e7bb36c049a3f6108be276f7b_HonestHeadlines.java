        for (String word : sensationalWords) {
            if (headline.toLowerCase().contains(word.toLowerCase())) {
                return "Sensational";
            }
        }
        return "Not Sensational";