/*
* */
function init_plot(canvas_id){
    chart = new Chart(canvas_id,
            {
                type: "line",
                data: {
                    labels: [],
                    datasets: [],
                },
                options: {
                    animation: {
                        duration: .1
                    },
                    scales: {
                        yAxes: [{
                            gridLines: {
                                color: 'lightgray',
                            }
                        }],
                        xAxes: [{
                            gridLines: {
                                color: 'lightgray'
                            }
                        }]
                    },
                    plugins: {
                        legend: {
                            labels: {
                                // This more specific font property overrides the global property
                                fontColor: 'yellow'
                            }
                        }
                    }
                }
            }
        )
}
function plot_datasets(datasets, x_labels, datasets_names) {
    // USEFUL LINKS
    // https://www.w3schools.com/ai/ai_chartjs.asp

    // transform the datasets
    let lines_colors = ['rgba(200, 0, 0, 1)', 'rgba(0, 100, 0, 1)', 'rgba(0, 0, 255, 1)'],
        background_colors = ['rgba(100, 0, 0, .1)', 'rgba(0, 100, 0, .1)', 'rgba(0, 0, 100, .1)']

    let transformed_dataset = []
    for (let i = 0; i < datasets.length; i++) {
        let line_color = lines_colors[i], background_color = background_colors[i], data = datasets[i]
        transformed_dataset.push([{
            pointBackgroundColor: 'transparent',
            pointBorderColor: "rgba(0,0,0,0)",
            backgroundColor: background_color,
            borderColor: line_color,
            data: data,
            label: datasets_names[i]
        }])
    }
    datasets = transformed_dataset.flat()

    // plot the dataset
    chart.data.labels = x_labels;
    for (let i = 0; i < datasets.length; i++)
        if (i < chart.data.datasets.length) chart.data.datasets[i] = datasets[i]
        else chart.data.datasets.push(datasets[i])
    for (let i = 0; i < chart.data.datasets.length - datasets.length; i++)
        chart.data.datasets.pop()
    chart.update();
}