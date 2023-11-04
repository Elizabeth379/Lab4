let rotationInterval = null;
let isPageActive = true;
let bannerIndex = 0;

function updateRotationInterval() {
    const intervalInput = document.getElementById('interval');
    const newInterval = parseInt(intervalInput.value, 10) * 1000; // Convert to milliseconds
    clearInterval(rotationInterval);
    rotationInterval = setInterval(rotateBanner, newInterval);
}

function rotateBanner() {
    if (isPageActive) {
        const banners = document.querySelectorAll('.banner');
        banners.forEach((banner, index) => {
            banner.style.opacity = index === bannerIndex ? '1' : '0';
        });

        bannerIndex = (bannerIndex + 1) % banners.length;
    }
}

function openLink(url) {
    window.open(url, '_blank');
}

document.addEventListener('visibilitychange', function () {
    isPageActive = document.visibilityState === 'visible';


    if (isPageActive) {
        rotateBanner(); // Manually rotate banner when the page becomes active
    }
});

// Initial setup
updateRotationInterval();
rotateBanner();