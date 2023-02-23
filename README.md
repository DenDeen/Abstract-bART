# Datathon Submission: Abstract-bART
This repository contains the code and documentation for our submission, organized by **KU Leuven** and **LSTAT**.

## Overview
Abstract-bART is a diffusion model trained from scratch on the given data. In this project, we aim to generate art based on a text prompt and try to fool our classifier in thinking it's not AI-generated.

## Data
The data used in this project is provided by KU Leuven and LSTAT, and consists of over 10000 artworks with descriptions.

## Methodology
We employed the following methods in our project:

0. Preprocess texts: Preprocess texts by removing stopwords with nltk and   summarize texts with pre-trained transformer T5 model.
1. Text embeddings: Tokenize and embed texts with pre-trained CLIP text encoder.
2. Image embeddings: Create latent descriptions of images with pre-trained VQ-GAN image auto-encoder.
3. Train diffusion model: Train diffusion model from scratch using text and image encodings from previous steps.
4. Generate art: Generate art using our trained diffusion model with textual inputs.
5. Train image classifier: Train a classifier by fine-tuning imagenet model with both AI-generated and human-made artworks.
5. Fool image classifier: Test our generated art against our image classifier.

## Results
Our results show that generating art on this dataset was not easy. We are satisfied with the results, but there are some steps that can greatly improve the model.

Curating the images, processing the images differently and improving the text embedding will improve the model greatly.

We only trained the model for 20 epochs on 64x64 images.
Increasing training time and increasing image size will improve the model further.

## Authors
The labrats: Eduardo V, Mikkel S, Muratzhan K, Tutku K, Vaishnav D

## **Acknowledgments**
We would like to thank **KU Leuven** and **LSTAT** for providing the data used in this project, and for organizing this years datathon.