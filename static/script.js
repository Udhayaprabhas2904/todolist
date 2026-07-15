const API = "http://127.0.0.1:8000";

window.onload = function () {
    loadTasks();
};

// -------------------- CREATE TASK --------------------

async function createTask() {

    const task_name = document.getElementById("task_name").value.trim();
    const description = document.getElementById("description").value.trim();
    const time_limit = document.getElementById("time_limit").value;
    const status = document.getElementById("status").value;

    if(task_name==="" || description==="" || time_limit===""){

        alert("Please fill all fields.");

        return;

    }

    const task = {

        task_name,
        description,
        time_limit:Number(time_limit),
        status

    };

    const response = await fetch(`${API}/todo`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(task)

    });

    if(response.ok){

        alert("Task Created Successfully");

        clearForm();

        loadTasks();

    }

}

// -------------------- VIEW ALL TASKS --------------------

async function loadTasks() {

    const response = await fetch(`${API}/todo`);
    const tasks = await response.json();

    let pendingOutput = "";
    let completedOutput = "";

    tasks.forEach(task => {

        const row = `
        <tr>

            <td>${task.id}</td>

            <td>${task.task_name}</td>

            <td>${task.description}</td>

            <td>${task.time_limit}</td>

            <td>
                ${task.status === "Done"
    ? '<span class="completed"><i class="fa-solid fa-circle-check"></i> Completed</span>'
    : '<span class="pending"><i class="fa-solid fa-hourglass-half"></i> Pending</span>'}
            </td>

            <td>

               <button class="action-btn edit"
onclick="editTask(
    ${task.id},
    '${task.task_name}',
    '${task.description}',
    ${task.time_limit},
    '${task.status}'
)">
    <i class="fa-solid fa-pen-to-square"></i> Edit
</button>

<button class="action-btn delete"
onclick="deleteTask(${task.id})">
    <i class="fa-solid fa-trash"></i> Delete
</button>

            </td>

        </tr>
        `;

        if(task.status === "Done"){
            completedOutput += row;
        }
        else{
            pendingOutput += row;
        }

    });

  document.getElementById("pendingTasks").innerHTML = pendingOutput;
document.getElementById("completedTasks").innerHTML = completedOutput;

document.getElementById("pendingTasks").scrollIntoView({
    behavior: "smooth"
});

}
// -------------------- EDIT TASK --------------------

function editTask(id,task_name,description,time_limit,status){

    document.getElementById("task_id").value=id;
    document.getElementById("task_name").value=task_name;
    document.getElementById("description").value=description;
    document.getElementById("time_limit").value=time_limit;
    document.getElementById("status").value=status;

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

}

async function updateTask(){

    const id=document.getElementById("task_id").value;

    if(id===""){

        alert("Please click Edit before updating.");

        return;

    }

    const task={

        task_name:document.getElementById("task_name").value,
        description:document.getElementById("description").value,
        time_limit:Number(document.getElementById("time_limit").value),
        status:document.getElementById("status").value

    };

    const response=await fetch(`${API}/todo/${id}`,{

        method:"PUT",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify(task)

    });

    if(response.ok){

        alert("Task Updated Successfully");

        clearForm();

        loadTasks();

    }

}
// -------------------- DELETE TASK --------------------

async function deleteTask(id){

    if(!confirm("Delete this task?"))
        return;

    await fetch(`${API}/todo/${id}`,{

        method:"DELETE"

    });

    loadTasks();

}

// -------------------- MARK ALL DONE --------------------

async function markAllDone(){

    await fetch(`${API}/todo`,{

        method:"PUT"

    });

    alert("All Tasks Marked as Done");

    loadTasks();

}

// -------------------- DELETE ALL TASKS --------------------

async function deleteAllTasks(){

    if(!confirm("Delete All Tasks?"))
        return;

    await fetch(`${API}/todo`,{

        method:"DELETE"

    });

    loadTasks();

}

// -------------------- CLEAR FORM --------------------

function clearForm(){

    document.getElementById("task_id").value="";
    document.getElementById("task_name").value="";
    document.getElementById("description").value="";
    document.getElementById("time_limit").value="";
    document.getElementById("status").value="Pending";

}