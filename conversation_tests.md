#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## claim insurance acc
  - utter_greet
* greet: hey
  - utter_selfintroduction
* claim: can I claim my insurance?
  - utter_request
* affirm: yes
  - utter_question1
* accident:It was an accident
  - utter_question2
* serious: normal
  - utter_question3
* affirm: yes
  - utter_question4
* proff: govt
  - utter_sleep

## claim insurance heal
  - utter_greet
* greet: hey
  - utter_selfintroduction
* claim: can I claim my insurance?
  - utter_request
* affirm: yes
  - utter_question1
* health: improper health
  - utter_question2
* serious: normal
  - utter_question3
* affirm: yes
  - utter_question4
* proff: govt
  - utter_sleep

## claim insurance fstop
  - utter_greet
* greet: hi
  - utter_selfintroduction
* deny: nope
  - utter_goodbye

## claim insurance sstop
  - utter_greet
* greet: hey
  - utter_selfintroduction
* claim: tell me about mine
  - utter_request
* deny: no
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
