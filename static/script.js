
function redirectToPrompt(promptType) {
    // Redirect to the common prompt page with the selected prompt type
    window.location.href = "/prompt/" + encodeURIComponent(promptType);
}


function submitPrompt() {
    const userInput = document.getElementById('userInput').value.trim(); // Get user input and remove leading/trailing whitespace

    if (userInput) {
        const encodedInput = encodeURIComponent(userInput); // Encode user input for safe URL parameter
        window.location.href = `/next?userPrompt=${encodedInput}`; // Redirect to next page with user prompt as query parameter
    } else {
        alert('Please enter a valid prompt.'); // Alert user if input is empty
    }
}

// Function to handle click on follow-up prompts
function selectFollowUpPrompt(promptText) {
    const userInput = document.getElementById('userInput');
    userInput.value = promptText; // Set the text box value to the clicked prompt
}

// Event delegation to handle click events on follow-up prompts
document.addEventListener('DOMContentLoaded', function() {
    // Get all follow-up prompts (list items) and add click event listener
    const followUpPrompts = document.querySelectorAll('#followUpPrompts li');
    followUpPrompts.forEach(prompt => {
        prompt.addEventListener('click', function() {
            const selectedPrompt = this.textContent; // Get the text content of the clicked prompt
            selectFollowUpPrompt(selectedPrompt); // Call function to set text box value
        });
    });
});

function handlePromptClick(userPrompt) {
    const encodedPrompt = encodeURIComponent(userPrompt);
    const nextPageUrl = `/next?userPrompt=${encodedPrompt}`;

    // Redirect to the next page with the selected user prompt
    window.location.href = nextPageUrl;
}


function handleDoneButtonClick() {
    // Action for the "Done" button
    document.getElementById("something_else_form").action = "/something_else_final";
}