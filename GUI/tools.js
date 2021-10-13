let main_str = 'main',
    pressure_sensor_str = 'pressure_sensor',
    bioreactor_str = 'bioreactor'

function redirect(page) {
    throw_event('redirect_' + page)
    window.location.href = page + '.html'
}

let events_buffer = []


function throw_event(event) {
    events_buffer.push(event)
}

function waiting_events() {
    return events_buffer
}

function clean_events() {
    events_buffer = []
}