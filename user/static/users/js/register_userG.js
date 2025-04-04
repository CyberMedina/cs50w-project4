const main = document.querySelector("main");

const bullets = document.querySelectorAll(".bullets span");

const images = document.querySelectorAll(".image");

document.addEventListener("DOMContentLoaded", function () {

  main.classList.toggle("sign-up-mode");

  // Al hacer clic al botón de siguiente este hace la función de moveslider y simula que ha sido tocado un bullet
  moveSlider.call(bullets[1]);

});

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

// Botón "Continuar"
// Al tocar el botón 
document.getElementById('saveButton').addEventListener("click", function (e) {

  const loaderContainer = document.getElementById('loaderContainer'); // Obtiene la animacion del loader
  const body = document.body; // Obtiene todo el body del DOM

  loaderContainer.style.display = 'block'; // Muestra la animación del loader
  body.classList.add('dark-background'); // Pone oscuro el body con el css dark-background


  // Obtiene el valor del radio button seleccionado
  let selectedOption = document.querySelector('input[name="radio-group"]:checked');
  let selectedText = selectedOption ? document.querySelector(`label[for="${selectedOption.id}"]`).textContent.trim() : null;

  document.getElementById('saveButton').classList.add('disabled-button'); // Pone el botón desactivado
  e.preventDefault();

  // Obtén el token CSRF del formulario
  let csrfToken = document.getElementById('sign-up-form').querySelectorAll('[name=csrfmiddlewaretoken]').value;
  console.log(csrfToken);

  let data = {
    csrfmiddlewaretoken: csrfToken,
    addressInput: document.getElementById('addressInput').value,
    latitude: document.getElementById('latitude').value,
    longitude: document.getElementById('longitude').value,
    houseNumber: document.getElementById('houseNumber').value,
    text: document.getElementById('text').value,
    telephoneNumber: document.getElementById('telephoneNumber').value,
    selectedRadioButton: selectedText,
  };

  fetch('/register_location_API/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
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

        titleToast.innerText = data.message



        loaderContainer.style.display = 'none';
        body.classList.remove('dark-background');
        $('.toast').toast({ delay: 5000 }); // El toast se mostrará durante 5 segundos
        $('.toast').toast('show');



        document.getElementById('saveButton').classList.remove('disabled-button');// Quita el botón deshabilitado

      }
    })
    .catch(error => {
      var toast = new bootstrap.Toast(document.getElementById('toastStatus'))
      // Selecciono el id de los componentes de mi toastStatus

      titleToast.innerText = data.message



      loaderContainer.style.display = 'none';
      body.classList.remove('dark-background');
      $('.toast').toast({ delay: 5000 }); // El toast se mostrará durante 5 segundos
      $('.toast').toast('show');


      document.getElementById('saveButton').classList.remove('disabled-button');// Quita el botón deshabilitado
      loaderContainer.style.display = 'none'; // Quitar la animación del loader
      body.classList.remove('dark-background');// Quitar lo oscuro del body
    });
});

// Fin botón de "Continuar"




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

document.getElementById('dismiss-btn').addEventListener("click", function (e){

  e.preventDefault();

  window.location.href="/";
});



