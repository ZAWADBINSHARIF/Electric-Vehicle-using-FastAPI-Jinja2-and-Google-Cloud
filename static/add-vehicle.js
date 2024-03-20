const addForm = document.querySelector("#add-form");
const addVehicleBtn = document.querySelector('#add-vehicle-btn');

if (addVehicleBtn) {
    addVehicleBtn.addEventListener('click', async e => {
        e.preventDefault();

        const formData = new FormData(addForm);
        const formObj = Object.fromEntries(formData);
        

        if (Object.values(formObj).every((value) => value == '')) {
            return;
        }

        try {
            const response = await fetch('/vehicle', {
                method: 'post',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(formObj)
            })

            if (response.status == 500) {
                const errorP = document.getElementById("error")
                errorP.innerText = "Name must be unique"
            } else {
                window.location = "/";
            }
            

        } catch (error) {
            console.log(error);
        }
    });
}
