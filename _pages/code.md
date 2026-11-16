---
layout: single
title: "Code"
permalink: /code/
description: "A guided tour of Gonzalo Loayza's public ML and software repositories, with implementation scope and limitations."
---

# Explore the implementation

My industrial case studies explain the problem, contribution and outcome. These public repositories offer a separate view of software implementation and learning projects. They are not copies of employer code or operational datasets.

## Java systems: multiplayer chess

[Repository](https://github.com/Gonza055/chess) · Java 21, HTTP, WebSocket, MySQL

Start with the shared chess rules, then follow the HTTP server into services and data-access implementations. The terminal client and real-time messages show how the parts fit together. BYU CS 240 coursework includes supplied starter code and passoff tests; the README identifies this context and local-only deployment limitations.

## Machine learning: NLP experiments

[Repository](https://github.com/Gonza055/LSTM-Based-Text-Generator-with-Bidirectional-Layers) · Python, TensorFlow/Keras

Inspect `create_poetry.py` for n-gram preparation and bidirectional LSTM text generation, and `sentiment_analysis.py` for the headline-sarcasm classification exercises. These are learning experiments. Training accuracy and reused validation data are not presented as independent generalization results.

## Python web integration: Find It Quickly

[Repository](https://github.com/Gonza055/CS50-Find-It-Quickly) · Flask, JavaScript, geolocation

A category-based nearby-place search project. Follow the Flask routes and data-driven templates into the Maps client. Local setup and route tests are documented; live map requests require the visitor's permission and a configured provider key.

## React state: employee team manager

[Repository](https://github.com/Gonza055/Employee-Management-System) · React, routing, local storage

A browser-only sample roster demonstrating shared state, immutable member reassignment, grouped views and persistence. It is an educational application rather than an HR backend.

## Earlier prototype: StudyBuddy

[Repository](https://github.com/Gonza055/CS260-StudyBuddy) · Express, WebSocket, HTML/CSS

An early study-collaboration demo with simulated users. The README distinguishes working interface/server behavior from planned authentication, matching and scheduling features.

[Read the applied experience case studies](/projects/) · [Resume](/resume/) · [GitHub profile](https://github.com/Gonza055)
