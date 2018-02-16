// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");
var $loadMoreBtn = document.querySelector("#load-btn");


// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$loadMoreBtn.addEventListener("click", handleButtonClick);


// Set sliced dataSet.js to newData variable initially
var newData = dataSet.slice(0, 50);

//Initially define filterData with no value, this will be used later in the code
var filteredData;

//Create variable for displaying 50 items
var resultsPerPage = 50;

//handleButtonClick Function for loading more data
function handleButtonClick() {
  if (filteredData) {
    resultsPerPage += filteredData.length;
  } else {
    resultsPerPage += 50;
  }
  var startingIndex = resultsPerPage - 50 + 1;
  var nextData = dataSet.slice(startingIndex, resultsPerPage);
  newData = newData.concat(nextData);

  renderTable();
}



// renderTable renders the filteredData to the tbody
function renderTable(filteredData) {
  if (filteredData) {
    $tbody.innerHTML = "";
    for (var i = 0; i < filteredData.length; i++) {
      // Get get the current filteredData object and its fields
      var data = filteredData[i];
      var fields = Object.keys(data);
      // Create a new row in the tbody, set the index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the data object, create a new cell at set its inner text to be the current value at the current data field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = data[field];
      }
    }
  } else {
    $tbody.innerHTML = "";
    for (var i = 0; i < newData.length; i++) {
      // Get get the current filteredData object and its fields
      var data = newData[i];
      var fields = Object.keys(data);
      // Create a new row in the tbody, set the index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the data object, create a new cell at set its inner text to be the current value at the current data field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = data[field];
      }
    }
  }
}


function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();


 // Set filteredAddresses to an array of all addresses who's "state" matches the filter
  filteredData = newData.filter(function(data) {
    var Datetime = data.datetime.substring(0, filterDatetime.length).toLowerCase();
    var City = data.city.substring(0, filterCity.length).toLowerCase();
    var State = data.state.substring(0, filterState.length).toLowerCase();
    var Country = data.country.substring(0, filterCountry.length).toLowerCase();
    var Shape = data.shape.substring(0, filterShape.length).toLowerCase();

    if (Datetime === filterDatetime && City === filterCity && State === filterState && Country === filterCountry && Shape === filterShape) {
      return true;
    }
    return false;
  });
renderTable(filteredData);
}


// Render the table for the first time on page load
renderTable();