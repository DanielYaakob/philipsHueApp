function get_state(state) {
    console.log(state[1]);

    if(state[0] == false) {
        document.getElementById(state[1]).style.backgroundColor = "white";

        if (state[1] == "Living Room") {
            document.getElementById("Chandelier 1").style.backgroundColor = "white";
            document.getElementById("Chandelier 2").style.backgroundColor = "white";
            document.getElementById("Couch Left").style.backgroundColor = "white";
            document.getElementById("Couch Right").style.backgroundColor = "white";
        }
    }
    else if(state[0] == true) {
        document.getElementById(state[1]).style.backgroundColor = "grey";

        if (state[1] == "Living Room") {
            document.getElementById("Chandelier 1").style.backgroundColor = "grey";
            document.getElementById("Chandelier 2").style.backgroundColor = "grey";
            document.getElementById("Couch Left").style.backgroundColor = "grey";
            document.getElementById("Couch Right").style.backgroundColor = "grey";
        }
    }
}

function get_states(states) {
    console.log(states);

    for(var i = 0; i < states.length; i++) {
        if (states[i][0] == false) {
            console.log(states[i][0])
            document.getElementById(states[i][1]).style.backgroundColor = "grey";
        }
        else if(states[i][0] == true) {
            document.getElementById(states[i][1]).style.backgroundColor = "white";
        }
    }
}

function get_initial_states () {
    eel.get_initial_states()(get_states)
}

//////////////////// GROUPS ////////////////////

function toggle_all() {
    eel.toggle_all()(get_state)
}

function toggle_living_room() {
    eel.toggle_living_room()(get_state)
}

//////////////////// LIGHTS ////////////////////

function toggle_chandelier_1() {
    eel.toggle_chandelier_1()(get_state)
}

function toggle_chandelier_2() {
    eel.toggle_chandelier_2()(get_state)
}

function toggle_couch_left() {
    eel.toggle_couch_left()(get_state)
}

function toggle_couch_right() {
    eel.toggle_couch_right()(get_state)
}

//////////////////// CUSTOM ACTIONS ////////////////////

function strobe_living_room() {
    eel.strobe_living_room()(get_state)
}
