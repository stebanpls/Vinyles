/********************************************
 * FORMATEAR PRECIOS A MONEDA COLOMBIANA (COP)
 ********************************************/
function formatCOP(value) {
  // Usa Intl.NumberFormat para formatear en pesos colombianos
  return new Intl.NumberFormat('es-CO', {
  style: 'currency',
  currency: 'COP',
  minimumFractionDigits: 0
  }).format(value);
}

/********************************************
 * LÓGICA DEL CARRITO
 ********************************************/
document.addEventListener("DOMContentLoaded", function () {
  const cartItemsContainer = document.getElementById("cart-items");
  const cartTotalContainer = document.querySelector(".cart-total");
  const cartTotalAmount = document.getElementById("cart-total-amount");
  const checkoutButton = document.getElementById("checkout-button");
  
  // Recuperamos el carrito del localStorage (si existe), en formato JSON
  let cartProducts = [];
  const storedCart = localStorage.getItem("cartProducts");
  if (storedCart) {
      try {
          cartProducts = JSON.parse(storedCart);
      } catch(e) {
          console.error("Error al parsear el carrito:", e);
          cartProducts = [];
      }
  }

  // Función que actualiza el localStorage
  function updateLocalStorage() {
      localStorage.setItem("cartProducts", JSON.stringify(cartProducts));
  }

  // Función para renderizar los productos en el carrito
  function renderCart() {
    // Limpiamos el contenedor
  cartItemsContainer.innerHTML = "";

  if (cartProducts.length === 0) {
      // Si no hay productos, mostramos mensaje
      cartItemsContainer.innerHTML = "<p>Tu carrito está vacío.</p>";
      cartTotalContainer.style.display = "none";
      checkoutButton.style.display = "none";
      return;
  }

    // Si hay productos, recorremos y pintamos
  cartProducts.forEach((product, index) => {
      const { albumName, artistName, price, imageURL } = product;

      // Creamos el contenedor del ítem
      const itemDiv = document.createElement("div");
      itemDiv.classList.add("cart-item");

      // Estructura del ítem con imagen, texto y botón de eliminar
      itemDiv.innerHTML = `
      <img src="${imageURL}" alt="${albumName}" class="cart-item-image" />
      <div class="cart-item-details">
          <p class="cart-item-title">${albumName}</p>
          <p class="cart-item-artist">${artistName}</p>
          <p class="cart-item-price">${formatCOP(price)}</p>
      </div>
      <button class="cart-item-remove" data-index="${index}">🗑</button>
      `;

      // Agregamos el ítem al contenedor principal
      cartItemsContainer.appendChild(itemDiv);
  });

    // Mostramos total y botón de comprar
  cartTotalContainer.style.display = "block";
  checkoutButton.style.display = "block";

    // Actualizamos el total
  updateCartTotal();
  }

  // Función para actualizar el total
  function updateCartTotal() {
  let total = 0;
  cartProducts.forEach(product => {
      total += product.price;
  });
  cartTotalAmount.textContent = formatCOP(total);
  }

    // Función para agregar productos al carrito
    function addToCart(albumName, artistName, price, imageURL) {
      // Agrega el producto al array
      cartProducts.push({ albumName, artistName, price, imageURL });
      updateLocalStorage();
      renderCart();
    }

  // Evento para eliminar un ítem del carrito
  cartItemsContainer.addEventListener("click", function (e) {
  if (e.target.classList.contains("cart-item-remove")) {
      const index = e.target.dataset.index;
      // Eliminamos el producto del array
      cartProducts.splice(index, 1);
      updateLocalStorage();
      // Renderizamos de nuevo
      renderCart();
  }
  });

    // Extraer parámetros de la URL (si existen) y agregar el producto
    const params = new URLSearchParams(window.location.search);
    if (params.has('album_name')) {
      const albumName = params.get('album_name');
      const artistName = params.get('artist');
      const price = parseInt(params.get('price'), 10);
      const imageURL = params.get('image');
  
      addToCart(albumName, artistName, price, imageURL);
    }
  renderCart();


  // Botón de comprar
  checkoutButton.addEventListener("click", function () {
      window.location.href = "/checkout/";
  });
  
});