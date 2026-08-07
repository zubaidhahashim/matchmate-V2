const analysisForm = document.querySelector("form");
const loadingScreen = document.getElementById("loading-screen");

analysisForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    loadingScreen.style.display = "flex";

    const formData = new FormData(analysisForm);

    const steps = [
        "Uploading Resume...",
        "Reading Resume...",
        "Identifying Skills...",
        "Comparing with Job Description...",
        "Calculating Match Score...",
        "Preparing Recommendations..."
    ];

    const loadingText = document.getElementById("loading-text");

    let step = 0;

    loadingText.textContent = steps[0];

    const interval = setInterval(() => {

        step++;

        if (step < steps.length) {

            loadingText.textContent = steps[step];

        }

    }, 650);

    const startTime = Date.now();

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        const elapsed = Date.now() - startTime;

        const minimumTime = 4000;

        if (elapsed < minimumTime) {

            await new Promise(resolve =>
                setTimeout(resolve, minimumTime - elapsed)
            );

        }

        clearInterval(interval);

        loadingText.textContent = "Opening Results...";

        await new Promise(resolve =>
            setTimeout(resolve, 700)
        );

        loadingScreen.style.display = "none";

        const results = document.getElementById("results-container");

        results.style.display = "block";

        const score = Math.round(data.score);

        const progress = score * 3.6;

        results.innerHTML = `

        <div class="results-card">

            <h2 style="text-align:center;margin-bottom:40px;">
                Resume Analysis Complete
            </h2>

            <div class="score-wrapper">

                <div class="score-circle" style="--progress:${progress}deg;">

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

                <button class="secondary-btn"
                        onclick="window.location.reload()">

                    Analyze Another Resume

                </button>

            </div>

        </div>

        `;

    }

    catch (error) {

        clearInterval(interval);

        console.error(error);

        loadingScreen.style.display = "none";

        alert("Something went wrong while analyzing the resume.");

    }

});