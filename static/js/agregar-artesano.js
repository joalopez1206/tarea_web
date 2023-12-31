let err_msgs = {
    "nombre": "El nombre debe tener entre 3 y 80 caracteres",
    "mail": "El mail debe ser válido",
    "comuna" : "Debe seleccionar una comuna",
    "region" : "Debe seleccionar una region",
    "archivos" : "Debe seleccionar entre 1 y 3 fotos de formato jpg, png o gif",
    "artesanias" : "Debe seleccionar entre 1 y 3 artesanias",
    "telefono": "El telefono debe ser valido"
}

let RegionesYcomunas = {
    "regiones": [
        {
            "NombreRegion": "Región de Tarapacá",
            "comunas": [
                "Camiña",
                "Huara",
                "Pozo Almonte",
                "Iquique",
                "Pica",
                "Colchane",
                "Alto Hospicio"
            ]
        },
        {
            "NombreRegion": "Región de Antofagasta",
            "comunas": [
                "Tocopilla",
                "Maria Elena",
                "Ollague",
                "Calama",
                "San Pedro Atacama",
                "Sierra Gorda",
                "Mejillones",
                "Antofagasta",
                "Taltal"
            ]
        },
        {
            "NombreRegion": "Región de Atacama",
            "comunas": [
                "Diego de Almagro",
                "Chañaral",
                "Caldera",
                "Copiapo",
                "Tierra Amarilla",
                "Huasco",
                "Freirina",
                "Vallenar",
                "Alto del Carmen"
            ]
        },
        {
            "NombreRegion": "Región de Coquimbo",
            "comunas": [
                "La Higuera",
                "La Serena",
                "Vicuña",
                "Paihuano",
                "Coquimbo",
                "Andacollo",
                "Rio Hurtado",
                "Ovalle",
                "Monte Patria",
                "Punitaqui",
                "Combarbala",
                "Mincha",
                "Illapel",
                "Salamanca",
                "Los Vilos"
            ]
        },
        {
            "NombreRegion": "Región de Valparaíso",
            "comunas": [
                "Petorca",
                "Cabildo",
                "Papudo",
                "La Ligua",
                "Zapallar",
                "Putaendo",
                "Santa Maria",
                "San Felipe",
                "Pencahue",
                "Catemu",
                "Llay Llay",
                "Nogales",
                "La Calera",
                "Hijuelas",
                "La Cruz",
                "Quillota",
                "Olmue",
                "Limache",
                "Los Andes",
                "Rinconada",
                "Calle Larga",
                "San Esteban",
                "Puchuncavi",
                "Quintero",
                "Viña del Mar",
                "Villa Alemana",
                "Quilpue",
                "Valparaiso",
                "Juan Fernandez",
                "Casablanca",
                "Concon",
                "Isla de Pascua",
                "Algarrobo",
                "El Quisco",
                "El Tabo",
                "Cartagena",
                "San Antonio",
                "Santo Domingo"
            ]
        },
        {
            "NombreRegion": "Región del Libertador Bernardo Ohiggins",
            "comunas": [
                "Mostazal",
                "Codegua",
                "Graneros",
                "Machali",
                "Rancagua",
                "Olivar",
                "Doñihue",
                "Requinoa",
                "Coinco",
                "Coltauco",
                "Quinta Tilcoco",
                "Las Cabras",
                "Rengo",
                "Peumo",
                "Pichidegua",
                "Malloa",
                "San Vicente",
                "Navidad",
                "La Estrella",
                "Marchigue",
                "Pichilemu",
                "Litueche",
                "Paredones",
                "San Fernando",
                "Peralillo",
                "Placilla",
                "Chimbarongo",
                "Palmilla",
                "Nancagua",
                "Santa Cruz",
                "Pumanque",
                "Chepica",
                "Lolol"
            ]
        },
        {
            "NombreRegion": "Región del Maule",
            "comunas": [
                "Teno",
                "Romeral",
                "Rauco",
                "Curico",
                "Sagrada Familia",
                "Hualañe",
                "Vichuquen",
                "Molina",
                "Licanten",
                "Rio Claro",
                "Curepto",
                "Pelarco",
                "Talca",
                "Pencahue",
                "San Clemente",
                "Constitucion",
                "Maule",
                "Empedrado",
                "San Rafael",
                "San Javier",
                "Colbun",
                "Villa Alegre",
                "Yerbas Buenas",
                "Linares",
                "Longavi",
                "Retiro",
                "Parral",
                "Chanco",
                "Pelluhue",
                "Cauquenes"
            ]
        },
        {
            "NombreRegion": "Región del Biobío",
            "comunas": [
                "Tome",
                "Florida",
                "Penco",
                "Talcahuano",
                "Concepcion",
                "Hualqui",
                "Coronel",
                "Lota",
                "Santa Juana",
                "Chiguayante",
                "San Pedro de la Paz",
                "Hualpen",
                "Cabrero",
                "Yumbel",
                "Tucapel",
                "Antuco",
                "San Rosendo",
                "Laja",
                "Quilleco",
                "Los Angeles",
                "Nacimiento",
                "Negrete",
                "Santa Barbara",
                "Quilaco",
                "Mulchen",
                "Alto Bio Bio",
                "Arauco",
                "Curanilahue",
                "Los Alamos",
                "Lebu",
                "Cañete",
                "Contulmo",
                "Tirua"
            ]
        },
        {
            "NombreRegion": "Región de La Araucanía",
            "comunas": [
                "Renaico",
                "Angol",
                "Collipulli",
                "Los Sauces",
                "Puren",
                "Ercilla",
                "Lumaco",
                "Victoria",
                "Traiguen",
                "Curacautin",
                "Lonquimay",
                "Perquenco",
                "Galvarino",
                "Lautaro",
                "Vilcun",
                "Temuco",
                "Carahue",
                "Melipeuco",
                "Nueva Imperial",
                "Puerto Saavedra",
                "Cunco",
                "Freire",
                "Pitrufquen",
                "Teodoro Schmidt",
                "Gorbea",
                "Pucon",
                "Villarrica",
                "Tolten",
                "Curarrehue",
                "Loncoche",
                "Padre Las Casas",
                "Cholchol"
            ]
        },
        {
            "NombreRegion": "Región de Los Lagos",
            "comunas": [
                "San Pablo",
                "San Juan",
                "Osorno",
                "Puyehue",
                "Rio Negro",
                "Purranque",
                "Puerto Octay",
                "Frutillar",
                "Fresia",
                "Llanquihue",
                "Puerto Varas",
                "Los Muermos",
                "Puerto Montt",
                "Maullin",
                "Calbuco",
                "Cochamo",
                "Ancud",
                "Quemchi",
                "Dalcahue",
                "Curaco de Velez",
                "Castro",
                "Chonchi",
                "Queilen",
                "Quellon",
                "Quinchao",
                "Puqueldon",
                "Chaiten",
                "Futaleufu",
                "Palena",
                "Hualaihue"
            ]
        },
        {
            "NombreRegion": "Región Aisén del General Carlos Ibáñez del Campo",
            "comunas": [
                "Guaitecas",
                "Cisnes",
                "Aysen",
                "Coyhaique",
                "Lago Verde",
                "Rio Iba?ez",
                "Chile Chico",
                "Cochrane",
                "Tortel",
                "O'Higins"
            ]
        },
        {
            "NombreRegion": "Región de Magallanes y la Antártica Chilena",
            "comunas": [
                "Torres del Paine",
                "Puerto Natales",
                "Laguna Blanca",
                "San Gregorio",
                "Rio Verde",
                "Punta Arenas",
                "Porvenir",
                "Primavera",
                "Timaukel",
                "Antartica"
            ]
        },
        {
            "NombreRegion": "Región Metropolitana de Santiago",
            "comunas": [
                "Tiltil",
                "Colina",
                "Lampa",
                "Conchali",
                "Quilicura",
                "Renca",
                "Las Condes",
                "Pudahuel",
                "Quinta Normal",
                "Providencia",
                "Santiago",
                "La Reina",
                "Ñuñoa",
                "San Miguel",
                "Maipú",
                "La Cisterna",
                "La Florida",
                "La Granja",
                "Independencia",
                "Huechuraba",
                "Recoleta",
                "Vitacura",
                "Lo Barrenechea",
                "Macul",
                "Peñalolén",
                "San Joaquín",
                "La Pintana",
                "San Ramon",
                "El Bosque",
                "Pedro Aguirre Cerda",
                "Lo Espejo",
                "Estacion Central",
                "Cerrillos",
                "Lo Prado",
                "Cerro Navia",
                "San José de Maipo",
                "Puente Alto",
                "Pirque",
                "San Bernardo",
                "Calera de Tango",
                "Buin",
                "Paine",
                "Peñaflor",
                "Talagante",
                "El Monte",
                "Isla de Maipo",
                "Curacavi",
                "María Pinto",
                "Melipilla",
                "San Pedro",
                "Alhué",
                "Padre Hurtado"
            ]
        },
        {
            "NombreRegion": "Región de Los Ríos",
            "comunas": [
                "Lanco",
                "Mariquina",
                "Panguipulli",
                "Mafil",
                "Valdivia",
                "Los Lagos",
                "Corral",
                "Paillaco",
                "Futrono",
                "Lago Ranco",
                "La Union",
                "Rio Bueno"
            ]
        },
        {
            "NombreRegion": "Región Arica y Parinacota",
            "comunas": [
                "Gral. Lagos",
                "Putre",
                "Arica",
                "Camarones"
            ]
        },
        {
            "NombreRegion": "Región del Ñuble",
            "comunas": [
                "Cobquecura",
                "Ñiquen",
                "San Fabian",
                "San Carlos",
                "Quirihue",
                "Ninhue",
                "Trehuaco",
                "San Nicolas",
                "Coihueco",
                "Chillan",
                "Portezuelo",
                "Pinto",
                "Coelemu",
                "Bulnes",
                "San Ignacio",
                "Ranquil",
                "Quillon",
                "El Carmen",
                "Pemuco",
                "Yungay",
                "Chillan Viejo"
            ]
        }
    ]
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

const validate_files = (files) => {
    if (files.length == 0) return false;

    let is_valid_len = (1<= files.length) && (files.length <= 3);

    let typeValid = true;

    for (const file of files) {
        let fileFamily = file.type.split("/")[0];
        typeValid &&= (fileFamily == "image");
    }
    return is_valid_len && typeValid;
}

const validate_artesanias = (artesanias) => {
    if(artesanias.length == 0) return false;
    return artesanias.length >= 1 && artesanias.length <= 3;
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

const validate_mail = (mail) => {
    if(!mail) return false;
    let re = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g;
    return re.test(mail);
}

const validate_phone = (phone) => {
    let re = /^[0-9]+$/;
    let largo_valido = phone.length >= 9;
    return re.test(phone) && largo_valido;
}

const validate_form = () => {
    let myform = document.forms["reg-artesano"];
    let name = document.getElementById("nombre").value;
    let mail = document.getElementById("myemail").value;
    let region = document.getElementById("region").value;
    let comuna = document.getElementById("comuna").value;
    let files = document.forms["reg-artesano"].files.files;
    let temp_artesanias = document.getElementsByName("artesania[]");
    let artesanias = [];
    for (const arte of temp_artesanias){
        if(arte.checked) {
            artesanias.push(arte.value);
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
    if(!validate_region(region)){
        setInvalidInput("region");
    }
    if(!validate_comuna(comuna)){
        setInvalidInput("comuna");
    }
    if(!validate_files(files)){
        setInvalidInput("archivos");
    }
    if (!validate_artesanias(artesanias)){
        setInvalidInput("artesanias");
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
        validation_box.hidden = true;
        if (confirm("¿Confirma el registro de este artesano?")){
            //aqui usaria un myform.submit pero como es estatico solo redirecionare al index
            myform.submit();
        }else{
            return;
        }
    }
}

let btn_submit = document.getElementById("enviar")
btn_submit.addEventListener("click", validate_form)