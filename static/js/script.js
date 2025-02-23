$(document).ready(function() {
    // Handle input for predictions
    $('#inputText').on('input', function() {
        const text = $(this).val(); // Get the current input text
        const style = $('#style').val(); // Get the selected writing style

        if (text) {
            // Send the input and selected style to the server for predictions
            $.ajax({
                url: '/predict', // Flask route to handle prediction
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ text, style }),
                success: function(response) {
                    // Empty the previous predictions
                    $('#predictions').empty();

                    // Append new predictions to the predictions container
                    response.predictions.forEach(function(word) {
                        $('#predictions').append(`<span class="prediction">${word}</span>`);
                    });
                },
                error: function() {
                    console.error("Error fetching predictions");
                }
            });
        } else {
            // Clear predictions if input is empty
            $('#predictions').empty();
        }
    });

    // Handle click on predicted word
    $(document).on('click', '.prediction', function() {
        const word = $(this).text();
        const currentText = $('#inputText').val();

        // Append clicked word to the current input text
        $('#inputText').val(currentText + ' ' + word);

        // Clear predictions after word is selected
        $('#predictions').empty();
    });

    // Handle category change (for dynamic layout change)
    $('#style').on('change', function() {
        const style = $(this).val();
        changeLayout(style); // Change layout dynamically based on selected style
    });

    // Function to change layout dynamically
    function changeLayout(style) {
        // Update the layout based on the selected category/style
        const layoutContainer = $('#layout');
        layoutContainer.removeClass().addClass(`container ${style}-layout`);
    }
});
