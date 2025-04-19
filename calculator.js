function calculaotion_selector() {
    math_list = {
        1: "Add",
        2: "Sub",
        3: "Multiply",
        4: "Divide",
        5: "Exponential",
        6: "Square",
        7: "Square Root"
    }

    console.log("Choose a calculation to perform")
    // loop the above dict
    for (let key in math_list) {
        console.log(key, ".", math_list[key]);
    }
    try {
        while (true) {
            user_input = prompt("Input to pick any of the above")
        }
    } catch (error) {
        console.log(error)
    }
}