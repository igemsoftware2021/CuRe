let pump_state = false, valve_state = false

function pump_set(state) {
    document.getElementById('pumpbutton').classList = [state ? 'switchbutton_on' : 'switchbutton_off']
    throw_event('pump_' + (state ? 'on' : 'off'))
}

function pump_switch() {
    pump_set(!pump_state)
    pump_state = !pump_state
}

function valve_set(state) {
    document.getElementById('valvebutton').classList = [state ? 'switchbutton_on' : 'switchbutton_off']
    throw_event('valve_' +(state ? 'on' : 'off'))
}

function valve_switch() {
    valve_set(!valve_state)
    valve_state = !valve_state
}