<script>
        /*
        document.addEventListener("DOMContentLoaded", function () {
            console.log("DOM content loaded.");
            // Define timer variable globally
            var timer;
            // Get the checkout button element
            var checkoutButton = document.getElementById("checkout-button");
            var countdownElement = document.getElementById("countdown");

            // Function to update the countdown timer
            function updateCountdown(endTime) {
                var now = new Date();
                var distance = new Date(endTime) - now;
                if (distance > 0) {
                    console.log("Countdown active. Distance remaining:", distance);
                    disableCheckoutButton(false); // Enable the button when countdown is active
                    updateTimerUI(distance); // Update the countdown timer UI
                } else {
                    console.log("Countdown expired.");
                    clearInterval(timer);
                    disableCheckoutButton(true); // Disable the button when countdown expires
                    if (countdownElement) {
                        countdownElement.innerHTML = "EXPIRED"; // Update the countdown element with "EXPIRED"
                    }
                }
            }

            // Function to enable/disable checkout button
            function disableCheckoutButton(disable) {
                if (checkoutButton) {
                    checkoutButton.disabled = disable;
                    if (disable) {
                        checkoutButton.setAttribute("title", "Production is ongoing");
                        console.log("Checkout button disabled.");
                    } else {
                        checkoutButton.removeAttribute("title");
                        console.log("Checkout button enabled.");
                    }
                } else {
                    console.log("Checkout button element not found.");
                }
            }

            // Function to update the countdown timer UI
            function updateTimerUI(distance) {
                if (countdownElement) {
                    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                    countdownElement.innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
                } else {
                    console.log("Countdown element not found.");
                }
            }

            var eventUrl = "{% url 'get_event_data' %}";
            fetch(eventUrl)
                .then(response => response.json())
                .then(data => {
                    if (data.has_event) {
                        var endTime = data.end_datetime;
                        console.log("End time fetched:", endTime);
                        // Assign timer variable
                        timer = setInterval(function () {
                            updateCountdown(endTime);
                        }, 1000);
                        // Initial update to show countdown immediately
                        updateCountdown(endTime);
                    } else {
                        console.log("No event found.");
                        disableCheckoutButton(true); // Disable the button when no event is found
                        if (countdownElement) {
                            countdownElement.innerHTML = "No Production Batch.";
                        }
                    }
                })
                .catch(error => console.error('Error:', error));
        });*/
    </script>