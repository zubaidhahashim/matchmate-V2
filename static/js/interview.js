// ==========================================
// INTERVIEW COACH
// Personalized Questions Only
// ==========================================

const form = document.getElementById("interview-form");
const results = document.getElementById("interview-results");

const uploadBox = document.querySelector(".upload-box");
const fileInput = document.getElementById("interview-resume");
const fileName = document.getElementById("interview-file-name");


// ==========================================
// PDF UPLOAD
// ==========================================

if (uploadBox && fileInput) {

    uploadBox.addEventListener("click", function () {

        fileInput.click();

    });

}


if (fileInput) {

    fileInput.addEventListener("change", function () {

        if (fileInput.files.length > 0) {

            const file = fileInput.files[0];

            if (file.type !== "application/pdf") {

                alert("Please select a PDF file.");

                fileInput.value = "";

                if (fileName) {
                    fileName.textContent = "";
                }

                return;

            }

            if (fileName) {

                fileName.textContent =
                    "✓ " + file.name + " selected successfully";

            }

        }

    });

}


// ==========================================
// DRAG & DROP
// ==========================================

if (uploadBox) {

    uploadBox.addEventListener("dragover", function (event) {

        event.preventDefault();

        uploadBox.classList.add("dragging");

    });


    uploadBox.addEventListener("dragleave", function () {

        uploadBox.classList.remove("dragging");

    });


    uploadBox.addEventListener("drop", function (event) {

        event.preventDefault();

        uploadBox.classList.remove("dragging");

        const files = event.dataTransfer.files;

        if (files.length === 0) {
            return;
        }

        const file = files[0];

        if (file.type !== "application/pdf") {

            alert("Please upload a PDF file.");

            return;

        }

        fileInput.files = files;

        if (fileName) {

            fileName.textContent =
                "✓ " + file.name + " selected successfully";

        }

    });

}


// ==========================================
// START INTERVIEW
// ==========================================

form.addEventListener("submit", async function (event) {

    event.preventDefault();


    // Check resume

    if (!fileInput.files || fileInput.files.length === 0) {

        alert("Please upload your resume PDF first.");

        return;

    }


    const formData = new FormData(form);


    // Show results area

    results.style.display = "block";


    // Loading screen

    results.innerHTML = `

        <div class="results-card">

            <div style="
                text-align:center;
                padding:40px;
            ">

                <div class="spinner"></div>

                <h2 style="margin-top:25px;">
                    Preparing Your Interview
                </h2>

                <p style="color:#64748B;">
                    Creating personalized questions
                    based on your resume and job...
                </p>

            </div>

        </div>

    `;


    results.scrollIntoView({

        behavior: "smooth",

        block: "start"

    });


    try {

        const response = await fetch("/interview", {

            method: "POST",

            body: formData

        });


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const data = await response.json();


        if (
            !data.questions ||
            data.questions.length === 0
        ) {

            throw new Error(
                "No interview questions were generated."
            );

        }


        showQuestions(data.questions);

    }


    catch (error) {

        console.error(
            "Interview error:",
            error
        );


        results.innerHTML = `

            <div class="results-card">

                <h2 style="
                    text-align:center;
                    color:#DC2626;
                ">
                    Unable to Generate Questions
                </h2>

                <p style="
                    text-align:center;
                    color:#64748B;
                ">
                    Something went wrong while generating
                    your personalized interview questions.
                </p>

                <div style="
                    text-align:center;
                    margin-top:25px;
                ">

                    <button
                        class="secondary-btn"
                        onclick="location.reload()">

                        Try Again

                    </button>

                </div>

            </div>

        `;

    }

});


// ==========================================
// DISPLAY QUESTIONS
// ==========================================

function showQuestions(questionList) {

    let questionsHTML = "";


    questionList.forEach(function (item, index) {

        // The backend normally returns an object.
        // This also supports plain strings just in case.

        const question =
            typeof item === "object"
                ? item.question
                : item;


        const category =
            typeof item === "object"
                ? item.category || "General"
                : "General";


        const difficulty =
            typeof item === "object"
                ? item.difficulty || "Medium"
                : "Medium";


        questionsHTML += `

            <div class="interview-question-card">

                <div class="question-top">

                    <span class="question-number">
                        ${index + 1}
                    </span>

                    <div class="question-meta">

                        <span class="question-category">
                            ${escapeHTML(category)}
                        </span>

                        <span class="question-difficulty">
                            ${escapeHTML(difficulty)}
                        </span>

                    </div>

                </div>


                <h3>
                    ${escapeHTML(question)}
                </h3>

            </div>

        `;

    });


    results.innerHTML = `

        <div class="results-card interview-results-card">


            <!-- ==========================
                 HEADER
                 ========================== -->

            <div class="interview-results-header">

                <span class="optimizer-label">
                    Personalized Interview
                </span>

                <h2>
                    Your Interview Questions
                </h2>

                <p>
                    These questions were generated using
                    your resume and target job description.
                </p>

            </div>


            <!-- ==========================
                 QUESTIONS
                 ========================== -->

            <div class="interview-question-list">

                ${questionsHTML}

            </div>


            <!-- ==========================
                 FOOTER
                 ========================== -->

            <div class="interview-results-footer">

                <p>
                    💡 Practice answering each question
                    aloud and use examples from your
                    actual experience whenever possible.
                </p>


                <div class="dashboard-buttons">

                    <button
                        class="primary-btn"
                        type="button"
                        onclick="location.reload()">

                        Generate New Questions

                    </button>


                    <a
                        href="/"
                        class="secondary-btn">

                        Back to Home

                    </a>

                </div>

            </div>


        </div>

    `;


    results.scrollIntoView({

        behavior: "smooth",

        block: "start"

    });

}


// ==========================================
// ESCAPE HTML
// ==========================================

function escapeHTML(value) {

    return String(value)

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;")

        .replace(/"/g, "&quot;")

        .replace(/'/g, "&#039;");

}