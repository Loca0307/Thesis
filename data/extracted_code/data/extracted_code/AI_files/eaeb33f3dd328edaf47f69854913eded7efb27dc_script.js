
// Funktion zum Anzeigen des Login-Formulars
function showLoginForm() {
    document.getElementById('loginForm').classList.remove('hidden');  // Zeige das Login-Formular
}

// Funktion zum Überprüfen des Tokens beim Laden der Seite
window.onload = function() {
    if (token) {
        // Versuche, die Ligen mit dem gespeicherten Token abzurufen
        fetchLeagues();
    } else {
        // Zeige das Login-Formular, falls kein Token vorhanden ist
        showLoginForm();
    }
};