// When the document is ready
$(document).ready(function () {
    // Get the element with the 'makeHistogram' id
    var scripts = document.getElementById('makeHistogram');

    // Get the base64-encoded image string from the 'image' attribute
    var imageStr = scripts.getAttribute('image');

    // Create a new Image object
    var image = new Image();

    // Set the base64 value as the image source
    image.src = "data:image/png;base64," + imageStr;

    // Wait for the image to be fully loaded before calling calculateRGBHistogram
    image.onload = function() {
        var histogram = calculateRGBHistogram(image);
        drawRGBHistogramWithChartJS(histogram);
    };
});

// Function to calculate the RGB histogram from the given image
function calculateRGBHistogram(image) {
    // Create a 2D array to store the histogram values
    var histogram = Array(256).fill().map(() => Array(3).fill(0));

    // Create a temporary canvas to get the context
    var canvas = document.createElement('canvas');
    var context = canvas.getContext('2d');
    canvas.width = image.width;
    canvas.height = image.height;

    // Draw the image onto the canvas
    context.drawImage(image, 0, 0, image.width, image.height);

    // Get the pixel data from the canvas
    var imageData = context.getImageData(0, 0, image.width, image.height);
    var pixels = imageData.data;

    // Loop through each pixel and update the histogram
    for (var i = 0; i < pixels.length; i += 4) {
        var red = pixels[i];
        var green = pixels[i + 1];
        var blue = pixels[i + 2];

        histogram[red][0]++;
        histogram[green][1]++;
        histogram[blue][2]++;
    }

    return histogram;
}

// Function to draw the RGB histogram using Chart.js
function drawRGBHistogramWithChartJS(histogram) {
    // Create the labels for the x-axis and y-axis
    var labelsX = Array.from({ length: 256 }, (_, i) => i);
    var labelsY = ['Red', 'Green', 'Blue'];

    // Create the data for the histogram
    var data = {
        labels: labelsX,
        datasets: labelsY.map((label, index) => ({
            label: label,
            backgroundColor: `rgba(${index === 0 ? '255, 0, 0' : index === 1 ? '0, 255, 0' : '0, 0, 255'}, 0.5)`,
            data: histogram.map(row => row[index])
        }))
    };

    // Setup the config for the chart
    var config = {
        type: 'bar',
        data: data,
        options: {
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'RGB Value'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Frequency'
                    }
                }
            }
        }
    };

    // Create the chart
    var ctx = document.getElementById('histogramCanvas').getContext('2d');
    new Chart(ctx, config);
}
