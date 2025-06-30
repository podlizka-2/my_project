let currentData = [];
let currentSort = { field: null, direction: 'asc' };

function loadData() {
    const params = new URLSearchParams({
        min_price: document.getElementById('minPrice').value || '',
        max_price: document.getElementById('maxPrice').value || '',
        min_rating: document.getElementById('minRating').value || '',
        min_reviews: document.getElementById('minReviews').value || ''
    });

    fetch(`/api/products/?${params}`)
        .then(response => response.json())
        .then(data => {
            currentData = data;
            renderTable(data);
            renderCharts(data);
        });
}

function sortTable(field) {
    if (currentSort.field === field) {
        currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
    } else {
        currentSort.field = field;
        currentSort.direction = 'asc';
    }

    currentData.sort((a, b) => {
        const valA = a[field];
        const valB = b[field];
        
        if (valA < valB) return currentSort.direction === 'asc' ? -1 : 1;
        if (valA > valB) return currentSort.direction === 'asc' ? 1 : -1;
        return 0;
    });

    renderTable(currentData);
}

function renderTable(data) {
    const table = document.getElementById('productsTable');
    table.innerHTML = '';
    
    data.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.price} ₽</td>
            <td>${item.sale_price} ₽</td>
            <td>${item.rating}</td>
            <td>${item.reviews_count}</td>
        `;
        table.appendChild(row);
    });
}

function updatePagination(data) {
    const totalPages = Math.ceil(data.count / 10);
    document.getElementById('currentPage').textContent = data.current_page;
    document.getElementById('prevPage').disabled = !data.previous;
    document.getElementById('nextPage').disabled = !data.next;
}


document.getElementById('nextPage').addEventListener('click', () => {
    params.append('page', currentPage + 1);
    updateFilters();
});

function renderCharts(data) {
    // Гистограмма цен
    const priceCtx = document.getElementById('priceChart').getContext('2d');
    const prices = data.map(item => item.price);
    const priceRanges = [0, 1000, 5000, 10000, 20000, 50000];
    const counts = new Array(priceRanges.length - 1).fill(0);
    
    prices.forEach(price => {
        for (let i = 0; i < priceRanges.length - 1; i++) {
            if (price >= priceRanges[i] && price < priceRanges[i + 1]) {
                counts[i]++;
                break;
            }
        }
    });
    
    new Chart(priceCtx, {
        type: 'bar',
        data: {
            labels: priceRanges.slice(0, -1).map((_, i) => `${priceRanges[i]}-${priceRanges[i+1]}₽`),
            datasets: [{
                label: 'Количество товаров',
                data: counts,
                backgroundColor: 'rgba(54, 162, 235, 0.5)'
            }]
        }
    });
    
    // График скидка vs рейтинг
    const discountCtx = document.getElementById('discountChart').getContext('2d');
    const discounts = data.map(item => ((item.price - item.sale_price) / item.price * 100).toFixed(0));
    const ratings = data.map(item => item.rating);
    
    new Chart(discountCtx, {
        type: 'line',
        data: {
            labels: discounts,
            datasets: [{
                label: 'Рейтинг товара',
                data: ratings,
                borderColor: 'rgba(255, 99, 132, 1)',
                fill: false
            }]
        },
        options: {
            scales: {
                x: { title: { display: true, text: 'Размер скидки (%)' } },
                y: { title: { display: true, text: 'Рейтинг' } }
            }
        }
    });
}

// Инициализация при загрузке
document.addEventListener('DOMContentLoaded', loadData);