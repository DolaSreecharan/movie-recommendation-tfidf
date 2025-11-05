# 🎬 Movie Recommendation System using TF-IDF & Cosine Similarity

## 📚 Overview

This project is part of my **Machine Learning learning journey**.
After learning **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**, I built a **movie recommendation system from scratch** — **without using libraries like scikit-learn**.
The goal was to deeply understand how text data can be represented mathematically and compared using vector similarity.

The system recommends movies based on **how similar their descriptions are to the movies data**.

---

## 🧠 Key Concepts Demonstrated

| Concept                              | Explanation                                                    |
| ------------------------------------ | -------------------------------------------------------------- |
| **TF (Term Frequency)**              | Measures how commonly a word appears in a movie description.   |
| **IDF (Inverse Document Frequency)** | Assigns higher weight to unique / informative words.           |
| **TF-IDF Vectorization**             | Converts text into meaningful numerical vectors.               |
| **Cosine Similarity**                | Measures similarity between text vectors by comparing angles.  |
| **Vector Space Model**               | Represents documents in high-dimensional space for comparison. |

By implementing TF-IDF manually, this project reinforces **NLP fundamentals + linear algebra**.

---

## 🗂️ Project Structure

```markdown
movie-recommendation-tfidf/
├── movie_recommendation.py
├── movie_data.csv
└── README.md
```
---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DolaSreecharan/movie-recommendation-tfidf.git
cd movie-recommendation-tfidf
```

### 2️⃣ Run the script

```bash
python movie_recommendation.py
```

### 3️⃣ Enter a movie description when prompted

Example:

```
Enter Description: mystery investigation with detectives
```

The system will display **top 5 recommended movies** based on similarity.

---

## 📊 How the System Works

1. Each movie description is broken into words.
2. A TF (Term Frequency) vector is built for each movie.
3. IDF (Inverse Document Frequency) is computed across all movies.
4. TF and IDF are multiplied to get **TF-IDF vectors**.
5. The user input is also converted into a TF-IDF vector.
6. **Cosine similarity** is used to calculate similarity between vectors.
7. Movies are ranked by similarity and the top recommendations are displayed.

---

## 🏗️ Skills Demonstrated

* Python (Core Programming)
* Natural Language Processing (Basics)
* Manual TF-IDF implementation
* Linear Algebra (Dot Product & Norms)
* Vector Similarity Search
* CSV Dataset Handling

---

## 🙋 About This Project

I am building small but meaningful projects as I progress through machine learning concepts.
This project represents my milestone in understanding **text feature extraction and similarity-based recommendations**.

> **Learning → Applying → Documenting → Showcasing**

---

## ⭐ Support

If you find this project helpful, consider giving the repository a **star** — it supports and motivates my ML journey.

GitHub Profile: [https://github.com/DolaSreecharan](https://github.com/DolaSreecharan)


