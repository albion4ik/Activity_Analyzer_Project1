from flask import Flask, render_template, request
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import os
from werkzeug.utils import secure_filename

# === Импорт всех алгоритмов ===
from ai_modules import (
    linear_regression,
    logistic_regression,
    decision_tree,
    random_forest,
    naive_bayes,
    knn,
    svm,
    gradient_boosting,
    kmeans,
    fp_growth,
    pca,
    object_detection
)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    activity_summary = None
    suggestion = None
    ai_results = []
    chart_url = None
    kmeans_result = None
    pca_result = None
    fpgrowth_result = None
    image_result = None
    image_path = None

    if request.method == "POST":
        run_mode = request.form.get("run_mode")

        if run_mode == "analyze_activity":
            activities = {}
            for hour in range(6, 23):
                activity = request.form.get(f"hour_{hour}", "Other")
                activities[hour] = activity

            activity_summary = dict(Counter(activities.values()))
            studying_hours = activity_summary.get("Studying", 0)
            suggestion = "✅ Ваш учебный режим выглядит сбалансированным." if studying_hours >= 3 else "📌 Рекомендуется увеличить учебное время хотя бы до 3 часов в день."

        elif run_mode == "run_ai":
            X_train = np.array([[1], [2], [3], [4]])
            y_train = np.array(["Studying", "Reading", "Eating", "Resting"])
            X_test = np.array([[5]])
            y_test = np.array(["Studying"])

            ai_results = [
                ("Linear Regression", *linear_regression.run(X_train, y_train, X_test, y_test)),
                ("Logistic Regression", *logistic_regression.run(X_train, y_train, X_test, y_test)),
                ("Decision Tree", *decision_tree.run(X_train, y_train, X_test, y_test)),
                ("Random Forest", *random_forest.run(X_train, y_train, X_test, y_test)),
                ("Naive Bayes", *naive_bayes.run(X_train, y_train, X_test, y_test)),
                ("KNN", *knn.run(X_train, y_train, X_test, y_test)),
                ("SVM", *svm.run(X_train, y_train, X_test, y_test)),
                ("Gradient Boosting", *gradient_boosting.run(X_train, y_train, X_test, y_test)),
            ]

            labels = [r[0] for r in ai_results]
            accuracies = [r[2] for r in ai_results]
            fig, ax = plt.subplots()
            ax.barh(labels, accuracies, color='mediumorchid')
            ax.set_xlabel("Accuracy")
            ax.set_title("Algorithm Accuracy Comparison")
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            chart_url = base64.b64encode(buf.getvalue()).decode('utf-8')
            plt.close()

            # Task B
            kmeans_result = kmeans.run(X_train)
            pca_result = pca.run(X_train)
            fpgrowth_result = fp_growth.run([["Studying", "Reading"], ["Eating", "Resting"]])

        elif run_mode == "run_cv":
            image = request.files.get("image_file")
            if image:
                filename = secure_filename(image.filename)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                image.save(save_path)
                image_result = object_detection.run(save_path)
                image_path = f"/static/uploads/{filename}"

    return render_template("index.html",
                           activity_summary=activity_summary,
                           suggestion=suggestion,
                           ai_results=ai_results,
                           chart_url=chart_url,
                           kmeans_result=kmeans_result,
                           pca_result=pca_result,
                           fpgrowth_result=fpgrowth_result,
                           image_result=image_result,
                           image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
