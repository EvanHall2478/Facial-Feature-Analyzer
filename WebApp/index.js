// Suppose you have a list of image sources
let imageSources = ["./testPics/IMG_2433.JPG", "./testPics/IMG_E2364.JPG", "./testPics/IMG_E2378.JPG", "./testPics/IMG_E2393.JPG"];

// You can select the container where you want to insert the images
let container = document.querySelector('.dynamic-container');

// Check if the container element exists
if (container) {
    // Then you can loop through the image sources and create an img element for each one
    imageSources.forEach(src => {
        let img = document.createElement('img');
        img.src = src;
        img.alt = "Dynamic Image";
        img.className = "dynamic-image";
        container.appendChild(img);
    });
}
