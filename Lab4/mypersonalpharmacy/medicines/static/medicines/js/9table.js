    let tableSize = 0;
let maxSelection = 1;

function generateTable() {
    tableSize = document.getElementById('size').value;
    maxSelection = document.getElementById('maxSelection').value;
    const table = document.getElementById('myTable');

    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }

    const tbody = document.createElement('tbody');

    for (let i = 0; i < tableSize; i++) {
        const row = document.createElement('tr');

        for (let j = 0; j < tableSize; j++) {
            const cell = document.createElement('td');
            cell.textContent = Math.floor(Math.random() * 100) + 1;
            cell.addEventListener('click', highlightCell);
            row.appendChild(cell);
        }

        tbody.appendChild(row);
    }

    table.appendChild(tbody);
}

function highlightCell() {
    const isSelected = this.classList.contains('highlight');

    // Проверяем, есть ли выделенные ячейки в текущем ряду
    const currentRow = this.parentElement;
    const selectedInRow = Array.from(currentRow.querySelectorAll('.highlight'));

    // Проверяем, есть ли выделенные ячейки в текущем столбце
    const currentColumnIndex = Array.from(currentRow.children).indexOf(this);
    const selectedInColumn = Array.from(document.querySelectorAll(`td:nth-child(${currentColumnIndex + 1})`)).filter(cell => cell.classList.contains('highlight'));

    if (!isSelected && selectedInRow.length >= maxSelection || selectedInColumn.length >= maxSelection) {
        // Превышено максимальное количество выделенных ячеек в ряду/столбце
        return;
    }

    // Проверяем, есть ли соседние выделенные ячейки
    const neighbors = [currentRow.previousElementSibling, currentRow.nextElementSibling]
        .map(row => row && row.querySelector(`td:nth-child(${currentColumnIndex + 1})`))
        .filter(cell => cell && cell.classList.contains('highlight'));

    if (!isSelected && neighbors.length > 0) {
        // Нельзя выделять соседние ячейки
        return;
    }

    // Проверяем, есть ли соседние выделенные ячейки в текущем ряду
    const neighborCellsInRow = Array.from(currentRow.children).filter(cell => cell.classList.contains('highlight') && cell !== this && Math.abs(Array.from(currentRow.children).indexOf(cell) - currentColumnIndex) <= 1);

    if (neighborCellsInRow.length > 0) {
        // Нельзя выделять соседние ячейки в ряду
        return;
    }

    // Проверяем, есть ли соседние выделенные ячейки в текущем столбце
    const neighborCellsInColumn = Array.from(document.querySelectorAll(`td:nth-child(${currentColumnIndex + 1})`)).filter(cell => cell.classList.contains('highlight') && cell !== this && Math.abs(Array.from(currentRow.parentElement.children).indexOf(cell.parentElement) - Array.from(currentRow.parentElement.children).indexOf(currentRow)) <= 1);

    if (neighborCellsInColumn.length > 0) {
        // Нельзя выделять соседние ячейки в столбце
        return;
    }

    this.classList.toggle('highlight');
    this.classList.toggle('multiple-of-two', parseInt(this.textContent) % 2 === 0);
}

    function transposeTable() {
    const table = document.getElementById('myTable');
    const rows = Array.from(table.querySelectorAll('tr'));

    const cols = rows[0].querySelectorAll('td');

    const transposedTable = [];
    for (let i = 0; i < cols.length; i++) {
        const newRow = [];

        for (let j = 0; j < rows.length; j++) {
            newRow.push(rows[j].querySelectorAll('td')[i].cloneNode(true));
        }

        transposedTable.push(newRow);
    }

    // Очищаем текущую таблицу
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }

    // Добавляем транспонированные ячейки обратно в таблицу
    transposedTable.forEach(row => {
        const newRow = document.createElement('tr');
        row.forEach(cell => {
            newRow.appendChild(cell);
        });
        table.appendChild(newRow);
    });
}

    function addRow() {
    const table = document.getElementById('myTable');
    const newRow = document.createElement('tr');

    for (let i = 0; i < tableSize; i++) {
        const cell = document.createElement('td');
        cell.textContent = Math.floor(Math.random() * 100) + 1;
        cell.addEventListener('click', highlightCell);
        newRow.appendChild(cell);
    }

    table.appendChild(newRow);
}


    function addColumn() {
    const table = document.getElementById('myTable');
    const colCount = table.rows[0].cells.length;
    const newCell = document.createElement('td');
    newCell.textContent = Math.floor(Math.random() * 100) + 1;
    newCell.addEventListener('click', highlightCell);

    for (const row of table.rows) {
        const cell = newCell.cloneNode(true);
        row.appendChild(cell);
    }

    tableSize++;
}


    document.addEventListener('DOMContentLoaded', function () {
    const table = document.getElementById('myTable');
    table.addEventListener('click', handleCellClick);
});

function handleCellClick(event) {
    const cell = event.target;

    if (cell.tagName === 'TD') {
        const value = parseInt(cell.textContent);

        // Определяем цвет для выделения
        const color = value % 2 === 0 ? 'lightblue' : 'lightcoral';

        // Выделяем ячейку цветом
        cell.style.backgroundColor = color;
    }
}
