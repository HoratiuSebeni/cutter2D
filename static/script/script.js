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
