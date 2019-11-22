// main.js 
// Andrew Slavin

// called by submit button press in finalize contact
function submitContact() {
	var fname = document.getElementsByName("fname")[0].value; // first name
	var lname = document.getElementsByName("lname")[0].value; // last name
	var date = document.getElementsByName("date")[0].value; // date
	var email = document.getElementsByName("email")[0].value; // email
	var pnumber = document.getElementsByName("pnumber")[0].value; // phone number
	var address = document.getElementsByName("addr")[0].value; // address
	var em_name = document.getElementsByName("infl_name")[0].value;
	var em_num = document.getElementsByName("infl_relation")[0].value;
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
	var text = JSON.stringify({"Title": fname, "Last Name": lname, "Email": email, "Phone Number": pnumber, "Address": address, "Risk Level": rlevel, "Support Needed": sneeded, "Gang Affiliation": gaffil, "Emergency Contact Number": em_num, "Emergency Contact", em_name});

	// send request
	xhr.send(text);
}

// submit note to be stored in back end by time
function submitNote() {
	var note = document.getElementsByName("notebox")[0].value; // get note
	// send post request to server
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'http://127.0.0.1:51017/notes/', true);

	xhr.onload = function(e) {

		if (xhr.readyState != 4) { // failed
			console.error(xhr.statusText);
		}
	}
	var text = JSON.stringify({"note": note});

	// send request
	xhr.send(text);
}

// get notes from db and add them as options
function loadNotes() {
	// get existing notes
	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://127.0.0.1:51017/notes/', true);

	xhr.onload = function(e) {

		if (xhr.readyState != 4) { // failed
			console.error(xhr.statusText);
		}
		response = JSON.parse(xhr.response);
		notes = JSON.parse(response["notes"]);

		edit_dropdown = document.getElementById("note_edit");
		for (var time in notes) {
			var option = document.createElement('option');
			option.text = time + " " + notes[time].substring(0,8);
			option.value = time;
			edit_dropdown.add(option, -1);
		}
	}

	// send request
	xhr.send();

	updateNoteField();
	
}

// update note field in edit_notes.html with the selected note from the dropdown
function updateNoteField() {

	// get notes and select the one that was selected
	var xhr = new XMLHttpRequest();
	xhr.open('GET', 'http://127.0.0.1:51017/notes/', true);

	xhr.onload = function(e) {

		if (xhr.readyState != 4) { // failed
			console.error(xhr.statusText);
		}
		response = JSON.parse(xhr.response);
		notes = JSON.parse(response["notes"]);

		// get text for the note that's being editted
		var edit_dropdown = document.getElementById("note_edit")
		var selected_timestamp = edit_dropdown.options[edit_dropdown.selectedIndex].value;
		note_to_edit = notes[selected_timestamp];

		// fill in box with the note that's being editted
		document.getElementById("notebox").innerHTML=note_to_edit;
	}

	// send request
	xhr.send();
}

// update note with what's been typed in the note field
function updateNote() {

	var xhr = new XMLHttpRequest();

	xhr.open('POST', 'http://127.0.0.1:51017/update_notes/', true);

	xhr.onload = function(e) {

		if (xhr.readyState != 4) { // failed
			console.error(xhr.statusText);
		}
	}

	// get timestamp for the note that's being editted
	var edit_dropdown = document.getElementById("note_edit")
	var selected_timestamp = edit_dropdown.options[edit_dropdown.selectedIndex].value;

	// get text for the note that's being editted
	updated_text = document.getElementById("notebox").value;

	request = {'timestamp': selected_timestamp, 'updated_note': updated_text};

	console.log(request);

	// send request
	xhr.send(JSON.stringify(request));

}
