function calculateAgeAndCheckPermission() {
        // Запрашиваем дату рождения
        const dobString = prompt("Введите свою дату рождения в формате ГГГГ-ММ-ДД", "2000-01-01");

        // Преобразуем введенную строку в объект Date
        const dob = new Date(dobString);

        // Рассчитываем возраст
        const age = calculateAge(dob);

        // Определяем день недели
        const dayOfWeek = getDayOfWeek(dob);

        // Проверяем, является ли пользователь совершеннолетним
        if (age >= 18) {
            alert(`Вам ${age} лет. День недели вашего рождения: ${dayOfWeek}`);
        } else {
            // Пользователь несовершеннолетний
            const parentalConsent = confirm("Вы несовершеннолетний. Для продолжения использования сайта необходимо разрешение родителей. Продолжить?");
            if (parentalConsent) {
                alert(`Вам ${age} лет. День недели вашего рождения: ${dayOfWeek}. Разрешение родителей получено.`);
            } else {
                alert("Извините, доступ запрещен без разрешения родителей.");
            }
        }
    }

    function calculateAge(dateOfBirth) {
        const today = new Date();
        let age = today.getFullYear() - dateOfBirth.getFullYear();
        const monthDiff = today.getMonth() - dateOfBirth.getMonth();

        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dateOfBirth.getDate())) {
            age--;
        }

        return age;
    }

    function getDayOfWeek(date) {
        const daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
        return daysOfWeek[date.getDay()];
    }

    // Запуск функции при загрузке страницы
    calculateAgeAndCheckPermission();