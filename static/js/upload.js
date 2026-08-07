// Upload Box

const uploadBox = document.querySelector(".upload-box");
const fileInput = document.getElementById("resume");
const fileName = document.getElementById("file-name");

// Open file browser

uploadBox.addEventListener("click", () => {

    fileInput.click();

});

// When a file is selected

fileInput.addEventListener("change", () => {

    if (fileInput.files.length > 0) {

        fileName.textContent =
            "✓ " + fileInput.files[0].name + " selected successfully";

    }

});

// Drag over

uploadBox.addEventListener("dragover", (e) => {

    e.preventDefault();

    uploadBox.classList.add("dragging");

});

// Drag leave

uploadBox.addEventListener("dragleave", () => {

    uploadBox.classList.remove("dragging");

});

// Drop file

uploadBox.addEventListener("drop", (e) => {

    e.preventDefault();

    uploadBox.classList.remove("dragging");

    fileInput.files = e.dataTransfer.files;

    if (fileInput.files.length > 0) {

        fileName.textContent =
            "✓ " + fileInput.files[0].name + " selected successfully";

    }

});