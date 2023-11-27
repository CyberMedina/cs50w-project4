// Esperar a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {


  const loaderContainer = document.getElementById('loaderContainer');
  const body = document.body;

  // Obtener el formulario y los elementos de entrada
  const form = document.querySelector(".sign-in-form");
  const emailInput = document.querySelector("#email");
  const passwordInput = form.querySelector("#password");
  const confirmPasswordInput = form.querySelector("#confirm-password");
  const signBtn = form.querySelector(".sign-btn");



  // Elementos para el correcto cambio de formulario
  const toggle_btn = document.querySelectorAll(".toggle");
  const bullets = document.querySelectorAll(".bullets span");
  const main = document.querySelector("main");
  const images = document.querySelectorAll(".image");

  // Elementos para mostrar mensajes de error
  const errorEmailTooltip = form.querySelector("#error-email-tooltip");
  const passwordErrorTooltip = form.querySelector("#password-error");
  const confirmPasswordErrorTooltip = form.querySelector("#confirm-password-error");

  // Obtener todos los campos de entrada
  const inputs = form.querySelectorAll("input[required]");


  // Función para verificar si todos los campos de entrada están llenos
  function checkAllInputsFilled() {
    const inputs = form.querySelectorAll("input[required]");
    return Array.from(inputs).every((input) => input.value.trim() !== "");
  }

  // Función para mostrar el tooltip
  function showTooltip(tooltip) {
    tooltip.style.display = "block";
  }

  // Función para ocultar el tooltip
  function hideTooltip(tooltip) {
    tooltip.style.display = "none";
  }

  // Función para verificar el formato de correo electrónico
  function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  }

  // Función para verificar la longitud de la contraseña
  function isValidPassword(password) {
    return password.length >= 8 && password.length <= 16;
  }

  // Función para manejar el evento de entrada para el correo electrónico
  emailInput.addEventListener("input", function () {
    const email = this.value.trim();
    if (email !== "" && !isValidEmail(email)) {
      showTooltip(errorEmailTooltip);
      errorEmailTooltip.textContent = "Debe proporcionar un correo electrónico válido";
    } else {
      hideTooltip(errorEmailTooltip);
    }
    enableOrDisableSubmitButton();
  });

  // Agregar un evento de entrada a cada campo de entrada
  inputs.forEach((input) => {
    input.addEventListener("input", function () {
      enableOrDisableSubmitButton();
    });
  });

  // Función para manejar el evento de entrada para la contraseña
  passwordInput.addEventListener("input", function () {
    const password = this.value.trim();
    if (password !== "" && !isValidPassword(password)) {
      showTooltip(passwordErrorTooltip);
      passwordErrorTooltip.textContent =
        "Debe introducir una contraseña con una cantidad mínima de 8 dígitos y una máxima de 16 dígitos";
      confirmPasswordInput.disabled = true;
      confirmPasswordInput.value = "";
      hideTooltip(confirmPasswordErrorTooltip);
    } else {
      hideTooltip(passwordErrorTooltip);
      confirmPasswordInput.disabled = false;
    }
    enableOrDisableSubmitButton();
  });

  // Función para manejar el evento de entrada para confirmar la contraseña
  confirmPasswordInput.addEventListener("input", function () {
    const password = passwordInput.value.trim();
    const confirmPassword = this.value.trim();
    if (confirmPassword !== password) {
      showTooltip(confirmPasswordErrorTooltip);
      confirmPasswordErrorTooltip.textContent = "Las contraseñas no coinciden";
    } else {
      hideTooltip(confirmPasswordErrorTooltip);
    }
    enableOrDisableSubmitButton();
  });

  // Función para habilitar o deshabilitar el botón de envío según los valores de entrada
  function enableOrDisableSubmitButton() {
    const isEmailValid = isValidEmail(emailInput.value.trim());
    const isPasswordValid = isValidPassword(passwordInput.value.trim());
    const isConfirmPasswordValid = confirmPasswordInput.value.trim() === passwordInput.value.trim();

    if (checkAllInputsFilled() && isEmailValid && isPasswordValid && isConfirmPasswordValid) {
      signBtn.disabled = false;
    } else {
      signBtn.disabled = true;
    }
  }





  function btncontinue() {

    loaderContainer.style.display = 'block';
    body.classList.add('dark-background');


    // Obtén el token CSRF del formulario
    let csrfToken = document.getElementById('sign-in-form').querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(csrfToken);

    let data = {
      csrfmiddlewaretoken: csrfToken,
      name: document.getElementById('name').value,
      lastname: document.getElementById('lastname').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value
    };

    fetch('/validation_register_API/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response data as needed

        loaderContainer.style.display = 'none';
        // Handle the response data as needed
        console.log(data);

        if (data.status === 'success') {
          main.classList.toggle("sign-up-mode");


          // Al hacer clic al botón de siguiente este hace la función de moveslider y simula que ha sido tocado un bullet
          moveSlider.call(bullets[1]);

          loaderContainer.style.display = 'none';
          body.classList.remove('dark-background');



        } else {

          var toast = new bootstrap.Toast(document.getElementById('toastStatus'))
          // Selecciono el id de los componentes de mi toastStatus

          titleToast.innerText = data.message



          loaderContainer.style.display = 'none';
          body.classList.remove('dark-background');
          $('.toast').toast({ delay: 5000 }); // El toast se mostrará durante 5 segundos
          $('.toast').toast('show');


        }
      })
      .catch(error => {
        console.error('Error:', error);

        loaderContainer.style.display = 'none';
        body.classList.remove('dark-background');
      });

  };

  toggle_btn.forEach((btn) => {

    btn.addEventListener("click", () => {
      btncontinue();
    });


  });


  document.getElementById("sign-in-form").addEventListener("keyup", function (event) {
    // Número 13 es la tecla "Enter"
    if (event.keyCode === 13) {
      event.preventDefault();
      // Verifica si el botón está habilitado
      if (!document.getElementById("sign-btn").disabled) {
        // Llama a la función btncontinue
        btncontinue();
      }
    }
  });

  function SendWithEnter(event) {
    if (event.key === 'Enter') {
      btncontinue();
    }
  }

  function moveSlider() {
    let register_user = this.dataset.value;

    let currentImage = document.querySelector(`.img-${register_user}`);
    images.forEach((img) => img.classList.remove("show"));
    currentImage.classList.add("show");

    const textSlider = document.querySelector(".text-group");
    textSlider.style.transform = `translateY(${-(register_user - 1) * 2.2}rem)`;

    bullets.forEach((bull) => bull.classList.remove("active"));
    this.classList.add("active");
  }

  // Al hacer clic al botón de siguiente este hace la función de moveslider y simula que ha sido tocado un bullet
  signBtn.addEventListener("click", () => {

  });

  // Estado inicial del formulario
  confirmPasswordInput.disabled = true;
  signBtn.disabled = true;

  // Función para hacer que el textarea se autocreciente
  function autoGrowTextArea(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;

    // Actualizar el label con la cantidad de caracteres escritos y el límite (100)
    const charCountLabel = document.getElementById("char-count-indicaciones");
    const currentCount = textarea.value.length;
    charCountLabel.textContent = `${currentCount}/100`;

    // Limitar la escritura cuando se alcanzan los 100 caracteres
    if (currentCount >= 100) {
      textarea.value = textarea.value.slice(0, 100);
      charCountLabel.style.color = "red"; // Cambiar el color del label si se alcanza el límite
    } else {
      charCountLabel.style.color = "#bbb"; // Restaurar el color del label si no se alcanza el límite
    }
  }

  // Función para limitar el número de dígitos en el campo de teléfono a 8
  function limitInputToEightDigits(event) {
    const input = event.target;
    const inputValue = input.value.replace(/\D/g, ''); // Elimina todos los caracteres no numéricos
    const maxLength = 8;

    if (inputValue.length > maxLength) {
      // Trunca el valor a 8 dígitos si es más largo
      input.value = inputValue.slice(0, maxLength);
    } else {
      input.value = inputValue; // Si tiene menos de 8 dígitos, simplemente asigna el valor sin cambios
    }
  }

  // Evento de entrada para el textarea para ajustar su tamaño automáticamente
  const textArea = document.getElementById("text");
  if (textArea) {
    textArea.addEventListener("input", function () {
      autoGrowTextArea(this);
    });
  }

  // Evento de entrada para el campo de teléfono para limitar a 8 dígitos
  const phoneInput = document.querySelector("input[type='tel']");
  if (phoneInput) {
    phoneInput.addEventListener("input", function (event) {
      limitInputToEightDigits(event);
    });
  }

  // Botón "Continuar"
  // Al tocar el botón 
  document.getElementById('saveButton').addEventListener("click", function (e) {

    const loaderContainer = document.getElementById('loaderContainer'); // Obtiene la animacion del loader
    const body = document.body; // Obtiene todo el body del DOM

    loaderContainer.style.display = 'block'; // Muestra la animación del loader
    body.classList.add('dark-background'); // Pone oscuro el body con el css dark-background

    document.getElementById('saveButton').classList.add('disabled-button'); // Pone el botón desactivado
    e.preventDefault();

    // Obtén el token CSRF del formulario
    let csrfToken = document.getElementById('sign-in-form').querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(csrfToken);

    let data = {
      csrfmiddlewaretoken: csrfToken,
      name: document.getElementById('name').value,
      lastname: document.getElementById('lastname').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      addressInput: document.getElementById('addressInput').value,
      latitude: document.getElementById('latitude').value,
      longitude: document.getElementById('longitude').value,
      houseNumber: document.getElementById('houseNumber').value,
      text: document.getElementById('text').value,
      telephoneNumber: document.getElementById('telephoneNumber').value,
      radio2: document.getElementById('radio2').value
    };

    fetch('/register_user_API/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response data as needed
        console.log(data);

        if (data.status === 'success') {

          loaderContainer.style.display = 'none'; // Elimina la animación del loader
          body.classList.remove('dark-background'); // Elimina lo oscuro del body

          window.location.href = "/"; // Redirige a la página principal



        } else {
          loaderContainer.style.display = 'none'; // Quitar la animación del loader
          body.classList.remove('dark-background');// Quitar lo oscuro del body

          var toast = new bootstrap.Toast(document.getElementById('toastStatus'))
          // Selecciono el id de los componentes de mi toastStatus
          var titleToast = document.getElementById('titleToast');

          titleToast.innerText = data.message

          toast.show();

          document.getElementById('saveButton').classList.remove('disabled-button');// Quita el botón deshabilitado

        }
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('saveButton').classList.remove('disabled-button');// Quita el botón deshabilitado
        loaderContainer.style.display = 'none'; // Quitar la animación del loader
        body.classList.remove('dark-background');// Quitar lo oscuro del body
      });
  });

  // Fin botón de "Continuar"
});

