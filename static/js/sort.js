/*
Course: CST205-01_FA23: Multimedia Design & Progmng
Title: Currency Exchanage Project
Abstract: These client-side JavaScript functions are used in the rates.html to sort the exchange rates.
Authors: Delight Lee
Date: 12/11/23
*/

/*
The sortCurrency function sort a table of currency exchange rates 
according to different criteria selected by the user through a dropdown menu.
*/
function sortCurrency() {
    // Get the dropdown element
    let selectBox = document.getElementById("sortSelect");
    let selectedOption = selectBox.options[selectBox.selectedIndex].value;
    
    // Get the table
    let table = document.getElementById("ratesTable");
    let rows, i, shouldSwitch; // Table element's rows, loop counter, swtich flag
    let switching = true; // Switch flag

    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
        
        for (i = 2; i < (rows.length - 1); i++) { // Exclude the column names and the base code
            shouldSwitch = false;
            // Select the span based on the sort option: find the correct cell(TD) in the current and next row
            x = (selectedOption === "nameAsc" || selectedOption === "nameDesc") ? 
                rows[i].querySelector(".currency-code") : 
                rows[i].querySelector(".currency-rate");
            y = (selectedOption === "nameAsc" || selectedOption === "nameDesc") ? 
                rows[i + 1].querySelector(".currency-code") : 
                rows[i + 1].querySelector(".currency-rate");
            
            // Check if the two rows should switch place, based on the selected option
            if (shouldSwitchRows(x, y, selectedOption)) {
                shouldSwitch = true;
                break;
            }
        }
        
        // Check if the current row "x" and next row "y" should switch places
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

/*
The shouldSwitchRows function assists sortCurrency 
by checking whether the two rows being compared should be switched
*/
function shouldSwitchRows(x, y, option) {
    // Extracting the text content for comparison
    let xContent = x.textContent;
    let yContent = y.textContent;

    // Parsing the innerText to float for rate comparison, and using innerText for name comparison
    if (option === "rateAsc" || option === "rateDesc") {
        // Replace any characters in the strings that are not digits, a period (.), or a minus sign (-) with an empty string
        // Basically leave the currency symbmol out of the comparision
        xContent = parseFloat(x.textContent.replace(/[^0-9.eE-]/g, ''));
        yContent = parseFloat(y.textContent.replace(/[^0-9.eE-]/g, ''));
    }

    // Comparing based on the selected option
    if ((option === "rateAsc" && xContent > yContent) ||
        (option === "rateDesc" && xContent < yContent) ||
        (option === "nameAsc" && xContent.toLowerCase() > yContent.toLowerCase()) ||
        (option === "nameDesc" && xContent.toLowerCase() < yContent.toLowerCase())) {
        return true;
    }
    return false;
}
