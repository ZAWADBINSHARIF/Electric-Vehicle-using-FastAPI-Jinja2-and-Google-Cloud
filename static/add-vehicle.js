const addForm = document.querySelector("#add-form");
const addVehicleBtn = document.querySelector('#add-vehicle-btn');

if (addVehicleBtn) {
    addVehicleBtn.addEventListener('click', async e => {
        e.preventDefault();

        const formData = new FormData(addForm);
        const formObj = Object.fromEntries(formData);

        try {
            await fetch('/vehicle', {
                method: 'post',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(formObj)
            });

            window.location = "/";
        } catch (error) {
            console.log(error);
        }
    });
}
