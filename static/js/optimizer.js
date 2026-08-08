const form = document.getElementById("optimizer-form");
const loadingScreen = document.getElementById("loading-screen");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    loadingScreen.style.display = "flex";

    const loadingText =
        document.getElementById("loading-text");

    loadingText.textContent =
        "Analyzing your resume and identifying improvements...";

    const formData = new FormData(form);

    try {

        const response = await fetch("/optimizer", {

            method: "POST",

            body: formData

        });


        if (!response.ok) {

            throw new Error(
                `Server returned ${response.status}`
            );

        }


        const data = await response.json();


        loadingScreen.style.display = "none";


        const results =
            document.getElementById("optimizer-results");


        results.style.display = "block";


        results.scrollIntoView({

            behavior: "smooth",

            block: "start"

        });


        let html = `

            <div class="results-card optimizer-results-card">

                <div class="optimizer-results-header">

                    <span class="optimizer-label">
                        Resume Improvement Report
                    </span>

                    <h2>
                        Resume Optimization Suggestions
                    </h2>

                    <p>
                        Review the recommendations below and
                        update your resume where they apply.
                    </p>

                </div>

        `;


        data.suggestions.forEach((section, index) => {

            html += `

                <div class="optimizer-section">

                    <div class="optimizer-section-header">

                        <span class="optimizer-number">
                            ${index + 1}
                        </span>

                        <h3>
                            ${section.title}
                        </h3>

                    </div>

                    <ul class="optimizer-list">

            `;


            section.items.forEach(item => {

                html += `

                    <li>

                        <span class="optimizer-check">
                            ✓
                        </span>

                        <span>
                            ${item}
                        </span>

                    </li>

                `;

            });


            html += `

                    </ul>

                </div>

            `;


            if (index < data.suggestions.length - 1) {

                html += `<hr class="optimizer-divider">`;

            }

        });


        html += `

                <div class="optimizer-footer">

                    <p>
                        💡 Apply the suggestions that are
                        relevant to your actual experience.
                        Never add skills or experience you
                        don't genuinely have.
                    </p>

                    <button
                        class="secondary-btn"
                        type="button"
                        onclick="location.reload()">

                        Optimize Another Resume

                    </button>

                </div>

            </div>

        `;


        results.innerHTML = html;


    }

    catch (error) {

        console.error(
            "Resume optimizer error:",
            error
        );


        loadingScreen.style.display = "none";


        const results =
            document.getElementById("optimizer-results");


        results.style.display = "block";


        results.innerHTML = `

            <div class="results-card">

                <h2>
                    Unable to Optimize Resume
                </h2>

                <p>
                    Something went wrong while analyzing
                    your resume. Please check your PDF and
                    job description and try again.
                </p>

                <button
                    class="secondary-btn"
                    onclick="location.reload()">

                    Try Again

                </button>

            </div>

        `;

    }

});