// Inicio mapa

var map;
var marker;
var searchBox;

function initMap() {
  var location = new google.maps.LatLng(12.11501075424433, -86.2360456940407);
  var mapOptions = {
    center: location,
    zoom: 15,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    disableDefaultUI: true, // Desactiva la interfaz predeterminada del mapa
    mapTypeControl: false, // Desactiva el control de tipos de mapa (Satélite, Mapa)
  };
  map = new google.maps.Map(document.getElementById("map"), mapOptions);
  marker = new google.maps.Marker({
    position: location,
    map: map,
    draggable: true
  });

  google.maps.event.addListener(marker, "dragend", function () {
    updateAddressFromMarker();
  });

  // Crea la caja de búsqueda con restricciones de país
  var input = document.getElementById("searchInput");
  var options = {
    componentRestrictions: { country: "ni" }
  };
  var autocomplete = new google.maps.places.Autocomplete(input, options);

  autocomplete.addListener("place_changed", function () {
    var place = autocomplete.getPlace();
    if (!place.geometry) return;

    // Establecer la ubicación del marcador en la ubicación seleccionada del cuadro de búsqueda
    marker.setPosition(place.geometry.location);
    map.fitBounds(place.geometry.viewport || place.geometry.location);
    updateAddressFromMarker();
  });

  $("#getLocationButton").click(function () {
    getCurrentLocation();
  });

  $("#saveLocation").click(function () {
    var address = $("#addressInput").val();
    var latitude = marker.getPosition().lat();
    var longitude = marker.getPosition().lng();

    // Set the values of hidden inputs
    $("#latitude").val(latitude);
    $("#longitude").val(longitude);

    alert("Address saved: " + address);
    $("#myModal").modal("hide");
  });
}

