# 🧠 VARK Learning Style Assessment Quiz  
**Due Date**: [11/06/25]  
**Course/Instructor**: [Course:MCS 253  Instructor:Ms Shirley KOMOGI]  

---

## 1. 📘 Project Title  
**VARK Learning Style Quiz - A Self-Assessment Tool for Discovering Learning Preferences**

---

## 2. 📌 What the Project is About  

This project implements a command-line based interactive quiz designed to determine a user's preferred learning style based on the **VARK model** — Visual (V), Aural (A), Read/Write (R), and Kinesthetic (K). The application presents 16 multiple-choice questions to the user and evaluates the responses to suggest a dominant or multimodal learning preference.

---

## 3. 🔍 Code Breakdown  

### 🧱 Class Usage  
- **Class Created**: `VARK`
  - This is the only class used in the program.
  - **No subclasses** are created or inherited.

### 🔁 Number of Functions and Their Purpose

| Function Name         | Purpose |
|-----------------------|---------|
| `__init__(self)`      | Initializes the response dictionary to track V, A, R, and K scores. |
| `ask_question(self, q_num)` | Displays a question and accepts 1 or 2 answers from the user, mapping them to learning style categories. |
| `calculate_scores(self)`   | Calculates total scores for each category and raises an error if no data is recorded. |
| `determine_preference(self)` | Analyzes the score data and determines the dominant or multimodal learning preference. |
| `run(self)`               | Executes the quiz loop, manages question flow, and handles exceptions. |

---

## 4. 🧮 Data Handling  

### ✅ Data Captured  
- User responses to 16 structured multiple-choice questions.

### 🧊 Data Types Used  
- `List[Dict]`: For storing questions and answer options.
- `Dict[str, int]`: For tracking scores (`{"V": 0, "A": 0, "R": 0, "K": 0}`).
- `Dict[int, Dict[str, str]]`: For mapping answer choices to VARK categories.

### 📚 Data Source  
- All data (questions and scoring chart) is **hardcoded** in the script.

---

## 5. ⚠️ Exception Handling  

The program includes several mechanisms to ensure smooth execution and valid user input:
- **Invalid question number**: Raises `ValueError`.
- **Invalid or duplicate input (e.g., "AA")**: Prompts the user to re-enter a valid choice.
- **Empty responses** before score calculation: Raises `ValueError` to prevent inaccurate analysis.

---

## 6. ✅ Program Outcome  

Upon successful execution:
- The user completes 16 questions.
- The system calculates and displays VARK scores.
- It prints out whether the user has a **primary** or **multimodal** learning preference.
- Helps users understand how they most effectively absorb and retain information.

---

## 7. 🪞 Reflection  

### 💡 Challenges Encountered  
- Designing a clean structure for mapping user input to scoring categories.
- Validating user inputs while allowing flexibility for single or multiple selections.
- Handling edge cases such as repeated or incorrect inputs.

### 📚 What I Learned  
- Importance of modular design using functions and classes.
- How to handle exceptions gracefully.
- Better understanding of Python data structures (dicts and lists) and input handling.

### 🔧 Areas for Improvement  
- Adding file-saving functionality to retain user results.

---

## 8. 🙏 Word of Thanks  

I would like to express my gratitude to my instructor, peers, and all the resources that supported me during the development of this project. This experience helped me strengthen my Python skills and deepen my understanding of user-centered design in programming.

---

## ▶️ Running the Program  

To run the script:
```bash
python vark_quiz.py
