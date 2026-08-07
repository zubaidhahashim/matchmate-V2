const analysisForm = document.querySelector("#analysis-form");
const loadingScreen = document.getElementById("loading-screen");

analysisForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    loadingScreen.style.display = "flex";

    const loadingText = document.getElementById("loading-text");
    loadingText.textContent = "Analyzing your resume...";

    const formData = new FormData(analysisForm);

    const startTime = Date.now();

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        const elapsed = Date.now() - startTime;

        if (elapsed < 3000) {
            await new Promise(resolve =>
                setTimeout(resolve, 3000 - elapsed)
            );
        }

        loadingScreen.style.display = "none";

        const results = document.getElementById("results-container");

        results.style.display = "block";

        results.scrollIntoView({
            behavior: "smooth"
        });

        const score = Number(data.score).toFixed(2);
        const progress = parseFloat(score) * 3.6;

        results.innerHTML = `
        <div class="results-card">

            <h2 class="results-title">
                Resume Analysis Report
            </h2>

            <div class="score-wrapper">

                <div class="score-circle"
                     style="--progress:${progress}deg;">

                    <div class="score-inner">

                        <h1>${score}%</h1>

                        <p>Match Score</p>

                    </div>

                </div>

            </div>

            <hr>

            <div class="dashboard-section">

                <h3>✅ Matching Skills</h3>

                <div class="badge-container">

                    ${data.matching_skills.map(skill =>
                        `<span class="skill-badge success">${skill}</span>`
                    ).join("")}

                </div>

            </div>

            <hr>

            <div class="dashboard-section">

                <h3>❌ Missing Skills</h3>

                <div class="badge-container">

                    ${data.missing_skills.map(skill =>
                        `<span class="skill-badge danger">${skill}</span>`
                    ).join("")}

                </div>

            </div>

            <hr>

            <div class="dashboard-section">

                <h3>💡 Recommendations</h3>

                <ul class="recommendation-list">

                    ${data.recommendations.map(item =>
                        `<li>${item}</li>`
                    ).join("")}

                </ul>

            </div>

            <div class="dashboard-buttons">

    <a href="/optimizer" class="primary-btn">
        Optimize Resume
    </a>

    <button
        type="button"
        class="secondary-btn"
        onclick="window.location.reload()">

        Analyze Another Resume

    </button>

</div>

        </div>
        `;

    }

    catch (error) {

        console.error(error);

        loadingScreen.style.display = "none";

        alert("Something went wrong while analyzing the resume.");

    }

});