function updateAddressFromMarker() {
  var latLng = marker.getPosition();
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({ location: latLng }, function (results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      if (results[0]) {
        $("#addressInput").val(results[0].formatted_address);
        $("#selectedLocationLabel").text(results[0].formatted_address);
      }
    }
  });
}



function getCurrentLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        var latLng = new google.maps.LatLng(
          position.coords.latitude,
          position.coords.longitude
        );
        map.setCenter(latLng);
        map.setZoom(15);
        marker.setPosition(latLng);
        updateAddressFromMarker();
      },
      function (error) {
        alert("Error obteniendo la dirección: " + error.message);
      }
    );
  } else {
    alert("La geolocalización no es soportada en este navegador.");
  }







  document.addEventListener("DOMContentLoaded", function () {
    const radio3 = document.getElementById("radio3");
    const otrosModal = new bootstrap.Modal(document.getElementById("otrosModal"));
    const guardarBtn = document.getElementById("guardarBtn");
    const otrosInputLabel = document.querySelector(".radio-button__label[for='radio3']");

    radio3.addEventListener("click", function () {
      $("#otrosModal").modal("show");
    });


    guardarBtn.addEventListener("click", function () {
      const otrosInput = document.getElementById("otros-input").value;
      otrosInputLabel.textContent = otrosInput;
      otrosModal.hide();
    });
  });



  // Fin de mapa

}

// Abrir modal para poder visualizar el mapa en el registro
function openModal() {
  $("#myModal").modal("show");
}


document.addEventListener("DOMContentLoaded", function () {
  const radio3 = document.getElementById("radio3");
  const otrosModal = new bootstrap.Modal(document.getElementById("otrosModal"));
  const guardarBtn = document.getElementById("guardarBtn");
  const otrosInputLabel = document.querySelector(".radio-button__label[for='radio3']");

  radio3.addEventListener("click", function () {
    $("#otrosModal").modal("show");
  });


  guardarBtn.addEventListener("click", function () {
    const otrosInput = document.getElementById("otros-input").value;
    otrosInputLabel.textContent = otrosInput;
    otrosModal.hide();
  });
});



