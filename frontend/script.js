fetch('food dataset.json')
  .then(response => response.json())
  .then(data => {
    const menuDiv = document.getElementById('menu');
    data.forEach(item => {
      const div = document.createElement('div');
      div.className = 'menu-item';
      div.innerHTML = `
        <h3>${item['Food Item']}</h3>
        <p>Category: ${item['Category']}</p>
        <p>Price: ₹${item['Price']}</p>
      `;
      menuDiv.appendChild(div);
    });
  });
