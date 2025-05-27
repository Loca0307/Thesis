package com.example.lengapp;


public class Flashcard {
    private String word;           // The word in the source language
    private String translation;    // The translation of the word
    private String soundFileName;  // The file name of the sound associated with the word

    // Constructor
    public Flashcard(String word, String translation, String soundFileName) {
        this.word = word;
        this.translation = translation;
        this.soundFileName = soundFileName;
    }

    // Getters and Setters
    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public String getTranslation() {
        return translation;
    }

    public void setTranslation(String translation) {
        this.translation = translation;
    }

    public String getSoundFileName() {
        return soundFileName;
    }

    public void setSoundFileName(String soundFileName) {
        this.soundFileName = soundFileName;
    }

    @Override
    public String toString() {
        return "Flashcard{" +
                "word='" + word + '\'' +
                ", translation='" + translation + '\'' +
                ", soundFileName='" + soundFileName + '\'' +
                '}';
    }
}