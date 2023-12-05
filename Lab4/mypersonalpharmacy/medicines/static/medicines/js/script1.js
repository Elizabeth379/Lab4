document.addEventListener("DOMContentLoaded", function() {
    function updateTime() {
        // Получаем ссылку на элемент
        const currentTimeElement = document.getElementById("current-time");
        // Создание объекта
        const now = new Date();
        // Текущее значение времени преобразуем в строку, используя функцию padStart
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        // Текстовое содержание элемента
        const formattedTime = `${hours}:${minutes}:${seconds}`;
        currentTimeElement.textContent = formattedTime;
    }
    // Обновление времени каждую секунду
    setInterval(updateTime, 1000);
});
