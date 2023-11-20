Highcharts.chart('container-hinchas', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Cantidad de Hinchas por deporte'
    },
    xAxis: {
        categories: []
    },
    yAxis: {
        title: {
            text: 'Cantidad de Hinchas'
        }
    },
    series: [{
        name: 'Cantidad de Hinchas',
        data: []
    }]
});


Highcharts.chart('container-artesanos', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Cantidad de artesanos por artesania'
    },
    xAxis: {
        categories: []
    },
    yAxis: {
        title: {
            text: 'Cantidad de Artesanos'
        }
    },
    series: [{
        name: 'Cantidad de Artesanos',
        data: []
    }]
});

fetch("http://localhost:5000/get_hinchas_por_deporte")
    .then ((response) => response.json())
    .then((data)=> {
        // Extract the sport names and quantities from the data
        const sportNames = data.data.map(item => item.name);
        const sportQuantities = data.data.map(item => item.cantidad);
        

        const chart = Highcharts.charts.find(
            (chart) => chart && chart.renderTo.id === "container-hinchas"
        ); 
        // Update the chart with the new data
        chart.xAxis[0].setCategories(sportNames);
        chart.series[0].setData(sportQuantities);
    }).catch((error) => console.error("Error en conseguir los datos: ", error))

fetch("http://localhost:5000/get_artesanos_por_artesania")
    .then ((response) => response.json())
    .then((data)=> {
        // Extract the sport names and quantities from the data
        const sportNames = data.data.map(item => item.name);
        const sportQuantities = data.data.map(item => item.cantidad);
        

        const chart = Highcharts.charts.find(
            (chart) => chart && chart.renderTo.id === "container-artesanos"
        ); 
        // Update the chart with the new data
        chart.xAxis[0].setCategories(sportNames);
        chart.series[0].setData(sportQuantities);
    }).catch((error) => console.error("Error en conseguir los datos: ", error))
