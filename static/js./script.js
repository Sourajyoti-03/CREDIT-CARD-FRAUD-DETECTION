// Add a fade-in effect to the header bar
document.addEventListener("DOMContentLoaded", function() {
    var headerBar = document.querySelector(".header-bar");
    headerBar.style.opacity = 0;
    setTimeout(function() {
        headerBar.style.opacity = 1;
    }, 500);
});

// Add a hover effect to the prediction button
var button = document.querySelector(".button");
button.addEventListener("mouseover", function() {
    button.style.transform = "scale(1.1)";
});
button.addEventListener("mouseout", function() {
    button.style.transform = "scale(1)";
});
document.addEventListener('DOMContentLoaded', function() {
    const lines = document.querySelectorAll('.line');

    // Example: Start animation on button click
    document.querySelector('.button').addEventListener('click', function() {
        lines.forEach(line => line.style.animationPlayState = 'running');
    });

    // Example: Stop animation after 5 seconds
    setTimeout(() => {
        lines.forEach(line => line.style.animationPlayState = 'paused');
    }, 5000);
});
