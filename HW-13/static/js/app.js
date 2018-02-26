
// CTa - HW-13 - BellyButton Biodiversity
// Part 02 - Plotly.js


function selectedOption(value){
    console.log(value)  
    return buildPlot(value);
};

function buildPlot(chosenSample) {

    Plotly.d3.json(`/samples/${chosenSample}`, function(error, response) {
        
        console.log(response);
        
        var data = [{
            values: response.sample_values,
            labels: response.otu_ids,
            type: "pie"
        }];

        var layout = {
            title: "Top 10 samples by otu_id",
            height: 600,
            width: 800
        };

    Plotly.newPlot("pie", data, layout)
    });
    
   