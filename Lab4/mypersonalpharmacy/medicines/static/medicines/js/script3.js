document.addEventListener("DOMContentLoaded", function() {
    const left = document.getElementById("left_img");
    const right = document.getElementById("right_img");

    window.addEventListener("scroll", () => {
        // Получаем текущее значение вертикальной прокрутки
        const scrollY = window.scrollY;
        left.style.transform = `translateY(-${scrollY}px)`;
        right.style.transform = `translateY(-${scrollY}px)`;
    });

    const partnerBlocks = document.querySelectorAll(".partner-block");
});
