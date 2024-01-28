const fs = require('fs');

function createListFromFile() {
    const filePath = '/path/to/file_paths.txt';
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const fileItems = fileContent.split('\n').filter(item => item.trim() !== '');

    return fileItems;
}

const fileList = createListFromFile();
console.log(fileList);

// You can select the container where you want to insert the images
let container = document.querySelector('.dynamic-container');

// Check if the container element exists
if (container) {
    // Then you can loop through the image sources and create an img element for each one
    extractedData.forEach(item => {
        let img = document.createElement('img');
        img.src = fileList;
        img.alt = "Dynamic Image";
        img.className = "dynamic-image";
        container.appendChild(img); // Append the img element to the container
    });
}
