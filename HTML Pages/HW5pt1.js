<!--script.js-->

var i = 0;

function createTable() {

    var ingredient = [

        "One pakcage of Masien Bodega Corn Tortillas",

        "One gallon of canola oil (dependent on serving size)",

        "Kosher salt and black pepper",

        "3 small ripe avacados",

        "1 clove of garlic",

        "A small red onion",

        "Equivalent of 1 juiced lime",

        "Ground Cumin",
		
		"2 tablespoons of cilantro",
		
		"1 jalepeno",

    ];

    if (i == 7) {

        alert("Additional ingredients are optional");

        return false

    }

    var table = document.getElementById("myTable");

    var row = table.insertRow(0);

    var cell1 = row.insertCell(0);

    cell1.innerHTML = ingredient[i];

    i++;

}