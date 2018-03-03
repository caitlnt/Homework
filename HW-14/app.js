
// CTa - HW14 - Data Journalism and D3
// Part 03 - Visualize the Data

var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 100 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


// Create canvas for the graph.
var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var chart = svg.append("g");


// Div for tool tip
d3.select(".chart")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);

d3.csv("data.csv", function(err, data) {
  if (err) throw err;

  data.forEach(function(data) {
    data.total_HH_FS = +total_HH_FS;
    data.total_HH = +total_HH;
    data.med_income= +med_income;

  });


  // Scaling Functions
  var yLinearScale = d3.scaleLinear()
    .range([height, 0]);

  var xLinearScale = d3.scaleLinear()
    .range([0, width]);

  // Axis Functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);





 // These variables store the minimum and maximum values in a column in data.csv
 var xMin;
 var xMax;
 var yMax;


    function findMinAndMax(dataColumnX) {
        xMin = d3.min(data, function (data) {
            return +data[dataColumnX] * 0.8;
        });

        xMax = d3.max(data, function (data) {
            return +data[dataColumnX] * 1.1;
        });

        yMax = d3.max(data, function (data) {
            return +data.total_HH_FS * 1.1;
        });
    }


  var currentAxisLabelX = "total_HH_FS";


findMinAndMax(currentAxisLabelX);


xLinearScale.domain([xMin, xMax]);
yLinearScale.domain([0, yMax]);

// Initialize tooltip
var toolTip = d3
    .tip()
    .attr("class", "tooltip")
    // Define position
    .offset([80, -60])
    // The html() method allows us to mix JavaScript with HTML in the callback function
    .html(function(data) {
      var state = data.state;
      var HH_FS = +data.total_HH_FS; 
      var total_HS = +data[currentAxisLabelX]; 
      var incomeString;
      // Tooltip text depends on which axis is active/has been clicked
      if (currentAxisLabelX === "HH_FS") {
        incomeString = "? ";
      }
      else {
        incomeString = "? ";
      }
      return state +
        "<br>" +
        incomeString +
        total_HH_FS + 
        "%" +
        "<br> ? " +
        med_income + "%";
    });

  


  // Create toolitp
  chart.call(toolTip);

  chart.selectAll("circle")
    .data(Data)
    .enter().append("circle")
      .attr("cx", function(data, index) {
        console.log(data.total_HH_FS);
        return xLinearScale(+data[currentAxisLabelX]);
      })
      .attr("cy", function(data, index) {
        return yLinearScale(data.total_HH);
      })
      .attr("r", "5")
      .attr("fill", "lightsteelblue")
      .on("click", function(data) {
        toolTip.show(data);
      })
      .attr("r", "5")
      .attr("fill", "lightsteelblue")
      .on("mouseover", function(data) {
        toolTip.show(data);
      })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

  chart.append("g")
    .attr("transform", "translate(0," + height + ")")
    .attr("class", "x-axis")
    .call(bottomAxis);

  chart.append("g")
    .call(leftAxis);

// Append y-axis lables  
  chart.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text(" (%)");

// Append x-axis labels
  chart
    .append("text")
    .attr(
        "transform", 
        "translate(" + (width / 2) + " ," + (height + margin.top + 30) + ")"
    )
    // This axis label is active by default
    .attr("class", "axis-text active")
    .attr("data-axis-name", "total_HH_FS")
    .text(" (%)");

// Append other x axis
  chart
    .append("text")
    .attr(
      "transform",
      "translate(" + width / 2 + " ," + (height + margin.top + 45) + ")"
    )
    // This axis label is inactive by default
    .attr("class", "axis-text inactive")
    .attr("data-axis-name", "College grads")
    .text(" (%)");

  // Change an axis's status from inactive to active when clicked (if it was inactive)
  // Change the status of all active axes to inactive otherwise
  function labelChange(clickedAxis) {
    d3
      .selectAll(".axis-text")
      .filter(".active")
      // An alternative to .attr("class", <className>) method. Used to toggle classes.
      .classed("active", false)
      .classed("inactive", true);

    clickedAxis.classed("inactive", false).classed("active", true);
  }

  d3.selectAll(".axis-text").on("click", function() {
    // Assign a variable to current axis
    var clickedSelection = d3.select(this);
    // "true" or "false" based on whether the axis is currently selected
    var isClickedSelectionInactive = clickedSelection.classed("inactive");
    // console.log("this axis is inactive", isClickedSelectionInactive)
    // Grab the data-attribute of the axis and assign it to a variable
    // e.g. if data-axis-name is "poverty," var clickedAxis = "poverty"
    var clickedAxis = clickedSelection.attr("data-axis-name");
    console.log("current axis: ", clickedAxis);

    // The onclick events below take place only if the x-axis is inactive
    // Clicking on an already active axis will therefore do nothing
    if (isClickedSelectionInactive) {
      // Assign the clicked axis to the variable currentAxisLabelX
      currentAxisLabelX = clickedAxis;
      // Call findMinAndMax() to define the min and max domain values.
      findMinAndMax(currentAxisLabelX);
      // Set the domain for the x-axis
      xLinearScale.domain([xMin, xMax]);
      // Create a transition effect for the x-axis
      svg
        .select(".x-axis")
        .transition()
        // .ease(d3.easeElastic)
        .duration(1800)
        .call(bottomAxis);
      // Select all circles to create a transition effect, then relocate its horizontal location
      // based on the new axis that was selected/clicked
      d3.selectAll("circle").each(function() {
        d3
          .select(this)
          .transition()
          // .ease(d3.easeBounce)
          .attr("cx", function(data) {
            return xLinearScale(+data[currentAxisLabelX]);
          })
          .duration(1800);
      });

      // Change the status of the axes. See above for more info on this function.
      labelChange(clickedSelection);
    }
  });  
});
