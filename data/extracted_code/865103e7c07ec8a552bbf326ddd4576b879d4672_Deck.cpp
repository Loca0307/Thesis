//
// Created by damya on 1.2.2024 г..
//

#ifndef CARDSHUFFLE_CARD_H
#define CARDSHUFFLE_CARD_H

using namespace std;
#include "iostream"


class Card {
public:


    enum Type {
            ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING
    };

    enum Suit {
        HEARTS, DIAMONDS, CLUBS, SPADES
    };

    Card(Type, Suit);


    Type getType() const;
    Suit getSuit() const;



private:
    Type type;
    Suit suit;
};



#endif //CARDSHUFFLE_CARD_H