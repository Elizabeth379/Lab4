// Функция для отображения обратного отсчета
    function countdown() {
        // Получаем текущее время
        const currentTime = new Date().getTime();

        // Получаем сохраненное время старта из локального хранилища
        const storedStartTime = localStorage.getItem('countdownStartTime');

        // Если время старта не сохранено, сохраняем текущее время
        if (!storedStartTime) {
            localStorage.setItem('countdownStartTime', currentTime);
        }

        // Рассчитываем разницу во времени с сохраненным значением
        const timeDifference = storedStartTime ? currentTime - storedStartTime : 0;

        // Рассчитываем оставшееся время с учетом прошедшего времени
        const remainingTime = 60 * 60 * 1000 - timeDifference;

        // Запускаем новый отсчет с учетом прошедшего времени
        startTimer(remainingTime);
    }

    // Функция для запуска таймера
    function startTimer(duration) {
        const countdownElement = document.getElementById('countdown');

        // Запускаем интервал с обновлением каждую секунду
        const intervalId = setInterval(function () {
            // Рассчитываем минуты и секунды
            const minutes = Math.floor((duration % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((duration % (1000 * 60)) / 1000);

            // Отображаем оставшееся время
            countdownElement.textContent = `${minutes} минут ${seconds} секунд`;

            // Уменьшаем время на 1 секунду
            duration -= 1000;

            // Проверяем, закончился ли отсчет
            if (duration < 0) {
                clearInterval(intervalId);
                countdownElement.textContent = "Отсчет завершен";
            }
        }, 1000);
    }

    // Запуск функции при загрузке страницы
    countdown();