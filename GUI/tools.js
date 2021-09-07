let main = 'main',
    pressure_sensor = 'pressure_sensor',
    valve = 'valve',
    settings = 'config',
    current_page = main

function redirect(page) {
    throw_event('redirect_' + page)
    window.location.href = page + '.html'
    current_page = page
}

let events_buffer = []

function get_current_page() {
    return current_page
}

function throw_event(event) {
    events_buffer.push(event)
}

function waiting_events() {
    return events_buffer
}

function clean_events() {
    events_buffer = []
}