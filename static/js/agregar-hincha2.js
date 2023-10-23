let err_msgs = {
    "nombre": "El nombre debe tener entre 3 y 80 caracteres",
    "mail": "El mail debe ser válido",
    "transporte": "Debe seleccionar al menos un medio de transporte",
    "comuna" : "Debe seleccionar una comuna",
    "region" : "Debe seleccionar una region",
    "deportes": "Debe de escoger entre 1 y 3 deportes",
    "telefono": "El telefono debe ser valido"
}

let RegionesYcomunas = {

	"regiones": [{
			"NombreRegion": "Arica y Parinacota",
			"comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
	},
		{
			"NombreRegion": "Tarapacá",
			"comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
	},
		{
			"NombreRegion": "Antofagasta",
			"comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
	},
		{
			"NombreRegion": "Atacama",
			"comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
	},
		{
			"NombreRegion": "Coquimbo",
			"comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
	},
		{
			"NombreRegion": "Valparaíso",
			"comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
	},
		{
			"NombreRegion": "Región del Libertador Gral. Bernardo O’Higgins",
			"comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
	},
		{
			"NombreRegion": "Región del Maule",
			"comunas": ["Talca", "ConsVtución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "ReVro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
	},
		{
			"NombreRegion": "Región del Biobío",
			"comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío", "Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]
	},
		{
			"NombreRegion": "Región de la Araucanía",
			"comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria", ]
	},
		{
			"NombreRegion": "Región de Los Ríos",
			"comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
	},
		{
			"NombreRegion": "Región de Los Lagos",
			"comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "FruVllar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
	},
		{
			"NombreRegion": "Región Aisén del Gral. Carlos Ibáñez del Campo",
			"comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
	},
		{
			"NombreRegion": "Región de Magallanes y de la AntárVca Chilena",
			"comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "AntárVca", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
	},
		{
			"NombreRegion": "Región Metropolitana de Santiago",
			"comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "TilVl", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
	}]
}

var expanded = false;

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}

const change_comunas = () => {
    let region_name= document.getElementById("region").value
    if (!region_name) {
        document.getElementById("comuna").innerHTML = "";
        return;
    }
    document.getElementById("comuna").innerHTML = "";
    let comunas = RegionesYcomunas["regiones"].find(region => region.NombreRegion == region_name).comunas;
    comunas.forEach(element => {
        document.getElementById("comuna").innerHTML += `<option value="${element}">${element}</option>`;
    });
}

let region_select = document.getElementById("region")
region_select.addEventListener("change", change_comunas)

const validate_deportes = (deportes) => {
    return deportes.length >= 1&& deportes.length <=3
}

const validate_name = (name) => {
    if(!name) return false;
    return name.length >= 3 && name.length <= 80;
}

const validate_region = (region) => {
    if(!region) return false;
    return true;
}

const validate_comuna = (comuna) => {
    if(!comuna) return false;
    return true;
}
const validate_phone = (phone) => {
    let re = /^[0-9]+$/;
    let largo_valido = phone.length >= 9;
    return re.test(phone) && largo_valido;
}

const validate_mail = (mail) => {
    if(!mail) return false;
    let re = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g;
    return re.test(mail);
}

const validate_transport = (list_transport) => {
    if(!list_transport) return false;
    return list_transport.length > 0;
}


let validate_form = () => {
    let name = document.getElementById("nombre").value;
    let mail = document.getElementById("myemail").value;
    let comuna = document.getElementById("region").value
    let region = document.getElementById("comuna").value
    //lista de transportes
    let temp_list_transport = document.getElementsByName("transporte[]");
    let list_transport = [];
    for(transporte of temp_list_transport) {
        if(transporte.checked) {
            list_transport.push(transporte.value);
        }
    }
    // lista de deportes
    let temp_list_deportes = document.getElementsByName("deportes[]");
    let list_deportes = [];
    for (deporte of temp_list_deportes) {
        if (deporte.checked) {
            list_deportes.push(deporte.value);
        }
    }


    let invalidsInputs = [];
    let isValid = true;
    //Validacion handler
    const setInvalidInput = (input) => {
        invalidsInputs.push(input);
        isValid = isValid && false;
    }

    //validanding
    if(!validate_name(name)){
        setInvalidInput("nombre");
    }
    if(!validate_mail(mail)){
        setInvalidInput("mail");
    }
    if(!validate_transport(list_transport)){
        setInvalidInput("transporte");
    }
    if(!validate_region(region)){
        setInvalidInput("region");
    }
    if(!validate_comuna(comuna)){
        setInvalidInput("comuna");
    }
    if(!validate_deportes(list_deportes)){
        setInvalidInput("deportes");
    }

    //optionals
    let telefono = document.getElementById("mynumber").value;
    if (telefono!=""){
        if(!validate_phone(telefono)) {
            setInvalidInput("telefono");
        }
    }

    let validation_box= document.getElementById("val-box");
    let validation_message_elem = document.getElementById("val-msg");
    let validation_list_elem = document.getElementById("val-list");

    if(!isValid) {
        validation_list_elem.textContent=""
        for (input of invalidsInputs) {
            let list_element = document.createElement("li");
            list_element.innerText = input + ": " + err_msgs[input];
            validation_list_elem.append(list_element)
        }
        validation_message_elem.innerText = "Los siguientes campos son invalidos:"
        validation_box.hidden = false;
    } else {
        if (confirm("¿Confirma el registro de este hincha?")){
            //aqui usaria un myform.submit pero como es estatico solo redirecionare al index
            let msg = document.getElementById("msg-ready")
            msg.hidden = false;
            let msg_text = document.createElement("h2")
            msg_text.innerText = "Hemos recibido el registro del hincha. Muchas gracias. Espere un momento para ir al menu."
            msg.append(msg_text)
            scrollBy(0,200)
            setTimeout(() => {
                window.location.href = "index.html"
            }, 3500);

        }else{
            return;
        }

    }
}

let btn_submit = document.getElementById("enviar")
btn_submit.addEventListener("click", validate_form)
