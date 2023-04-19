function renderContent(containerID) {
    let allElements = document.getElementsByName('content');
    for (let i = 0; i < allElements.length; ++i) {
        displaySection(allElements[i].id, 'none');
    }
    allElements = document.getElementsByName('contentBarButton');
    for (let i = 0; i < allElements.length; ++i) {
        modifyClass(allElements[i].id, 'btn btn-outline-info btn-sm');
    }
    modifyClass(containerID, 'btn btn-outline-info btn-sm active');
    displaySection(containerID + 'Content', '');
}

function displaySection(containerID, type) {
    document.getElementById(containerID).style.display= type;
}

function modifyClass(containerID, name) {
    document.getElementById(containerID).className= name;
}

function verifyPass() {
    let pass = document.getElementById('pass').value;
    let confirmPass = document.getElementById('equalPass').value;
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    if (pass == confirmPass) {
        $.ajax({
            type: 'POST',
            url: 'changePassword',
            data: {csrfmiddlewaretoken: csrfToken,
                password: pass
            },
            success: function(response){
                alert(response);
            },
            error: function(response){
                alert(response);
            }
        });
    } else {
        alert('Enter the same password');
    }
    document.getElementById('pass').value = "";
    document.getElementById('equalPass').value = "";
}

function changeName() {
    let name = document.getElementById('name').value;
    let middleName = document.getElementById('middleName').value;
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        type: 'POST',
        url: 'updateName',
        data: {csrfmiddlewaretoken: csrfToken,
            name: name,
            middleName: middleName
        },
        success: function(response){
            alert(response);
        },
        error: function(response){
            alert(response);
        }
    });
    document.getElementById('name').value = "";
    document.getElementById('middleName').value = "";
}

function changeCompanyDetails() {
    let country = document.getElementById('newCountry').value;
    let city = document.getElementById('newCity').value;
    let adress = document.getElementById('newAdress').value;
    let phone = document.getElementById('newPhone').value;
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        type: 'POST',
        url: 'updateCompanyDetails',
        data: {csrfmiddlewaretoken: csrfToken,
            country: country,
            city: city,
            adress: adress,
            phone: phone
        },
        success: function(response){
            alert(response);
        },
        error: function(response){
            alert(response);
        }
    });
    document.getElementById('newCountry').value = "";
    document.getElementById('newCity').value = "";
    document.getElementById('newAdress').value = "";
    document.getElementById('newPhone').value = "";
}

function addEmployer() {
    let email = document.getElementById('employerEmail').value;
    let password = document.getElementById('employerPassword').value;
    let name = document.getElementById('employerName').value;
    let middleName = document.getElementById('employerMiddleName').value;
    let permisions = document.getElementById('employerPermisions').value;
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    $.ajax({
        type: 'POST',
        url: 'createEmployer',
        data: {csrfmiddlewaretoken: csrfToken,
            email: email,
            password: password,
            name: name,
            middleName: middleName,
            permisions: permisions
        },
        success: function(response){
            alert(response);
        },
        error: function(response){
            alert(response);
        }
    });
    document.getElementById('employerEmail').value = "";
    document.getElementById('employerPassword').value = "";
    document.getElementById('employerName').value = "";
    document.getElementById('employerMiddleName').value = "";
    document.getElementById('employerPermisions').value = "";
}