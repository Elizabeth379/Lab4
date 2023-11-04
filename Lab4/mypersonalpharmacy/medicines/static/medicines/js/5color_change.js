    function applyStyles() {
        const fontSizeCheckbox = document.getElementById('fontSizeCheckbox');
        const fontSizeInput = document.getElementById('fontSizeInput');
        const textColorCheckbox = document.getElementById('textColorCheckbox');
        const textColorInput = document.getElementById('textColorInput');
        const backgroundColorCheckbox = document.getElementById('backgroundColorCheckbox');
        const backgroundColorInput = document.getElementById('backgroundColorInput');

        if (fontSizeCheckbox.checked) {
            document.body.style.fontSize = fontSizeInput.value + 'px';
        }

        if (textColorCheckbox.checked) {
            document.body.style.color = textColorInput.value;
        }

        if (backgroundColorCheckbox.checked) {
            document.querySelector('aside').style.backgroundColor = backgroundColorInput.value;
        }
    }

    // Обработчики для активации/деактивации соответствующих полей
    document.getElementById('fontSizeCheckbox').addEventListener('change', function () {
        document.getElementById('fontSizeInput').disabled = !this.checked;
    });

    document.getElementById('textColorCheckbox').addEventListener('change', function () {
        document.getElementById('textColorInput').disabled = !this.checked;
    });

    document.getElementById('backgroundColorCheckbox').addEventListener('change', function () {
        document.getElementById('backgroundColorInput').disabled = !this.checked;
    });
