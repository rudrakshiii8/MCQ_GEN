from flask import Flask, render_template, request, redirect, session
from mcq_bank import mcq_bank

app = Flask(__name__)
app.secret_key = "supersecretkey"

classes = [str(i) for i in range(1, 13)]
subjects_per_class = {cls: list(mcq_bank.get(cls, {}).keys()) for cls in classes}

@app.route("/", methods=["GET"])
def select_class():
    return render_template("select_class.html", classes=classes)

@app.route("/subjects", methods=["POST"])
def class_subjects():
    selected_class = request.form["selected_class"]
    subjects = subjects_per_class.get(selected_class, [])
    return render_template("select_subjects.html", selected_class=selected_class, subjects=subjects)

@app.route("/select_level", methods=["POST"])
def select_level():
    selected_class = request.form["selected_class"]
    selected_subject = request.form["selected_subject"]
    levels = list(mcq_bank.get(selected_class, {}).get(selected_subject, {}).keys())
    return render_template("select_level.html",
                           selected_class=selected_class,
                           selected_subject=selected_subject,
                           levels=levels)

@app.route("/quiz", methods=["POST"])
def quiz():
    if "selected_level" in request.form:
        selected_class = request.form["selected_class"]
        selected_subject = request.form["selected_subject"]
        selected_level = request.form["selected_level"]

        questions = mcq_bank.get(selected_class, {}).get(selected_subject, {}).get(selected_level, [])

        session["questions"] = questions
        session["score"] = 0
        session["current_question_index"] = 0
        session["selected_class"] = selected_class
        session["selected_subject"] = selected_subject
        session["selected_level"] = selected_level
        session["user_answers"] = []

    else:
        selected_option = request.form.get("selected_option")
        current_question_index = int(request.form.get("current_question_index"))
        score = int(request.form.get("score"))
        questions = session.get("questions", [])
        user_answers = session.get("user_answers", [])

        correct_answer = questions[current_question_index]["answer"]
        if selected_option == correct_answer:
            score += 1

        user_answers.append(selected_option)
        session["score"] = score
        session["user_answers"] = user_answers
        session["current_question_index"] = current_question_index + 1

    current_question_index = session.get("current_question_index")
    questions = session.get("questions", [])

    if current_question_index >= len(questions):
        return redirect("/result")

    question = questions[current_question_index]
    return render_template("quiz.html",
                           question=question,
                           current_question_index=current_question_index,
                           total_questions=len(questions),
                           score=session.get("score", 0),
                           selected_class=session.get("selected_class", ""),
                           selected_subject=session.get("selected_subject", ""),
                           selected_level=session.get("selected_level", ""))

@app.route("/result", methods=["GET"])
def result():
    questions = session.get("questions", [])
    user_answers = session.get("user_answers", [])
    score = session.get("score", 0)

    results = []
    for i, q in enumerate(questions):
        user_answer = user_answers[i] if i < len(user_answers) else None
        results.append({
            "question": q["question"],
            "options": q["options"],
            "user_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": (user_answer == q["answer"])
        })

    return render_template("result.html",
                           score=score,
                           total=len(questions),
                           selected_class=session.get("selected_class", ""),
                           selected_subject=session.get("selected_subject", ""),
                           selected_level=session.get("selected_level", ""),
                           results=results)

if __name__ == "__main__":
    app.run(debug=True)
