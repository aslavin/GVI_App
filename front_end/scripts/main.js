// main.js 
// Andrew Slavin

// called by submit button press in finalize contact
function submitContact() {
	console.log("here");
	var fname = document.getElementsByName("fname")[0].value; // first name
	var lname = document.getElementsByName("lname")[0].value; // last name
	var date = document.getElementsByName("date")[0].value; // date
	var email = document.getElementsByName("email")[0].value; // email
	var pnumber = document.getElementsByName("pnumber")[0].value; // phone number
	var address = document.getElementsByName("addr")[0].value; // address
	var rlevel = document.getElementById("rlevel"); // risk level
	rlevel = rlevel.options[rlevel.selectedIndex].text;
	var sneeded = document.getElementById("sneeded"); // support needed
	sneeded = sneeded.options[sneeded.selectedIndex].text;
	var gaffil = document.getElementById("gaffil"); // gang affiliation
	gaffil = gaffil.options[gaffil.selectedIndex].text;

	// send post request to server
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://127.0.0.1:51017/contacts/', true);

	xhr.onload = function(e) {

		if (xhr.readyState != 4) { // failed
			console.error(xhr.statusText);
		}
	}
	var text = JSON.stringify({"First Name": fname, "Last Name": lname, "Email": email, "Phone Number": pnumber, "Address": address, "Risk Level": rlevel, "Support Needed": sneeded, "Gang Affiliation": gaffil});

	// send request
	xhr.send(text);
}

